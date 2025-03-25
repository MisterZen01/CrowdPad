import ctypes
import time

#video of code: https://www.youtube.com/watch?v=RPiQ_PXMf3w&list=WL&index=2
#source of code: https://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# https://pypi.org/project/pytchat/

import pytchat
chat = pytchat.create(video_id="iMjeDXerL1M")

# Change this to your desired keyword
keyword1 = "up"     # W
keyword2 = "left"   # A
keyword3 = "down"   # S
keyword4 = "right"  # D
keyword5 = "A"      # X
keyword6 = "B"      # Z
keyword7 = "start"  # Enter
keyword8 = "select" # Space
while chat.is_alive():
    for c in chat.get().sync_items():
        print(f"{c.message}")

        time.sleep(3)
        if keyword1 in c.message:
            PressKey(17)
            time.sleep(0.25)
            ReleaseKey(17)
        if keyword2 in c.message:
            PressKey(30)
            time.sleep(0.25)
            ReleaseKey(30)
        if keyword3 in c.message:
            PressKey(31)
            time.sleep(0.25)
            ReleaseKey(31)
        if keyword4 in c.message:
            PressKey(32)
            time.sleep(0.25)
            ReleaseKey(32)
        if keyword5 in c.message:
            PressKey(45)
            time.sleep(0.25)
            ReleaseKey(45)
        if keyword6 in c.message:
            PressKey(44)
            time.sleep(0.25)
            ReleaseKey(44)
        if keyword7 in c.message:
            PressKey(28)
            time.sleep(0.25)
            ReleaseKey(28)
        if keyword8 in c.message:
            PressKey(57)
            time.sleep(0.25)
            ReleaseKey(57)

#Hex Codes to simulate key presses: https://wiki.nexusmods.com/index.php/DirectX_Scancodes_And_How_To_Use_Them
