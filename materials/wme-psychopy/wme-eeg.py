#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on November 09, 2023, at 10:20
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
expName = 'wme-eeg'  # from the Builder filename that created this script
expInfo = {
    'id': '',
    'counterbalance': ['L', 'R'],
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
filename = _thisDir + os.sep + u'data/sub-%s_%s_s%s_r%s_e1_%s' % (expInfo['id'], expName, expInfo['session'], expInfo['run'], expInfo['counterbalance'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\NDCLab\\Desktop\\Experiments\\wme\\wme-eeg.py',
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
    monitor='sys-1-asus', color=[0,0,0], colorSpace='rgb',
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

# whether we want letters from WM and flanker could be same
repeat_letters = False
# whether we want letters inside flanker could be same
repeat_letters_fl = False

used_letters = [] # letters used in WM and flanker trials (to prevent repeates in WM and flanker within supertrial)
used_letters_fl = [] # letters used in flanker trials (to prevent repeats within flanker trials)
shown_letters = [] # exact letters shown in WM (i.e., considered lower-/uppercase)

cross_y = -0.71 # position of fix cross (to easily adjust when switch from macbook to asus), for asus should be -0.71

# initialize thresholds for flanker and WM practice
wm_thresh = 0.7
fl_thresh = 0.7

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

# consontant capital letters without Y and L 
# (because lowercase l looks like capitalized i)
wm_letters = ['B', 'C', 'D',
'F', 'G', 'H',
'J', 'K', #'L',
'M', 'N', 'P',
'Q', 'R', 'S',
'T', 'V', 'W',
'X', 'Z']

# initialize the thisISI variable used for all ISI
thisISI = 0

# initialize reminders for flanker trials
if expInfo["counterbalance"] == "L":
    left_reminder = "Left button\nCAPITALIZED"
    right_reminder = "Right button\nlowercase"
elif expInfo["counterbalance"] == "R":
    left_reminder = "Left button\nlowercase"
    right_reminder = "Right button\nCAPITALIZED"

# --- Initialize components for Routine "welcome" ---
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text='Today you are going to play 2 different games. In both games you will be dealing with letters, but in a different way. Before starting playing you will do some practice to learn the rules.\n\nPress SPACE to proceed to the practice',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
space_end_keyResp = keyboard.Keyboard()

# --- Initialize components for Routine "instructWM1" ---
instructWM_text1 = visual.TextStim(win=win, name='instructWM_text1',
    text='Welcome to the Memory Game! In this game, you will be shown a set of letters presented one by one. Your goal is to remember these letters and recall them in the order they appeared without making mistakes. Please, do not say the letters out loud.\n\n\nPress SPACE to see an example',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
space_end_keyResp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "prac_initFixaion_WM" ---
initFixation_img_4 = visual.ImageStim(
    win=win,
    name='initFixation_img_4', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, cross_y), size=(.24, .24),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "instructWM_seq1" ---
wm_stim_2 = visual.TextStim(win=win, name='wm_stim_2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
wm_fixImg_2 = visual.ImageStim(
    win=win,
    name='wm_fixImg_2', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, cross_y), size=(.24, .24),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "instructWM3" ---
instructWM_text3 = visual.TextStim(win=win, name='instructWM_text3',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
space_end_keyResp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "prac_initFixaion_WM" ---
initFixation_img_4 = visual.ImageStim(
    win=win,
    name='initFixation_img_4', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, cross_y), size=(.24, .24),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "instructWM_seq2" ---
wm_stim_3 = visual.TextStim(win=win, name='wm_stim_3',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
wm_fixImg_3 = visual.ImageStim(
    win=win,
    name='wm_fixImg_3', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, cross_y), size=(.24, .24),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "instructWM4" ---
instructWM_text4 = visual.TextStim(win=win, name='instructWM_text4',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
space_end_keyResp_4 = keyboard.Keyboard()

# --- Initialize components for Routine "prac_initFixaion_WM" ---
initFixation_img_4 = visual.ImageStim(
    win=win,
    name='initFixation_img_4', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, cross_y), size=(.24, .24),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "instructWM_seq3" ---
wm_stim_6 = visual.TextStim(win=win, name='wm_stim_6',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
wm_fixImg_6 = visual.ImageStim(
    win=win,
    name='wm_fixImg_6', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, cross_y), size=(.24, .24),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "instructWM_recall" ---
wm_recall_text_4 = visual.TextStim(win=win, name='wm_recall_text_4',
    text='Type the letters from the Memory Game in the order they appeared\n\n\n\n\n\n\n\nPress SPACE when you finish',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
wm_recall_typedResp_4 = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(0.5, 0.5), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='wm_recall_typedResp_4',
     autoLog=True,
)
wm_recall_keyResp_4 = keyboard.Keyboard()
underscores_text_4 = visual.TextStim(win=win, name='underscores_text_4',
    text='',
    font='Arial',
    pos=(0, 0.01), height=0.045, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
full_response_reminder_text_4 = visual.TextStim(win=win, name='full_response_reminder_text_4',
    text='',
    font='Arial',
    pos=(0, -0.1), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "instructWM_fb" ---
instructWM_fb_text = visual.TextStim(win=win, name='instructWM_fb_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructWM_cont_text = visual.TextStim(win=win, name='instructWM_cont_text',
    text='\n\n\n\n\n\n\n\nPress SPACE to continue practicing',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
space_end_keyResp_5 = keyboard.Keyboard()

# --- Initialize components for Routine "prac_initFixaion_WM" ---
initFixation_img_4 = visual.ImageStim(
    win=win,
    name='initFixation_img_4', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, cross_y), size=(.24, .24),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "pracWM_seq" ---
wm_stim_4 = visual.TextStim(win=win, name='wm_stim_4',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
wm_fixImg_4 = visual.ImageStim(
    win=win,
    name='wm_fixImg_4', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, cross_y), size=(.24, .24),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "pracWM_recall" ---
wm_recall_text_2 = visual.TextStim(win=win, name='wm_recall_text_2',
    text='Type the letters from the Memory Game in the order they appeared\n\n\n\n\n\n\n\nPress SPACE when you finish',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
wm_recall_typedResp_2 = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(0.5, 0.5), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='wm_recall_typedResp_2',
     autoLog=True,
)
wm_recall_keyResp_2 = keyboard.Keyboard()
underscores_text_2 = visual.TextStim(win=win, name='underscores_text_2',
    text='',
    font='Arial',
    pos=(0, 0.01), height=0.045, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
full_response_reminder_text_2 = visual.TextStim(win=win, name='full_response_reminder_text_2',
    text='',
    font='Arial',
    pos=(0, -0.1), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "pracWM_fb" ---
instructWM_fb_text_2 = visual.TextStim(win=win, name='instructWM_fb_text_2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructWM_cont_text_2 = visual.TextStim(win=win, name='instructWM_cont_text_2',
    text='\n\n\n\n\n\n\n\nPress SPACE to continue practicing',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
space_end_keyResp_6 = keyboard.Keyboard()

# --- Initialize components for Routine "pracWM_feed" ---
prac_blockFeed_text_2 = visual.TextStim(win=win, name='prac_blockFeed_text_2',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
prac_pressContinue_2 = visual.TextStim(win=win, name='prac_pressContinue_2',
    text='Press SPACE to continue practicing',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
prac_blockFeed_keyResp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "instructMiddle" ---
welcome_text_2_L = visual.TextStim(win=win, name='welcome_text_2_L',
    text='',
    font='Arial',
    units='height', pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
welcome_text_2_R = visual.TextStim(win=win, name='welcome_text_2_R',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
space_end_keyResp_7 = keyboard.Keyboard()

# --- Initialize components for Routine "instructRight" ---
instructRight_text_2_L = visual.TextStim(win=win, name='instructRight_text_2_L',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructRight_text_2_R = visual.TextStim(win=win, name='instructRight_text_2_R',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
instructRight_letters2 = visual.TextStim(win=win, name='instructRight_letters2',
    text='',
    font='Arial',
    pos=(0, -.05), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
prac_highlight_circle_2 = visual.ShapeStim(
    win=win, name='prac_highlight_circle_2',
    size=(0.05, 0.05), vertices='circle',
    ori=0.0, pos=(0, -0.053), anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor='yellow', fillColor='yellow',
    opacity=0.3, depth=-3.0, interpolate=True)
insructRight_keyResp_2_L = keyboard.Keyboard()
insructRight_keyResp_2_R = keyboard.Keyboard()

# --- Initialize components for Routine "instructLeft" ---
instructLeft_text_2_L = visual.TextStim(win=win, name='instructLeft_text_2_L',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructLeft_text_2_R = visual.TextStim(win=win, name='instructLeft_text_2_R',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instructLeft_letters2 = visual.TextStim(win=win, name='instructLeft_letters2',
    text='MMMMM',
    font='Arial',
    pos=(0, -.05), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
prac_highlight_circle_4 = visual.ShapeStim(
    win=win, name='prac_highlight_circle_4',
    size=(0.05, 0.05), vertices='circle',
    ori=0.0, pos=(0, -0.053), anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor='yellow', fillColor='yellow',
    opacity=0.3, depth=-3.0, interpolate=True)
instructLeft_keyResp_2_L = keyboard.Keyboard()
instructLeft_keyResp_2_R = keyboard.Keyboard()

# --- Initialize components for Routine "instructInconRight" ---
instructInconRight_text_2_L = visual.TextStim(win=win, name='instructInconRight_text_2_L',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructInconRight_text_2_R = visual.TextStim(win=win, name='instructInconRight_text_2_R',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instructionRight_letters2 = visual.TextStim(win=win, name='instructionRight_letters2',
    text='FFfFF',
    font='Open Sans',
    pos=(0, -.05), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
prac_highlight_circle_6 = visual.ShapeStim(
    win=win, name='prac_highlight_circle_6',
    size=(0.05, 0.05), vertices='circle',
    ori=0.0, pos=(0, -0.053), anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor='yellow', fillColor='yellow',
    opacity=0.3, depth=-3.0, interpolate=True)
insructInconRight_keyResp_2_L = keyboard.Keyboard()
insructInconRight_keyResp_2_R = keyboard.Keyboard()

# --- Initialize components for Routine "instructInconLeft" ---
instructInconLeft_text_2_L = visual.TextStim(win=win, name='instructInconLeft_text_2_L',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructInconLeft_text_2_R = visual.TextStim(win=win, name='instructInconLeft_text_2_R',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instructInconLeft_letters2 = visual.TextStim(win=win, name='instructInconLeft_letters2',
    text='ttTtt',
    font='Arial',
    pos=(0, -.05), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
prac_highlight_circle_8 = visual.ShapeStim(
    win=win, name='prac_highlight_circle_8',
    size=(0.05, 0.05), vertices='circle',
    ori=0.0, pos=(0, -0.053), anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor='yellow', fillColor='yellow',
    opacity=0.3, depth=-3.0, interpolate=True)
instructInconLeft_keyResp_2_L = keyboard.Keyboard()
instructInconLeft_keyResp_2_R = keyboard.Keyboard()

# --- Initialize components for Routine "respond_onceInstruct" ---
respond_once_text = visual.TextStim(win=win, name='respond_once_text',
    text='Each time you see the letters appear, respond as quickly as you can without making mistakes.\n\nHowever, only respond once each time you see the letters appear. Even if you think you made the wrong response, do not respond again until you see the next set of letters appear.\n\nPress SPACE to continue',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
space_end_keyResp_8 = keyboard.Keyboard()
left_reminder_text_2 = visual.TextStim(win=win, name='left_reminder_text_2',
    text='',
    font='Arial',
    pos=(-.6, -.4), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
right_reminder_text_2 = visual.TextStim(win=win, name='right_reminder_text_2',
    text='',
    font='Arial',
    pos=(.6, -.4), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

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
    text='Respond as quickly as you can without making mistakes. Only respond once each time you see the letters appear. Always respond whether the MIDDLE letter is CAPITALIZED or lowercase.\n\nRemember not to say any of the letters out loud. To get ready, rest your thumbs on the right and left buttons.\n\n\nPress SPACE to continue',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
left_reminder_text = visual.TextStim(win=win, name='left_reminder_text',
    text='',
    font='Arial',
    pos=(-.6, -.4), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
right_reminder_text = visual.TextStim(win=win, name='right_reminder_text',
    text='',
    font='Arial',
    pos=(.6, -.4), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
space_end_keyResp_9 = keyboard.Keyboard()

# --- Initialize components for Routine "prac_initFixation" ---
initFixation_img_2 = visual.ImageStim(
    win=win,
    name='initFixation_img_2', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, cross_y), size=(.24, .24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
left_reminder_text_3 = visual.TextStim(win=win, name='left_reminder_text_3',
    text='',
    font='Arial',
    pos=(-.6, -.4), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
right_reminder_text_3 = visual.TextStim(win=win, name='right_reminder_text_3',
    text='',
    font='Arial',
    pos=(.6, -.4), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "prac_stimRoutine" ---
prac_flanker_text_stim = visual.TextStim(win=win, name='prac_flanker_text_stim',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
prac_fixImg = visual.ImageStim(
    win=win,
    name='prac_fixImg', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, cross_y), size=(.24, .24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
left_reminder_text_4 = visual.TextStim(win=win, name='left_reminder_text_4',
    text='',
    font='Arial',
    pos=(-.6, -.4), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
right_reminder_text_4 = visual.TextStim(win=win, name='right_reminder_text_4',
    text='',
    font='Arial',
    pos=(.6, -.4), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
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
    text='Press SPACE to continue',
    font='Arial',
    pos=(0, -.3), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
prac_blockFeed_keyResp = keyboard.Keyboard()

# --- Initialize components for Routine "instruct_SuperTrial" ---
intruct_SuperTrial_text = visual.TextStim(win=win, name='intruct_SuperTrial_text',
    text='For the rest of today you will play both games at the same time! You will be presented with letters for the Memory Game and have to remember the letters while you play the BiG Letters Game. You will then have to recall the letters from the Memory Game, in the order they appeared. Remember not to say the letters out loud.\n\nLet’s do some practice!\n\n\nPress SPACE to continue',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
space_end_keyResp_10 = keyboard.Keyboard()

# --- Initialize components for Routine "reminder_SuperTrial" ---
prac_blockText_3 = visual.TextStim(win=win, name='prac_blockText_3',
    text='Practice',
    font='Arial',
    pos=(0, .4), height=0.06, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
task_blockReminders_text_2 = visual.TextStim(win=win, name='task_blockReminders_text_2',
    text='When the Memory Game letters are displayed, be sure to keep these in your memory. You will then recall these letters in the order that they appeared, after the BiG Letters Game.\n\nFor the BiG Letters Game, respond as quickly as you can without making mistakes. Only respond once each time you see the letters appear in the BiG Letters Game. Always respond whether the MIDDLE letter is CAPITALIZED or lowercase. \n\nRemember not to say any of the letters out loud. To get ready, rest your thumbs on the right and left buttons.\n\n\nPress SPACE to begin',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
task_blockReminders_keyResp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "prac_initFixaion_WM" ---
initFixation_img_4 = visual.ImageStim(
    win=win,
    name='initFixation_img_4', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, cross_y), size=(.24, .24),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "pracSuperTrial_seq" ---
wm_stim_5 = visual.TextStim(win=win, name='wm_stim_5',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.0, ori=0.0, 
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
wm_fixImg = visual.ImageStim(
    win=win,
    name='wm_fixImg', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, cross_y), size=(.24, .24),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "prac_SuperTrialFixation" ---
initFixation_img_3 = visual.ImageStim(
    win=win,
    name='initFixation_img_3', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, cross_y), size=(.24, .24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
left_reminder_text_5 = visual.TextStim(win=win, name='left_reminder_text_5',
    text='',
    font='Arial',
    pos=(-.6, -.4), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
right_reminder_text_5 = visual.TextStim(win=win, name='right_reminder_text_5',
    text='',
    font='Arial',
    pos=(.6, -.4), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "pracSuperTrial_flanker" ---
flanker_text_stim_2 = visual.TextStim(win=win, name='flanker_text_stim_2',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
left_reminder_text_6 = visual.TextStim(win=win, name='left_reminder_text_6',
    text='',
    font='Arial',
    pos=(-.6, -.4), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
right_reminder_text_6 = visual.TextStim(win=win, name='right_reminder_text_6',
    text='',
    font='Arial',
    pos=(.6, -.4), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
task_fixImg_2 = visual.ImageStim(
    win=win,
    name='task_fixImg_2', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, cross_y), size=(.24, .24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
task_stim_keyResp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "pracSuperTrial_recall" ---
wm_recall_text_3 = visual.TextStim(win=win, name='wm_recall_text_3',
    text='Type the letters from the Memory Game in the order they appeared\n\n\n\n\n\n\n\nPress SPACE when you finish',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
wm_recall_typedResp_3 = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(0.5, 0.5), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='wm_recall_typedResp_3',
     autoLog=True,
)
wm_recall_keyResp_3 = keyboard.Keyboard()
underscores_text_3 = visual.TextStim(win=win, name='underscores_text_3',
    text='',
    font='Arial',
    pos=(0, 0.01), height=0.045, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
full_response_reminder_text_3 = visual.TextStim(win=win, name='full_response_reminder_text_3',
    text='',
    font='Arial',
    pos=(0, -0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "pracSuperTrial_feed" ---
prac_blockFeed_text = visual.TextStim(win=win, name='prac_blockFeed_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
prac_pressContinue = visual.TextStim(win=win, name='prac_pressContinue',
    text='Press SPACE to continue',
    font='Arial',
    pos=(0, -.3), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
prac_blockFeed_keyResp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "task_condition" ---
task_blockText_2 = visual.TextStim(win=win, name='task_blockText_2',
    text='',
    font='Arial',
    pos=(0, .4), height=0.06, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
condition_reminder_text = visual.TextStim(win=win, name='condition_reminder_text',
    text='When the Memory Game letters are displayed, be sure to keep these in your memory. You will then recall these letters in the order that they appeared, after the BiG Letters Game.\n\nFor the BiG Letters Game, respond as quickly as you can without making mistakes. Only respond once each time you see the letters appear in the BiG Letters Game.\n\nAlways respond whether the MIDDLE letter is CAPITALIZED or lowercase. \n\nRemember not to say any of the letters out loud. To get ready, rest your thumbs on the right and left buttons.\n\nPress SPACE to begin',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
space_end_keyResp_11 = keyboard.Keyboard()

# --- Initialize components for Routine "eeg_trigger_check" ---

# --- Initialize components for Routine "supertrial_initFixation" ---
initFixation_img_5 = visual.ImageStim(
    win=win,
    name='initFixation_img_5', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, cross_y), size=(.24, .24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "wm_routine" ---
wm_stim = visual.TextStim(win=win, name='wm_stim',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.0, ori=0.0, 
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
wm_fixImg_7 = visual.ImageStim(
    win=win,
    name='wm_fixImg_7', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, cross_y), size=(.24, .24),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "task_initFixation" ---
initFixation_img = visual.ImageStim(
    win=win,
    name='initFixation_img', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, cross_y), size=(.24, .24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
left_reminder_text_7 = visual.TextStim(win=win, name='left_reminder_text_7',
    text='',
    font='Arial',
    pos=(-.6, -.4), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
right_reminder_text_7 = visual.TextStim(win=win, name='right_reminder_text_7',
    text='',
    font='Arial',
    pos=(.6, -.4), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "task_stimRoutine" ---
flanker_text_stim = visual.TextStim(win=win, name='flanker_text_stim',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
left_reminder_text_8 = visual.TextStim(win=win, name='left_reminder_text_8',
    text='',
    font='Arial',
    pos=(-.6, -.4), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
right_reminder_text_8 = visual.TextStim(win=win, name='right_reminder_text_8',
    text='',
    font='Arial',
    pos=(.6, -.4), height=0.04, wrapWidth=1.3, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
task_fixImg = visual.ImageStim(
    win=win,
    name='task_fixImg', units='deg', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, cross_y), size=(.24, .24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
task_stim_keyResp = keyboard.Keyboard()

# --- Initialize components for Routine "wm_recall" ---
wm_recall_text = visual.TextStim(win=win, name='wm_recall_text',
    text='Type the letters from the Memory Game in the order they appeared\n\n\n\n\n\n\n\nPress SPACE when you finish',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
wm_recall_typedResp = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(0.5, 0.5), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='wm_recall_typedResp',
     autoLog=True,
)
wm_recall_keyResp = keyboard.Keyboard()
underscores_text = visual.TextStim(win=win, name='underscores_text',
    text='',
    font='Arial',
    pos=(0, 0.01), height=0.045, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
full_response_reminder_text = visual.TextStim(win=win, name='full_response_reminder_text',
    text='',
    font='Arial',
    pos=(0, -0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "task_conditionComplete" ---
conditionComplete_text = visual.TextStim(win=win, name='conditionComplete_text',
    text='Press SPACE to continue',
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

# --- Prepare to start Routine "welcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
space_end_keyResp.keys = []
space_end_keyResp.rt = []
_space_end_keyResp_allKeys = []
# keep track of which components have finished
welcomeComponents = [welcome_text, space_end_keyResp]
for thisComponent in welcomeComponents:
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

# --- Run Routine "welcome" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_text* updates
    if welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_text.frameNStart = frameN  # exact frame index
        welcome_text.tStart = t  # local t and not account for scr refresh
        welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'welcome_text.started')
        welcome_text.setAutoDraw(True)
    
    # *space_end_keyResp* updates
    waitOnFlip = False
    if space_end_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_end_keyResp.frameNStart = frameN  # exact frame index
        space_end_keyResp.tStart = t  # local t and not account for scr refresh
        space_end_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_end_keyResp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'space_end_keyResp.started')
        space_end_keyResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space_end_keyResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space_end_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space_end_keyResp.status == STARTED and not waitOnFlip:
        theseKeys = space_end_keyResp.getKeys(keyList=['space'], waitRelease=False)
        _space_end_keyResp_allKeys.extend(theseKeys)
        if len(_space_end_keyResp_allKeys):
            space_end_keyResp.keys = _space_end_keyResp_allKeys[-1].name  # just the last key pressed
            space_end_keyResp.rt = _space_end_keyResp_allKeys[-1].rt
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
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "welcome" ---
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if space_end_keyResp.keys in ['', [], None]:  # No response was made
    space_end_keyResp.keys = None
thisExp.addData('space_end_keyResp.keys',space_end_keyResp.keys)
if space_end_keyResp.keys != None:  # we had a response
    thisExp.addData('space_end_keyResp.rt', space_end_keyResp.rt)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructWM1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
space_end_keyResp_2.keys = []
space_end_keyResp_2.rt = []
_space_end_keyResp_2_allKeys = []
# keep track of which components have finished
instructWM1Components = [instructWM_text1, space_end_keyResp_2]
for thisComponent in instructWM1Components:
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

# --- Run Routine "instructWM1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructWM_text1* updates
    if instructWM_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructWM_text1.frameNStart = frameN  # exact frame index
        instructWM_text1.tStart = t  # local t and not account for scr refresh
        instructWM_text1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructWM_text1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructWM_text1.started')
        instructWM_text1.setAutoDraw(True)
    
    # *space_end_keyResp_2* updates
    waitOnFlip = False
    if space_end_keyResp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_end_keyResp_2.frameNStart = frameN  # exact frame index
        space_end_keyResp_2.tStart = t  # local t and not account for scr refresh
        space_end_keyResp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_end_keyResp_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'space_end_keyResp_2.started')
        space_end_keyResp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space_end_keyResp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space_end_keyResp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space_end_keyResp_2.status == STARTED and not waitOnFlip:
        theseKeys = space_end_keyResp_2.getKeys(keyList=['space'], waitRelease=False)
        _space_end_keyResp_2_allKeys.extend(theseKeys)
        if len(_space_end_keyResp_2_allKeys):
            space_end_keyResp_2.keys = _space_end_keyResp_2_allKeys[-1].name  # just the last key pressed
            space_end_keyResp_2.rt = _space_end_keyResp_2_allKeys[-1].rt
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
    for thisComponent in instructWM1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructWM1" ---
for thisComponent in instructWM1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if space_end_keyResp_2.keys in ['', [], None]:  # No response was made
    space_end_keyResp_2.keys = None
thisExp.addData('space_end_keyResp_2.keys',space_end_keyResp_2.keys)
if space_end_keyResp_2.keys != None:  # we had a response
    thisExp.addData('space_end_keyResp_2.rt', space_end_keyResp_2.rt)
thisExp.nextEntry()
# the Routine "instructWM1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "prac_initFixaion_WM" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from prac_fixWM_code
# pick the ISI for the next routine
# for the online version, this code component should be set to 'both' to remove the 'np'
# at the start of np.linspace (this is a python library JS won't know what to call. 

# make range from a to b in n stepsizes
ISIRange = np.linspace(2600, 3000, 400)

# picking from a shuffled array is easier for random selection in JS
shuffle(ISIRange)
thisISI = ISIRange[0]/1000 # the first item of the shuffled array 

# empty lists of used letters
used_letters = []
used_letters_fl = []
shown_letters = []
initFixation_img_4.setImage('img/fixationCross.png')
# keep track of which components have finished
prac_initFixaion_WMComponents = [initFixation_img_4]
for thisComponent in prac_initFixaion_WMComponents:
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

# --- Run Routine "prac_initFixaion_WM" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *initFixation_img_4* updates
    if initFixation_img_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        initFixation_img_4.frameNStart = frameN  # exact frame index
        initFixation_img_4.tStart = t  # local t and not account for scr refresh
        initFixation_img_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(initFixation_img_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'initFixation_img_4.started')
        initFixation_img_4.setAutoDraw(True)
    if initFixation_img_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > initFixation_img_4.tStartRefresh + thisISI-frameTolerance:
            # keep track of stop time/frame for later
            initFixation_img_4.tStop = t  # not accounting for scr refresh
            initFixation_img_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'initFixation_img_4.stopped')
            initFixation_img_4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prac_initFixaion_WMComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "prac_initFixaion_WM" ---
for thisComponent in prac_initFixaion_WMComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "prac_initFixaion_WM" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
instructWM_loop = data.TrialHandler(nReps=4.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='instructWM_loop')
thisExp.addLoop(instructWM_loop)  # add the loop to the experiment
thisInstructWM_loop = instructWM_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstructWM_loop.rgb)
if thisInstructWM_loop != None:
    for paramName in thisInstructWM_loop:
        exec('{} = thisInstructWM_loop[paramName]'.format(paramName))

for thisInstructWM_loop in instructWM_loop:
    currentLoop = instructWM_loop
    # abbreviate parameter names if possible (e.g. rgb = thisInstructWM_loop.rgb)
    if thisInstructWM_loop != None:
        for paramName in thisInstructWM_loop:
            exec('{} = thisInstructWM_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "instructWM_seq1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from we_seq_code_2
    # choose the case of a letter randomly (0 = capitalized, 1 = lowercase)
    case_randomizer = random.randint(0, 1)
    
    # pick a letter to show for this trial
    shuffle(wm_letters)
    
    if case_randomizer == 0:
        letter = [i for i in wm_letters if i not in used_letters][0]
    elif case_randomizer == 1:
        letter = [i.lower() for i in wm_letters if i not in used_letters][0]
    
    # remember a letter shown in each trial
    used_letters.append(letter.upper())
    shown_letters.append(letter)
    # Run 'Begin Routine' code from wm_isi_code_2
    # pick the ISI for the next letter to appear
    
    # make range from a to b in n stepsizes
    wm_ISIRange = np.linspace(400, 800, 400)
    
    # picking from a shuffled array is easier for random selection in JS
    shuffle(wm_ISIRange)
    wm_thisISI = wm_ISIRange[0]/1000 # the first item of the shuffled array 
    
    # save this ISI to our output file
    instructWM_loop.addData('instructWM_isi', wm_thisISI)
    
    wm_stim_2.setText(letter)
    wm_fixImg_2.setImage('img/fixationCross.png')
    # keep track of which components have finished
    instructWM_seq1Components = [wm_stim_2, wm_fixImg_2]
    for thisComponent in instructWM_seq1Components:
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
    
    # --- Run Routine "instructWM_seq1" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *wm_stim_2* updates
        if wm_stim_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wm_stim_2.frameNStart = frameN  # exact frame index
            wm_stim_2.tStart = t  # local t and not account for scr refresh
            wm_stim_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wm_stim_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'wm_stim_2.started')
            wm_stim_2.setAutoDraw(True)
        if wm_stim_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wm_stim_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                wm_stim_2.tStop = t  # not accounting for scr refresh
                wm_stim_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'wm_stim_2.stopped')
                wm_stim_2.setAutoDraw(False)
        
        # *wm_fixImg_2* updates
        if wm_fixImg_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wm_fixImg_2.frameNStart = frameN  # exact frame index
            wm_fixImg_2.tStart = t  # local t and not account for scr refresh
            wm_fixImg_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wm_fixImg_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'wm_fixImg_2.started')
            wm_fixImg_2.setAutoDraw(True)
        if wm_fixImg_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wm_fixImg_2.tStartRefresh + wm_thisISI+0.5-frameTolerance:
                # keep track of stop time/frame for later
                wm_fixImg_2.tStop = t  # not accounting for scr refresh
                wm_fixImg_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'wm_fixImg_2.stopped')
                wm_fixImg_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructWM_seq1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructWM_seq1" ---
    for thisComponent in instructWM_seq1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from we_seq_code_2
    # write used and shown letters to data
    instructWM_loop.addData('instructWM_used_letters',
    ''.join(used_letters))
    instructWM_loop.addData('instructWM_shown_letters',
    ''.join(shown_letters))
    # the Routine "instructWM_seq1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'instructWM_loop'


# --- Prepare to start Routine "instructWM3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instructWM_text3.setText("For example, this time the letters were:\n {}\n\n\n\n Press SPACE to see another example".format("".join(used_letters)))
space_end_keyResp_3.keys = []
space_end_keyResp_3.rt = []
_space_end_keyResp_3_allKeys = []
# keep track of which components have finished
instructWM3Components = [instructWM_text3, space_end_keyResp_3]
for thisComponent in instructWM3Components:
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

# --- Run Routine "instructWM3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructWM_text3* updates
    if instructWM_text3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructWM_text3.frameNStart = frameN  # exact frame index
        instructWM_text3.tStart = t  # local t and not account for scr refresh
        instructWM_text3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructWM_text3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructWM_text3.started')
        instructWM_text3.setAutoDraw(True)
    
    # *space_end_keyResp_3* updates
    waitOnFlip = False
    if space_end_keyResp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_end_keyResp_3.frameNStart = frameN  # exact frame index
        space_end_keyResp_3.tStart = t  # local t and not account for scr refresh
        space_end_keyResp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_end_keyResp_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'space_end_keyResp_3.started')
        space_end_keyResp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space_end_keyResp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space_end_keyResp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space_end_keyResp_3.status == STARTED and not waitOnFlip:
        theseKeys = space_end_keyResp_3.getKeys(keyList=['space'], waitRelease=False)
        _space_end_keyResp_3_allKeys.extend(theseKeys)
        if len(_space_end_keyResp_3_allKeys):
            space_end_keyResp_3.keys = _space_end_keyResp_3_allKeys[-1].name  # just the last key pressed
            space_end_keyResp_3.rt = _space_end_keyResp_3_allKeys[-1].rt
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
    for thisComponent in instructWM3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructWM3" ---
for thisComponent in instructWM3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from instructWM_code3
# empty lists of used letters
used_letters = []
shown_letters = []
# check responses
if space_end_keyResp_3.keys in ['', [], None]:  # No response was made
    space_end_keyResp_3.keys = None
thisExp.addData('space_end_keyResp_3.keys',space_end_keyResp_3.keys)
if space_end_keyResp_3.keys != None:  # we had a response
    thisExp.addData('space_end_keyResp_3.rt', space_end_keyResp_3.rt)
thisExp.nextEntry()
# the Routine "instructWM3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "prac_initFixaion_WM" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from prac_fixWM_code
# pick the ISI for the next routine
# for the online version, this code component should be set to 'both' to remove the 'np'
# at the start of np.linspace (this is a python library JS won't know what to call. 

# make range from a to b in n stepsizes
ISIRange = np.linspace(2600, 3000, 400)

# picking from a shuffled array is easier for random selection in JS
shuffle(ISIRange)
thisISI = ISIRange[0]/1000 # the first item of the shuffled array 

# empty lists of used letters
used_letters = []
used_letters_fl = []
shown_letters = []
initFixation_img_4.setImage('img/fixationCross.png')
# keep track of which components have finished
prac_initFixaion_WMComponents = [initFixation_img_4]
for thisComponent in prac_initFixaion_WMComponents:
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

# --- Run Routine "prac_initFixaion_WM" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *initFixation_img_4* updates
    if initFixation_img_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        initFixation_img_4.frameNStart = frameN  # exact frame index
        initFixation_img_4.tStart = t  # local t and not account for scr refresh
        initFixation_img_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(initFixation_img_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'initFixation_img_4.started')
        initFixation_img_4.setAutoDraw(True)
    if initFixation_img_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > initFixation_img_4.tStartRefresh + thisISI-frameTolerance:
            # keep track of stop time/frame for later
            initFixation_img_4.tStop = t  # not accounting for scr refresh
            initFixation_img_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'initFixation_img_4.stopped')
            initFixation_img_4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prac_initFixaion_WMComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "prac_initFixaion_WM" ---
for thisComponent in prac_initFixaion_WMComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "prac_initFixaion_WM" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
instructWM_loop2 = data.TrialHandler(nReps=5.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='instructWM_loop2')
thisExp.addLoop(instructWM_loop2)  # add the loop to the experiment
thisInstructWM_loop2 = instructWM_loop2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstructWM_loop2.rgb)
if thisInstructWM_loop2 != None:
    for paramName in thisInstructWM_loop2:
        exec('{} = thisInstructWM_loop2[paramName]'.format(paramName))

for thisInstructWM_loop2 in instructWM_loop2:
    currentLoop = instructWM_loop2
    # abbreviate parameter names if possible (e.g. rgb = thisInstructWM_loop2.rgb)
    if thisInstructWM_loop2 != None:
        for paramName in thisInstructWM_loop2:
            exec('{} = thisInstructWM_loop2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "instructWM_seq2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from we_seq_code_3
    # choose the case of a letter randomly (0 = capitalized, 1 = lowercase)
    case_randomizer = random.randint(0, 1)
    
    # pick a letter to show for this trial
    shuffle(wm_letters)
    
    if case_randomizer == 0:
        letter = [i for i in wm_letters if i not in used_letters][0]
    elif case_randomizer == 1:
        letter = [i.lower() for i in wm_letters if i not in used_letters][0]
    
    # remember a letter shown in each trial
    used_letters.append(letter.upper())
    shown_letters.append(letter)
    # Run 'Begin Routine' code from wm_isi_code_3
    # pick the ISI for the next letter to appear
    
    # make range from a to b in n stepsizes
    wm_ISIRange = np.linspace(400, 800, 400)
    
    # picking from a shuffled array is easier for random selection in JS
    shuffle(wm_ISIRange)
    wm_thisISI = wm_ISIRange[0]/1000 # the first item of the shuffled array 
    
    # save this ISI to our output file
    instructWM_loop2.addData('instructWM_isi', wm_thisISI)
    
    wm_stim_3.setText(letter)
    wm_fixImg_3.setImage('img/fixationCross.png')
    # keep track of which components have finished
    instructWM_seq2Components = [wm_stim_3, wm_fixImg_3]
    for thisComponent in instructWM_seq2Components:
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
    
    # --- Run Routine "instructWM_seq2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *wm_stim_3* updates
        if wm_stim_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wm_stim_3.frameNStart = frameN  # exact frame index
            wm_stim_3.tStart = t  # local t and not account for scr refresh
            wm_stim_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wm_stim_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'wm_stim_3.started')
            wm_stim_3.setAutoDraw(True)
        if wm_stim_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wm_stim_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                wm_stim_3.tStop = t  # not accounting for scr refresh
                wm_stim_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'wm_stim_3.stopped')
                wm_stim_3.setAutoDraw(False)
        
        # *wm_fixImg_3* updates
        if wm_fixImg_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wm_fixImg_3.frameNStart = frameN  # exact frame index
            wm_fixImg_3.tStart = t  # local t and not account for scr refresh
            wm_fixImg_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wm_fixImg_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'wm_fixImg_3.started')
            wm_fixImg_3.setAutoDraw(True)
        if wm_fixImg_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wm_fixImg_3.tStartRefresh + wm_thisISI+0.5-frameTolerance:
                # keep track of stop time/frame for later
                wm_fixImg_3.tStop = t  # not accounting for scr refresh
                wm_fixImg_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'wm_fixImg_3.stopped')
                wm_fixImg_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructWM_seq2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructWM_seq2" ---
    for thisComponent in instructWM_seq2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from we_seq_code_3
    # write used and shown letters to data
    instructWM_loop2.addData('instructWM_used_letters',
    ''.join(used_letters))
    instructWM_loop2.addData('instructWM_shown_letters',
    ''.join(shown_letters))
    # the Routine "instructWM_seq2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'instructWM_loop2'


# --- Prepare to start Routine "instructWM4" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instructWM_text4.setText("This time the letters were:\n {}\n\n Did you notice that this time there were 5 letters? In this game, sequences you will need to remember may consist of 4 or 5 letters.\n\n Now you will practice yourself. Remember to not read the letters out loud.\n\n\n Press SPACE to start the practice".format("".join(used_letters)))
space_end_keyResp_4.keys = []
space_end_keyResp_4.rt = []
_space_end_keyResp_4_allKeys = []
# keep track of which components have finished
instructWM4Components = [instructWM_text4, space_end_keyResp_4]
for thisComponent in instructWM4Components:
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

# --- Run Routine "instructWM4" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructWM_text4* updates
    if instructWM_text4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructWM_text4.frameNStart = frameN  # exact frame index
        instructWM_text4.tStart = t  # local t and not account for scr refresh
        instructWM_text4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructWM_text4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructWM_text4.started')
        instructWM_text4.setAutoDraw(True)
    
    # *space_end_keyResp_4* updates
    waitOnFlip = False
    if space_end_keyResp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_end_keyResp_4.frameNStart = frameN  # exact frame index
        space_end_keyResp_4.tStart = t  # local t and not account for scr refresh
        space_end_keyResp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_end_keyResp_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'space_end_keyResp_4.started')
        space_end_keyResp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space_end_keyResp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space_end_keyResp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space_end_keyResp_4.status == STARTED and not waitOnFlip:
        theseKeys = space_end_keyResp_4.getKeys(keyList=['space'], waitRelease=False)
        _space_end_keyResp_4_allKeys.extend(theseKeys)
        if len(_space_end_keyResp_4_allKeys):
            space_end_keyResp_4.keys = _space_end_keyResp_4_allKeys[-1].name  # just the last key pressed
            space_end_keyResp_4.rt = _space_end_keyResp_4_allKeys[-1].rt
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
    for thisComponent in instructWM4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructWM4" ---
for thisComponent in instructWM4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from instructWM_code4
# empty lists of used letters
used_letters = []
shown_letters = []
# check responses
if space_end_keyResp_4.keys in ['', [], None]:  # No response was made
    space_end_keyResp_4.keys = None
thisExp.addData('space_end_keyResp_4.keys',space_end_keyResp_4.keys)
if space_end_keyResp_4.keys != None:  # we had a response
    thisExp.addData('space_end_keyResp_4.rt', space_end_keyResp_4.rt)
thisExp.nextEntry()
# the Routine "instructWM4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
instructWM_loop3 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='instructWM_loop3')
thisExp.addLoop(instructWM_loop3)  # add the loop to the experiment
thisInstructWM_loop3 = instructWM_loop3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstructWM_loop3.rgb)
if thisInstructWM_loop3 != None:
    for paramName in thisInstructWM_loop3:
        exec('{} = thisInstructWM_loop3[paramName]'.format(paramName))

for thisInstructWM_loop3 in instructWM_loop3:
    currentLoop = instructWM_loop3
    # abbreviate parameter names if possible (e.g. rgb = thisInstructWM_loop3.rgb)
    if thisInstructWM_loop3 != None:
        for paramName in thisInstructWM_loop3:
            exec('{} = thisInstructWM_loop3[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "prac_initFixaion_WM" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from prac_fixWM_code
    # pick the ISI for the next routine
    # for the online version, this code component should be set to 'both' to remove the 'np'
    # at the start of np.linspace (this is a python library JS won't know what to call. 
    
    # make range from a to b in n stepsizes
    ISIRange = np.linspace(2600, 3000, 400)
    
    # picking from a shuffled array is easier for random selection in JS
    shuffle(ISIRange)
    thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
    
    # empty lists of used letters
    used_letters = []
    used_letters_fl = []
    shown_letters = []
    initFixation_img_4.setImage('img/fixationCross.png')
    # keep track of which components have finished
    prac_initFixaion_WMComponents = [initFixation_img_4]
    for thisComponent in prac_initFixaion_WMComponents:
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
    
    # --- Run Routine "prac_initFixaion_WM" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *initFixation_img_4* updates
        if initFixation_img_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            initFixation_img_4.frameNStart = frameN  # exact frame index
            initFixation_img_4.tStart = t  # local t and not account for scr refresh
            initFixation_img_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(initFixation_img_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'initFixation_img_4.started')
            initFixation_img_4.setAutoDraw(True)
        if initFixation_img_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > initFixation_img_4.tStartRefresh + thisISI-frameTolerance:
                # keep track of stop time/frame for later
                initFixation_img_4.tStop = t  # not accounting for scr refresh
                initFixation_img_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'initFixation_img_4.stopped')
                initFixation_img_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_initFixaion_WMComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prac_initFixaion_WM" ---
    for thisComponent in prac_initFixaion_WMComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "prac_initFixaion_WM" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    instructWM_loop4 = data.TrialHandler(nReps=4.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='instructWM_loop4')
    thisExp.addLoop(instructWM_loop4)  # add the loop to the experiment
    thisInstructWM_loop4 = instructWM_loop4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInstructWM_loop4.rgb)
    if thisInstructWM_loop4 != None:
        for paramName in thisInstructWM_loop4:
            exec('{} = thisInstructWM_loop4[paramName]'.format(paramName))
    
    for thisInstructWM_loop4 in instructWM_loop4:
        currentLoop = instructWM_loop4
        # abbreviate parameter names if possible (e.g. rgb = thisInstructWM_loop4.rgb)
        if thisInstructWM_loop4 != None:
            for paramName in thisInstructWM_loop4:
                exec('{} = thisInstructWM_loop4[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "instructWM_seq3" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from we_seq_code_6
        # choose the case of a letter randomly (0 = capitalized, 1 = lowercase)
        case_randomizer = random.randint(0, 1)
        
        # pick a letter to show for this trial
        shuffle(wm_letters)
        
        if case_randomizer == 0:
            letter = [i for i in wm_letters if i not in used_letters][0]
        elif case_randomizer == 1:
            letter = [i.lower() for i in wm_letters if i not in used_letters][0]
        
        # remember a letter shown in each trial
        used_letters.append(letter.upper())
        shown_letters.append(letter)
        # Run 'Begin Routine' code from wm_isi_code_6
        # pick the ISI for the next letter to appear
        
        # make range from a to b in n stepsizes
        wm_ISIRange = np.linspace(400, 800, 400)
        
        # picking from a shuffled array is easier for random selection in JS
        shuffle(wm_ISIRange)
        wm_thisISI = wm_ISIRange[0]/1000 # the first item of the shuffled array 
        
        # save this ISI to our output file
        instructWM_loop4.addData('instructWM_isi', wm_thisISI)
        
        wm_stim_6.setText(letter)
        wm_fixImg_6.setImage('img/fixationCross.png')
        # keep track of which components have finished
        instructWM_seq3Components = [wm_stim_6, wm_fixImg_6]
        for thisComponent in instructWM_seq3Components:
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
        
        # --- Run Routine "instructWM_seq3" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *wm_stim_6* updates
            if wm_stim_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wm_stim_6.frameNStart = frameN  # exact frame index
                wm_stim_6.tStart = t  # local t and not account for scr refresh
                wm_stim_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_stim_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'wm_stim_6.started')
                wm_stim_6.setAutoDraw(True)
            if wm_stim_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wm_stim_6.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    wm_stim_6.tStop = t  # not accounting for scr refresh
                    wm_stim_6.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'wm_stim_6.stopped')
                    wm_stim_6.setAutoDraw(False)
            
            # *wm_fixImg_6* updates
            if wm_fixImg_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                wm_fixImg_6.frameNStart = frameN  # exact frame index
                wm_fixImg_6.tStart = t  # local t and not account for scr refresh
                wm_fixImg_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_fixImg_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'wm_fixImg_6.started')
                wm_fixImg_6.setAutoDraw(True)
            if wm_fixImg_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wm_fixImg_6.tStartRefresh + wm_thisISI+0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    wm_fixImg_6.tStop = t  # not accounting for scr refresh
                    wm_fixImg_6.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'wm_fixImg_6.stopped')
                    wm_fixImg_6.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in instructWM_seq3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "instructWM_seq3" ---
        for thisComponent in instructWM_seq3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from we_seq_code_6
        # write used letters to data
        instructWM_loop4.addData('instructWM_used_letters',
        ''.join(used_letters))
        instructWM_loop4.addData('instructWM_shown_letters',
        ''.join(shown_letters))
        # the Routine "instructWM_seq3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 4.0 repeats of 'instructWM_loop4'
    
    
    # --- Prepare to start Routine "instructWM_recall" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from wm_recall_code_4
    # define underscores for typing field according to WM load
    n_underscores = 4
    reminder_text = ""
    
    # define allowed keys for typed response (only letters)
    wm_allowed_keys =\
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
    'Y', 'Z']
    wm_recall_typedResp_4.reset()
    wm_recall_keyResp_4.keys = []
    wm_recall_keyResp_4.rt = []
    _wm_recall_keyResp_4_allKeys = []
    underscores_text_4.setText("\n"+n_underscores*" _")
    # keep track of which components have finished
    instructWM_recallComponents = [wm_recall_text_4, wm_recall_typedResp_4, wm_recall_keyResp_4, underscores_text_4, full_response_reminder_text_4]
    for thisComponent in instructWM_recallComponents:
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
    
    # --- Run Routine "instructWM_recall" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from wm_recall_code_4
        # if used lowercase letters in the response, turn into upper
        wm_recall_typedResp_4.text = \
        wm_recall_typedResp_4.text.upper()
        
        # limit length of input to the length of wm load in the block
        if len(wm_recall_typedResp_4.text) > n_underscores:
            wm_recall_typedResp_4.text = \
            wm_recall_typedResp_4.text[:n_underscores]
        
        # limit keys allowed to use to only letters
        if any(i not in wm_allowed_keys \
        for i in wm_recall_typedResp_4.text):
            wm_recall_typedResp_4.text = \
            wm_recall_typedResp_4.text[:-1]
        
        # restrict participant of giving a partial response (e.g. 3 letters when 4 required)
        if len(wm_recall_typedResp_4.text) < n_underscores\
        and 'space' in wm_recall_keyResp_4.getKeys():
            reminder_text = "please, provide a full response ({} letters)".format(n_underscores)
        elif len(wm_recall_typedResp_4.text) == n_underscores\
        and 'space' in wm_recall_keyResp_4.getKeys():
            continueRoutine = False
        elif len(wm_recall_typedResp_4.text) == n_underscores:
            reminder_text = ""
        
        # *wm_recall_text_4* updates
        if wm_recall_text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wm_recall_text_4.frameNStart = frameN  # exact frame index
            wm_recall_text_4.tStart = t  # local t and not account for scr refresh
            wm_recall_text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wm_recall_text_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'wm_recall_text_4.started')
            wm_recall_text_4.setAutoDraw(True)
        
        # *wm_recall_typedResp_4* updates
        if wm_recall_typedResp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wm_recall_typedResp_4.frameNStart = frameN  # exact frame index
            wm_recall_typedResp_4.tStart = t  # local t and not account for scr refresh
            wm_recall_typedResp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wm_recall_typedResp_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'wm_recall_typedResp_4.started')
            wm_recall_typedResp_4.setAutoDraw(True)
        
        # *wm_recall_keyResp_4* updates
        waitOnFlip = False
        if wm_recall_keyResp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wm_recall_keyResp_4.frameNStart = frameN  # exact frame index
            wm_recall_keyResp_4.tStart = t  # local t and not account for scr refresh
            wm_recall_keyResp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wm_recall_keyResp_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'wm_recall_keyResp_4.started')
            wm_recall_keyResp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(wm_recall_keyResp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(wm_recall_keyResp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if wm_recall_keyResp_4.status == STARTED and not waitOnFlip:
            theseKeys = wm_recall_keyResp_4.getKeys(keyList=['space'], waitRelease=False)
            _wm_recall_keyResp_4_allKeys.extend(theseKeys)
            if len(_wm_recall_keyResp_4_allKeys):
                wm_recall_keyResp_4.keys = _wm_recall_keyResp_4_allKeys[-1].name  # just the last key pressed
                wm_recall_keyResp_4.rt = _wm_recall_keyResp_4_allKeys[-1].rt
        
        # *underscores_text_4* updates
        if underscores_text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            underscores_text_4.frameNStart = frameN  # exact frame index
            underscores_text_4.tStart = t  # local t and not account for scr refresh
            underscores_text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(underscores_text_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'underscores_text_4.started')
            underscores_text_4.setAutoDraw(True)
        
        # *full_response_reminder_text_4* updates
        if full_response_reminder_text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            full_response_reminder_text_4.frameNStart = frameN  # exact frame index
            full_response_reminder_text_4.tStart = t  # local t and not account for scr refresh
            full_response_reminder_text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(full_response_reminder_text_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'full_response_reminder_text_4.started')
            full_response_reminder_text_4.setAutoDraw(True)
        if full_response_reminder_text_4.status == STARTED:  # only update if drawing
            full_response_reminder_text_4.setText(reminder_text, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructWM_recallComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructWM_recall" ---
    for thisComponent in instructWM_recallComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instructWM_loop3.addData('wm_recall_typedResp_4.text',wm_recall_typedResp_4.text)
    # check responses
    if wm_recall_keyResp_4.keys in ['', [], None]:  # No response was made
        wm_recall_keyResp_4.keys = None
    instructWM_loop3.addData('wm_recall_keyResp_4.keys',wm_recall_keyResp_4.keys)
    if wm_recall_keyResp_4.keys != None:  # we had a response
        instructWM_loop3.addData('wm_recall_keyResp_4.rt', wm_recall_keyResp_4.rt)
    # Run 'End Routine' code from wm_accuracy_code_4
    # check if typed response matches the letter sequece presented
    # and generate feedback
    if wm_recall_typedResp_4.text == ''.join(used_letters[-4:]):
        wm_fb_text = "You are right! \nThe letters were {}".format(''.join(used_letters[-4:]))
    else:
        wm_fb_text = "Not quite right... \nThe letters were {} \n\nPlease try to recall the letters in the order they appeared".format(''.join(used_letters[-4:]))
    
    # write used and shown letters to data (redundant)
    # instructWM_loop4.addData('instructWM_used_letters',
    # ''.join(used_letters))
    # instructWM_loop4.addData('instructWM_shown_letters',
    # ''.join(shown_letters))
    
    # empty lists of used letters
    used_letters = []
    shown_letters = []
    # the Routine "instructWM_recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructWM_fb" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    instructWM_fb_text.setText(wm_fb_text)
    space_end_keyResp_5.keys = []
    space_end_keyResp_5.rt = []
    _space_end_keyResp_5_allKeys = []
    # keep track of which components have finished
    instructWM_fbComponents = [instructWM_fb_text, instructWM_cont_text, space_end_keyResp_5]
    for thisComponent in instructWM_fbComponents:
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
    
    # --- Run Routine "instructWM_fb" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructWM_fb_text* updates
        if instructWM_fb_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructWM_fb_text.frameNStart = frameN  # exact frame index
            instructWM_fb_text.tStart = t  # local t and not account for scr refresh
            instructWM_fb_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructWM_fb_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instructWM_fb_text.started')
            instructWM_fb_text.setAutoDraw(True)
        
        # *instructWM_cont_text* updates
        if instructWM_cont_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructWM_cont_text.frameNStart = frameN  # exact frame index
            instructWM_cont_text.tStart = t  # local t and not account for scr refresh
            instructWM_cont_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructWM_cont_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instructWM_cont_text.started')
            instructWM_cont_text.setAutoDraw(True)
        
        # *space_end_keyResp_5* updates
        waitOnFlip = False
        if space_end_keyResp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            space_end_keyResp_5.frameNStart = frameN  # exact frame index
            space_end_keyResp_5.tStart = t  # local t and not account for scr refresh
            space_end_keyResp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space_end_keyResp_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'space_end_keyResp_5.started')
            space_end_keyResp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(space_end_keyResp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(space_end_keyResp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if space_end_keyResp_5.status == STARTED and not waitOnFlip:
            theseKeys = space_end_keyResp_5.getKeys(keyList=['space'], waitRelease=False)
            _space_end_keyResp_5_allKeys.extend(theseKeys)
            if len(_space_end_keyResp_5_allKeys):
                space_end_keyResp_5.keys = _space_end_keyResp_5_allKeys[-1].name  # just the last key pressed
                space_end_keyResp_5.rt = _space_end_keyResp_5_allKeys[-1].rt
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
        for thisComponent in instructWM_fbComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructWM_fb" ---
    for thisComponent in instructWM_fbComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if space_end_keyResp_5.keys in ['', [], None]:  # No response was made
        space_end_keyResp_5.keys = None
    instructWM_loop3.addData('space_end_keyResp_5.keys',space_end_keyResp_5.keys)
    if space_end_keyResp_5.keys != None:  # we had a response
        instructWM_loop3.addData('space_end_keyResp_5.rt', space_end_keyResp_5.rt)
    # the Routine "instructWM_fb" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'instructWM_loop3'


# set up handler to look after randomisation of conditions etc
pracWM_block_loop = data.TrialHandler(nReps=99.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='pracWM_block_loop')
thisExp.addLoop(pracWM_block_loop)  # add the loop to the experiment
thisPracWM_block_loop = pracWM_block_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracWM_block_loop.rgb)
if thisPracWM_block_loop != None:
    for paramName in thisPracWM_block_loop:
        exec('{} = thisPracWM_block_loop[paramName]'.format(paramName))

for thisPracWM_block_loop in pracWM_block_loop:
    currentLoop = pracWM_block_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPracWM_block_loop.rgb)
    if thisPracWM_block_loop != None:
        for paramName in thisPracWM_block_loop:
            exec('{} = thisPracWM_block_loop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    pracWM_trial_loop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='pracWM_trial_loop')
    thisExp.addLoop(pracWM_trial_loop)  # add the loop to the experiment
    thisPracWM_trial_loop = pracWM_trial_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracWM_trial_loop.rgb)
    if thisPracWM_trial_loop != None:
        for paramName in thisPracWM_trial_loop:
            exec('{} = thisPracWM_trial_loop[paramName]'.format(paramName))
    
    for thisPracWM_trial_loop in pracWM_trial_loop:
        currentLoop = pracWM_trial_loop
        # abbreviate parameter names if possible (e.g. rgb = thisPracWM_trial_loop.rgb)
        if thisPracWM_trial_loop != None:
            for paramName in thisPracWM_trial_loop:
                exec('{} = thisPracWM_trial_loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "prac_initFixaion_WM" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from prac_fixWM_code
        # pick the ISI for the next routine
        # for the online version, this code component should be set to 'both' to remove the 'np'
        # at the start of np.linspace (this is a python library JS won't know what to call. 
        
        # make range from a to b in n stepsizes
        ISIRange = np.linspace(2600, 3000, 400)
        
        # picking from a shuffled array is easier for random selection in JS
        shuffle(ISIRange)
        thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
        
        # empty lists of used letters
        used_letters = []
        used_letters_fl = []
        shown_letters = []
        initFixation_img_4.setImage('img/fixationCross.png')
        # keep track of which components have finished
        prac_initFixaion_WMComponents = [initFixation_img_4]
        for thisComponent in prac_initFixaion_WMComponents:
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
        
        # --- Run Routine "prac_initFixaion_WM" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *initFixation_img_4* updates
            if initFixation_img_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                initFixation_img_4.frameNStart = frameN  # exact frame index
                initFixation_img_4.tStart = t  # local t and not account for scr refresh
                initFixation_img_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(initFixation_img_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'initFixation_img_4.started')
                initFixation_img_4.setAutoDraw(True)
            if initFixation_img_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > initFixation_img_4.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    initFixation_img_4.tStop = t  # not accounting for scr refresh
                    initFixation_img_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'initFixation_img_4.stopped')
                    initFixation_img_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prac_initFixaion_WMComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "prac_initFixaion_WM" ---
        for thisComponent in prac_initFixaion_WMComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "prac_initFixaion_WM" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        pracWM_seq_loop = data.TrialHandler(nReps=4.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='pracWM_seq_loop')
        thisExp.addLoop(pracWM_seq_loop)  # add the loop to the experiment
        thisPracWM_seq_loop = pracWM_seq_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPracWM_seq_loop.rgb)
        if thisPracWM_seq_loop != None:
            for paramName in thisPracWM_seq_loop:
                exec('{} = thisPracWM_seq_loop[paramName]'.format(paramName))
        
        for thisPracWM_seq_loop in pracWM_seq_loop:
            currentLoop = pracWM_seq_loop
            # abbreviate parameter names if possible (e.g. rgb = thisPracWM_seq_loop.rgb)
            if thisPracWM_seq_loop != None:
                for paramName in thisPracWM_seq_loop:
                    exec('{} = thisPracWM_seq_loop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "pracWM_seq" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from we_seq_code_4
            # choose the case of a letter randomly (0 = capitalized, 1 = lowercase)
            case_randomizer = random.randint(0, 1)
            
            # pick a letter to show for this trial
            shuffle(wm_letters)
            
            if case_randomizer == 0:
                letter = [i for i in wm_letters if i not in used_letters][0]
            elif case_randomizer == 1:
                letter = [i.lower() for i in wm_letters if i not in used_letters][0]
            
            # remember the letter shown in each trial
            used_letters.append(letter.upper())
            shown_letters.append(letter)
            # Run 'Begin Routine' code from wm_isi_code_4
            # pick the ISI for the next letter to appear
            
            # make range from a to b in n stepsizes
            wm_ISIRange = np.linspace(400, 800, 400)
            
            # picking from a shuffled array is easier for random selection in JS
            shuffle(wm_ISIRange)
            wm_thisISI = wm_ISIRange[0]/1000 # the first item of the shuffled array 
            
            # save this ISI to our output file
            pracWM_seq_loop.addData('pracWM_isi', wm_thisISI)
            wm_stim_4.setText(letter)
            wm_fixImg_4.setImage('img/fixationCross.png')
            # keep track of which components have finished
            pracWM_seqComponents = [wm_stim_4, wm_fixImg_4]
            for thisComponent in pracWM_seqComponents:
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
            
            # --- Run Routine "pracWM_seq" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *wm_stim_4* updates
                if wm_stim_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    wm_stim_4.frameNStart = frameN  # exact frame index
                    wm_stim_4.tStart = t  # local t and not account for scr refresh
                    wm_stim_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(wm_stim_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'wm_stim_4.started')
                    wm_stim_4.setAutoDraw(True)
                if wm_stim_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > wm_stim_4.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        wm_stim_4.tStop = t  # not accounting for scr refresh
                        wm_stim_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'wm_stim_4.stopped')
                        wm_stim_4.setAutoDraw(False)
                
                # *wm_fixImg_4* updates
                if wm_fixImg_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    wm_fixImg_4.frameNStart = frameN  # exact frame index
                    wm_fixImg_4.tStart = t  # local t and not account for scr refresh
                    wm_fixImg_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(wm_fixImg_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'wm_fixImg_4.started')
                    wm_fixImg_4.setAutoDraw(True)
                if wm_fixImg_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > wm_fixImg_4.tStartRefresh + wm_thisISI+0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        wm_fixImg_4.tStop = t  # not accounting for scr refresh
                        wm_fixImg_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'wm_fixImg_4.stopped')
                        wm_fixImg_4.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in pracWM_seqComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "pracWM_seq" ---
            for thisComponent in pracWM_seqComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from we_seq_code_4
            # write used and shown letters to data
            pracWM_seq_loop.addData('pracWM_used_letters',
            ''.join(used_letters))
            pracWM_seq_loop.addData('pracWM_shown_letters',
            ''.join(shown_letters))
            # the Routine "pracWM_seq" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 4.0 repeats of 'pracWM_seq_loop'
        
        
        # --- Prepare to start Routine "pracWM_recall" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from wm_recall_code_2
        # define underscores for typing field according to WM load
        n_underscores = 4
        reminder_text = ""
        
        # define allowed keys for typed response (only letters)
        wm_allowed_keys =\
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z']
        
        wm_recall_typedResp_2.reset()
        wm_recall_keyResp_2.keys = []
        wm_recall_keyResp_2.rt = []
        _wm_recall_keyResp_2_allKeys = []
        underscores_text_2.setText("\n"+n_underscores*" _")
        # keep track of which components have finished
        pracWM_recallComponents = [wm_recall_text_2, wm_recall_typedResp_2, wm_recall_keyResp_2, underscores_text_2, full_response_reminder_text_2]
        for thisComponent in pracWM_recallComponents:
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
        
        # --- Run Routine "pracWM_recall" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from wm_recall_code_2
            # if used lowercase letters in the response, turn into upper
            wm_recall_typedResp_2.text = \
            wm_recall_typedResp_2.text.upper()
            
            # limit length of input to the length of wm load in the block
            if len(wm_recall_typedResp_2.text) > n_underscores:
                wm_recall_typedResp_2.text = \
                wm_recall_typedResp_2.text[:n_underscores]
            # limit keys allowed to use to only letters
            if any(i not in wm_allowed_keys \
            for i in wm_recall_typedResp_2.text):
                wm_recall_typedResp_2.text = \
                wm_recall_typedResp_2.text[:-1]
            # restrict participant of giving a partial response (e.g. 3 letters when 4 required)
            if len(wm_recall_typedResp_2.text) < n_underscores\
            and 'space' in wm_recall_keyResp_2.getKeys():
                reminder_text = "please, provide a full response ({} letters)".format(n_underscores)
            elif len(wm_recall_typedResp_2.text) == n_underscores\
            and 'space' in wm_recall_keyResp_2.getKeys():
                continueRoutine = False
            elif len(wm_recall_typedResp_2.text) == n_underscores:
                reminder_text = ""
            
            # *wm_recall_text_2* updates
            if wm_recall_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wm_recall_text_2.frameNStart = frameN  # exact frame index
                wm_recall_text_2.tStart = t  # local t and not account for scr refresh
                wm_recall_text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_recall_text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'wm_recall_text_2.started')
                wm_recall_text_2.setAutoDraw(True)
            
            # *wm_recall_typedResp_2* updates
            if wm_recall_typedResp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wm_recall_typedResp_2.frameNStart = frameN  # exact frame index
                wm_recall_typedResp_2.tStart = t  # local t and not account for scr refresh
                wm_recall_typedResp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_recall_typedResp_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'wm_recall_typedResp_2.started')
                wm_recall_typedResp_2.setAutoDraw(True)
            
            # *wm_recall_keyResp_2* updates
            waitOnFlip = False
            if wm_recall_keyResp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wm_recall_keyResp_2.frameNStart = frameN  # exact frame index
                wm_recall_keyResp_2.tStart = t  # local t and not account for scr refresh
                wm_recall_keyResp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_recall_keyResp_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'wm_recall_keyResp_2.started')
                wm_recall_keyResp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(wm_recall_keyResp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(wm_recall_keyResp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if wm_recall_keyResp_2.status == STARTED and not waitOnFlip:
                theseKeys = wm_recall_keyResp_2.getKeys(keyList=['space'], waitRelease=False)
                _wm_recall_keyResp_2_allKeys.extend(theseKeys)
                if len(_wm_recall_keyResp_2_allKeys):
                    wm_recall_keyResp_2.keys = _wm_recall_keyResp_2_allKeys[-1].name  # just the last key pressed
                    wm_recall_keyResp_2.rt = _wm_recall_keyResp_2_allKeys[-1].rt
            
            # *underscores_text_2* updates
            if underscores_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                underscores_text_2.frameNStart = frameN  # exact frame index
                underscores_text_2.tStart = t  # local t and not account for scr refresh
                underscores_text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(underscores_text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'underscores_text_2.started')
                underscores_text_2.setAutoDraw(True)
            
            # *full_response_reminder_text_2* updates
            if full_response_reminder_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                full_response_reminder_text_2.frameNStart = frameN  # exact frame index
                full_response_reminder_text_2.tStart = t  # local t and not account for scr refresh
                full_response_reminder_text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(full_response_reminder_text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'full_response_reminder_text_2.started')
                full_response_reminder_text_2.setAutoDraw(True)
            if full_response_reminder_text_2.status == STARTED:  # only update if drawing
                full_response_reminder_text_2.setText(reminder_text, log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pracWM_recallComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pracWM_recall" ---
        for thisComponent in pracWM_recallComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        pracWM_trial_loop.addData('wm_recall_typedResp_2.text',wm_recall_typedResp_2.text)
        # check responses
        if wm_recall_keyResp_2.keys in ['', [], None]:  # No response was made
            wm_recall_keyResp_2.keys = None
        pracWM_trial_loop.addData('wm_recall_keyResp_2.keys',wm_recall_keyResp_2.keys)
        if wm_recall_keyResp_2.keys != None:  # we had a response
            pracWM_trial_loop.addData('wm_recall_keyResp_2.rt', wm_recall_keyResp_2.rt)
        # Run 'End Routine' code from wm_accuracy_code_2
        # check if typed response matches the letter sequece presented
        # OLD VERSION (BINARY)
        #if wm_recall_typedResp_2.text == ''.join(used_letters[-4:]):
        #    wm_accuracy = 1
        #    numCorr += 1
        #    wm_fb_text = "You are right! \nThe letters were {}".format(''.join(used_letters[-4:]))
        #else:
        #    wm_accuracy = 0
        #    wm_fb_text = "Not quite right... \nThe letters were {} \n\nPlease try to recall the letters in the order they appeared".format(''.join(used_letters[-4:]))
        
        # check if typed response matches the letter sequece presented
        # and generate feedback
        wm_response = wm_recall_typedResp_2.text
        correct_letters = used_letters.copy()
        wm_accuracy = 0
        for i in wm_response:
            if i in correct_letters:
                wm_accuracy += 1/len(wm_response)
                correct_letters.remove(i)
        
        if wm_response == ''.join(used_letters):
            wm_fb_text = "You are right! \nThe letters were {}".format(''.join(used_letters[-4:]))
        elif wm_accuracy >= wm_thresh:
            wm_fb_text = "You have almost made it! \nThe letters were {} \n\nPlease try to recall the letters in the order they appeared".format(''.join(used_letters[-4:]))
        elif wm_accuracy < wm_thresh:
            wm_fb_text = "Not quite right... \nThe letters were {} \n\nPlease try to recall the letters in the order they appeared".format(''.join(used_letters[-4:]))
        
        # calculate accuracy and add trial to counter
        numCorr += wm_accuracy
        trialNum += 1
        
        # write used letters to data (redundant)
        # pracWM_trial_loop.addData('pracWM_used_letters',''.join(used_letters))
        # write shown letters to data (redundant)
        # pracWM_trial_loop.addData('pracWM_shown_letters',''.join(shown_letters))
        # write response letters to data
        pracWM_trial_loop.addData('pracWM_wm_response', wm_response)
        # save this trial's wm accuracy to our output file
        pracWM_trial_loop.addData('pracWM_wm_accuracy', wm_accuracy)
        
        # empty lists of used letters
        used_letters = []
        shown_letters = []
        # the Routine "pracWM_recall" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "pracWM_fb" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        instructWM_fb_text_2.setText(wm_fb_text)
        space_end_keyResp_6.keys = []
        space_end_keyResp_6.rt = []
        _space_end_keyResp_6_allKeys = []
        # keep track of which components have finished
        pracWM_fbComponents = [instructWM_fb_text_2, instructWM_cont_text_2, space_end_keyResp_6]
        for thisComponent in pracWM_fbComponents:
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
        
        # --- Run Routine "pracWM_fb" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *instructWM_fb_text_2* updates
            if instructWM_fb_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                instructWM_fb_text_2.frameNStart = frameN  # exact frame index
                instructWM_fb_text_2.tStart = t  # local t and not account for scr refresh
                instructWM_fb_text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instructWM_fb_text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instructWM_fb_text_2.started')
                instructWM_fb_text_2.setAutoDraw(True)
            
            # *instructWM_cont_text_2* updates
            if instructWM_cont_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                instructWM_cont_text_2.frameNStart = frameN  # exact frame index
                instructWM_cont_text_2.tStart = t  # local t and not account for scr refresh
                instructWM_cont_text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instructWM_cont_text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instructWM_cont_text_2.started')
                instructWM_cont_text_2.setAutoDraw(True)
            
            # *space_end_keyResp_6* updates
            waitOnFlip = False
            if space_end_keyResp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                space_end_keyResp_6.frameNStart = frameN  # exact frame index
                space_end_keyResp_6.tStart = t  # local t and not account for scr refresh
                space_end_keyResp_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(space_end_keyResp_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'space_end_keyResp_6.started')
                space_end_keyResp_6.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(space_end_keyResp_6.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(space_end_keyResp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if space_end_keyResp_6.status == STARTED and not waitOnFlip:
                theseKeys = space_end_keyResp_6.getKeys(keyList=['space'], waitRelease=False)
                _space_end_keyResp_6_allKeys.extend(theseKeys)
                if len(_space_end_keyResp_6_allKeys):
                    space_end_keyResp_6.keys = _space_end_keyResp_6_allKeys[-1].name  # just the last key pressed
                    space_end_keyResp_6.rt = _space_end_keyResp_6_allKeys[-1].rt
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
            for thisComponent in pracWM_fbComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pracWM_fb" ---
        for thisComponent in pracWM_fbComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if space_end_keyResp_6.keys in ['', [], None]:  # No response was made
            space_end_keyResp_6.keys = None
        pracWM_trial_loop.addData('space_end_keyResp_6.keys',space_end_keyResp_6.keys)
        if space_end_keyResp_6.keys != None:  # we had a response
            pracWM_trial_loop.addData('space_end_keyResp_6.rt', space_end_keyResp_6.rt)
        # the Routine "pracWM_fb" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'pracWM_trial_loop'
    
    
    # --- Prepare to start Routine "pracWM_feed" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from prac_blockFeed_code_2
    blockAcc = numCorr / trialNum #compute accuracy for this block
    
    if blockAcc >= wm_thresh: #if accuracy >= threshold then say practice is complete and end practice loop to continue to main exp
        outPut = 'Great! Now you are going to learn how to play the second game!'
        pracWM_block_loop.finished = True #end practice loop to continue to main exp
    elif blockAcc <= wm_thresh: #if accuracy < threshold then say that practice needs to be repeated and DO NOT end practice loop, instead, allow it to repeat
        outPut = 'You will now practice the Memory Game 5 more times' #feedback presented
        pracWM_block_loop.finished = False #DO NOT end practice loop and allow to repeat
    
    pracWM_block_loop.addData('pracWM_blockAcc', blockAcc)
    
    #reset the following variables to zero before the next practice block starts
    trialNum = 0
    numCorr = 0
    prac_blockFeed_text_2.setText('')
    prac_blockFeed_keyResp_2.keys = []
    prac_blockFeed_keyResp_2.rt = []
    _prac_blockFeed_keyResp_2_allKeys = []
    # keep track of which components have finished
    pracWM_feedComponents = [prac_blockFeed_text_2, prac_pressContinue_2, prac_blockFeed_keyResp_2]
    for thisComponent in pracWM_feedComponents:
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
    
    # --- Run Routine "pracWM_feed" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_blockFeed_text_2* updates
        if prac_blockFeed_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_blockFeed_text_2.frameNStart = frameN  # exact frame index
            prac_blockFeed_text_2.tStart = t  # local t and not account for scr refresh
            prac_blockFeed_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_blockFeed_text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_blockFeed_text_2.started')
            prac_blockFeed_text_2.setAutoDraw(True)
        
        # *prac_pressContinue_2* updates
        if prac_pressContinue_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_pressContinue_2.frameNStart = frameN  # exact frame index
            prac_pressContinue_2.tStart = t  # local t and not account for scr refresh
            prac_pressContinue_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_pressContinue_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_pressContinue_2.started')
            prac_pressContinue_2.setAutoDraw(True)
        
        # *prac_blockFeed_keyResp_2* updates
        waitOnFlip = False
        if prac_blockFeed_keyResp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_blockFeed_keyResp_2.frameNStart = frameN  # exact frame index
            prac_blockFeed_keyResp_2.tStart = t  # local t and not account for scr refresh
            prac_blockFeed_keyResp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_blockFeed_keyResp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_blockFeed_keyResp_2.started')
            prac_blockFeed_keyResp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(prac_blockFeed_keyResp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(prac_blockFeed_keyResp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if prac_blockFeed_keyResp_2.status == STARTED and not waitOnFlip:
            theseKeys = prac_blockFeed_keyResp_2.getKeys(keyList=['space', 's'], waitRelease=False)
            _prac_blockFeed_keyResp_2_allKeys.extend(theseKeys)
            if len(_prac_blockFeed_keyResp_2_allKeys):
                prac_blockFeed_keyResp_2.keys = _prac_blockFeed_keyResp_2_allKeys[-1].name  # just the last key pressed
                prac_blockFeed_keyResp_2.rt = _prac_blockFeed_keyResp_2_allKeys[-1].rt
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
        for thisComponent in pracWM_feedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pracWM_feed" ---
    for thisComponent in pracWM_feedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from prac_blockFeed_code_2
    if prac_blockFeed_keyResp_2.keys[-1] == 's':
        pracWM_block_loop.finished = True #end practice loop to continue to main exp
    # check responses
    if prac_blockFeed_keyResp_2.keys in ['', [], None]:  # No response was made
        prac_blockFeed_keyResp_2.keys = None
    pracWM_block_loop.addData('prac_blockFeed_keyResp_2.keys',prac_blockFeed_keyResp_2.keys)
    if prac_blockFeed_keyResp_2.keys != None:  # we had a response
        pracWM_block_loop.addData('prac_blockFeed_keyResp_2.rt', prac_blockFeed_keyResp_2.rt)
    # the Routine "pracWM_feed" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 99.0 repeats of 'pracWM_block_loop'


# --- Prepare to start Routine "instructMiddle" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
welcome_text_2_L.setText('Welcome to the BiG Letters Game! This game will require you to quickly respond to letters based on whether they are CAPITALIZED or lowercase.\n\nDuring this game, five letters will appear at a time. They will be quickly flashed on the screen. Your goal is to respond to the MIDDLE letter, and to respond as quickly as you can without making mistakes.\n\nIf the MIDDLE letter is lowercase, use your right hand to press the right button (8). If the MIDDLE letter is CAPITALIZED, use your left hand to press the left button (1).\n\nPress SPACE to continue')
welcome_text_2_R.setText('Welcome to the BiG Letters Game! This game will require you to quickly respond to letters based on whether they are CAPITALIZED or lowercase.\n\nDuring this part, five letters will appear at a time. They will be quickly flashed on the screen. Your goal is to respond to the MIDDLE letter, and to respond as quickly as you can without making mistakes.\n\nIf the MIDDLE letter is lowercase, use your left hand to press the left button (1). If the MIDDLE letter is CAPITALIZED, use your right hand to press the right button (8).\n\nPress SPACE to continue')
space_end_keyResp_7.keys = []
space_end_keyResp_7.rt = []
_space_end_keyResp_7_allKeys = []
# keep track of which components have finished
instructMiddleComponents = [welcome_text_2_L, welcome_text_2_R, space_end_keyResp_7]
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
    
    # *welcome_text_2_L* updates
    if welcome_text_2_L.status == NOT_STARTED and expInfo["counterbalance"] == "L":
        # keep track of start time/frame for later
        welcome_text_2_L.frameNStart = frameN  # exact frame index
        welcome_text_2_L.tStart = t  # local t and not account for scr refresh
        welcome_text_2_L.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text_2_L, 'tStartRefresh')  # time at next scr refresh
        welcome_text_2_L.setAutoDraw(True)
    
    # *welcome_text_2_R* updates
    if welcome_text_2_R.status == NOT_STARTED and expInfo["counterbalance"] == "R":
        # keep track of start time/frame for later
        welcome_text_2_R.frameNStart = frameN  # exact frame index
        welcome_text_2_R.tStart = t  # local t and not account for scr refresh
        welcome_text_2_R.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text_2_R, 'tStartRefresh')  # time at next scr refresh
        welcome_text_2_R.setAutoDraw(True)
    
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
        theseKeys = space_end_keyResp_7.getKeys(keyList=['space'], waitRelease=False)
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

# --- Prepare to start Routine "instructRight" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instructRight_text_2_L.setText('Below, the MIDDLE letter is lowercase, so you would respond by pressing the right button (8) with your right hand.\n\n\n\n\n\n\n\nPress the right button (8) to continue')
instructRight_text_2_R.setText('Below, the MIDDLE letter is lowercase, so you would respond by pressing the left button (1) with your left hand.\n\n\n\n\n\n\n\nPress the left button (1) to continue')
instructRight_letters2.setText('hhhhh')
insructRight_keyResp_2_L.keys = []
insructRight_keyResp_2_L.rt = []
_insructRight_keyResp_2_L_allKeys = []
insructRight_keyResp_2_R.keys = []
insructRight_keyResp_2_R.rt = []
_insructRight_keyResp_2_R_allKeys = []
# keep track of which components have finished
instructRightComponents = [instructRight_text_2_L, instructRight_text_2_R, instructRight_letters2, prac_highlight_circle_2, insructRight_keyResp_2_L, insructRight_keyResp_2_R]
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
    
    # *instructRight_text_2_L* updates
    if instructRight_text_2_L.status == NOT_STARTED and expInfo["counterbalance"] == "L":
        # keep track of start time/frame for later
        instructRight_text_2_L.frameNStart = frameN  # exact frame index
        instructRight_text_2_L.tStart = t  # local t and not account for scr refresh
        instructRight_text_2_L.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRight_text_2_L, 'tStartRefresh')  # time at next scr refresh
        instructRight_text_2_L.setAutoDraw(True)
    
    # *instructRight_text_2_R* updates
    if instructRight_text_2_R.status == NOT_STARTED and expInfo["counterbalance"] == "R":
        # keep track of start time/frame for later
        instructRight_text_2_R.frameNStart = frameN  # exact frame index
        instructRight_text_2_R.tStart = t  # local t and not account for scr refresh
        instructRight_text_2_R.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRight_text_2_R, 'tStartRefresh')  # time at next scr refresh
        instructRight_text_2_R.setAutoDraw(True)
    
    # *instructRight_letters2* updates
    if instructRight_letters2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        instructRight_letters2.frameNStart = frameN  # exact frame index
        instructRight_letters2.tStart = t  # local t and not account for scr refresh
        instructRight_letters2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRight_letters2, 'tStartRefresh')  # time at next scr refresh
        instructRight_letters2.setAutoDraw(True)
    
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
    
    # *insructRight_keyResp_2_L* updates
    waitOnFlip = False
    if insructRight_keyResp_2_L.status == NOT_STARTED and expInfo["counterbalance"] == "L":
        # keep track of start time/frame for later
        insructRight_keyResp_2_L.frameNStart = frameN  # exact frame index
        insructRight_keyResp_2_L.tStart = t  # local t and not account for scr refresh
        insructRight_keyResp_2_L.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(insructRight_keyResp_2_L, 'tStartRefresh')  # time at next scr refresh
        insructRight_keyResp_2_L.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(insructRight_keyResp_2_L.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(insructRight_keyResp_2_L.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if insructRight_keyResp_2_L.status == STARTED and not waitOnFlip:
        theseKeys = insructRight_keyResp_2_L.getKeys(keyList=['8'], waitRelease=False)
        _insructRight_keyResp_2_L_allKeys.extend(theseKeys)
        if len(_insructRight_keyResp_2_L_allKeys):
            insructRight_keyResp_2_L.keys = _insructRight_keyResp_2_L_allKeys[-1].name  # just the last key pressed
            insructRight_keyResp_2_L.rt = _insructRight_keyResp_2_L_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *insructRight_keyResp_2_R* updates
    waitOnFlip = False
    if insructRight_keyResp_2_R.status == NOT_STARTED and expInfo["counterbalance"] == "R":
        # keep track of start time/frame for later
        insructRight_keyResp_2_R.frameNStart = frameN  # exact frame index
        insructRight_keyResp_2_R.tStart = t  # local t and not account for scr refresh
        insructRight_keyResp_2_R.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(insructRight_keyResp_2_R, 'tStartRefresh')  # time at next scr refresh
        insructRight_keyResp_2_R.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(insructRight_keyResp_2_R.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(insructRight_keyResp_2_R.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if insructRight_keyResp_2_R.status == STARTED and not waitOnFlip:
        theseKeys = insructRight_keyResp_2_R.getKeys(keyList=['1'], waitRelease=False)
        _insructRight_keyResp_2_R_allKeys.extend(theseKeys)
        if len(_insructRight_keyResp_2_R_allKeys):
            insructRight_keyResp_2_R.keys = _insructRight_keyResp_2_R_allKeys[-1].name  # just the last key pressed
            insructRight_keyResp_2_R.rt = _insructRight_keyResp_2_R_allKeys[-1].rt
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

# --- Prepare to start Routine "instructLeft" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instructLeft_text_2_L.setText('Below, the MIDDLE letter is CAPITALIZED, so you would respond by pressing the left button (1) with your left hand.\n\n\n\n\n\n\n\nPress the left button (1) to continue')
instructLeft_text_2_R.setText('Below, the MIDDLE letter is CAPITALIZED, so you would respond by pressing the right button (8) with your right hand.\n\n\n\n\n\n\n\nPress the right button (8) to continue')
instructLeft_keyResp_2_L.keys = []
instructLeft_keyResp_2_L.rt = []
_instructLeft_keyResp_2_L_allKeys = []
instructLeft_keyResp_2_R.keys = []
instructLeft_keyResp_2_R.rt = []
_instructLeft_keyResp_2_R_allKeys = []
# keep track of which components have finished
instructLeftComponents = [instructLeft_text_2_L, instructLeft_text_2_R, instructLeft_letters2, prac_highlight_circle_4, instructLeft_keyResp_2_L, instructLeft_keyResp_2_R]
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
    
    # *instructLeft_text_2_L* updates
    if instructLeft_text_2_L.status == NOT_STARTED and expInfo["counterbalance"] == "L":
        # keep track of start time/frame for later
        instructLeft_text_2_L.frameNStart = frameN  # exact frame index
        instructLeft_text_2_L.tStart = t  # local t and not account for scr refresh
        instructLeft_text_2_L.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_text_2_L, 'tStartRefresh')  # time at next scr refresh
        instructLeft_text_2_L.setAutoDraw(True)
    
    # *instructLeft_text_2_R* updates
    if instructLeft_text_2_R.status == NOT_STARTED and expInfo["counterbalance"] == "R":
        # keep track of start time/frame for later
        instructLeft_text_2_R.frameNStart = frameN  # exact frame index
        instructLeft_text_2_R.tStart = t  # local t and not account for scr refresh
        instructLeft_text_2_R.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_text_2_R, 'tStartRefresh')  # time at next scr refresh
        instructLeft_text_2_R.setAutoDraw(True)
    
    # *instructLeft_letters2* updates
    if instructLeft_letters2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructLeft_letters2.frameNStart = frameN  # exact frame index
        instructLeft_letters2.tStart = t  # local t and not account for scr refresh
        instructLeft_letters2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_letters2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructLeft_letters2.started')
        instructLeft_letters2.setAutoDraw(True)
    
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
    
    # *instructLeft_keyResp_2_L* updates
    waitOnFlip = False
    if instructLeft_keyResp_2_L.status == NOT_STARTED and expInfo["counterbalance"] == "L":
        # keep track of start time/frame for later
        instructLeft_keyResp_2_L.frameNStart = frameN  # exact frame index
        instructLeft_keyResp_2_L.tStart = t  # local t and not account for scr refresh
        instructLeft_keyResp_2_L.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_keyResp_2_L, 'tStartRefresh')  # time at next scr refresh
        instructLeft_keyResp_2_L.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructLeft_keyResp_2_L.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructLeft_keyResp_2_L.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructLeft_keyResp_2_L.status == STARTED and not waitOnFlip:
        theseKeys = instructLeft_keyResp_2_L.getKeys(keyList=['1'], waitRelease=False)
        _instructLeft_keyResp_2_L_allKeys.extend(theseKeys)
        if len(_instructLeft_keyResp_2_L_allKeys):
            instructLeft_keyResp_2_L.keys = _instructLeft_keyResp_2_L_allKeys[-1].name  # just the last key pressed
            instructLeft_keyResp_2_L.rt = _instructLeft_keyResp_2_L_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *instructLeft_keyResp_2_R* updates
    waitOnFlip = False
    if instructLeft_keyResp_2_R.status == NOT_STARTED and expInfo["counterbalance"] == "R":
        # keep track of start time/frame for later
        instructLeft_keyResp_2_R.frameNStart = frameN  # exact frame index
        instructLeft_keyResp_2_R.tStart = t  # local t and not account for scr refresh
        instructLeft_keyResp_2_R.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructLeft_keyResp_2_R, 'tStartRefresh')  # time at next scr refresh
        instructLeft_keyResp_2_R.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructLeft_keyResp_2_R.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructLeft_keyResp_2_R.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructLeft_keyResp_2_R.status == STARTED and not waitOnFlip:
        theseKeys = instructLeft_keyResp_2_R.getKeys(keyList=['8'], waitRelease=False)
        _instructLeft_keyResp_2_R_allKeys.extend(theseKeys)
        if len(_instructLeft_keyResp_2_R_allKeys):
            instructLeft_keyResp_2_R.keys = _instructLeft_keyResp_2_R_allKeys[-1].name  # just the last key pressed
            instructLeft_keyResp_2_R.rt = _instructLeft_keyResp_2_R_allKeys[-1].rt
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

# --- Prepare to start Routine "instructInconRight" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instructInconRight_text_2_L.setText('Sometimes the MIDDLE letter will have a different case from the other letters. However, your goal is to always respond to the MIDDLE letter.\n\nBelow, the MIDDLE letter is lowercase, so you would respond by pressing the right button (8) with your right hand.\n\n\n\n\n\nPress the right button (8) to continue')
instructInconRight_text_2_R.setText('Sometimes the MIDDLE letter will have a different case from the other letters. However, your goal is to always respond to the MIDDLE letter.\n\nBelow, the MIDDLE letter is lowercase, so you would respond by pressing the left button (1) with your left hand.\n\n\n\n\n\nPress the left button (1) to continue')
insructInconRight_keyResp_2_L.keys = []
insructInconRight_keyResp_2_L.rt = []
_insructInconRight_keyResp_2_L_allKeys = []
insructInconRight_keyResp_2_R.keys = []
insructInconRight_keyResp_2_R.rt = []
_insructInconRight_keyResp_2_R_allKeys = []
# keep track of which components have finished
instructInconRightComponents = [instructInconRight_text_2_L, instructInconRight_text_2_R, instructionRight_letters2, prac_highlight_circle_6, insructInconRight_keyResp_2_L, insructInconRight_keyResp_2_R]
for thisComponent in instructInconRightComponents:
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

# --- Run Routine "instructInconRight" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructInconRight_text_2_L* updates
    if instructInconRight_text_2_L.status == NOT_STARTED and expInfo["counterbalance"] == "L":
        # keep track of start time/frame for later
        instructInconRight_text_2_L.frameNStart = frameN  # exact frame index
        instructInconRight_text_2_L.tStart = t  # local t and not account for scr refresh
        instructInconRight_text_2_L.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconRight_text_2_L, 'tStartRefresh')  # time at next scr refresh
        instructInconRight_text_2_L.setAutoDraw(True)
    
    # *instructInconRight_text_2_R* updates
    if instructInconRight_text_2_R.status == NOT_STARTED and expInfo["counterbalance"] == "R":
        # keep track of start time/frame for later
        instructInconRight_text_2_R.frameNStart = frameN  # exact frame index
        instructInconRight_text_2_R.tStart = t  # local t and not account for scr refresh
        instructInconRight_text_2_R.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconRight_text_2_R, 'tStartRefresh')  # time at next scr refresh
        instructInconRight_text_2_R.setAutoDraw(True)
    
    # *instructionRight_letters2* updates
    if instructionRight_letters2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionRight_letters2.frameNStart = frameN  # exact frame index
        instructionRight_letters2.tStart = t  # local t and not account for scr refresh
        instructionRight_letters2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionRight_letters2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructionRight_letters2.started')
        instructionRight_letters2.setAutoDraw(True)
    
    # *prac_highlight_circle_6* updates
    if prac_highlight_circle_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prac_highlight_circle_6.frameNStart = frameN  # exact frame index
        prac_highlight_circle_6.tStart = t  # local t and not account for scr refresh
        prac_highlight_circle_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prac_highlight_circle_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'prac_highlight_circle_6.started')
        prac_highlight_circle_6.setAutoDraw(True)
    
    # *insructInconRight_keyResp_2_L* updates
    waitOnFlip = False
    if insructInconRight_keyResp_2_L.status == NOT_STARTED and expInfo["counterbalance"] == "L":
        # keep track of start time/frame for later
        insructInconRight_keyResp_2_L.frameNStart = frameN  # exact frame index
        insructInconRight_keyResp_2_L.tStart = t  # local t and not account for scr refresh
        insructInconRight_keyResp_2_L.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(insructInconRight_keyResp_2_L, 'tStartRefresh')  # time at next scr refresh
        insructInconRight_keyResp_2_L.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(insructInconRight_keyResp_2_L.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(insructInconRight_keyResp_2_L.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if insructInconRight_keyResp_2_L.status == STARTED and not waitOnFlip:
        theseKeys = insructInconRight_keyResp_2_L.getKeys(keyList=['8'], waitRelease=False)
        _insructInconRight_keyResp_2_L_allKeys.extend(theseKeys)
        if len(_insructInconRight_keyResp_2_L_allKeys):
            insructInconRight_keyResp_2_L.keys = _insructInconRight_keyResp_2_L_allKeys[-1].name  # just the last key pressed
            insructInconRight_keyResp_2_L.rt = _insructInconRight_keyResp_2_L_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *insructInconRight_keyResp_2_R* updates
    waitOnFlip = False
    if insructInconRight_keyResp_2_R.status == NOT_STARTED and expInfo["counterbalance"] == "R":
        # keep track of start time/frame for later
        insructInconRight_keyResp_2_R.frameNStart = frameN  # exact frame index
        insructInconRight_keyResp_2_R.tStart = t  # local t and not account for scr refresh
        insructInconRight_keyResp_2_R.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(insructInconRight_keyResp_2_R, 'tStartRefresh')  # time at next scr refresh
        insructInconRight_keyResp_2_R.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(insructInconRight_keyResp_2_R.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(insructInconRight_keyResp_2_R.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if insructInconRight_keyResp_2_R.status == STARTED and not waitOnFlip:
        theseKeys = insructInconRight_keyResp_2_R.getKeys(keyList=['1'], waitRelease=False)
        _insructInconRight_keyResp_2_R_allKeys.extend(theseKeys)
        if len(_insructInconRight_keyResp_2_R_allKeys):
            insructInconRight_keyResp_2_R.keys = _insructInconRight_keyResp_2_R_allKeys[-1].name  # just the last key pressed
            insructInconRight_keyResp_2_R.rt = _insructInconRight_keyResp_2_R_allKeys[-1].rt
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
    for thisComponent in instructInconRightComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructInconRight" ---
for thisComponent in instructInconRightComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructInconRight" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructInconLeft" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instructInconLeft_text_2_L.setText('Below, the MIDDLE letter is CAPITALIZED, so you would respond by pressing the left button (1) with your left hand.\n\n\n\n\n\n\n\nPress the left button (1) to continue')
instructInconLeft_text_2_R.setText('Below, the MIDDLE letter is CAPITALIZED, so you would respond by pressing the right button (8) with your right hand.\n\n\n\n\n\n\n\nPress the right button (8) to continue')
instructInconLeft_keyResp_2_L.keys = []
instructInconLeft_keyResp_2_L.rt = []
_instructInconLeft_keyResp_2_L_allKeys = []
instructInconLeft_keyResp_2_R.keys = []
instructInconLeft_keyResp_2_R.rt = []
_instructInconLeft_keyResp_2_R_allKeys = []
# keep track of which components have finished
instructInconLeftComponents = [instructInconLeft_text_2_L, instructInconLeft_text_2_R, instructInconLeft_letters2, prac_highlight_circle_8, instructInconLeft_keyResp_2_L, instructInconLeft_keyResp_2_R]
for thisComponent in instructInconLeftComponents:
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

# --- Run Routine "instructInconLeft" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructInconLeft_text_2_L* updates
    if instructInconLeft_text_2_L.status == NOT_STARTED and expInfo["counterbalance"] == "L":
        # keep track of start time/frame for later
        instructInconLeft_text_2_L.frameNStart = frameN  # exact frame index
        instructInconLeft_text_2_L.tStart = t  # local t and not account for scr refresh
        instructInconLeft_text_2_L.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconLeft_text_2_L, 'tStartRefresh')  # time at next scr refresh
        instructInconLeft_text_2_L.setAutoDraw(True)
    
    # *instructInconLeft_text_2_R* updates
    if instructInconLeft_text_2_R.status == NOT_STARTED and expInfo["counterbalance"] == "R":
        # keep track of start time/frame for later
        instructInconLeft_text_2_R.frameNStart = frameN  # exact frame index
        instructInconLeft_text_2_R.tStart = t  # local t and not account for scr refresh
        instructInconLeft_text_2_R.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconLeft_text_2_R, 'tStartRefresh')  # time at next scr refresh
        instructInconLeft_text_2_R.setAutoDraw(True)
    
    # *instructInconLeft_letters2* updates
    if instructInconLeft_letters2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructInconLeft_letters2.frameNStart = frameN  # exact frame index
        instructInconLeft_letters2.tStart = t  # local t and not account for scr refresh
        instructInconLeft_letters2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconLeft_letters2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructInconLeft_letters2.started')
        instructInconLeft_letters2.setAutoDraw(True)
    
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
    
    # *instructInconLeft_keyResp_2_L* updates
    waitOnFlip = False
    if instructInconLeft_keyResp_2_L.status == NOT_STARTED and expInfo["counterbalance"] == "L":
        # keep track of start time/frame for later
        instructInconLeft_keyResp_2_L.frameNStart = frameN  # exact frame index
        instructInconLeft_keyResp_2_L.tStart = t  # local t and not account for scr refresh
        instructInconLeft_keyResp_2_L.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconLeft_keyResp_2_L, 'tStartRefresh')  # time at next scr refresh
        instructInconLeft_keyResp_2_L.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructInconLeft_keyResp_2_L.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructInconLeft_keyResp_2_L.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructInconLeft_keyResp_2_L.status == STARTED and not waitOnFlip:
        theseKeys = instructInconLeft_keyResp_2_L.getKeys(keyList=['1'], waitRelease=False)
        _instructInconLeft_keyResp_2_L_allKeys.extend(theseKeys)
        if len(_instructInconLeft_keyResp_2_L_allKeys):
            instructInconLeft_keyResp_2_L.keys = _instructInconLeft_keyResp_2_L_allKeys[-1].name  # just the last key pressed
            instructInconLeft_keyResp_2_L.rt = _instructInconLeft_keyResp_2_L_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *instructInconLeft_keyResp_2_R* updates
    waitOnFlip = False
    if instructInconLeft_keyResp_2_R.status == NOT_STARTED and expInfo["counterbalance"] == "R":
        # keep track of start time/frame for later
        instructInconLeft_keyResp_2_R.frameNStart = frameN  # exact frame index
        instructInconLeft_keyResp_2_R.tStart = t  # local t and not account for scr refresh
        instructInconLeft_keyResp_2_R.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructInconLeft_keyResp_2_R, 'tStartRefresh')  # time at next scr refresh
        instructInconLeft_keyResp_2_R.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructInconLeft_keyResp_2_R.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructInconLeft_keyResp_2_R.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructInconLeft_keyResp_2_R.status == STARTED and not waitOnFlip:
        theseKeys = instructInconLeft_keyResp_2_R.getKeys(keyList=['8'], waitRelease=False)
        _instructInconLeft_keyResp_2_R_allKeys.extend(theseKeys)
        if len(_instructInconLeft_keyResp_2_R_allKeys):
            instructInconLeft_keyResp_2_R.keys = _instructInconLeft_keyResp_2_R_allKeys[-1].name  # just the last key pressed
            instructInconLeft_keyResp_2_R.rt = _instructInconLeft_keyResp_2_R_allKeys[-1].rt
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
    for thisComponent in instructInconLeftComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructInconLeft" ---
for thisComponent in instructInconLeftComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructInconLeft" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "respond_onceInstruct" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
space_end_keyResp_8.keys = []
space_end_keyResp_8.rt = []
_space_end_keyResp_8_allKeys = []
left_reminder_text_2.setText(left_reminder)
right_reminder_text_2.setText(right_reminder)
# keep track of which components have finished
respond_onceInstructComponents = [respond_once_text, space_end_keyResp_8, left_reminder_text_2, right_reminder_text_2]
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
        theseKeys = space_end_keyResp_8.getKeys(keyList=['space'], waitRelease=False)
        _space_end_keyResp_8_allKeys.extend(theseKeys)
        if len(_space_end_keyResp_8_allKeys):
            space_end_keyResp_8.keys = _space_end_keyResp_8_allKeys[-1].name  # just the last key pressed
            space_end_keyResp_8.rt = _space_end_keyResp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *left_reminder_text_2* updates
    if left_reminder_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        left_reminder_text_2.frameNStart = frameN  # exact frame index
        left_reminder_text_2.tStart = t  # local t and not account for scr refresh
        left_reminder_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(left_reminder_text_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'left_reminder_text_2.started')
        left_reminder_text_2.setAutoDraw(True)
    
    # *right_reminder_text_2* updates
    if right_reminder_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        right_reminder_text_2.frameNStart = frameN  # exact frame index
        right_reminder_text_2.tStart = t  # local t and not account for scr refresh
        right_reminder_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(right_reminder_text_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'right_reminder_text_2.started')
        right_reminder_text_2.setAutoDraw(True)
    
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
    left_reminder_text.setText(left_reminder)
    right_reminder_text.setText(right_reminder)
    space_end_keyResp_9.keys = []
    space_end_keyResp_9.rt = []
    _space_end_keyResp_9_allKeys = []
    # keep track of which components have finished
    prac_blockRemindersComponents = [prac_blockText, prac_reminder_text, left_reminder_text, right_reminder_text, space_end_keyResp_9]
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
        
        # *left_reminder_text* updates
        if left_reminder_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            left_reminder_text.frameNStart = frameN  # exact frame index
            left_reminder_text.tStart = t  # local t and not account for scr refresh
            left_reminder_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_reminder_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'left_reminder_text.started')
            left_reminder_text.setAutoDraw(True)
        
        # *right_reminder_text* updates
        if right_reminder_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            right_reminder_text.frameNStart = frameN  # exact frame index
            right_reminder_text.tStart = t  # local t and not account for scr refresh
            right_reminder_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_reminder_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'right_reminder_text.started')
            right_reminder_text.setAutoDraw(True)
        
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
            theseKeys = space_end_keyResp_9.getKeys(keyList=['space'], waitRelease=False)
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
    # pick the ISI for the next routine
    # for the online version, this code component should be set to 'both' to remove the 'np'
    # at the start of np.linspace (this is a python library JS won't know what to call. 
    
    # make range from a to b in n stepsizes
    ISIRange = np.linspace(2600, 3000, 400)
    
    # picking from a shuffled array is easier for random selection in JS
    shuffle(ISIRange)
    thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
    
    # save this ISI to our output file
    # prac_block_loop.addData('ISI_fixation', thisISI)
    
    #if endCondition: # skip all trials for this condition; participant will not play game.
    #    task_block_loop.finished = True
    #    continueRoutine = False
    
    # empty lists of used letters
    used_letters = []
    shown_letters = []
    initFixation_img_2.setImage('img/fixationCross.png')
    left_reminder_text_3.setText(left_reminder)
    right_reminder_text_3.setText(right_reminder)
    # keep track of which components have finished
    prac_initFixationComponents = [initFixation_img_2, left_reminder_text_3, right_reminder_text_3]
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
        
        # *left_reminder_text_3* updates
        if left_reminder_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            left_reminder_text_3.frameNStart = frameN  # exact frame index
            left_reminder_text_3.tStart = t  # local t and not account for scr refresh
            left_reminder_text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_reminder_text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'left_reminder_text_3.started')
            left_reminder_text_3.setAutoDraw(True)
        if left_reminder_text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > left_reminder_text_3.tStartRefresh + thisISI-frameTolerance:
                # keep track of stop time/frame for later
                left_reminder_text_3.tStop = t  # not accounting for scr refresh
                left_reminder_text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'left_reminder_text_3.stopped')
                left_reminder_text_3.setAutoDraw(False)
        
        # *right_reminder_text_3* updates
        if right_reminder_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            right_reminder_text_3.frameNStart = frameN  # exact frame index
            right_reminder_text_3.tStart = t  # local t and not account for scr refresh
            right_reminder_text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_reminder_text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'right_reminder_text_3.started')
            right_reminder_text_3.setAutoDraw(True)
        if right_reminder_text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > right_reminder_text_3.tStartRefresh + thisISI-frameTolerance:
                # keep track of stop time/frame for later
                right_reminder_text_3.tStop = t  # not accounting for scr refresh
                right_reminder_text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'right_reminder_text_3.stopped')
                right_reminder_text_3.setAutoDraw(False)
        
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
    prac_trial_loop = data.TrialHandler(nReps=1.0, method='fullRandom', 
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
        # Run 'Begin Routine' code from prac_flanker_letters_code
        # leave only not-used letters for flanker
        if repeat_letters == True:
            flanker_letters = \
            [i for i in wm_letters]
        elif repeat_letters == False:
            flanker_letters = \
            [i for i in wm_letters\
            if i not in used_letters]
        
        # if there is an L, we don't want in in flanker
        if "L" in flanker_letters:
            flanker_letters.remove("L")
            
        # shuffle again
        shuffle(flanker_letters)
        
        # take flanker letter and add to used flanker letters
        flanker_stim = flanker_letters[0]
        
        # create flanker stimuli based on the congruency and case
        if congruent == 1 and target == "uppercase":
            flanker_stim = "{}".format(flanker_stim*5)
        elif congruent == 1 and target == "lowercase":
            flanker_stim = "{}".format(flanker_stim.lower()*5)
        elif congruent == 0 and target == "uppercase":
            flanker_stim = "{}{}{}".format(flanker_stim.lower()*2,
            flanker_stim, flanker_stim.lower()*2)
        elif congruent == 0 and target == "lowercase":
            flanker_stim = "{}{}{}".format(flanker_stim*2,
            flanker_stim.lower(), flanker_stim*2)
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
        left_reminder_text_4.setText(left_reminder)
        right_reminder_text_4.setText(right_reminder)
        prac_stim_keyResp.keys = []
        prac_stim_keyResp.rt = []
        _prac_stim_keyResp_allKeys = []
        # keep track of which components have finished
        prac_stimRoutineComponents = [prac_flanker_text_stim, prac_fixImg, left_reminder_text_4, right_reminder_text_4, prac_stim_keyResp]
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
            
            # *left_reminder_text_4* updates
            if left_reminder_text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                left_reminder_text_4.frameNStart = frameN  # exact frame index
                left_reminder_text_4.tStart = t  # local t and not account for scr refresh
                left_reminder_text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left_reminder_text_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'left_reminder_text_4.started')
                left_reminder_text_4.setAutoDraw(True)
            if left_reminder_text_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > left_reminder_text_4.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    left_reminder_text_4.tStop = t  # not accounting for scr refresh
                    left_reminder_text_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'left_reminder_text_4.stopped')
                    left_reminder_text_4.setAutoDraw(False)
            
            # *right_reminder_text_4* updates
            if right_reminder_text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                right_reminder_text_4.frameNStart = frameN  # exact frame index
                right_reminder_text_4.tStart = t  # local t and not account for scr refresh
                right_reminder_text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right_reminder_text_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'right_reminder_text_4.started')
                right_reminder_text_4.setAutoDraw(True)
            if right_reminder_text_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > right_reminder_text_4.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    right_reminder_text_4.tStop = t  # not accounting for scr refresh
                    right_reminder_text_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'right_reminder_text_4.stopped')
                    right_reminder_text_4.setAutoDraw(False)
            
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
        # Run 'End Routine' code from prac_flanker_letters_code
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
        
        if expInfo["counterbalance"] == "L":
            if prac_stim_keyResp.keys: #if at least one response was made this trial
                if prac_stim_keyResp.keys[0] == '1': #if the FIRST button pressed was a '1'
                    if target == 'uppercase': #if a left target stim was shown this trial
                        accuracy = 1 #mark this trial as correct
                        numCorr = numCorr +1 #iterate number of correct responses for this supertrial
                    elif target == 'lowercase': #if a right target stim was shown this trial
                        accuracy = 0 #mark this trial as an error
                elif prac_stim_keyResp.keys[0] == '8': #if the FIRST button pressed was a '8'
                    if target == 'lowercase': #if a right target stim was shown this trial
                        accuracy = 1 #mark this trial as correct
                        numCorr = numCorr +1 #iterate number of correct responses for this supertrial
                    elif target == 'uppercase': #if a left target stim was shown this trial
                        accuracy = 0 #mark this trial as an error
        
            elif not prac_stim_keyResp.keys: # if no response was made
                accuracy = 0
            
        elif expInfo["counterbalance"] == "R":
            if prac_stim_keyResp.keys: #if at least one response was made this trial
                if prac_stim_keyResp.keys[0] == '1': #if the FIRST button pressed was a '1'
                    if target == 'lowercase': #if a left target stim was shown this trial
                        accuracy = 1 #mark this trial as correct
                        numCorr = numCorr +1 #iterate number of correct responses for this supertrial
                    elif target == 'uppercase': #if a right target stim was shown this trial
                        accuracy = 0 #mark this trial as an error
                elif prac_stim_keyResp.keys[0] == '8': #if the FIRST button pressed was a '8'
                    if target == 'uppercase': #if a right target stim was shown this trial
                        accuracy = 1 #mark this trial as correct
                        numCorr = numCorr +1 #iterate number of correct responses for this supertrial
                    elif target == 'lowercase': #if a left target stim was shown this trial
                        accuracy = 0 #mark this trial as an error
        
            elif not prac_stim_keyResp.keys: # if no response was made
                accuracy = 0
                    
        # save this trial's accuracy to our output file
        prac_trial_loop.addData('prac_flanker_accuracy', accuracy)
        # the Routine "prac_stimRoutine" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'prac_trial_loop'
    
    
    # --- Prepare to start Routine "prac_blockFeed" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from prac_blockFeed_code
    blockAcc = numCorr / trialNum # compute accuracy for this block
    
    if blockAcc >= fl_thresh: # if accuracy >= threshold then say practice is complete and end practice loop to continue to main exp
        outPut = 'Well done! Now you are ready to practice both games together!' #feedback presented
        prac_block_loop.finished = True #end practice loop to continue to main exp
    elif blockAcc <= fl_thresh: # if accuracy < threshold then say that practice needs to be repeated and DO NOT end practice loop, instead, allow it to repeat
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
            theseKeys = prac_blockFeed_keyResp.getKeys(keyList=['space','s'], waitRelease=False)
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


# --- Prepare to start Routine "instruct_SuperTrial" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
space_end_keyResp_10.keys = []
space_end_keyResp_10.rt = []
_space_end_keyResp_10_allKeys = []
# keep track of which components have finished
instruct_SuperTrialComponents = [intruct_SuperTrial_text, space_end_keyResp_10]
for thisComponent in instruct_SuperTrialComponents:
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

# --- Run Routine "instruct_SuperTrial" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intruct_SuperTrial_text* updates
    if intruct_SuperTrial_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intruct_SuperTrial_text.frameNStart = frameN  # exact frame index
        intruct_SuperTrial_text.tStart = t  # local t and not account for scr refresh
        intruct_SuperTrial_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intruct_SuperTrial_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intruct_SuperTrial_text.started')
        intruct_SuperTrial_text.setAutoDraw(True)
    
    # *space_end_keyResp_10* updates
    waitOnFlip = False
    if space_end_keyResp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_end_keyResp_10.frameNStart = frameN  # exact frame index
        space_end_keyResp_10.tStart = t  # local t and not account for scr refresh
        space_end_keyResp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_end_keyResp_10, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'space_end_keyResp_10.started')
        space_end_keyResp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space_end_keyResp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space_end_keyResp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space_end_keyResp_10.status == STARTED and not waitOnFlip:
        theseKeys = space_end_keyResp_10.getKeys(keyList=['space'], waitRelease=False)
        _space_end_keyResp_10_allKeys.extend(theseKeys)
        if len(_space_end_keyResp_10_allKeys):
            space_end_keyResp_10.keys = _space_end_keyResp_10_allKeys[-1].name  # just the last key pressed
            space_end_keyResp_10.rt = _space_end_keyResp_10_allKeys[-1].rt
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
    for thisComponent in instruct_SuperTrialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruct_SuperTrial" ---
for thisComponent in instruct_SuperTrialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if space_end_keyResp_10.keys in ['', [], None]:  # No response was made
    space_end_keyResp_10.keys = None
thisExp.addData('space_end_keyResp_10.keys',space_end_keyResp_10.keys)
if space_end_keyResp_10.keys != None:  # we had a response
    thisExp.addData('space_end_keyResp_10.rt', space_end_keyResp_10.rt)
thisExp.nextEntry()
# the Routine "instruct_SuperTrial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
pracSuperTrial_block_loop = data.TrialHandler(nReps=99.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='pracSuperTrial_block_loop')
thisExp.addLoop(pracSuperTrial_block_loop)  # add the loop to the experiment
thisPracSuperTrial_block_loop = pracSuperTrial_block_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracSuperTrial_block_loop.rgb)
if thisPracSuperTrial_block_loop != None:
    for paramName in thisPracSuperTrial_block_loop:
        exec('{} = thisPracSuperTrial_block_loop[paramName]'.format(paramName))

for thisPracSuperTrial_block_loop in pracSuperTrial_block_loop:
    currentLoop = pracSuperTrial_block_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPracSuperTrial_block_loop.rgb)
    if thisPracSuperTrial_block_loop != None:
        for paramName in thisPracSuperTrial_block_loop:
            exec('{} = thisPracSuperTrial_block_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "reminder_SuperTrial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from wm_letters_code_2
    # define a new letters list before new supertrial
    supertrial_letters = wm_letters.copy()
    shuffle(supertrial_letters)
    
    # clean used letters list before new supertrial
    used_letters = []
    used_letters_fl = []
    shown_letters = []
    task_blockReminders_keyResp_2.keys = []
    task_blockReminders_keyResp_2.rt = []
    _task_blockReminders_keyResp_2_allKeys = []
    # keep track of which components have finished
    reminder_SuperTrialComponents = [prac_blockText_3, task_blockReminders_text_2, task_blockReminders_keyResp_2]
    for thisComponent in reminder_SuperTrialComponents:
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
    
    # --- Run Routine "reminder_SuperTrial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_blockText_3* updates
        if prac_blockText_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_blockText_3.frameNStart = frameN  # exact frame index
            prac_blockText_3.tStart = t  # local t and not account for scr refresh
            prac_blockText_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_blockText_3, 'tStartRefresh')  # time at next scr refresh
            prac_blockText_3.setAutoDraw(True)
        
        # *task_blockReminders_text_2* updates
        if task_blockReminders_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            task_blockReminders_text_2.frameNStart = frameN  # exact frame index
            task_blockReminders_text_2.tStart = t  # local t and not account for scr refresh
            task_blockReminders_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(task_blockReminders_text_2, 'tStartRefresh')  # time at next scr refresh
            task_blockReminders_text_2.setAutoDraw(True)
        
        # *task_blockReminders_keyResp_2* updates
        waitOnFlip = False
        if task_blockReminders_keyResp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            task_blockReminders_keyResp_2.frameNStart = frameN  # exact frame index
            task_blockReminders_keyResp_2.tStart = t  # local t and not account for scr refresh
            task_blockReminders_keyResp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(task_blockReminders_keyResp_2, 'tStartRefresh')  # time at next scr refresh
            task_blockReminders_keyResp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(task_blockReminders_keyResp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(task_blockReminders_keyResp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if task_blockReminders_keyResp_2.status == STARTED and not waitOnFlip:
            theseKeys = task_blockReminders_keyResp_2.getKeys(keyList=['space'], waitRelease=False)
            _task_blockReminders_keyResp_2_allKeys.extend(theseKeys)
            if len(_task_blockReminders_keyResp_2_allKeys):
                task_blockReminders_keyResp_2.keys = _task_blockReminders_keyResp_2_allKeys[-1].name  # just the last key pressed
                task_blockReminders_keyResp_2.rt = _task_blockReminders_keyResp_2_allKeys[-1].rt
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
        for thisComponent in reminder_SuperTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "reminder_SuperTrial" ---
    for thisComponent in reminder_SuperTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "reminder_SuperTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    pracSuperTrial_loop = data.TrialHandler(nReps=2.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='pracSuperTrial_loop')
    thisExp.addLoop(pracSuperTrial_loop)  # add the loop to the experiment
    thisPracSuperTrial_loop = pracSuperTrial_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracSuperTrial_loop.rgb)
    if thisPracSuperTrial_loop != None:
        for paramName in thisPracSuperTrial_loop:
            exec('{} = thisPracSuperTrial_loop[paramName]'.format(paramName))
    
    for thisPracSuperTrial_loop in pracSuperTrial_loop:
        currentLoop = pracSuperTrial_loop
        # abbreviate parameter names if possible (e.g. rgb = thisPracSuperTrial_loop.rgb)
        if thisPracSuperTrial_loop != None:
            for paramName in thisPracSuperTrial_loop:
                exec('{} = thisPracSuperTrial_loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "prac_initFixaion_WM" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from prac_fixWM_code
        # pick the ISI for the next routine
        # for the online version, this code component should be set to 'both' to remove the 'np'
        # at the start of np.linspace (this is a python library JS won't know what to call. 
        
        # make range from a to b in n stepsizes
        ISIRange = np.linspace(2600, 3000, 400)
        
        # picking from a shuffled array is easier for random selection in JS
        shuffle(ISIRange)
        thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
        
        # empty lists of used letters
        used_letters = []
        used_letters_fl = []
        shown_letters = []
        initFixation_img_4.setImage('img/fixationCross.png')
        # keep track of which components have finished
        prac_initFixaion_WMComponents = [initFixation_img_4]
        for thisComponent in prac_initFixaion_WMComponents:
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
        
        # --- Run Routine "prac_initFixaion_WM" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *initFixation_img_4* updates
            if initFixation_img_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                initFixation_img_4.frameNStart = frameN  # exact frame index
                initFixation_img_4.tStart = t  # local t and not account for scr refresh
                initFixation_img_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(initFixation_img_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'initFixation_img_4.started')
                initFixation_img_4.setAutoDraw(True)
            if initFixation_img_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > initFixation_img_4.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    initFixation_img_4.tStop = t  # not accounting for scr refresh
                    initFixation_img_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'initFixation_img_4.stopped')
                    initFixation_img_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prac_initFixaion_WMComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "prac_initFixaion_WM" ---
        for thisComponent in prac_initFixaion_WMComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "prac_initFixaion_WM" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        pracSuperTrial_seq_loop = data.TrialHandler(nReps=4.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='pracSuperTrial_seq_loop')
        thisExp.addLoop(pracSuperTrial_seq_loop)  # add the loop to the experiment
        thisPracSuperTrial_seq_loop = pracSuperTrial_seq_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPracSuperTrial_seq_loop.rgb)
        if thisPracSuperTrial_seq_loop != None:
            for paramName in thisPracSuperTrial_seq_loop:
                exec('{} = thisPracSuperTrial_seq_loop[paramName]'.format(paramName))
        
        for thisPracSuperTrial_seq_loop in pracSuperTrial_seq_loop:
            currentLoop = pracSuperTrial_seq_loop
            # abbreviate parameter names if possible (e.g. rgb = thisPracSuperTrial_seq_loop.rgb)
            if thisPracSuperTrial_seq_loop != None:
                for paramName in thisPracSuperTrial_seq_loop:
                    exec('{} = thisPracSuperTrial_seq_loop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "pracSuperTrial_seq" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from we_seq_code_5
            # choose the case of a letter randomly (0 = capitalized, 1 = lowercase)
            case_randomizer = random.randint(0, 1)
            
            # pick a letter to show for this trial
            shuffle(wm_letters)
            
            if case_randomizer == 0:
                letter = [i for i in wm_letters if i not in used_letters][0]
            elif case_randomizer == 1:
                letter = [i.lower() for i in wm_letters if i not in used_letters][0]
            
            # remember the letter shown in each trial
            used_letters.append(letter.upper())
            shown_letters.append(letter)
            # Run 'Begin Routine' code from wm_isi_code_5
            # pick the ISI for the next letter to appear
            
            # make range from a to b in n stepsizes
            wm_ISIRange = np.linspace(400, 800, 400)
            
            # picking from a shuffled array is easier for random selection in JS
            shuffle(wm_ISIRange)
            wm_thisISI = wm_ISIRange[0]/1000 # the first item of the shuffled array 
            
            # save this ISI to our output file
            pracSuperTrial_seq_loop.addData('pracSuperTrial_wm_isi', wm_thisISI)
            
            wm_stim_5.setText(letter)
            wm_fixImg.setImage('img/fixationCross.png')
            # keep track of which components have finished
            pracSuperTrial_seqComponents = [wm_stim_5, wm_fixImg]
            for thisComponent in pracSuperTrial_seqComponents:
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
            
            # --- Run Routine "pracSuperTrial_seq" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *wm_stim_5* updates
                if wm_stim_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    wm_stim_5.frameNStart = frameN  # exact frame index
                    wm_stim_5.tStart = t  # local t and not account for scr refresh
                    wm_stim_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(wm_stim_5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'wm_stim_5.started')
                    wm_stim_5.setAutoDraw(True)
                if wm_stim_5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > wm_stim_5.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        wm_stim_5.tStop = t  # not accounting for scr refresh
                        wm_stim_5.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'wm_stim_5.stopped')
                        wm_stim_5.setAutoDraw(False)
                
                # *wm_fixImg* updates
                if wm_fixImg.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    wm_fixImg.frameNStart = frameN  # exact frame index
                    wm_fixImg.tStart = t  # local t and not account for scr refresh
                    wm_fixImg.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(wm_fixImg, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'wm_fixImg.started')
                    wm_fixImg.setAutoDraw(True)
                if wm_fixImg.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > wm_fixImg.tStartRefresh + wm_thisISI+0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        wm_fixImg.tStop = t  # not accounting for scr refresh
                        wm_fixImg.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'wm_fixImg.stopped')
                        wm_fixImg.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in pracSuperTrial_seqComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "pracSuperTrial_seq" ---
            for thisComponent in pracSuperTrial_seqComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from we_seq_code_5
            # write used and shown letters to data
            pracSuperTrial_seq_loop.addData('pracSuperTrial_used_letters',
            ''.join(used_letters))
            pracSuperTrial_seq_loop.addData('pracSuperTrial_shown_letters',
            ''.join(shown_letters))
            # the Routine "pracSuperTrial_seq" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 4.0 repeats of 'pracSuperTrial_seq_loop'
        
        
        # --- Prepare to start Routine "prac_SuperTrialFixation" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from prac_endTask_code_2
        # pick the ISI for the next routine
        # for the online version, this code component should be set to 'both' to remove the 'np'
        # at the start of np.linspace (this is a python library JS won't know what to call. 
        
        # make range from a to b in n stepsizes
        ISIRange = np.linspace(1600, 2000, 400)
        
        # picking from a shuffled array is easier for random selection in JS
        shuffle(ISIRange)
        thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
        
        # save this ISI to our output file
        #prac_block_loop.addData('ISI_fixation', thisISI)
        #if endCondition: # skip all trials for this condition; participant will not play game.
        #    task_block_loop.finished = True
        #    continueRoutine = False
        initFixation_img_3.setImage('img/fixationCross.png')
        left_reminder_text_5.setText(left_reminder)
        right_reminder_text_5.setText(right_reminder)
        # keep track of which components have finished
        prac_SuperTrialFixationComponents = [initFixation_img_3, left_reminder_text_5, right_reminder_text_5]
        for thisComponent in prac_SuperTrialFixationComponents:
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
        
        # --- Run Routine "prac_SuperTrialFixation" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *initFixation_img_3* updates
            if initFixation_img_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                initFixation_img_3.frameNStart = frameN  # exact frame index
                initFixation_img_3.tStart = t  # local t and not account for scr refresh
                initFixation_img_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(initFixation_img_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'initFixation_img_3.started')
                initFixation_img_3.setAutoDraw(True)
            if initFixation_img_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > initFixation_img_3.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    initFixation_img_3.tStop = t  # not accounting for scr refresh
                    initFixation_img_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'initFixation_img_3.stopped')
                    initFixation_img_3.setAutoDraw(False)
            
            # *left_reminder_text_5* updates
            if left_reminder_text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                left_reminder_text_5.frameNStart = frameN  # exact frame index
                left_reminder_text_5.tStart = t  # local t and not account for scr refresh
                left_reminder_text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left_reminder_text_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'left_reminder_text_5.started')
                left_reminder_text_5.setAutoDraw(True)
            if left_reminder_text_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > left_reminder_text_5.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    left_reminder_text_5.tStop = t  # not accounting for scr refresh
                    left_reminder_text_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'left_reminder_text_5.stopped')
                    left_reminder_text_5.setAutoDraw(False)
            
            # *right_reminder_text_5* updates
            if right_reminder_text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                right_reminder_text_5.frameNStart = frameN  # exact frame index
                right_reminder_text_5.tStart = t  # local t and not account for scr refresh
                right_reminder_text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right_reminder_text_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'right_reminder_text_5.started')
                right_reminder_text_5.setAutoDraw(True)
            if right_reminder_text_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > right_reminder_text_5.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    right_reminder_text_5.tStop = t  # not accounting for scr refresh
                    right_reminder_text_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'right_reminder_text_5.stopped')
                    right_reminder_text_5.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prac_SuperTrialFixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "prac_SuperTrialFixation" ---
        for thisComponent in prac_SuperTrialFixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "prac_SuperTrialFixation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        pracSuperTrial_flanker_loop = data.TrialHandler(nReps=2.0, method='fullRandom', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('prac_trials.xlsx'),
            seed=None, name='pracSuperTrial_flanker_loop')
        thisExp.addLoop(pracSuperTrial_flanker_loop)  # add the loop to the experiment
        thisPracSuperTrial_flanker_loop = pracSuperTrial_flanker_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPracSuperTrial_flanker_loop.rgb)
        if thisPracSuperTrial_flanker_loop != None:
            for paramName in thisPracSuperTrial_flanker_loop:
                exec('{} = thisPracSuperTrial_flanker_loop[paramName]'.format(paramName))
        
        for thisPracSuperTrial_flanker_loop in pracSuperTrial_flanker_loop:
            currentLoop = pracSuperTrial_flanker_loop
            # abbreviate parameter names if possible (e.g. rgb = thisPracSuperTrial_flanker_loop.rgb)
            if thisPracSuperTrial_flanker_loop != None:
                for paramName in thisPracSuperTrial_flanker_loop:
                    exec('{} = thisPracSuperTrial_flanker_loop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "pracSuperTrial_flanker" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from flanker_letters_code_2
            # leave only not-used letters for flanker
            if repeat_letters == True:
                flanker_letters = \
                [i for i in wm_letters]
            elif repeat_letters == False:
                flanker_letters = \
                [i for i in wm_letters if i not in used_letters]
            
            if repeat_letters_fl == False:
                flanker_letters = [i for i in flanker_letters\
                if i not in used_letters_fl]
            
            # if there is an L, we don't want in in flanker
            if "L" in flanker_letters:
                flanker_letters.remove("L")
                
            # shuffle again
            shuffle(flanker_letters)
            
            # take flanker letter and add to used flanker letters
            flanker_stim = flanker_letters[0]
            used_letters_fl.append(flanker_stim)
            
            # create flanker stimuli based on the congruency and case
            if congruent == 1 and target == "uppercase":
                flanker_stim = "{}".format(flanker_stim*5)
            elif congruent == 1 and target == "lowercase":
                flanker_stim = "{}".format(flanker_stim.lower()*5)
            elif congruent == 0 and target == "uppercase":
                flanker_stim = "{}{}{}".format(flanker_stim.lower()*2,
                flanker_stim, flanker_stim.lower()*2)
            elif congruent == 0 and target == "lowercase":
                flanker_stim = "{}{}{}".format(flanker_stim*2,
                flanker_stim.lower(), flanker_stim*2)
            else: flanker_stim = "error"
            # Run 'Begin Routine' code from task_isi_code_2
            # pick the ISI for the next routine
            # for the online version, this code component should be set to 'both' to remove the 'np'
            # at the start of np.linspace (this is a python library JS won't know what to call. 
            
            # make range from a to b in n stepsizes
            ISIRange = np.linspace(1300, 1800, 500)
            
            # picking from a shuffled array is easier for random selection in JS
            shuffle(ISIRange)
            thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
            
            # save this ISI to our output file
            pracSuperTrial_flanker_loop.addData('prac_SuperTrial_fl_isi', thisISI)
            
            flanker_text_stim_2.setText(flanker_stim)
            left_reminder_text_6.setText(left_reminder)
            right_reminder_text_6.setText(right_reminder)
            task_fixImg_2.setImage('img/fixationCross.png')
            task_stim_keyResp_2.keys = []
            task_stim_keyResp_2.rt = []
            _task_stim_keyResp_2_allKeys = []
            # keep track of which components have finished
            pracSuperTrial_flankerComponents = [flanker_text_stim_2, left_reminder_text_6, right_reminder_text_6, task_fixImg_2, task_stim_keyResp_2]
            for thisComponent in pracSuperTrial_flankerComponents:
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
            
            # --- Run Routine "pracSuperTrial_flanker" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *flanker_text_stim_2* updates
                if flanker_text_stim_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    flanker_text_stim_2.frameNStart = frameN  # exact frame index
                    flanker_text_stim_2.tStart = t  # local t and not account for scr refresh
                    flanker_text_stim_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(flanker_text_stim_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'flanker_text_stim_2.started')
                    flanker_text_stim_2.setAutoDraw(True)
                if flanker_text_stim_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > flanker_text_stim_2.tStartRefresh + 0.2-frameTolerance:
                        # keep track of stop time/frame for later
                        flanker_text_stim_2.tStop = t  # not accounting for scr refresh
                        flanker_text_stim_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'flanker_text_stim_2.stopped')
                        flanker_text_stim_2.setAutoDraw(False)
                
                # *left_reminder_text_6* updates
                if left_reminder_text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    left_reminder_text_6.frameNStart = frameN  # exact frame index
                    left_reminder_text_6.tStart = t  # local t and not account for scr refresh
                    left_reminder_text_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(left_reminder_text_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'left_reminder_text_6.started')
                    left_reminder_text_6.setAutoDraw(True)
                if left_reminder_text_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > left_reminder_text_6.tStartRefresh + thisISI-frameTolerance:
                        # keep track of stop time/frame for later
                        left_reminder_text_6.tStop = t  # not accounting for scr refresh
                        left_reminder_text_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'left_reminder_text_6.stopped')
                        left_reminder_text_6.setAutoDraw(False)
                
                # *right_reminder_text_6* updates
                if right_reminder_text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    right_reminder_text_6.frameNStart = frameN  # exact frame index
                    right_reminder_text_6.tStart = t  # local t and not account for scr refresh
                    right_reminder_text_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(right_reminder_text_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'right_reminder_text_6.started')
                    right_reminder_text_6.setAutoDraw(True)
                if right_reminder_text_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > right_reminder_text_6.tStartRefresh + thisISI-frameTolerance:
                        # keep track of stop time/frame for later
                        right_reminder_text_6.tStop = t  # not accounting for scr refresh
                        right_reminder_text_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'right_reminder_text_6.stopped')
                        right_reminder_text_6.setAutoDraw(False)
                
                # *task_fixImg_2* updates
                if task_fixImg_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    task_fixImg_2.frameNStart = frameN  # exact frame index
                    task_fixImg_2.tStart = t  # local t and not account for scr refresh
                    task_fixImg_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(task_fixImg_2, 'tStartRefresh')  # time at next scr refresh
                    task_fixImg_2.setAutoDraw(True)
                if task_fixImg_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > task_fixImg_2.tStartRefresh + thisISI-frameTolerance:
                        # keep track of stop time/frame for later
                        task_fixImg_2.tStop = t  # not accounting for scr refresh
                        task_fixImg_2.frameNStop = frameN  # exact frame index
                        task_fixImg_2.setAutoDraw(False)
                
                # *task_stim_keyResp_2* updates
                waitOnFlip = False
                if task_stim_keyResp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    task_stim_keyResp_2.frameNStart = frameN  # exact frame index
                    task_stim_keyResp_2.tStart = t  # local t and not account for scr refresh
                    task_stim_keyResp_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(task_stim_keyResp_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'task_stim_keyResp_2.started')
                    task_stim_keyResp_2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(task_stim_keyResp_2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(task_stim_keyResp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if task_stim_keyResp_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > task_stim_keyResp_2.tStartRefresh + thisISI-frameTolerance:
                        # keep track of stop time/frame for later
                        task_stim_keyResp_2.tStop = t  # not accounting for scr refresh
                        task_stim_keyResp_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'task_stim_keyResp_2.stopped')
                        task_stim_keyResp_2.status = FINISHED
                if task_stim_keyResp_2.status == STARTED and not waitOnFlip:
                    theseKeys = task_stim_keyResp_2.getKeys(keyList=['1','8'], waitRelease=False)
                    _task_stim_keyResp_2_allKeys.extend(theseKeys)
                    if len(_task_stim_keyResp_2_allKeys):
                        task_stim_keyResp_2.keys = [key.name for key in _task_stim_keyResp_2_allKeys]  # storing all keys
                        task_stim_keyResp_2.rt = [key.rt for key in _task_stim_keyResp_2_allKeys]
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in pracSuperTrial_flankerComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "pracSuperTrial_flanker" ---
            for thisComponent in pracSuperTrial_flankerComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from flanker_letters_code_2
            # write flanker stimuli to data
            pracSuperTrial_flanker_loop.addData('pracSuperTrial_flanker_stim',
            flanker_stim)
            # check responses
            if task_stim_keyResp_2.keys in ['', [], None]:  # No response was made
                task_stim_keyResp_2.keys = None
            pracSuperTrial_flanker_loop.addData('task_stim_keyResp_2.keys',task_stim_keyResp_2.keys)
            if task_stim_keyResp_2.keys != None:  # we had a response
                pracSuperTrial_flanker_loop.addData('task_stim_keyResp_2.rt', task_stim_keyResp_2.rt)
            # Run 'End Routine' code from task_accuracy_code_2
            #iterate trial number for this supertrial
            trialNum = trialNum + 1
            #iterate trial number for this block
            trialNum_fl += 1
            
            if expInfo["counterbalance"] == "L":
                if task_stim_keyResp_2.keys: #if at least one response was made this trial
                    if task_stim_keyResp_2.keys[0] == '1': #if the FIRST button pressed was a '1'
                        if target == 'uppercase': #if a left target stim was shown this trial
                            accuracy = 1 #mark this trial as correct
                            numCorr = numCorr +1 #iterate number of correct responses for this supertrial
                            numCorr_fl += 1 #iterate number of correct responses for this block
                        elif target == 'lowercase': #if a right target stim was shown this trial
                            accuracy = 0 #mark this trial as an error
                    elif task_stim_keyResp_2.keys[0] == '8': #if the FIRST button pressed was a '8'
                        if target == 'lowercase': #if a right target stim was shown this trial
                            accuracy = 1 #mark this trial as correct
                            numCorr = numCorr +1 #iterate number of correct responses for this supertrial
                            numCorr_fl += 1 #iterate number of correct responses for this block
                        elif target == 'uppercase': #if a left target stim was shown this trial
                            accuracy = 0 #mark this trial as an error
            
                elif not task_stim_keyResp_2.keys: # if no response was made
                    accuracy = 0
                
            elif expInfo["counterbalance"] == "R":
                if task_stim_keyResp_2.keys: #if at least one response was made this trial
                    if task_stim_keyResp_2.keys[0] == '1': #if the FIRST button pressed was a '1'
                        if target == 'lowercase': #if a left target stim was shown this trial
                            accuracy = 1 #mark this trial as correct
                            numCorr = numCorr +1 #iterate number of correct responses for this supertrial
                            numCorr_fl += 1 #iterate number of correct responses for this block
                        elif target == 'uppercase': #if a right target stim was shown this trial
                            accuracy = 0 #mark this trial as an error
                    elif task_stim_keyResp_2.keys[0] == '8': #if the FIRST button pressed was a '8'
                        if target == 'uppercase': #if a right target stim was shown this trial
                            accuracy = 1 #mark this trial as correct
                            numCorr = numCorr +1 #iterate number of correct responses for this supertrial
                            numCorr_fl += 1 #iterate number of correct responses for this block
                        elif target == 'lowercase': #if a left target stim was shown this trial
                            accuracy = 0 #mark this trial as an error
            
                elif not task_stim_keyResp_2.keys: # if no response was made
                    accuracy = 0
            
            # save this trial's accuracy to our output file
            pracSuperTrial_flanker_loop.addData('prac_SuperTrial_flanker_accuracy', accuracy) 
            # the Routine "pracSuperTrial_flanker" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 2.0 repeats of 'pracSuperTrial_flanker_loop'
        
        
        # --- Prepare to start Routine "pracSuperTrial_recall" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from wm_recall_code_3
        # define underscores for typing field according to WM load
        n_underscores = 4
        reminder_text = ""
        
        # define allowed keys for typed response (only letters)
        wm_allowed_keys = \
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z']
        wm_recall_typedResp_3.reset()
        wm_recall_keyResp_3.keys = []
        wm_recall_keyResp_3.rt = []
        _wm_recall_keyResp_3_allKeys = []
        underscores_text_3.setText("\n"+n_underscores*" _")
        # keep track of which components have finished
        pracSuperTrial_recallComponents = [wm_recall_text_3, wm_recall_typedResp_3, wm_recall_keyResp_3, underscores_text_3, full_response_reminder_text_3]
        for thisComponent in pracSuperTrial_recallComponents:
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
        
        # --- Run Routine "pracSuperTrial_recall" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from wm_recall_code_3
            # if used lowercase letters in the response, turn into upper
            wm_recall_typedResp_3.text = \
            wm_recall_typedResp_3.text.upper()
            
            #wm_recall_keyResp.stop
            
            # limit length of input to the length of wm load in the block
            if len(wm_recall_typedResp_3.text) > n_underscores:
                wm_recall_typedResp_3.text = \
                wm_recall_typedResp_3.text[:n_underscores]
            # limit keys allowed to use to only letters
            if any(i not in wm_allowed_keys \
            for i in wm_recall_typedResp_3.text):
                wm_recall_typedResp_3.text = \
                wm_recall_typedResp_3.text[:-1]
            # restrict participant of giving a partial response (e.g. 3 letters when 4 required)
            if len(wm_recall_typedResp_3.text) < n_underscores\
            and 'space' in wm_recall_keyResp_3.getKeys():
                reminder_text = "please, provide a full response ({} letters)".format(n_underscores)
            elif len(wm_recall_typedResp_3.text) == n_underscores\
            and 'space' in wm_recall_keyResp_3.getKeys():
                continueRoutine = False
            elif len(wm_recall_typedResp_3.text) == n_underscores:
                reminder_text = ""
            
            # *wm_recall_text_3* updates
            if wm_recall_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wm_recall_text_3.frameNStart = frameN  # exact frame index
                wm_recall_text_3.tStart = t  # local t and not account for scr refresh
                wm_recall_text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_recall_text_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'wm_recall_text_3.started')
                wm_recall_text_3.setAutoDraw(True)
            
            # *wm_recall_typedResp_3* updates
            if wm_recall_typedResp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wm_recall_typedResp_3.frameNStart = frameN  # exact frame index
                wm_recall_typedResp_3.tStart = t  # local t and not account for scr refresh
                wm_recall_typedResp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_recall_typedResp_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'wm_recall_typedResp_3.started')
                wm_recall_typedResp_3.setAutoDraw(True)
            
            # *wm_recall_keyResp_3* updates
            waitOnFlip = False
            if wm_recall_keyResp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wm_recall_keyResp_3.frameNStart = frameN  # exact frame index
                wm_recall_keyResp_3.tStart = t  # local t and not account for scr refresh
                wm_recall_keyResp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_recall_keyResp_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'wm_recall_keyResp_3.started')
                wm_recall_keyResp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(wm_recall_keyResp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(wm_recall_keyResp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if wm_recall_keyResp_3.status == STARTED and not waitOnFlip:
                theseKeys = wm_recall_keyResp_3.getKeys(keyList=["space"], waitRelease=False)
                _wm_recall_keyResp_3_allKeys.extend(theseKeys)
                if len(_wm_recall_keyResp_3_allKeys):
                    wm_recall_keyResp_3.keys = _wm_recall_keyResp_3_allKeys[-1].name  # just the last key pressed
                    wm_recall_keyResp_3.rt = _wm_recall_keyResp_3_allKeys[-1].rt
            
            # *underscores_text_3* updates
            if underscores_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                underscores_text_3.frameNStart = frameN  # exact frame index
                underscores_text_3.tStart = t  # local t and not account for scr refresh
                underscores_text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(underscores_text_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'underscores_text_3.started')
                underscores_text_3.setAutoDraw(True)
            
            # *full_response_reminder_text_3* updates
            if full_response_reminder_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                full_response_reminder_text_3.frameNStart = frameN  # exact frame index
                full_response_reminder_text_3.tStart = t  # local t and not account for scr refresh
                full_response_reminder_text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(full_response_reminder_text_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'full_response_reminder_text_3.started')
                full_response_reminder_text_3.setAutoDraw(True)
            if full_response_reminder_text_3.status == STARTED:  # only update if drawing
                full_response_reminder_text_3.setText(reminder_text, log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pracSuperTrial_recallComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pracSuperTrial_recall" ---
        for thisComponent in pracSuperTrial_recallComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        pracSuperTrial_loop.addData('wm_recall_typedResp_3.text',wm_recall_typedResp_3.text)
        # check responses
        if wm_recall_keyResp_3.keys in ['', [], None]:  # No response was made
            wm_recall_keyResp_3.keys = None
        pracSuperTrial_loop.addData('wm_recall_keyResp_3.keys',wm_recall_keyResp_3.keys)
        if wm_recall_keyResp_3.keys != None:  # we had a response
            pracSuperTrial_loop.addData('wm_recall_keyResp_3.rt', wm_recall_keyResp_3.rt)
        # Run 'End Routine' code from wm_accuracy_code_3
        ## check if typed response matches the letter sequece presented
        #OLD VERSION (BINARY)
        #if wm_recall_typedResp_3.text == ''.join(used_letters):
        #    wm_accuracy = 1
        #    numCorr_wm += 1
        #else:
        #    wm_accuracy = 0
        
        trialNum_wm += 1
        
        # check if typed response matches the letter sequece presented
        wm_response = wm_recall_typedResp_3.text
        correct_letters = used_letters.copy()
        wm_accuracy = 0
        for i in wm_response:
            if i in correct_letters:
                wm_accuracy += 1/len(wm_response)
                correct_letters.remove(i)
        
        numCorr_wm += wm_accuracy
        #if wm_response == ''.join(used_letters):
        #    numCorr_wm += 1
        #elif wm_accuracy >= wm_thresh:
        #    numCorr_wm += 1
        
        # save this trial's wm accuracy to our output file
        pracSuperTrial_loop.addData('pracSuperTrial_wm_accuracy', wm_accuracy)
        
        # save this supertrial's flanker accuracy to our output file
        fl_accuracy = numCorr / trialNum
        pracSuperTrial_loop.addData('pracSuperTrial_fl_accuracy', fl_accuracy)
        # write response letters to data
        pracSuperTrial_loop.addData('pracSuperTrial_wm_response', wm_response)
        # write used letters to data (redundant)
        # pracSuperTrial_loop.addData('pracSuperTrial_used_letters',''.join(used_letters))
        
        # reset
        trialNum = 0
        numCorr = 0
        # the Routine "pracSuperTrial_recall" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 2.0 repeats of 'pracSuperTrial_loop'
    
    
    # --- Prepare to start Routine "pracSuperTrial_feed" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from prac_blockFeed_code_3
    blockAcc_wm = numCorr_wm / trialNum_wm #compute accuracy for this block
    blockAcc_fl = numCorr_fl / trialNum_fl #compute accuracy for this block
    
    if blockAcc_wm >= wm_thresh and  blockAcc_fl >= fl_thresh: #if accuracy >= 75% then say practice is complete and end practice loop to continue to main exp
        outPut = 'Well done! Now you are ready to play both games together! \n\nMemory Game accuracy: {}% \nBiG Letters Game accuracy: {}%'\
        .format(100 * round(blockAcc_wm, 2),
        100 * round(blockAcc_fl, 2)) #feedback presented
        pracSuperTrial_block_loop.finished = True #end practice loop to continue to main exp
    else: #if accuracy lower than threshold then say that practice needs to be repeated and DO NOT end practice loop, instead, allow it to repeat
        outPut = 'Please try the practice again \n\nMemory Game accuracy: {} \nBiG Letters Game accuracy: {}'\
        .format(round(blockAcc_wm, 2),
        round(blockAcc_fl, 2)) #feedback presented
        pracSuperTrial_block_loop.finished = False #DO NOT end practice loop and allow to repeat
    
    # write block accuracy to data
    pracSuperTrial_block_loop.addData('pracSuperTrial_blockAcc_fl', blockAcc_fl)
    pracSuperTrial_block_loop.addData('pracSuperTrial_blockAcc_wm', blockAcc_wm)
    
    #reset the following variables to zero before the next practice block starts
    trialNum_wm = 0
    trialNum_fl = 0
    numCorr_wm = 0
    numCorr_fl = 0
    prac_blockFeed_text.setText(outPut)
    prac_blockFeed_keyResp_3.keys = []
    prac_blockFeed_keyResp_3.rt = []
    _prac_blockFeed_keyResp_3_allKeys = []
    # keep track of which components have finished
    pracSuperTrial_feedComponents = [prac_blockFeed_text, prac_pressContinue, prac_blockFeed_keyResp_3]
    for thisComponent in pracSuperTrial_feedComponents:
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
    
    # --- Run Routine "pracSuperTrial_feed" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_blockFeed_text* updates
        if prac_blockFeed_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_blockFeed_text.frameNStart = frameN  # exact frame index
            prac_blockFeed_text.tStart = t  # local t and not account for scr refresh
            prac_blockFeed_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_blockFeed_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_blockFeed_text.started')
            prac_blockFeed_text.setAutoDraw(True)
        
        # *prac_pressContinue* updates
        if prac_pressContinue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_pressContinue.frameNStart = frameN  # exact frame index
            prac_pressContinue.tStart = t  # local t and not account for scr refresh
            prac_pressContinue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_pressContinue, 'tStartRefresh')  # time at next scr refresh
            prac_pressContinue.setAutoDraw(True)
        
        # *prac_blockFeed_keyResp_3* updates
        waitOnFlip = False
        if prac_blockFeed_keyResp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_blockFeed_keyResp_3.frameNStart = frameN  # exact frame index
            prac_blockFeed_keyResp_3.tStart = t  # local t and not account for scr refresh
            prac_blockFeed_keyResp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_blockFeed_keyResp_3, 'tStartRefresh')  # time at next scr refresh
            prac_blockFeed_keyResp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(prac_blockFeed_keyResp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(prac_blockFeed_keyResp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if prac_blockFeed_keyResp_3.status == STARTED and not waitOnFlip:
            theseKeys = prac_blockFeed_keyResp_3.getKeys(keyList=['space','s'], waitRelease=False)
            _prac_blockFeed_keyResp_3_allKeys.extend(theseKeys)
            if len(_prac_blockFeed_keyResp_3_allKeys):
                prac_blockFeed_keyResp_3.keys = _prac_blockFeed_keyResp_3_allKeys[-1].name  # just the last key pressed
                prac_blockFeed_keyResp_3.rt = _prac_blockFeed_keyResp_3_allKeys[-1].rt
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
        for thisComponent in pracSuperTrial_feedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pracSuperTrial_feed" ---
    for thisComponent in pracSuperTrial_feedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from prac_blockFeed_code_3
    if prac_blockFeed_keyResp_3.keys[-1] == 's':
        pracSuperTrial_block_loop.finished = True #end practice loop to continue to main exp
    # the Routine "pracSuperTrial_feed" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 99.0 repeats of 'pracSuperTrial_block_loop'


# set up handler to look after randomisation of conditions etc
task_condition_loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition.xlsx'),
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
        blockNumText = 'Block 1 of 12'
    elif blockCounter == 2:
        blockNumText = 'Block 2 of 12'
    elif blockCounter == 3:
        blockNumText = 'Block 3 of 12'
    elif blockCounter == 4:
        blockNumText = 'Block 4 of 12'
    elif blockCounter == 5:
        blockNumText = 'Block 5 of 12'
    elif blockCounter == 6:
        blockNumText = 'Block 6 of 12'
    elif blockCounter == 7:
        blockNumText = 'Block 7 of 12'
    elif blockCounter == 8:
        blockNumText = 'Block 8 of 12'
    elif blockCounter == 9:
        blockNumText = 'Block 9 of 12'
    elif blockCounter == 10:
        blockNumText = 'Block 10 of 12'
    elif blockCounter == 11:
        blockNumText = 'Block 11 of 12'
    elif blockCounter == 12:
        blockNumText = 'Block 12 of 12'
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
            theseKeys = space_end_keyResp_11.getKeys(keyList=['space'], waitRelease=False)
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
    
    # set up handler to look after randomisation of conditions etc
    supertrial_loop = data.TrialHandler(nReps=2.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='supertrial_loop')
    thisExp.addLoop(supertrial_loop)  # add the loop to the experiment
    thisSupertrial_loop = supertrial_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSupertrial_loop.rgb)
    if thisSupertrial_loop != None:
        for paramName in thisSupertrial_loop:
            exec('{} = thisSupertrial_loop[paramName]'.format(paramName))
    
    for thisSupertrial_loop in supertrial_loop:
        currentLoop = supertrial_loop
        # abbreviate parameter names if possible (e.g. rgb = thisSupertrial_loop.rgb)
        if thisSupertrial_loop != None:
            for paramName in thisSupertrial_loop:
                exec('{} = thisSupertrial_loop[paramName]'.format(paramName))
        
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
        
        # --- Prepare to start Routine "supertrial_initFixation" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from wm_letters_code_3
        # define a new letters list before new supertrial
        supertrial_letters = wm_letters.copy()
        shuffle(supertrial_letters)
        
        # clean used letters list before new supertrial
        used_letters = []
        used_letters_fl = []
        shown_letters = []
        # Run 'Begin Routine' code from endTask_code_4
        # pick the ISI for the next routine
        # for the online version, this code component should be set to 'both' to remove the 'np'
        # at the start of np.linspace (this is a python library JS won't know what to call. 
        
        # make range from a to b in n stepsizes
        ISIRange = np.linspace(2600, 3000, 400)
        
        # picking from a shuffled array is easier for random selection in JS
        shuffle(ISIRange)
        thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
        
        # save this ISI to our output file
        supertrial_loop.addData('ISI_fixation', thisISI)
        
        #if endCondition: # skip all trials for this condition; participant will not play game.
        #    task_block_loop.finished = True
        #    continueRoutine = False
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
        wm_seq_loop = data.TrialHandler(nReps=conditionText, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='wm_seq_loop')
        thisExp.addLoop(wm_seq_loop)  # add the loop to the experiment
        thisWm_seq_loop = wm_seq_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisWm_seq_loop.rgb)
        if thisWm_seq_loop != None:
            for paramName in thisWm_seq_loop:
                exec('{} = thisWm_seq_loop[paramName]'.format(paramName))
        
        for thisWm_seq_loop in wm_seq_loop:
            currentLoop = wm_seq_loop
            # abbreviate parameter names if possible (e.g. rgb = thisWm_seq_loop.rgb)
            if thisWm_seq_loop != None:
                for paramName in thisWm_seq_loop:
                    exec('{} = thisWm_seq_loop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "wm_routine" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from we_seq_code
            # choose the case of a letter randomly (0 = capitalized, 1 = lowercase)
            case_randomizer = random.randint(0, 1)
            
            # pick a letter to show for this trial
            shuffle(wm_letters)
            
            if case_randomizer == 0:
                letter = [i for i in wm_letters if i not in used_letters][0]
            elif case_randomizer == 1:
                letter = [i.lower() for i in wm_letters if i not in used_letters][0]
            
            # remember the letter shown in each trial
            used_letters.append(letter.upper())
            shown_letters.append(letter)
            # Run 'Begin Routine' code from wm_isi_code
            # pick the ISI for the next letter to appear
            
            # make range from a to b in n stepsizes
            wm_ISIRange = np.linspace(400, 800, 400)
            
            # picking from a shuffled array is easier for random selection in JS
            shuffle(wm_ISIRange)
            wm_thisISI = wm_ISIRange[0]/1000 # the first item of the shuffled array 
            
            # save this ISI to our output file
            wm_seq_loop.addData('wm_ISI', wm_thisISI)
            
            wm_stim.setText(letter)
            wm_fixImg_7.setImage('img/fixationCross.png')
            # keep track of which components have finished
            wm_routineComponents = [wm_stim, wm_fixImg_7]
            for thisComponent in wm_routineComponents:
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
            
            # --- Run Routine "wm_routine" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *wm_stim* updates
                if wm_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    wm_stim.frameNStart = frameN  # exact frame index
                    wm_stim.tStart = t  # local t and not account for scr refresh
                    wm_stim.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(wm_stim, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'wm_stim.started')
                    wm_stim.setAutoDraw(True)
                if wm_stim.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > wm_stim.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        wm_stim.tStop = t  # not accounting for scr refresh
                        wm_stim.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'wm_stim.stopped')
                        wm_stim.setAutoDraw(False)
                
                # *wm_fixImg_7* updates
                if wm_fixImg_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    wm_fixImg_7.frameNStart = frameN  # exact frame index
                    wm_fixImg_7.tStart = t  # local t and not account for scr refresh
                    wm_fixImg_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(wm_fixImg_7, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'wm_fixImg_7.started')
                    wm_fixImg_7.setAutoDraw(True)
                if wm_fixImg_7.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > wm_fixImg_7.tStartRefresh + wm_thisISI+0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        wm_fixImg_7.tStop = t  # not accounting for scr refresh
                        wm_fixImg_7.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'wm_fixImg_7.stopped')
                        wm_fixImg_7.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in wm_routineComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "wm_routine" ---
            for thisComponent in wm_routineComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from we_seq_code
            # write used and shown letters to data
            wm_seq_loop.addData('used_letters',
            ''.join(used_letters))
            wm_seq_loop.addData('shown_letters',
            ''.join(shown_letters))
            # the Routine "wm_routine" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed conditionText repeats of 'wm_seq_loop'
        
        
        # --- Prepare to start Routine "task_initFixation" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from endTask_code
        # pick the ISI for the next routine
        # for the online version, this code component should be set to 'both' to remove the 'np'
        # at the start of np.linspace (this is a python library JS won't know what to call. 
        
        # make range from a to b in n stepsizes
        ISIRange = np.linspace(1600, 2000, 400)
        
        # picking from a shuffled array is easier for random selection in JS
        shuffle(ISIRange)
        thisISI = ISIRange[0]/1000 # the first item of the shuffled array 
        
        # save this ISI to our output file
        supertrial_loop.addData('ISI_fixation', thisISI)
        
        #if endCondition: # skip all trials for this condition; participant will not play game.
        #    task_block_loop.finished = True
        #    continueRoutine = False
        initFixation_img.setImage('img/fixationCross.png')
        left_reminder_text_7.setText(left_reminder)
        right_reminder_text_7.setText(right_reminder)
        # keep track of which components have finished
        task_initFixationComponents = [initFixation_img, left_reminder_text_7, right_reminder_text_7]
        for thisComponent in task_initFixationComponents:
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
        
        # --- Run Routine "task_initFixation" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *initFixation_img* updates
            if initFixation_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                initFixation_img.frameNStart = frameN  # exact frame index
                initFixation_img.tStart = t  # local t and not account for scr refresh
                initFixation_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(initFixation_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'initFixation_img.started')
                initFixation_img.setAutoDraw(True)
            if initFixation_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > initFixation_img.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    initFixation_img.tStop = t  # not accounting for scr refresh
                    initFixation_img.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'initFixation_img.stopped')
                    initFixation_img.setAutoDraw(False)
            
            # *left_reminder_text_7* updates
            if left_reminder_text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                left_reminder_text_7.frameNStart = frameN  # exact frame index
                left_reminder_text_7.tStart = t  # local t and not account for scr refresh
                left_reminder_text_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left_reminder_text_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'left_reminder_text_7.started')
                left_reminder_text_7.setAutoDraw(True)
            if left_reminder_text_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > left_reminder_text_7.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    left_reminder_text_7.tStop = t  # not accounting for scr refresh
                    left_reminder_text_7.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'left_reminder_text_7.stopped')
                    left_reminder_text_7.setAutoDraw(False)
            
            # *right_reminder_text_7* updates
            if right_reminder_text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                right_reminder_text_7.frameNStart = frameN  # exact frame index
                right_reminder_text_7.tStart = t  # local t and not account for scr refresh
                right_reminder_text_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right_reminder_text_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'right_reminder_text_7.started')
                right_reminder_text_7.setAutoDraw(True)
            if right_reminder_text_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > right_reminder_text_7.tStartRefresh + thisISI-frameTolerance:
                    # keep track of stop time/frame for later
                    right_reminder_text_7.tStop = t  # not accounting for scr refresh
                    right_reminder_text_7.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'right_reminder_text_7.stopped')
                    right_reminder_text_7.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in task_initFixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "task_initFixation" ---
        for thisComponent in task_initFixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "task_initFixation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        task_trial_loop = data.TrialHandler(nReps=2.0, method='fullRandom', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(whichCondition),
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
            # Run 'Begin Routine' code from flanker_letters_code
            # leave only not-used letters for flanker
            if repeat_letters == True:
                flanker_letters = \
                [i for i in wm_letters]
            elif repeat_letters == False:
                flanker_letters = \
                [i for i in wm_letters if i not in used_letters]
            
            if repeat_letters_fl == False:
                flanker_letters = [i for i in flanker_letters\
                if i not in used_letters_fl]
            
            # if there is an L, we don't want in in flanker
            if "L" in flanker_letters:
                flanker_letters.remove("L")
                
            # shuffle again
            shuffle(flanker_letters)
            
            # take flanker letter and add to used flanker letters
            flanker_stim = flanker_letters[0]
            used_letters_fl.append(flanker_stim)
            
            # create flanker stimuli based on the congruency and case
            if congruent == 1 and target == "uppercase":
                flanker_stim = "{}".format(flanker_stim*5)
            elif congruent == 1 and target == "lowercase":
                flanker_stim = "{}".format(flanker_stim.lower()*5)
            elif congruent == 0 and target == "uppercase":
                flanker_stim = "{}{}{}".format(flanker_stim.lower()*2,
                flanker_stim, flanker_stim.lower()*2)
            elif congruent == 0 and target == "lowercase":
                flanker_stim = "{}{}{}".format(flanker_stim*2,
                flanker_stim.lower(), flanker_stim*2)
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
            left_reminder_text_8.setText(left_reminder)
            right_reminder_text_8.setText(right_reminder)
            task_fixImg.setImage('img/fixationCross.png')
            task_stim_keyResp.keys = []
            task_stim_keyResp.rt = []
            _task_stim_keyResp_allKeys = []
            # keep track of which components have finished
            task_stimRoutineComponents = [flanker_text_stim, left_reminder_text_8, right_reminder_text_8, task_fixImg, task_stim_keyResp]
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
                
                # *left_reminder_text_8* updates
                if left_reminder_text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    left_reminder_text_8.frameNStart = frameN  # exact frame index
                    left_reminder_text_8.tStart = t  # local t and not account for scr refresh
                    left_reminder_text_8.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(left_reminder_text_8, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'left_reminder_text_8.started')
                    left_reminder_text_8.setAutoDraw(True)
                if left_reminder_text_8.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > left_reminder_text_8.tStartRefresh + thisISI-frameTolerance:
                        # keep track of stop time/frame for later
                        left_reminder_text_8.tStop = t  # not accounting for scr refresh
                        left_reminder_text_8.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'left_reminder_text_8.stopped')
                        left_reminder_text_8.setAutoDraw(False)
                
                # *right_reminder_text_8* updates
                if right_reminder_text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    right_reminder_text_8.frameNStart = frameN  # exact frame index
                    right_reminder_text_8.tStart = t  # local t and not account for scr refresh
                    right_reminder_text_8.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(right_reminder_text_8, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'right_reminder_text_8.started')
                    right_reminder_text_8.setAutoDraw(True)
                if right_reminder_text_8.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > right_reminder_text_8.tStartRefresh + thisISI-frameTolerance:
                        # keep track of stop time/frame for later
                        right_reminder_text_8.tStop = t  # not accounting for scr refresh
                        right_reminder_text_8.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'right_reminder_text_8.stopped')
                        right_reminder_text_8.setAutoDraw(False)
                
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
            # Run 'End Routine' code from flanker_letters_code
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
            #iterate trial number for this supertrial
            trialNum = trialNum + 1
            #iterate trial number for this block
            trialNum_fl += 1
            
            if expInfo["counterbalance"] == "L":
                if task_stim_keyResp.keys: #if at least one response was made this trial
                    if task_stim_keyResp.keys[0] == '1': #if the FIRST button pressed was a '1'
                        if target == 'uppercase': #if a left target stim was shown this trial
                            accuracy = 1 #mark this trial as correct
                            numCorr = numCorr +1 #iterate number of correct responses for this supertrial
                            numCorr_fl += 1 #iterate number of correct responses for this block
                        elif target == 'lowercase': #if a right target stim was shown this trial
                            accuracy = 0 #mark this trial as an error
                    elif task_stim_keyResp.keys[0] == '8': #if the FIRST button pressed was a '8'
                        if target == 'lowercase': #if a right target stim was shown this trial
                            accuracy = 1 #mark this trial as correct
                            numCorr = numCorr +1 #iterate number of correct responses for this supertrial
                            numCorr_fl += 1 #iterate number of correct responses for this block
                        elif target == 'uppercase': #if a left target stim was shown this trial
                            accuracy = 0 #mark this trial as an error
            
                elif not task_stim_keyResp.keys: # if no response was made
                    accuracy = 0
                
            elif expInfo["counterbalance"] == "R":
                if task_stim_keyResp.keys: #if at least one response was made this trial
                    if task_stim_keyResp.keys[0] == '1': #if the FIRST button pressed was a '1'
                        if target == 'lowercase': #if a left target stim was shown this trial
                            accuracy = 1 #mark this trial as correct
                            numCorr = numCorr +1 #iterate number of correct responses for this supertrial
                            numCorr_fl += 1 #iterate number of correct responses for this block
                        elif target == 'uppercase': #if a right target stim was shown this trial
                            accuracy = 0 #mark this trial as an error
                    elif task_stim_keyResp.keys[0] == '8': #if the FIRST button pressed was a '8'
                        if target == 'uppercase': #if a right target stim was shown this trial
                            accuracy = 1 #mark this trial as correct
                            numCorr = numCorr +1 #iterate number of correct responses for this supertrial
                            numCorr_fl += 1 #iterate number of correct responses for this block
                        elif target == 'lowercase': #if a left target stim was shown this trial
                            accuracy = 0 #mark this trial as an error
            
                elif not task_stim_keyResp.keys: # if no response was made
                    accuracy = 0
            
            # save this trial's accuracy to our output file
            task_trial_loop.addData('fl_accuracy', accuracy) 
            # the Routine "task_stimRoutine" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 2.0 repeats of 'task_trial_loop'
        
        
        # --- Prepare to start Routine "wm_recall" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from wm_recall_code
        # define underscores for typing field according to WM load
        n_underscores = int(conditionText)
        reminder_text = ""
        
        # define allowed keys for typed response (only letters)
        wm_allowed_keys = \
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z']
        
        wm_recall_typedResp.reset()
        wm_recall_keyResp.keys = []
        wm_recall_keyResp.rt = []
        _wm_recall_keyResp_allKeys = []
        underscores_text.setText("\n"+n_underscores*" _")
        # keep track of which components have finished
        wm_recallComponents = [wm_recall_text, wm_recall_typedResp, wm_recall_keyResp, underscores_text, full_response_reminder_text]
        for thisComponent in wm_recallComponents:
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
        
        # --- Run Routine "wm_recall" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from wm_recall_code
            # if used lowercase letters in the response, turn into upper
            wm_recall_typedResp.text = \
            wm_recall_typedResp.text.upper()
            
            # limit length of input to the length of wm load in the block
            if len(wm_recall_typedResp.text) > n_underscores:
                wm_recall_typedResp.text = \
                wm_recall_typedResp.text[:n_underscores]
            # limit keys allowed to use to only letters
            if any(i not in wm_allowed_keys \
            for i in wm_recall_typedResp.text):
                wm_recall_typedResp.text = \
                wm_recall_typedResp.text[:-1]
            # restrict participant of giving a partial response (e.g. 3 letters when 4 required)
            if len(wm_recall_typedResp.text) < n_underscores\
            and 'space' in wm_recall_keyResp.getKeys():
                reminder_text = "please, provide a full response ({} letters)".format(n_underscores)
            elif len(wm_recall_typedResp.text) == n_underscores\
            and 'space' in wm_recall_keyResp.getKeys():
                continueRoutine = False
            elif len(wm_recall_typedResp.text) == n_underscores:
                reminder_text = ""
            
            # *wm_recall_text* updates
            if wm_recall_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wm_recall_text.frameNStart = frameN  # exact frame index
                wm_recall_text.tStart = t  # local t and not account for scr refresh
                wm_recall_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_recall_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'wm_recall_text.started')
                wm_recall_text.setAutoDraw(True)
            
            # *wm_recall_typedResp* updates
            if wm_recall_typedResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wm_recall_typedResp.frameNStart = frameN  # exact frame index
                wm_recall_typedResp.tStart = t  # local t and not account for scr refresh
                wm_recall_typedResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_recall_typedResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'wm_recall_typedResp.started')
                wm_recall_typedResp.setAutoDraw(True)
            
            # *wm_recall_keyResp* updates
            waitOnFlip = False
            if wm_recall_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wm_recall_keyResp.frameNStart = frameN  # exact frame index
                wm_recall_keyResp.tStart = t  # local t and not account for scr refresh
                wm_recall_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wm_recall_keyResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'wm_recall_keyResp.started')
                wm_recall_keyResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(wm_recall_keyResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(wm_recall_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if wm_recall_keyResp.status == STARTED and not waitOnFlip:
                theseKeys = wm_recall_keyResp.getKeys(keyList=["space"], waitRelease=False)
                _wm_recall_keyResp_allKeys.extend(theseKeys)
                if len(_wm_recall_keyResp_allKeys):
                    wm_recall_keyResp.keys = _wm_recall_keyResp_allKeys[-1].name  # just the last key pressed
                    wm_recall_keyResp.rt = _wm_recall_keyResp_allKeys[-1].rt
            
            # *underscores_text* updates
            if underscores_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                underscores_text.frameNStart = frameN  # exact frame index
                underscores_text.tStart = t  # local t and not account for scr refresh
                underscores_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(underscores_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'underscores_text.started')
                underscores_text.setAutoDraw(True)
            
            # *full_response_reminder_text* updates
            if full_response_reminder_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                full_response_reminder_text.frameNStart = frameN  # exact frame index
                full_response_reminder_text.tStart = t  # local t and not account for scr refresh
                full_response_reminder_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(full_response_reminder_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'full_response_reminder_text.started')
                full_response_reminder_text.setAutoDraw(True)
            if full_response_reminder_text.status == STARTED:  # only update if drawing
                full_response_reminder_text.setText(reminder_text, log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in wm_recallComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "wm_recall" ---
        for thisComponent in wm_recallComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        supertrial_loop.addData('wm_recall_typedResp.text',wm_recall_typedResp.text)
        # check responses
        if wm_recall_keyResp.keys in ['', [], None]:  # No response was made
            wm_recall_keyResp.keys = None
        supertrial_loop.addData('wm_recall_keyResp.keys',wm_recall_keyResp.keys)
        if wm_recall_keyResp.keys != None:  # we had a response
            supertrial_loop.addData('wm_recall_keyResp.rt', wm_recall_keyResp.rt)
        # Run 'End Routine' code from wm_accuracy_code
        ## check if typed response matches the letter sequece presented
        # OLD VERSION (BINARY)
        #if wm_recall_typedResp.text == ''.join(used_letters):
        #    wm_accuracy = 1
        #    numCorr_wm += 1
        #else:
        #    wm_accuracy = 0
        
        trialNum_wm += 1
        
        # check if typed response matches the letter sequece presented
        wm_response = wm_recall_typedResp.text
        correct_letters = used_letters.copy()
        wm_accuracy = 0
        for i in wm_response:
            if i in correct_letters:
                wm_accuracy += 1/len(wm_response)
                correct_letters.remove(i)
        
        numCorr_wm += wm_accuracy
        #if wm_response == ''.join(used_letters):
        #    numCorr_wm += 1
        #elif wm_accuracy >= wm_thresh:
        #    numCorr_wm += 1
        
        # save this trial's wm accuracy to our output file
        supertrial_loop.addData('supertrial_wm_accuracy', wm_accuracy)
        
        # write response letters to data
        supertrial_loop.addData('wm_response',wm_response)
        # write used letters to data (redundant)
        # supertrial_loop.addData('used_letters',''.join(used_letters))
        
        # save this trial's flanker accuracy to our output file
        fl_accuracy = numCorr / trialNum
        supertrial_loop.addData('supertrial_fl_accuracy', fl_accuracy)
        
        # reset
        trialNum = 0
        numCorr = 0
        # the Routine "wm_recall" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 2.0 repeats of 'supertrial_loop'
    
    
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
            theseKeys = space_end_keyResp_13.getKeys(keyList=['space'], waitRelease=False)
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
    # calculate block accuracy
    blockAcc_wm = numCorr_wm / trialNum_wm
    blockAcc_flanker = numCorr_fl / trialNum_fl
    
    # write block accuracy to data
    task_condition_loop.addData('supertrial_blockAcc_fl',
    blockAcc_fl)
    task_condition_loop.addData('supertrial_blockAcc_wm',
    blockAcc_wm)
    
    # reset
    numCorr_wm = 0
    trialNum_wm = 0
    numCorr_fl = 0
    trialNum_fl = 0
    # check responses
    if space_end_keyResp_13.keys in ['', [], None]:  # No response was made
        space_end_keyResp_13.keys = None
    task_condition_loop.addData('space_end_keyResp_13.keys',space_end_keyResp_13.keys)
    if space_end_keyResp_13.keys != None:  # we had a response
        task_condition_loop.addData('space_end_keyResp_13.rt', space_end_keyResp_13.rt)
    # the Routine "task_conditionComplete" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'task_condition_loop'


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
        theseKeys = space_end_keyResp_12.getKeys(keyList=['space'], waitRelease=False)
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
