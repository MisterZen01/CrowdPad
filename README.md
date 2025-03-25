# YouTube Chat Controller Integration
### Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation Guide](#installation-guide)
- [Usage](#usage)
- [Compatibility](#compatibility)
- [Additional Documentation](#additional-documentation)
- [License](#license)
- [Issues and Improvements](#issues-and-improvements)
- [Known Bugs](#known-bugs)
- [Contribution](#contribution)

## Overview
YouTube Chat Controller is a Python script that connects YouTube live chat with a Virtual Xbox 360 controller. Viewers can send commands in the chat to control the controller, just like they are playing the game. Commands like `!a` and `!up` can press buttons or move the joystick.

This project uses the `pytchat` and `vgamepad` Python libraries to read messages from YouTube and simulate controller actions. It allows real-time interaction, making the experience fun and interactive for both players and viewers.

## Features
- **YouTube Chat Integration**: The code reads live YouTube chat messages using pytchat. Chat viewers can type commands to control a virtual Xbox 360 controller.
- **Virtual Controller Simulation**: It uses **vgamepad** to act like a real Xbox 360 controller. This means button presses, joystick movements, and trigger pulls can all be simulated.
- **Command System**: Players can send simple commands like `!a` or `!up` to press controller buttons. The code has a dictionary called `COMMANDS` that matches chat commands to controller actions.
- **Hold Time Control**: Commands can be used with different hold times. Typing "**short**" or "**long**" before a command changes how long the button stays pressed. The default hold time is 1 second.
- **Joystick and Trigger Movements**: Players can control both joysticks using commands like `!ljn_` (left joystick north) or `!rjne` (right joystick northeast). Triggers can also be fully pressed using `!lt` or `!rt`.
- **DS and 3DS Touch Screen Support**: Additional scripts provide functionality to use the DS and 3DS touch screens by simulating the stylus pen using pyautogui.
- **Safe Input Management**: After each movement or press, the code uses **controller.update()** to ensure the input registers correctly. Joysticks automatically return to a neutral position after moving.
- **Expandable Design**: The code is easy to modify. You could add more commands, adjust hold times, or even create custom controller actions by changing the `COMMANDS` dictionary.


## Installation Guide
Before you begin, ensure you have the following installed:
- **Python 3.7** or higher.
- Libraries:
  - `pytchat` - For interacting with YouTube live chat.
  - `vgamepad` - For simulating Xbox 360 controller input.
  - `time` - For adding delays between commands.
  - `pyautogui` - For mouse emulation (DS/3DS Touch Screen Support).

1. Install missing libraries using `pip`:

```bash
pip install pytchat vgamepad pyautogui
```

- Install missing libraries using `pip` for DS and 3DS:

```bash
pip install pyautogui
```

2. Replace the default **YouTube video ID** in the script with your live stream video ID:

```python
video_id = "your_video_id_here"
```

- **Note**: Your video ID is found in the URL: youtube.com/live/**cgS56M2pkmw**

## Usage
The script listens for chat commands and simulates the corresponding button presses or joystick movements. The commands and their corresponding actions are defined in the COMMANDS dictionary. The list of available commands is viewable in the Commands.txt that can be used in the YouTube live stream chat.

**Example Usage**: In YouTube live chat, a user could type `!up`, which will simulate pressing the D-pad up on the Xbox 360 controller. If a user types `!ljw_`, it will move the left joystick to the west.

## Compatibility
- **DS and 3DS Touch Screen Support**: There's additional scipts labeled DS and 3DS that includes functionality for using the their touch screens by simulating the stylus pen using **pyautogui**.
- **Standalone Emulator Support**: It has been tested using the standalone versions of **DeSmuME** for DS emulation and **Citra** for 3DS emulation.
- **RetroArch Semi-incompatibility**: Vgamepad is fully compatible with Retroarch. The code for the DS and 3DS Touch Screen is **not compatible with RetroArch** due to the lack of external touch screen input support. For best results, use standalone emulators.

## Additional Documentation
**Libraries Used:**
- pytchat: https://github.com/taizan-hokuto/pytchat
- vgamepad: https://github.com/yannbouteiller/vgamepad
- pyautogui: https://pyautogui.readthedocs.io/

## License
This project is licensed under the Creative Commons Attribution 4.0 International License.

**You are free to:**
- Share — copy and redistribute the material in any medium or format.
- Adapt — remix, transform, and build upon the material.

**Under the following terms:**
- Attribution — You must give appropriate credit and indicate if changes were made.

See the LICENSE file for more details.

## Issues and Improvements
If you encounter any issues or have suggestions for improvements, please feel free to submit an issue using the **issues tab** above.

To see a list of planned improvements and future updates, please review the **Roadmap**.

## Known Bugs
No known bugs at this time (3/24/25)

## Contribution
Thank you for visiting this repository! Contributions are optional but always appreciated. You can help by:
- Reporting bugs or issues
- Suggesting features or improvements
- Submitting pull requests
- Starring the repository to show your support

Donations are also welcome to support the project.

**Support Options:**
- Send a donation via [Cash App](https://cash.app/$MisterZen01)
- Become a YouTube Member starting @ $0.99/mo
- Donate through YouTube Super Chat

### Your involvement means a lot—thank you!

