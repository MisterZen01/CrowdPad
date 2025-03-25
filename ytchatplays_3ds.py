import time
import pytchat
import pyautogui
import vgamepad as vg

video_id="your_video_id_here"
DEFAULT_HOLD_TIME = 1
SHORT_HOLD_TIME = 0.25
LONG_HOLD_TIME = 3

# Screen Region and Location
left_screen = 1067
top_screen = 204
width = 852
height = 640

# Original 3DS Resolution 320x240, emulation resolution 852x640, 2.66x larger
threeds_width = 320
threeds_height = 240

controller = vg.VX360Gamepad()  # Initialize Xbox 360 controller
print("Controller initialized.")

COMMANDS = {
    # D-Pad
    "!up": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,  
    "!left": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,  
    "!down": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,  
    "!right": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,  

    # Action Buttons
    "!b": vg.XUSB_BUTTON.XUSB_GAMEPAD_A,  
    "!a": vg.XUSB_BUTTON.XUSB_GAMEPAD_B,  
    "!y": vg.XUSB_BUTTON.XUSB_GAMEPAD_X,  
    "!x": vg.XUSB_BUTTON.XUSB_GAMEPAD_Y,  

    # Shoulder and Thumb Buttons
    "!ls": vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,  
    "!rs": vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER,  
    "!start": vg.XUSB_BUTTON.XUSB_GAMEPAD_START,  
    "!select": vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK,  

    # Analog Stick Directions (8 directions)
    "!ljn_": ("left_joystick", 0.0, 1.0),  # North
    "!ljnw": ("left_joystick", -1.0, 1.0),  # North-West
    "!ljw_": ("left_joystick", -1.0, 0.0),  # West
    "!ljsw": ("left_joystick", -1.0, -1.0),  # South-West
    "!ljs_": ("left_joystick", 0.0, -1.0),  # South
    "!ljse": ("left_joystick", 1.0, -1.0),  # South-East
    "!lje_": ("left_joystick", 1.0, 0.0),  # East
    "!ljne": ("left_joystick", 1.0, 1.0),  # North-East

    # Analog Stick Directions Alternative (8 directions)
    "!lju_": ("left_joystick", 0.0, 1.0),  # Up
    "!ljul": ("left_joystick", -1.0, 1.0),  # Up-Left
    "!ljl_": ("left_joystick", -1.0, 0.0),  # Left
    "!ljdl": ("left_joystick", -1.0, -1.0),  # Down-Left
    "!ljd_": ("left_joystick", 0.0, -1.0),  # Down
    "!ljdr": ("left_joystick", 1.0, -1.0),  # Down-Right
    "!ljr_": ("left_joystick", 1.0, 0.0),  # Right
    "!ljur": ("left_joystick", 1.0, 1.0)  # Up-Right
}

chat = pytchat.create(video_id=video_id)  # Replace with your live stream ID
print("Listening for YouTube chat commands...")

def press_button(controller, button_code, hold_time=DEFAULT_HOLD_TIME):
    controller.press_button(button=button_code)
    controller.update()  # Send the updated state to the computer
    time.sleep(hold_time)  # Hold for specified time
    controller.release_button(button=button_code)
    controller.update()  # Update the controller after releasing the button

def release_button(controller, button_code):
    controller.release_button(button=button_code)
    controller.update()  # Update the controller after releasing the button

def move_joystick(controller, joystick, x_value, y_value, hold_time=DEFAULT_HOLD_TIME):
    # Move the joystick to the desired position
    if joystick == "left_joystick":
        controller.left_joystick_float(x_value, y_value)
    elif joystick == "right_joystick":
        controller.right_joystick_float(x_value, y_value)
    controller.update()  # Update the joystick state
    time.sleep(hold_time)
    if joystick == "left_joystick":     # Return joystick to neutral position (0.0, 0.0)
        controller.left_joystick_float(0.0, 0.0)
    elif joystick == "right_joystick":
        controller.right_joystick_float(0.0, 0.0)
    controller.update()  # Update the joystick state after returning to neutral

def press_trigger(controller, trigger, hold_time=DEFAULT_HOLD_TIME):  # hold_time in seconds
    if trigger == "left_trigger":
        controller.left_trigger_float(1.0)  # Full press (1.0)
    elif trigger == "right_trigger":
        controller.right_trigger_float(1.0)  # Full press (1.0)
    controller.update()  # Update the trigger state
    time.sleep(hold_time)  # Hold for specified time
    controller.left_trigger_float(0.0)  # Release the trigger
    controller.update()  # Update the controller after releasing the trigger

if controller:  # Only proceed if controller is successfully initialized
    while chat.is_alive():
        for c in chat.get().sync_items():
            message = c.message.lower()  # Convert to lowercase for case insensitivity
            hold_time = DEFAULT_HOLD_TIME  # Default hold time
            
            # Check if 'short' or 'long' is mentioned
            if "short" in message:
                hold_time = SHORT_HOLD_TIME
                message = message.replace("short", "").strip()  # Remove "short" keyword
            elif "long" in message:
                hold_time = LONG_HOLD_TIME
                message = message.replace("long", "").strip()  # Remove "long" keyword

            if message.startswith("!"):  # Only process messages starting with '!'
                for command, action in COMMANDS.items():
                    if message == command:  # Ensure exact match
                        print(f'{c.author.name} pressed {command[1:]}')  # Print player name without "!"
                        
                        if isinstance(action, str) and action in ["left_trigger", "right_trigger"]:
                            press_trigger(controller, action, hold_time)  # Press triggers
                        elif isinstance(action, tuple) and len(action) == 3:
                            joystick, x_value, y_value = action
                            move_joystick(controller, joystick, x_value, y_value, hold_time)  # Move joystick
                        else:
                            press_button(controller, action, hold_time)  # Simulate button press

            # Check if the message starts with the trigger command !ts
            if c.message.lower().startswith("!ts"):
                try:
                    # Extract coordinates from the message
                    parts = c.message.split()
                    if len(parts) == 3:
                        initial_x = int(parts[1])
                        initial_y = int(parts[2])
                        
                        # Ensure coordinates are within the valid range
                        if 0 <= initial_x <= 320 and 0 <= initial_y <= 240:

                            # Ensure the coordinates are within the screen region
                            x = left_screen + (initial_x * (width / threeds_width))
                            y = top_screen + (initial_y * (height / threeds_height))

                            # Use pyautogui to move the mouse cursor and click
                            pyautogui.moveTo(x, y)
                            pyautogui.drag(1, None, 0.11, button='left')  # duration is optional
                            print(f"x: {x}, y: {y}")
                        else:
                            print("Coordinates out of range.")
                    else:
                        print("Invalid command format. Use !ts x y.")
                except ValueError:
                    print("Invalid coordinates. Use integers for x and y.")

else:
    print("Controller initialization failed.")