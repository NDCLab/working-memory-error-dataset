#!/bin/bash

usage() {
  cat <<EOF
  Usage: $0 [-s session:user1/user2,session:user1/user2 ] [-n session:user1/user2,session:user1/user2 ] [-c numcpus ] [-r] [-d]

  -s subjects and sessions to process, sessions separated by commas and users separated by slashes
  -n subjects and sessions not to process
  -c number cpus requested
  -r just score redcap data, no EEG
  -d just score redcap data, no EEG, don't update central tracker

  Default is to preprocess every subject.

  Examples:
	bash preprocess_wrapper.sh -s s1_r1:301/302/303,s2_r1:304/305/306

		This will process only subjects 301, 302, and 303 for session 1 run 1, and subjects 304, 305, and 306 for session 2 run 1.

	bash preprocess_wrapper.sh -n s1_r1:303

		This will process each subject in each session except subject 303 in session 1 run 1.

EOF
exit 0
}

while getopts "s:n:rdc:" opt; do
  case "${opt}" in
    s)
      sstr=${OPTARG}
      IFS=',' read -ra subs_to_process <<< $sstr && unset IFS
      ;;
    n)
      nstr=${OPTARG}
      IFS=',' read -ra subs_not_to_process <<< $nstr && unset IFS
      ;;
    r)
      score_only=true
      ;;
    d)
      dummy=true
      score_only=true
      ;;
    c)
      cpus=${OPTARG}
      ;;
    *)
      usage
      ;;
  esac
done

if [[ -z $cpus ]]
  then
  cpus=4
fi

if [[ -n $subs_to_process ]] && [[ -n $subs_not_to_process ]]
  then
  echo "Please specify either the -s flag, the -n flag, or neither."
  exit 0
fi

dataset=$(dirname $(pwd))
project=$(basename $dataset)
sessions=($(find ${dataset}/sourcedata/raw -mindepth 1 -maxdepth 1 -type d -printf "%f\n"))

sing_image="/home/data/NDClab/tools/instruments/containers/singularity/inst-container.simg"

totalsubs=0
if [[ -n $subs_to_process ]]
   then
   for s in ${subs_to_process[@]}
      do
      session=$(echo $s | cut -d':' -f1)
      subjects_to_process=$(echo $s | cut -d':' -f2)
      numsubs=$(echo $subjects_to_process | sed 's/\// /g' | wc -w)
      totalsubs=$(( $totalsubs + $numsubs ))
   done
elif [[ -n $subs_not_to_process ]]
   then
   for s in ${subs_not_to_process[@]}
      do
      session=$(echo $s | cut -d':' -f1)
      subjects_not_to_process=$(echo $s | cut -d':' -f2)
      numsubs_exclude=$(echo $subjects_not_to_process | sed 's/\// /g' | wc -w)
      subjects_to_process=$(singularity exec -e $sing_image python3 subjects_yet_to_process.py $project $session) #need container for pandas
      numsubs=$(echo $subjects_to_process | sed 's/\// /g' | wc -w)
      totalsubs=$(( $totalsubs + $numsubs - $numsubs_exclude))
   done
elif [[ -z "$score_only" ]]
   then
   totalsubs=0
   for session in ${sessions[@]}
      do
      subjects_to_process=$(singularity exec -e $sing_image python3 subjects_yet_to_process.py $project $session) #need container for pandas
      numsubs=$(echo $subjects_to_process | sed 's/\// /g' | wc -w)
      totalsubs=$(( $totalsubs + $numsubs ))
   done
fi

if [[ -z "$score_only" ]]
    then
    #mem_needed=$(( $totalsubs * 10 )) # ~10gb / sub
    mem_needed=$(( $cpus * 10 )) # ~10gb / sub
    walltime_needed=$(( (totalsubs+cpus-1) / 4 * 10 ))
    sbatch --mem=${mem_needed}G --time=${walltime_needed}:00:00 --cpus-per-task=$cpus --account=iacc_gbuzzell --partition=highmem1 --qos=highmem1 --export=ALL,sstr=${sstr},nstr=${nstr} preprocess.sub
else
    sbatch --mem=1G --time=00:30:00 --export=All,score=${score_only},dummy=${dummy} preprocess.sub
fi
