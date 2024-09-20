#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on January 25, 2024, at 15:27
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'number-flanker'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '1',
    'run': '1',
    'event': '1',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\NDCLab\\Desktop\\Experiments\\WME\\number-flanker\\number-flanker_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='sys-2-asus', color=[-.3,-.3,-.3], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "JS_code" ---

# --- Initialize components for Routine "setup" ---
# Run 'Begin Experiment' code from setup_code
#import serial #used for sending eeg triggers
#import time #indirerctly used for sending eeg triggers (how long to wait before clearing port)

#win.mouseVisible = False #hide mouse cursor
#port = serial.Serial('COM3') # Open specified serial port (COM4) for sending eeg triggers to   
#PulseWidth = 0.002 #how long to wait before clearing port after sending trigger (2 ms is sufficient at 1000 hz sampling rate)
#port.write([0x00]) #clear serial port
#time.sleep(PulseWidth) #wait PulseWidth amount of time before doing anything else
# Run 'Begin Experiment' code from config_code
import random

used_letters = [] # letters used in WM and flanker trials (to prevent repeates in WM and flanker within supertrial)
used_letters_fl = [] # letters used in flanker trials (to prevent repeats within flanker trials)
shown_letters = [] # exact letters shown in WM (i.e., considered lower-/uppercase)

CROSS_Y = -0.73 # position of fix cross (to easily adjust when switch from macbook to asus), for asus should be -0.71

# initialize thresholds for flanker and WM practice
#WM_THRESH = 0.7
FL_THRESH = 0.7

# initialize trial, block counters and accuracy
numCorr_wm = 0
trialNum_wm = 0
numCorr_fl = 0
trialNum_fl = 0
blockCounter = 0
trialNum = 0
accuracy = 0
numCorr = 0
blockAcc_wm = 0
blockAcc_fl = 0

# initialize the thisISI variable used for all ISI
thisISI = 0

NUMBERS = [
'1', '2', '3',
'4', '5', '6',
'7', '8', '9',
'0'
]

NUMBERS_LARGE = ['6', '7', '8', '9',]
NUMBERS_SMALL = ['1', '2', '3', '4',]

