import vgamepad as vg
import time

gamepad = vg.VX360Gamepad()

Y = vg.XUSB_BUTTON.XUSB_GAMEPAD_Y
X = vg.XUSB_BUTTON.XUSB_GAMEPAD_X
A = vg.XUSB_BUTTON.XUSB_GAMEPAD_A
B = vg.XUSB_BUTTON.XUSB_GAMEPAD_B
Start = vg.XUSB_BUTTON.XUSB_GAMEPAD_START
Back = vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK
Guide = vg.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE
DpadU = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP
DpadD = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN
DpadL = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT
DpadR = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT
LBumper = vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER
RBumper = vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER

def LeftTrigger(delay, value, value2):
    gamepad.left_trigger(value)
    gamepad.update()
    time.sleep(delay)
    gamepad.left_trigger(value2)
    gamepad.update()

def RightTrigger(delay, value, value2):
    gamepad.right_trigger(value)
    gamepad.update()
    time.sleep(delay)
    gamepad.right_trigger(value2)
    gamepad.update()

#####################LEFT STICK INPUTS#####################
def LeftStick(delay, xbefore, ybefore, xafter, yafter):
    gamepad.left_joystick(xbefore, ybefore)
    gamepad.update()
    time.sleep(delay)
    gamepad.left_joystick(xafter, yafter)
    gamepad.update()

def LeftStickPress(delay):
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
    gamepad.update()
    time.sleep(delay)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
    gamepad.update()

#####################RIGHT STICK INPUTS#####################
def RightStick(delay, xbefore, ybefore, xafter, yafter):
    gamepad.right_joystick(xbefore, ybefore)
    gamepad.update()
    time.sleep(delay)
    gamepad.right_joystick(xafter, yafter)
    gamepad.update()

def ButtonPress(delay, button):
    gamepad.press_button(button)
    gamepad.update()
    time.sleep(delay)
    gamepad.release_button(button)
    gamepad.update()