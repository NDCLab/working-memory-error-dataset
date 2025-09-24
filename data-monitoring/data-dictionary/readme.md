# Datadict Column Definitions

The columns below are expected in the central tracker datadict:

* **variable**: exact name of data variable; for non-questionnaire data (psychopy, audio, video, eeg, digi), the variable name should be "\<task\>_\<dataType\>"; for questionnaire data (redcap_data and redcap_scrd), the variable name should be the exact questionnaire or subscore name, except in the case that a self-report survey is administered to both parent and child (in which case, "_parent" is appended to the end of the variable name for the parent self-report to distinguish it from the child self-report)
* **datatype**: type of data; e.g., consent, psychopy, eeg, digi, audio, video, redcap_data, redcap_scrd, or other data type; for combination rows, the dataType is listed as "combination" and the provenance is updated accordingly to designate the variables that should be combined
* **description**: human-readable description of the variable
* **detail**: clarification of how the variable value is calculated/derived
* **allowedSuffix**: sX_rX_eX, where s=session, r=run, and e=event; separated by commas
* **measureUnit**: indication of the computer-readable value type used for the variable (i.e., Integer, Real, Logical, Char, Time)
* **allowedValues**: all allowed values for the variable, separated by commas: Integers and Real numbers as [x,y] (with integer sets separated by commas); Logical as 0, 1; Likert/Categorical as 1, 2, 3; Char as "text"
* **valueInfo**: indication of the meanings of the allowed values; categorical-type options may be separated by \| (vertical bar) or ; (semicolon)
* **naValueType**: indication of how NA values are flagged (NA, NaN, etc.)
* **provenance**: indication of whether variable is collected directly from the participant and by what platform (direct-psychopy, direct-pavlovia) or, if not direct, the origin of its derivation (that is, the script the calculates it, specified as code-SCRIPT, such as code-instruments or code-preproc.R, or the protocol used for manual coding, such as manual-errorCoding). for REDCap data, provenance will specify the REDCap file and the exact variable within that file that the row corresponds to (file: "\<name\>", variable:"\<name\>"); if the variable name is the same as what is listed in the variable column, the provenance can simply state variable: "". for combination rows, the provenance will specify the variables that should be combined in that row (variables: "\<name\>","\<name\>")
* **expectedFileExt**: the file extensions expected for each data type, separated by commas (e.g., ".eeg, .vmrk, .vhdr" for EEG data); if multiple extensions are allowed but not necessarily all expected, extensions can be separated by \| (vertical bar) (e.g., ".zip.gpg \| .tar.gz.gpg"); if this is not relevant, type NA