# --- Initialize components for Routine "instructMiddle" ---
welcome_text_2 = visual.TextStim(win=win, name='welcome_text_2',
    text='',
    font='Arial',
    units='height', pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
space_end_keyResp_7 = keyboard.Keyboard()

# --- Initialize components for Routine "instructLeft" ---
instructLeft_text_2 = visual.TextStim(win=win, name='instructLeft_text_2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructLeft_numbers2 = visual.TextStim(win=win, name='instructLeft_numbers2',
    text='',
    font='Arial',
    units='deg', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
prac_highlight_circle_2 = visual.ShapeStim(
    win=win, name='prac_highlight_circle_2',
    size=(0.05, 0.045), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor='yellow', fillColor='yellow',
    opacity=0.3, depth=-2.0, interpolate=True)
insructLeft_keyResp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "instructRight" ---
instrucRight_text_2 = visual.TextStim(win=win, name='instrucRight_text_2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructRight_numbers2 = visual.TextStim(win=win, name='instructRight_numbers2',
    text='66666',
    font='Arial',
    units='deg', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
prac_highlight_circle_4 = visual.ShapeStim(
    win=win, name='prac_highlight_circle_4',
    size=(0.05, 0.045), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor='yellow', fillColor='yellow',
    opacity=0.3, depth=-2.0, interpolate=True)
instructRight_keyResp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "instructionLeft" ---
instrucRight_text = visual.TextStim(win=win, name='instrucRight_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructRight_numbers2_2 = visual.TextStim(win=win, name='instructRight_numbers2_2',
    text='77277',
    font='Arial',
    units='deg', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
prac_highlight_circle = visual.ShapeStim(
    win=win, name='prac_highlight_circle',
    size=(0.05, 0.045), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor='yellow', fillColor='yellow',
    opacity=0.3, depth=-2.0, interpolate=True)
instructRight_keyResp = keyboard.Keyboard()

# --- Initialize components for Routine "instructionRight" ---
instructInconRight_text_2 = visual.TextStim(win=win, name='instructInconRight_text_2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructInconRight_letters2 = visual.TextStim(win=win, name='instructInconRight_letters2',
    text='33833',
    font='Arial',
    units='deg', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
prac_highlight_circle_8 = visual.ShapeStim(
    win=win, name='prac_highlight_circle_8',
    size=(0.05, 0.045), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor='yellow', fillColor='yellow',
    opacity=0.3, depth=-2.0, interpolate=True)
instructInconRight_keyResp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "respond_onceInstruct" ---
respond_once_text = visual.TextStim(win=win, name='respond_once_text',
    text='Each time you see the numbers appear, respond as quickly as you can without making mistakes.\n\nHowever, only respond once each time you see the numbers appear. Even if you think you made the wrong response, do not respond again until you see the next set of numbers appear. Also, please do not to say the numbers out loud. \n\nPress the right button to continue',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
space_end_keyResp_8 = keyboard.Keyboard()

# --- Initialize components for Routine "eeg_trigger_check" ---

# --- Initialize components for Routine "prac_blockReminders" ---
prac_blockText = visual.TextStim(win=win, name='prac_blockText',
    text='Practice',
    font='Arial',
    pos=(0, .3), height=0.06, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
prac_reminder_text = visual.TextStim(win=win, name='prac_reminder_text',
    text='Respond as quickly as you can without making mistakes. Only respond once each time you see the numbers appear. Always respond whether the MIDDLE number is lesser or greater than 5.\n\nRemember not to say any of the numbers out loud. To get ready, rest your thumbs on the right and left buttons.\n\n\nExperimenter: press key to continue',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
space_end_keyResp_9 = keyboard.Keyboard()

# --- Initialize components for Routine "prac_initFixation" ---
initFixation_img_2 = visual.ImageStim(
    win=win,
    name='initFixation_img_2', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, CROSS_Y), size=(.24, .24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "prac_stimRoutine" ---
prac_flanker_text_stim = visual.TextStim(win=win, name='prac_flanker_text_stim',
    text='',
    font='Arial',
    units='deg', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
prac_fixImg = visual.ImageStim(
    win=win,
    name='prac_fixImg', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, CROSS_Y), size=(.24, .24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
prac_stim_keyResp = keyboard.Keyboard()

# --- Initialize components for Routine "prac_blockFeed" ---
prac_blockFeed_text_3 = visual.TextStim(win=win, name='prac_blockFeed_text_3',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
prac_pressContinue_3 = visual.TextStim(win=win, name='prac_pressContinue_3',
    text='Experimenter: press key to continue',
    font='Arial',
    pos=(0, -.3), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
prac_blockFeed_keyResp = keyboard.Keyboard()

# --- Initialize components for Routine "task_condition" ---
task_blockText_2 = visual.TextStim(win=win, name='task_blockText_2',
    text='',
    font='Arial',
    pos=(0, .4), height=0.06, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
condition_reminder_text = visual.TextStim(win=win, name='condition_reminder_text',
    text='Respond as quickly as you can without making mistakes. Only respond once each time you see the numbers appear. Even if you think you made the wrong response, do not respond again until you see the next set of numbers appear.\n\nAlways respond whether the MIDDLE number is lesser or greater than 5. \n\nRemember not to say any of the numbers out loud. To get ready, rest your thumbs on the right and left buttons.\n\nPress the right button to begin',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
space_end_keyResp_11 = keyboard.Keyboard()

# --- Initialize components for Routine "eeg_trigger_check_2" ---

# --- Initialize components for Routine "supertrial_initFixation" ---
initFixation_img_5 = visual.ImageStim(
    win=win,
    name='initFixation_img_5', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, CROSS_Y), size=(.24, .24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "task_stimRoutine" ---
flanker_text_stim = visual.TextStim(win=win, name='flanker_text_stim',
    text='',
    font='Arial',
    units='deg', pos=(0, 0), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
task_fixImg = visual.ImageStim(
    win=win,
    name='task_fixImg', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, CROSS_Y), size=(.24, .24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
task_stim_keyResp = keyboard.Keyboard()

# --- Initialize components for Routine "task_conditionComplete" ---
conditionComplete_text = visual.TextStim(win=win, name='conditionComplete_text',
    text='Press the right button to continue',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
space_end_keyResp_13 = keyboard.Keyboard()

# --- Initialize components for Routine "task_finish" ---
taskComplete_text = visual.TextStim(win=win, name='taskComplete_text',
    text='Thank you for participating!\n\nPlease ring the bell for your experimenter.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
space_end_keyResp_12 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "JS_code" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
JS_codeComponents = []
for thisComponent in JS_codeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "JS_code" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in JS_codeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "JS_code" ---
for thisComponent in JS_codeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "JS_code" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "setup" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from setup_code
win.mouseVisible = False #hide mouse cursor
# keep track of which components have finished
setupComponents = []
for thisComponent in setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "setup" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "setup" ---
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructMiddle" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
welcome_text_2.setText('Welcome to the Number Alert Game! This game will require you to quickly respond to numbers based on whether they are lesser or greater than 5.\n\nDuring this game, five numbers between 1-9 will appear at a time. They will be quickly flashed on the screen. Your goal is to respond to the MIDDLE number, and to respond as quickly as you can without making mistakes.\n\nIf the MIDDLE number is lesser than 5, use your left hand to press the left button. If the MIDDLE number is greater than 5, use your right hand to press the right button.\n\nPress the right button to continue')
space_end_keyResp_7.keys = []
space_end_keyResp_7.rt = []
_space_end_keyResp_7_allKeys = []
# keep track of which components have finished
instructMiddleComponents = [welcome_text_2, space_end_keyResp_7]
for thisComponent in instructMiddleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructMiddle" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_text_2* updates
    if welcome_text_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        welcome_text_2.frameNStart = frameN  # exact frame index
        welcome_text_2.tStart = t  # local t and not account for scr refresh
        welcome_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text_2, 'tStartRefresh')  # time at next scr refresh
        welcome_text_2.setAutoDraw(True)
    
    # *space_end_keyResp_7* updates
    waitOnFlip = False
    if space_end_keyResp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_end_keyResp_7.frameNStart = frameN  # exact frame index
        space_end_keyResp_7.tStart = t  # local t and not account for scr refresh
        space_end_keyResp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_end_keyResp_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'space_end_keyResp_7.started')
        space_end_keyResp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space_end_keyResp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space_end_keyResp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space_end_keyResp_7.status == STARTED and not waitOnFlip:
        theseKeys = space_end_keyResp_7.getKeys(keyList=['8'], waitRelease=False)
        _space_end_keyResp_7_allKeys.extend(theseKeys)
        if len(_space_end_keyResp_7_allKeys):
            space_end_keyResp_7.keys = _space_end_keyResp_7_allKeys[-1].name  # just the last key pressed
            space_end_keyResp_7.rt = _space_end_keyResp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructMiddleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructMiddle" ---
for thisComponent in instructMiddleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if space_end_keyResp_7.keys in ['', [], None]:  # No response was made
    space_end_keyResp_7.keys = None
thisExp.addData('space_end_keyResp_7.keys',space_end_keyResp_7.keys)
if space_end_keyResp_7.keys != None:  # we had a response
    thisExp.addData('space_end_keyResp_7.rt', space_end_keyResp_7.rt)
thisExp.nextEntry()
# the Routine "instructMiddle" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructLeft" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instructLeft_text_2.setText('Below, the MIDDLE number is lesser than 5, so you would respond by pressing the left button with your left hand.\n\n\n\n\n\n\n\nPress the left button to continue')
instructLeft_numbers2.setText('11111')
insructLeft_keyResp_2.keys = []
insructLeft_keyResp_2.rt = []
_insructLeft_keyResp_2_allKeys = []
# keep track of which components have finished
instructLeftComponents = [instructLeft_text_2, instructLeft_numbers2, prac_highlight_circle_2, insructLeft_keyResp_2]
for thisComponent in instructLeftComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructLeft" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructLeft_text_2* updates
    if instructLeft_text_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        instructLeft_text_2.frameNStart = frameN  # exact frame index
        instructLeft_text_2.tStart = t  # local t and not account for scr refresh
        instructLeft_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_text_2, 'tStartRefresh')  # time at next scr refresh
        instructLeft_text_2.setAutoDraw(True)
    
    # *instructLeft_numbers2* updates
    if instructLeft_numbers2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        instructLeft_numbers2.frameNStart = frameN  # exact frame index
        instructLeft_numbers2.tStart = t  # local t and not account for scr refresh
        instructLeft_numbers2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_numbers2, 'tStartRefresh')  # time at next scr refresh
        instructLeft_numbers2.setAutoDraw(True)
    
    # *prac_highlight_circle_2* updates
    if prac_highlight_circle_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prac_highlight_circle_2.frameNStart = frameN  # exact frame index
        prac_highlight_circle_2.tStart = t  # local t and not account for scr refresh
        prac_highlight_circle_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prac_highlight_circle_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'prac_highlight_circle_2.started')
        prac_highlight_circle_2.setAutoDraw(True)
    
    # *insructLeft_keyResp_2* updates
    waitOnFlip = False
    if insructLeft_keyResp_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        insructLeft_keyResp_2.frameNStart = frameN  # exact frame index
        insructLeft_keyResp_2.tStart = t  # local t and not account for scr refresh
        insructLeft_keyResp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(insructLeft_keyResp_2, 'tStartRefresh')  # time at next scr refresh
        insructLeft_keyResp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(insructLeft_keyResp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(insructLeft_keyResp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if insructLeft_keyResp_2.status == STARTED and not waitOnFlip:
        theseKeys = insructLeft_keyResp_2.getKeys(keyList=['1'], waitRelease=False)
        _insructLeft_keyResp_2_allKeys.extend(theseKeys)
        if len(_insructLeft_keyResp_2_allKeys):
            insructLeft_keyResp_2.keys = _insructLeft_keyResp_2_allKeys[-1].name  # just the last key pressed
            insructLeft_keyResp_2.rt = _insructLeft_keyResp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructLeftComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructLeft" ---
for thisComponent in instructLeftComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructLeft" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructRight" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instrucRight_text_2.setText('Below, the MIDDLE number is greater than 5, so you would respond by pressing the right button with your right hand.\n\n\n\n\n\n\n\nPress the right button to continue')
instructRight_keyResp_2.keys = []
instructRight_keyResp_2.rt = []
_instructRight_keyResp_2_allKeys = []
# keep track of which components have finished
instructRightComponents = [instrucRight_text_2, instructRight_numbers2, prac_highlight_circle_4, instructRight_keyResp_2]
for thisComponent in instructRightComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructRight" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrucRight_text_2* updates
    if instrucRight_text_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        instrucRight_text_2.frameNStart = frameN  # exact frame index
        instrucRight_text_2.tStart = t  # local t and not account for scr refresh
        instrucRight_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrucRight_text_2, 'tStartRefresh')  # time at next scr refresh
        instrucRight_text_2.setAutoDraw(True)
    
    # *instructRight_numbers2* updates
    if instructRight_numbers2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructRight_numbers2.frameNStart = frameN  # exact frame index
        instructRight_numbers2.tStart = t  # local t and not account for scr refresh
        instructRight_numbers2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRight_numbers2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructRight_numbers2.started')
        instructRight_numbers2.setAutoDraw(True)
    
    # *prac_highlight_circle_4* updates
    if prac_highlight_circle_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prac_highlight_circle_4.frameNStart = frameN  # exact frame index
        prac_highlight_circle_4.tStart = t  # local t and not account for scr refresh
        prac_highlight_circle_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prac_highlight_circle_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'prac_highlight_circle_4.started')
        prac_highlight_circle_4.setAutoDraw(True)
    
    # *instructRight_keyResp_2* updates
    waitOnFlip = False
    if instructRight_keyResp_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        instructRight_keyResp_2.frameNStart = frameN  # exact frame index
        instructRight_keyResp_2.tStart = t  # local t and not account for scr refresh
        instructRight_keyResp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRight_keyResp_2, 'tStartRefresh')  # time at next scr refresh
        instructRight_keyResp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructRight_keyResp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructRight_keyResp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructRight_keyResp_2.status == STARTED and not waitOnFlip:
        theseKeys = instructRight_keyResp_2.getKeys(keyList=['8'], waitRelease=False)
        _instructRight_keyResp_2_allKeys.extend(theseKeys)
        if len(_instructRight_keyResp_2_allKeys):
            instructRight_keyResp_2.keys = _instructRight_keyResp_2_allKeys[-1].name  # just the last key pressed
            instructRight_keyResp_2.rt = _instructRight_keyResp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructRightComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructRight" ---
for thisComponent in instructRightComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructRight" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructionLeft" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instrucRight_text.setText('Sometimes the MIDDLE number will be different from the other numbers. However, your goal is to always respond to the MIDDLE number.\n\nBelow, the MIDDLE number is lesser than 5, so you would respond by pressing the left button with your left hand.\n\n\n\n\n\nPress the left button to continue')
instructRight_keyResp.keys = []
instructRight_keyResp.rt = []
_instructRight_keyResp_allKeys = []
# keep track of which components have finished
instructionLeftComponents = [instrucRight_text, instructRight_numbers2_2, prac_highlight_circle, instructRight_keyResp]
for thisComponent in instructionLeftComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructionLeft" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrucRight_text* updates
    if instrucRight_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        instrucRight_text.frameNStart = frameN  # exact frame index
        instrucRight_text.tStart = t  # local t and not account for scr refresh
        instrucRight_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrucRight_text, 'tStartRefresh')  # time at next scr refresh
        instrucRight_text.setAutoDraw(True)
    
    # *instructRight_numbers2_2* updates
    if instructRight_numbers2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructRight_numbers2_2.frameNStart = frameN  # exact frame index
        instructRight_numbers2_2.tStart = t  # local t and not account for scr refresh
        instructRight_numbers2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRight_numbers2_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructRight_numbers2_2.started')
        instructRight_numbers2_2.setAutoDraw(True)
    
    # *prac_highlight_circle* updates
    if prac_highlight_circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prac_highlight_circle.frameNStart = frameN  # exact frame index
        prac_highlight_circle.tStart = t  # local t and not account for scr refresh
        prac_highlight_circle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prac_highlight_circle, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'prac_highlight_circle.started')
        prac_highlight_circle.setAutoDraw(True)
    
    # *instructRight_keyResp* updates
    waitOnFlip = False
    if instructRight_keyResp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        instructRight_keyResp.frameNStart = frameN  # exact frame index
        instructRight_keyResp.tStart = t  # local t and not account for scr refresh
        instructRight_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRight_keyResp, 'tStartRefresh')  # time at next scr refresh
        instructRight_keyResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructRight_keyResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructRight_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructRight_keyResp.status == STARTED and not waitOnFlip:
        theseKeys = instructRight_keyResp.getKeys(keyList=['1'], waitRelease=False)
        _instructRight_keyResp_allKeys.extend(theseKeys)
        if len(_instructRight_keyResp_allKeys):
            instructRight_keyResp.keys = _instructRight_keyResp_allKeys[-1].name  # just the last key pressed
            instructRight_keyResp.rt = _instructRight_keyResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionLeftComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructionLeft" ---
for thisComponent in instructionLeftComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructionLeft" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructionRight" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instructInconRight_text_2.setText('Below, the MIDDLE number is greater than 5, so you would respond by pressing the right button with your right hand.\n\n\n\n\n\n\n\nPress the right button to continue')
instructInconRight_keyResp_2.keys = []
instructInconRight_keyResp_2.rt = []
_instructInconRight_keyResp_2_allKeys = []
# keep track of which components have finished
instructionRightComponents = [instructInconRight_text_2, instructInconRight_letters2, prac_highlight_circle_8, instructInconRight_keyResp_2]
for thisComponent in instructionRightComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructionRight" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructInconRight_text_2* updates
    if instructInconRight_text_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        instructInconRight_text_2.frameNStart = frameN  # exact frame index
        instructInconRight_text_2.tStart = t  # local t and not account for scr refresh
        instructInconRight_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconRight_text_2, 'tStartRefresh')  # time at next scr refresh
        instructInconRight_text_2.setAutoDraw(True)
    
    # *instructInconRight_letters2* updates
    if instructInconRight_letters2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconRight_letters2.frameNStart = frameN  # exact frame index
        instructInconRight_letters2.tStart = t  # local t and not account for scr refresh
        instructInconRight_letters2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconRight_letters2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructInconRight_letters2.started')
        instructInconRight_letters2.setAutoDraw(True)
    
    # *prac_highlight_circle_8* updates
    if prac_highlight_circle_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prac_highlight_circle_8.frameNStart = frameN  # exact frame index
        prac_highlight_circle_8.tStart = t  # local t and not account for scr refresh
        prac_highlight_circle_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prac_highlight_circle_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'prac_highlight_circle_8.started')
        prac_highlight_circle_8.setAutoDraw(True)
    
    # *instructInconRight_keyResp_2* updates
    waitOnFlip = False
    if instructInconRight_keyResp_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        instructInconRight_keyResp_2.frameNStart = frameN  # exact frame index
        instructInconRight_keyResp_2.tStart = t  # local t and not account for scr refresh
        instructInconRight_keyResp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconRight_keyResp_2, 'tStartRefresh')  # time at next scr refresh
        instructInconRight_keyResp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructInconRight_keyResp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructInconRight_keyResp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructInconRight_keyResp_2.status == STARTED and not waitOnFlip:
        theseKeys = instructInconRight_keyResp_2.getKeys(keyList=['8'], waitRelease=False)
        _instructInconRight_keyResp_2_allKeys.extend(theseKeys)
        if len(_instructInconRight_keyResp_2_allKeys):
            instructInconRight_keyResp_2.keys = _instructInconRight_keyResp_2_allKeys[-1].name  # just the last key pressed
            instructInconRight_keyResp_2.rt = _instructInconRight_keyResp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionRightComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructionRight" ---
for thisComponent in instructionRightComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructionRight" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "respond_onceInstruct" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
space_end_keyResp_8.keys = []
space_end_keyResp_8.rt = []
_space_end_keyResp_8_allKeys = []
# keep track of which components have finished
respond_onceInstructComponents = [respond_once_text, space_end_keyResp_8]
for thisComponent in respond_onceInstructComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "respond_onceInstruct" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *respond_once_text* updates
    if respond_once_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        respond_once_text.frameNStart = frameN  # exact frame index
        respond_once_text.tStart = t  # local t and not account for scr refresh
        respond_once_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(respond_once_text, 'tStartRefresh')  # time at next scr refresh
        respond_once_text.setAutoDraw(True)
    
    # *space_end_keyResp_8* updates
    waitOnFlip = False
    if space_end_keyResp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_end_keyResp_8.frameNStart = frameN  # exact frame index
        space_end_keyResp_8.tStart = t  # local t and not account for scr refresh
        space_end_keyResp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_end_keyResp_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'space_end_keyResp_8.started')
        space_end_keyResp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space_end_keyResp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space_end_keyResp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space_end_keyResp_8.status == STARTED and not waitOnFlip:
        theseKeys = space_end_keyResp_8.getKeys(keyList=['8'], waitRelease=False)
        _space_end_keyResp_8_allKeys.extend(theseKeys)
        if len(_space_end_keyResp_8_allKeys):
            space_end_keyResp_8.keys = _space_end_keyResp_8_allKeys[-1].name  # just the last key pressed
            space_end_keyResp_8.rt = _space_end_keyResp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in respond_onceInstructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "respond_onceInstruct" ---
for thisComponent in respond_onceInstructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if space_end_keyResp_8.keys in ['', [], None]:  # No response was made
    space_end_keyResp_8.keys = None
thisExp.addData('space_end_keyResp_8.keys',space_end_keyResp_8.keys)
if space_end_keyResp_8.keys != None:  # we had a response
    thisExp.addData('space_end_keyResp_8.rt', space_end_keyResp_8.rt)
thisExp.nextEntry()
# the Routine "respond_onceInstruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
prac_block_loop = data.TrialHandler(nReps=99.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='prac_block_loop')
thisExp.addLoop(prac_block_loop)  # add the loop to the experiment
thisPrac_block_loop = prac_block_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrac_block_loop.rgb)
if thisPrac_block_loop != None:
    for paramName in thisPrac_block_loop:
        exec('{} = thisPrac_block_loop[paramName]'.format(paramName))

for thisPrac_block_loop in prac_block_loop:
    currentLoop = prac_block_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_block_loop.rgb)
    if thisPrac_block_loop != None:
        for paramName in thisPrac_block_loop:
            exec('{} = thisPrac_block_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "eeg_trigger_check" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    eeg_trigger_checkComponents = []
    for thisComponent in eeg_trigger_checkComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "eeg_trigger_check" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in eeg_trigger_checkComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "eeg_trigger_check" ---
    for thisComponent in eeg_trigger_checkComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "eeg_trigger_check" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "prac_blockReminders" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    space_end_keyResp_9.keys = []
    space_end_keyResp_9.rt = []
    _space_end_keyResp_9_allKeys = []
    # keep track of which components have finished
    prac_blockRemindersComponents = [prac_blockText, prac_reminder_text, space_end_keyResp_9]
    for thisComponent in prac_blockRemindersComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prac_blockReminders" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_blockText* updates
        if prac_blockText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_blockText.frameNStart = frameN  # exact frame index
            prac_blockText.tStart = t  # local t and not account for scr refresh
            prac_blockText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_blockText, 'tStartRefresh')  # time at next scr refresh
            prac_blockText.setAutoDraw(True)
        
        # *prac_reminder_text* updates
        if prac_reminder_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_reminder_text.frameNStart = frameN  # exact frame index
            prac_reminder_text.tStart = t  # local t and not account for scr refresh
            prac_reminder_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_reminder_text, 'tStartRefresh')  # time at next scr refresh
            prac_reminder_text.setAutoDraw(True)
        
        # *space_end_keyResp_9* updates
        waitOnFlip = False
        if space_end_keyResp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            space_end_keyResp_9.frameNStart = frameN  # exact frame index
            space_end_keyResp_9.tStart = t  # local t and not account for scr refresh
            space_end_keyResp_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space_end_keyResp_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'space_end_keyResp_9.started')
            space_end_keyResp_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(space_end_keyResp_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(space_end_keyResp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if space_end_keyResp_9.status == STARTED and not waitOnFlip:
            theseKeys = space_end_keyResp_9.getKeys(keyList=['c'], waitRelease=False)
            _space_end_keyResp_9_allKeys.extend(theseKeys)
            if len(_space_end_keyResp_9_allKeys):
                space_end_keyResp_9.keys = _space_end_keyResp_9_allKeys[-1].name  # just the last key pressed
                space_end_keyResp_9.rt = _space_end_keyResp_9_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_blockRemindersComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prac_blockReminders" ---
    for thisComponent in prac_blockRemindersComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if space_end_keyResp_9.keys in ['', [], None]:  # No response was made
        space_end_keyResp_9.keys = None
    prac_block_loop.addData('space_end_keyResp_9.keys',space_end_keyResp_9.keys)
    if space_end_keyResp_9.keys != None:  # we had a response
        prac_block_loop.addData('space_end_keyResp_9.rt', space_end_keyResp_9.rt)
    # the Routine "prac_blockReminders" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "prac_initFixation" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from prac_endTask_code
    # make range from a to b in n stepsizes
    ISIRange = np.linspace(2600, 3000, 400)
    
    # picking from a shuffled array is easier for random selection in JS
    shuffle(ISIRange)
    thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
    
    # empty lists of used letters
    used_letters = []
    shown_letters = []
    initFixation_img_2.setImage('img/fixationCross.png')
    # keep track of which components have finished
    prac_initFixationComponents = [initFixation_img_2]
    for thisComponent in prac_initFixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prac_initFixation" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *initFixation_img_2* updates
        if initFixation_img_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            initFixation_img_2.frameNStart = frameN  # exact frame index
            initFixation_img_2.tStart = t  # local t and not account for scr refresh
            initFixation_img_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(initFixation_img_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'initFixation_img_2.started')
            initFixation_img_2.setAutoDraw(True)
        if initFixation_img_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > initFixation_img_2.tStartRefresh + thisISI-frameTolerance:
                # keep track of stop time/frame for later
                initFixation_img_2.tStop = t  # not accounting for scr refresh
                initFixation_img_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'initFixation_img_2.stopped')
                initFixation_img_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_initFixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prac_initFixation" ---
    for thisComponent in prac_initFixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "prac_initFixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    prac_trial_loop = data.TrialHandler(nReps=10.0, method='fullRandom', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('prac_trials.xlsx'),
        seed=None, name='prac_trial_loop')
    thisExp.addLoop(prac_trial_loop)  # add the loop to the experiment
    thisPrac_trial_loop = prac_trial_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_trial_loop.rgb)
    if thisPrac_trial_loop != None:
        for paramName in thisPrac_trial_loop:
            exec('{} = thisPrac_trial_loop[paramName]'.format(paramName))
    
    for thisPrac_trial_loop in prac_trial_loop:
        currentLoop = prac_trial_loop
        # abbreviate parameter names if possible (e.g. rgb = thisPrac_trial_loop.rgb)
        if thisPrac_trial_loop != None:
            for paramName in thisPrac_trial_loop:
                exec('{} = thisPrac_trial_loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "prac_stimRoutine" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from prac_flanker_numbers_code
        # take flanker letter and add to used flanker letters
        flanker_stim_large = NUMBERS_LARGE.copy()
        flanker_stim_small = NUMBERS_SMALL.copy()
        shuffle(flanker_stim_large)
        shuffle(flanker_stim_small)
        
        # create flanker stimuli based on the congruency and case
        if congruent == 1 and target == "large":
            flanker_stim = "{}".format(flanker_stim_large[0]*5)
        elif congruent == 1 and target == "small":
            flanker_stim = "{}".format(flanker_stim_small[0]*5)
        elif congruent == 0 and target == "large":
            flanker_stim = "{}{}{}".format(flanker_stim_small[0]*2,
            flanker_stim_large[0], flanker_stim_small[0]*2)
        elif congruent == 0 and target == "small":
            flanker_stim = "{}{}{}".format(flanker_stim_large[0]*2,
            flanker_stim_small[0], flanker_stim_large[0]*2)
        else: flanker_stim = "error"
        # Run 'Begin Routine' code from prac_isi_code
        # pick the ISI for the next routine
        # for the online version, this code component should be set to 'both' to remove the 'np'
        # at the start of np.linspace (this is a python library JS won't know what to call. 
        
        # make range from a to b in n stepsizes
        ISIRange = np.linspace(1300, 1800, 500)
        
        # picking from a shuffled array is easier for random selection in JS
        shuffle(ISIRange)
        thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
        
        # save this ISI to our output file
        prac_trial_loop.addData('prac_flanker_ISI', thisISI)
        
        # show in console for debugging
        #print('thisISI: ', thisISI)
        prac_flanker_text_stim.setText(flanker_stim)
        prac_fixImg.setImage('img/fixationCross.png')
        prac_stim_keyResp.keys = []
        prac_stim_keyResp.rt = []
        _prac_stim_keyResp_allKeys = []
        # keep track of which components have finished
        prac_stimRoutineComponents = [prac_flanker_text_stim, prac_fixImg, prac_stim_keyResp]
        for thisComponent in prac_stimRoutineComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "prac_stimRoutine" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *prac_flanker_text_stim* updates
            if prac_flanker_text_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_flanker_text_stim.frameNStart = frameN  # exact frame index
                prac_flanker_text_stim.tStart = t  # local t and not account for scr refresh
                prac_flanker_text_stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_flanker_text_stim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_flanker_text_stim.started')
                prac_flanker_text_stim.setAutoDraw(True)
            if prac_flanker_text_stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_flanker_text_stim.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_flanker_text_stim.tStop = t  # not accounting for scr refresh
                    prac_flanker_text_stim.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'prac_flanker_text_stim.stopped')
                    prac_flanker_text_stim.setAutoDraw(False)
            
            # *prac_fixImg* updates
            if prac_fixImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_fixImg.frameNStart = frameN  # exact frame index
                prac_fixImg.tStart = t  # local t and not account for scr refresh
                prac_fixImg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_fixImg, 'tStartRefresh')  # time at next scr refresh
                prac_fixImg.setAutoDraw(True)
            if prac_fixImg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_fixImg.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_fixImg.tStop = t  # not accounting for scr refresh
                    prac_fixImg.frameNStop = frameN  # exact frame index
                    prac_fixImg.setAutoDraw(False)
            
            # *prac_stim_keyResp* updates
            waitOnFlip = False
            if prac_stim_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_stim_keyResp.frameNStart = frameN  # exact frame index
                prac_stim_keyResp.tStart = t  # local t and not account for scr refresh
                prac_stim_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_stim_keyResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_stim_keyResp.started')
                prac_stim_keyResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(prac_stim_keyResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(prac_stim_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if prac_stim_keyResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_stim_keyResp.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_stim_keyResp.tStop = t  # not accounting for scr refresh
                    prac_stim_keyResp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'prac_stim_keyResp.stopped')
                    prac_stim_keyResp.status = FINISHED
            if prac_stim_keyResp.status == STARTED and not waitOnFlip:
                theseKeys = prac_stim_keyResp.getKeys(keyList=['1','8'], waitRelease=False)
                _prac_stim_keyResp_allKeys.extend(theseKeys)
                if len(_prac_stim_keyResp_allKeys):
                    prac_stim_keyResp.keys = [key.name for key in _prac_stim_keyResp_allKeys]  # storing all keys
                    prac_stim_keyResp.rt = [key.rt for key in _prac_stim_keyResp_allKeys]
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prac_stimRoutineComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "prac_stimRoutine" ---
        for thisComponent in prac_stimRoutineComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from prac_flanker_numbers_code
        # write flanker stimuli to data
        prac_trial_loop.addData('prac_flanker_stim',
        flanker_stim)
        # check responses
        if prac_stim_keyResp.keys in ['', [], None]:  # No response was made
            prac_stim_keyResp.keys = None
        prac_trial_loop.addData('prac_stim_keyResp.keys',prac_stim_keyResp.keys)
        if prac_stim_keyResp.keys != None:  # we had a response
            prac_trial_loop.addData('prac_stim_keyResp.rt', prac_stim_keyResp.rt)
        # Run 'End Routine' code from prac_accuracy_code
        trialNum = trialNum + 1 #iterate trial number for this block
        
        
        if prac_stim_keyResp.keys: #if at least one response was made this trial
            if prac_stim_keyResp.keys[0] == '1': #if the FIRST button pressed was a '1'
                if target == 'small': #if a left target stim was shown this trial
                    accuracy = 1 #mark this trial as correct
                    numCorr = numCorr +1 #iterate number of correct responses for this supertrial
                elif target == 'large': #if a right target stim was shown this trial
                    accuracy = 0 #mark this trial as an error
            elif prac_stim_keyResp.keys[0] == '8': #if the FIRST button pressed was a '8'
                if target == 'large': #if a right target stim was shown this trial
                    accuracy = 1 #mark this trial as correct
                    numCorr = numCorr +1 #iterate number of correct responses for this supertrial
                elif target == 'small': #if a left target stim was shown this trial
                    accuracy = 0 #mark this trial as an error
        
        elif not prac_stim_keyResp.keys: # if no response was made
            accuracy = 0
                    
        # save this trial's accuracy to our output file
        prac_trial_loop.addData('prac_flanker_accuracy', accuracy)
        # the Routine "prac_stimRoutine" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 10.0 repeats of 'prac_trial_loop'
    
    
    # --- Prepare to start Routine "prac_blockFeed" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from prac_blockFeed_code
    blockAcc = numCorr / trialNum # compute accuracy for this block
    
    if blockAcc >= FL_THRESH: # if accuracy >= threshold then say practice is complete and end practice loop to continue to main exp
        outPut = 'Well done! Now you are ready to play the real game!' #feedback presented
        prac_block_loop.finished = True #end practice loop to continue to main exp
    elif blockAcc <= FL_THRESH: # if accuracy < threshold then say that practice needs to be repeated and DO NOT end practice loop, instead, allow it to repeat
        outPut = 'Please try the practice again' #feedback presented
        prac_block_loop.finished = False #DO NOT end practice loop and allow to repeat
    
    prac_block_loop.addData('prac_flanker_blockAcc', blockAcc)
    
    # reset the following variables to zero before the next practice block starts
    trialNum = 0
    numCorr = 0
    prac_blockFeed_text_3.setText(outPut)
    prac_blockFeed_keyResp.keys = []
    prac_blockFeed_keyResp.rt = []
    _prac_blockFeed_keyResp_allKeys = []
    # keep track of which components have finished
    prac_blockFeedComponents = [prac_blockFeed_text_3, prac_pressContinue_3, prac_blockFeed_keyResp]
    for thisComponent in prac_blockFeedComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prac_blockFeed" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_blockFeed_text_3* updates
        if prac_blockFeed_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_blockFeed_text_3.frameNStart = frameN  # exact frame index
            prac_blockFeed_text_3.tStart = t  # local t and not account for scr refresh
            prac_blockFeed_text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_blockFeed_text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_blockFeed_text_3.started')
            prac_blockFeed_text_3.setAutoDraw(True)
        
        # *prac_pressContinue_3* updates
        if prac_pressContinue_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_pressContinue_3.frameNStart = frameN  # exact frame index
            prac_pressContinue_3.tStart = t  # local t and not account for scr refresh
            prac_pressContinue_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_pressContinue_3, 'tStartRefresh')  # time at next scr refresh
            prac_pressContinue_3.setAutoDraw(True)
        
        # *prac_blockFeed_keyResp* updates
        waitOnFlip = False
        if prac_blockFeed_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_blockFeed_keyResp.frameNStart = frameN  # exact frame index
            prac_blockFeed_keyResp.tStart = t  # local t and not account for scr refresh
            prac_blockFeed_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_blockFeed_keyResp, 'tStartRefresh')  # time at next scr refresh
            prac_blockFeed_keyResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(prac_blockFeed_keyResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(prac_blockFeed_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if prac_blockFeed_keyResp.status == STARTED and not waitOnFlip:
            theseKeys = prac_blockFeed_keyResp.getKeys(keyList=['c','s'], waitRelease=False)
            _prac_blockFeed_keyResp_allKeys.extend(theseKeys)
            if len(_prac_blockFeed_keyResp_allKeys):
                prac_blockFeed_keyResp.keys = _prac_blockFeed_keyResp_allKeys[-1].name  # just the last key pressed
                prac_blockFeed_keyResp.rt = _prac_blockFeed_keyResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_blockFeedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prac_blockFeed" ---
    for thisComponent in prac_blockFeedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from prac_blockFeed_code
    if prac_blockFeed_keyResp.keys[-1] == 's':
        prac_block_loop.finished = True #end practice loop to continue to main exp
    # the Routine "prac_blockFeed" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 99.0 repeats of 'prac_block_loop'


# set up handler to look after randomisation of conditions etc
task_condition_loop = data.TrialHandler(nReps=6.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='task_condition_loop')
thisExp.addLoop(task_condition_loop)  # add the loop to the experiment
thisTask_condition_loop = task_condition_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTask_condition_loop.rgb)
if thisTask_condition_loop != None:
    for paramName in thisTask_condition_loop:
        exec('{} = thisTask_condition_loop[paramName]'.format(paramName))

for thisTask_condition_loop in task_condition_loop:
    currentLoop = task_condition_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTask_condition_loop.rgb)
    if thisTask_condition_loop != None:
        for paramName in thisTask_condition_loop:
            exec('{} = thisTask_condition_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "task_condition" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from task_blockReminder_code_2
    #if endCondition: # skip all trials for this condition; participant will not play game.
    #    task_block_loop.finished = True
    #    continueRoutine = False
    
    blockCounter = blockCounter +1
    
    if blockCounter == 1:
        blockNumText = 'Block 1 of 6'
    elif blockCounter == 2:
        blockNumText = 'Block 2 of 6'
    elif blockCounter == 3:
        blockNumText = 'Block 3 of 6'
    elif blockCounter == 4:
        blockNumText = 'Block 4 of 6'
    elif blockCounter == 5:
        blockNumText = 'Block 5 of 6'
    elif blockCounter == 6:
        blockNumText = 'Block 6 of 6'
    task_blockText_2.setText(blockNumText)
    space_end_keyResp_11.keys = []
    space_end_keyResp_11.rt = []
    _space_end_keyResp_11_allKeys = []
    # keep track of which components have finished
    task_conditionComponents = [task_blockText_2, condition_reminder_text, space_end_keyResp_11]
    for thisComponent in task_conditionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "task_condition" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *task_blockText_2* updates
        if task_blockText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            task_blockText_2.frameNStart = frameN  # exact frame index
            task_blockText_2.tStart = t  # local t and not account for scr refresh
            task_blockText_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(task_blockText_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'task_blockText_2.started')
            task_blockText_2.setAutoDraw(True)
        
        # *condition_reminder_text* updates
        if condition_reminder_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            condition_reminder_text.frameNStart = frameN  # exact frame index
            condition_reminder_text.tStart = t  # local t and not account for scr refresh
            condition_reminder_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(condition_reminder_text, 'tStartRefresh')  # time at next scr refresh
            condition_reminder_text.setAutoDraw(True)
        
        # *space_end_keyResp_11* updates
        waitOnFlip = False
        if space_end_keyResp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            space_end_keyResp_11.frameNStart = frameN  # exact frame index
            space_end_keyResp_11.tStart = t  # local t and not account for scr refresh
            space_end_keyResp_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space_end_keyResp_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'space_end_keyResp_11.started')
            space_end_keyResp_11.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(space_end_keyResp_11.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(space_end_keyResp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if space_end_keyResp_11.status == STARTED and not waitOnFlip:
            theseKeys = space_end_keyResp_11.getKeys(keyList=['8'], waitRelease=False)
            _space_end_keyResp_11_allKeys.extend(theseKeys)
            if len(_space_end_keyResp_11_allKeys):
                space_end_keyResp_11.keys = _space_end_keyResp_11_allKeys[-1].name  # just the last key pressed
                space_end_keyResp_11.rt = _space_end_keyResp_11_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in task_conditionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "task_condition" ---
    for thisComponent in task_conditionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if space_end_keyResp_11.keys in ['', [], None]:  # No response was made
        space_end_keyResp_11.keys = None
    task_condition_loop.addData('space_end_keyResp_11.keys',space_end_keyResp_11.keys)
    if space_end_keyResp_11.keys != None:  # we had a response
        task_condition_loop.addData('space_end_keyResp_11.rt', space_end_keyResp_11.rt)
    # the Routine "task_condition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "eeg_trigger_check_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    eeg_trigger_check_2Components = []
    for thisComponent in eeg_trigger_check_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "eeg_trigger_check_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in eeg_trigger_check_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "eeg_trigger_check_2" ---
    for thisComponent in eeg_trigger_check_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "eeg_trigger_check_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "supertrial_initFixation" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from endTask_code_4
    # make range from a to b in n stepsizes
    ISIRange = np.linspace(2600, 3000, 400)
    
    # picking from a shuffled array is easier for random selection in JS
    shuffle(ISIRange)
    thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
    
    # save this ISI to our output file
    task_condition_loop.addData('ISI_fixation', thisISI)
    initFixation_img_5.setImage('img/fixationCross.png')
    # keep track of which components have finished
    supertrial_initFixationComponents = [initFixation_img_5]
    for thisComponent in supertrial_initFixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "supertrial_initFixation" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *initFixation_img_5* updates
        if initFixation_img_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            initFixation_img_5.frameNStart = frameN  # exact frame index
            initFixation_img_5.tStart = t  # local t and not account for scr refresh
            initFixation_img_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(initFixation_img_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'initFixation_img_5.started')
            initFixation_img_5.setAutoDraw(True)
        if initFixation_img_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > initFixation_img_5.tStartRefresh + thisISI-frameTolerance:
                # keep track of stop time/frame for later
                initFixation_img_5.tStop = t  # not accounting for scr refresh
                initFixation_img_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'initFixation_img_5.stopped')
                initFixation_img_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in supertrial_initFixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "supertrial_initFixation" ---
    for thisComponent in supertrial_initFixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "supertrial_initFixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    task_trial_loop = data.TrialHandler(nReps=10.0, method='fullRandom', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('4.xlsx'),
        seed=None, name='task_trial_loop')
    thisExp.addLoop(task_trial_loop)  # add the loop to the experiment
    thisTask_trial_loop = task_trial_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTask_trial_loop.rgb)
    if thisTask_trial_loop != None:
        for paramName in thisTask_trial_loop:
            exec('{} = thisTask_trial_loop[paramName]'.format(paramName))
    
    for thisTask_trial_loop in task_trial_loop:
        currentLoop = task_trial_loop
        # abbreviate parameter names if possible (e.g. rgb = thisTask_trial_loop.rgb)
        if thisTask_trial_loop != None:
            for paramName in thisTask_trial_loop:
                exec('{} = thisTask_trial_loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "task_stimRoutine" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from flanker_numbers_code
        # take flanker letter and add to used flanker letters
        flanker_stim_large = NUMBERS_LARGE.copy()
        flanker_stim_small = NUMBERS_SMALL.copy()
        shuffle(flanker_stim_large)
        shuffle(flanker_stim_small)
        
        # create flanker stimuli based on the congruency and case
        if congruent == 1 and target == "large":
            flanker_stim = "{}".format(flanker_stim_large[0]*5)
        elif congruent == 1 and target == "small":
            flanker_stim = "{}".format(flanker_stim_small[0]*5)
        elif congruent == 0 and target == "large":
            flanker_stim = "{}{}{}".format(flanker_stim_small[0]*2,
            flanker_stim_large[0], flanker_stim_small[0]*2)
        elif congruent == 0 and target == "small":
            flanker_stim = "{}{}{}".format(flanker_stim_large[0]*2,
            flanker_stim_small[0], flanker_stim_large[0]*2)
        else: flanker_stim = "error"
        # Run 'Begin Routine' code from task_isi_code
        # pick the ISI for the next routine
        # for the online version, this code component should be set to 'both' to remove the 'np'
        # at the start of np.linspace (this is a python library JS won't know what to call. 
        
        # make range from a to b in n stepsizes
        ISIRange = np.linspace(1300, 1800, 500)
        
        # picking from a shuffled array is easier for random selection in JS
        shuffle(ISIRange)
        thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
        
        # save this ISI to our output file
        task_trial_loop.addData('ISI', thisISI)
        flanker_text_stim.setText(flanker_stim)
        task_fixImg.setImage('img/fixationCross.png')
        task_stim_keyResp.keys = []
        task_stim_keyResp.rt = []
        _task_stim_keyResp_allKeys = []
        # keep track of which components have finished
        task_stimRoutineComponents = [flanker_text_stim, task_fixImg, task_stim_keyResp]
        for thisComponent in task_stimRoutineComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "task_stimRoutine" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *flanker_text_stim* updates
            if flanker_text_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                flanker_text_stim.frameNStart = frameN  # exact frame index
                flanker_text_stim.tStart = t  # local t and not account for scr refresh
                flanker_text_stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(flanker_text_stim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'flanker_text_stim.started')
                flanker_text_stim.setAutoDraw(True)
            if flanker_text_stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > flanker_text_stim.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    flanker_text_stim.tStop = t  # not accounting for scr refresh
                    flanker_text_stim.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'flanker_text_stim.stopped')
                    flanker_text_stim.setAutoDraw(False)
            
            # *task_fixImg* updates
            if task_fixImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                task_fixImg.frameNStart = frameN  # exact frame index
                task_fixImg.tStart = t  # local t and not account for scr refresh
                task_fixImg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task_fixImg, 'tStartRefresh')  # time at next scr refresh
                task_fixImg.setAutoDraw(True)
            if task_fixImg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > task_fixImg.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    task_fixImg.tStop = t  # not accounting for scr refresh
                    task_fixImg.frameNStop = frameN  # exact frame index
                    task_fixImg.setAutoDraw(False)
            
            # *task_stim_keyResp* updates
            waitOnFlip = False
            if task_stim_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                task_stim_keyResp.frameNStart = frameN  # exact frame index
                task_stim_keyResp.tStart = t  # local t and not account for scr refresh
                task_stim_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task_stim_keyResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'task_stim_keyResp.started')
                task_stim_keyResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(task_stim_keyResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(task_stim_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if task_stim_keyResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > task_stim_keyResp.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    task_stim_keyResp.tStop = t  # not accounting for scr refresh
                    task_stim_keyResp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'task_stim_keyResp.stopped')
                    task_stim_keyResp.status = FINISHED
            if task_stim_keyResp.status == STARTED and not waitOnFlip:
                theseKeys = task_stim_keyResp.getKeys(keyList=['1','8'], waitRelease=False)
                _task_stim_keyResp_allKeys.extend(theseKeys)
                if len(_task_stim_keyResp_allKeys):
                    task_stim_keyResp.keys = [key.name for key in _task_stim_keyResp_allKeys]  # storing all keys
                    task_stim_keyResp.rt = [key.rt for key in _task_stim_keyResp_allKeys]
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in task_stimRoutineComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "task_stimRoutine" ---
        for thisComponent in task_stimRoutineComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from flanker_numbers_code
        # write flanker stimuli to data
        task_trial_loop.addData('flanker_stim',
        flanker_stim)
        # check responses
        if task_stim_keyResp.keys in ['', [], None]:  # No response was made
            task_stim_keyResp.keys = None
        task_trial_loop.addData('task_stim_keyResp.keys',task_stim_keyResp.keys)
        if task_stim_keyResp.keys != None:  # we had a response
            task_trial_loop.addData('task_stim_keyResp.rt', task_stim_keyResp.rt)
        # Run 'End Routine' code from task_accuracy_code
        #iterate trial number for this block
        trialNum = trialNum + 1
        
        if task_stim_keyResp.keys: #if at least one response was made this trial
            if task_stim_keyResp.keys[0] == '1': #if the FIRST button pressed was a '1'
                if target == 'small': #if a left target stim was shown this trial
                    accuracy = 1 #mark this trial as correct
                    numCorr = numCorr +1 #iterate number of correct responses for this supertrial
                elif target == 'large': #if a right target stim was shown this trial
                    accuracy = 0 #mark this trial as an error
            elif task_stim_keyResp.keys[0] == '8': #if the FIRST button pressed was a '8'
                if target == 'large': #if a right target stim was shown this trial
                    accuracy = 1 #mark this trial as correct
                    numCorr = numCorr +1 #iterate number of correct responses for this supertrial
                elif target == 'small': #if a left target stim was shown this trial
                    accuracy = 0 #mark this trial as an error
        
        # save this trial's accuracy to our output file
        task_trial_loop.addData('fl_accuracy', accuracy) 
        # the Routine "task_stimRoutine" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 10.0 repeats of 'task_trial_loop'
    
    
    # --- Prepare to start Routine "task_conditionComplete" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    space_end_keyResp_13.keys = []
    space_end_keyResp_13.rt = []
    _space_end_keyResp_13_allKeys = []
    # keep track of which components have finished
    task_conditionCompleteComponents = [conditionComplete_text, space_end_keyResp_13]
    for thisComponent in task_conditionCompleteComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "task_conditionComplete" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *conditionComplete_text* updates
        if conditionComplete_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            conditionComplete_text.frameNStart = frameN  # exact frame index
            conditionComplete_text.tStart = t  # local t and not account for scr refresh
            conditionComplete_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(conditionComplete_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'conditionComplete_text.started')
            conditionComplete_text.setAutoDraw(True)
        
        # *space_end_keyResp_13* updates
        waitOnFlip = False
        if space_end_keyResp_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            space_end_keyResp_13.frameNStart = frameN  # exact frame index
            space_end_keyResp_13.tStart = t  # local t and not account for scr refresh
            space_end_keyResp_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space_end_keyResp_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'space_end_keyResp_13.started')
            space_end_keyResp_13.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(space_end_keyResp_13.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(space_end_keyResp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if space_end_keyResp_13.status == STARTED and not waitOnFlip:
            theseKeys = space_end_keyResp_13.getKeys(keyList=['8'], waitRelease=False)
            _space_end_keyResp_13_allKeys.extend(theseKeys)
            if len(_space_end_keyResp_13_allKeys):
                space_end_keyResp_13.keys = _space_end_keyResp_13_allKeys[-1].name  # just the last key pressed
                space_end_keyResp_13.rt = _space_end_keyResp_13_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in task_conditionCompleteComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "task_conditionComplete" ---
    for thisComponent in task_conditionCompleteComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from stimTask_code_4
    # save this trial's flanker accuracy to our output file
    fl_accuracy = numCorr / trialNum
    task_condition_loop.addData('block_accuracy', fl_accuracy)
    
    # reset
    trialNum = 0
    numCorr = 0
    # check responses
    if space_end_keyResp_13.keys in ['', [], None]:  # No response was made
        space_end_keyResp_13.keys = None
    task_condition_loop.addData('space_end_keyResp_13.keys',space_end_keyResp_13.keys)
    if space_end_keyResp_13.keys != None:  # we had a response
        task_condition_loop.addData('space_end_keyResp_13.rt', space_end_keyResp_13.rt)
    # the Routine "task_conditionComplete" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 6.0 repeats of 'task_condition_loop'


# --- Prepare to start Routine "task_finish" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
space_end_keyResp_12.keys = []
space_end_keyResp_12.rt = []
_space_end_keyResp_12_allKeys = []
# keep track of which components have finished
task_finishComponents = [taskComplete_text, space_end_keyResp_12]
for thisComponent in task_finishComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "task_finish" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *taskComplete_text* updates
    if taskComplete_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        taskComplete_text.frameNStart = frameN  # exact frame index
        taskComplete_text.tStart = t  # local t and not account for scr refresh
        taskComplete_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(taskComplete_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'taskComplete_text.started')
        taskComplete_text.setAutoDraw(True)
    
    # *space_end_keyResp_12* updates
    waitOnFlip = False
    if space_end_keyResp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_end_keyResp_12.frameNStart = frameN  # exact frame index
        space_end_keyResp_12.tStart = t  # local t and not account for scr refresh
        space_end_keyResp_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_end_keyResp_12, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'space_end_keyResp_12.started')
        space_end_keyResp_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space_end_keyResp_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space_end_keyResp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space_end_keyResp_12.status == STARTED and not waitOnFlip:
        theseKeys = space_end_keyResp_12.getKeys(keyList=['c'], waitRelease=False)
        _space_end_keyResp_12_allKeys.extend(theseKeys)
        if len(_space_end_keyResp_12_allKeys):
            space_end_keyResp_12.keys = _space_end_keyResp_12_allKeys[-1].name  # just the last key pressed
            space_end_keyResp_12.rt = _space_end_keyResp_12_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in task_finishComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "task_finish" ---
for thisComponent in task_finishComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if space_end_keyResp_12.keys in ['', [], None]:  # No response was made
    space_end_keyResp_12.keys = None
thisExp.addData('space_end_keyResp_12.keys',space_end_keyResp_12.keys)
if space_end_keyResp_12.keys != None:  # we had a response
    thisExp.addData('space_end_keyResp_12.rt', space_end_keyResp_12.rt)
thisExp.nextEntry()
# the Routine "task_finish" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# Run 'End Experiment' code from setup_code
win.mouseVisible = True #make the mouse cursor visable again
#port.write([0xFF]) #set port values back to default state (FF)
#time.sleep(PulseWidth) #wait PulseWidth amount of time before doing anything else
#port.close() #close port opened at start of exp

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
