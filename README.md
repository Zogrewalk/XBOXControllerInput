# XBOXControllerInput
With this module you can easily implement XBox controls into your own code.
To make this work you need to install vgamepad by typing the following in the cmd-window

python -m pip install vgamepad

You don't have to import it into your project though, since this module already imported it.
But you do have to import time to make the durations work

To learn more about the XBOX Input, visit this website: https://pypi.org/project/vgamepad/

The sticks work with x and y coordinates, so if you want the stick to move to the left, you can give it a value of 32767 to move it all the way to the left. -32768 to move it all the way to the right.
Here is an example code to move the left stick to the left for 2 seconds:

XBOXControllerInput.LeftStick(2, 0, 32767, 0, 0)

All this means is that the stick is put to the left for 2 seconds. After the 2 seconds it returns to a neutral position of 0, 0.

The triggers work similar, but they just need a duration and two values, so they know how far down they have to be pressed before and after the given timeout.
Here's and example:

XBOXControllerInput.LeftTrigger(0.1, 255, 0)
  
This code presses the left trigger all the way down for 0.1 second.
255 is all the way pressed down, 0 is the neutral state after the press happened.

Buttons are pretty simple, all you have to do is put in the duration of the press and which button it should press.

XBOXControllerInput.ButtonPress(0.1, XBOXControllerInput.Y)

This code pressesthe Y-button for 0.1 second. You can do this for all the buttons on the controller.
