# GamepadLearning

A Python project for learning how to read and interpret gamepad input using Pygame. This repository contains a collection of scripts that monitor joystick axes, triggers, face buttons, bumpers, and D-pad states in real time.

The goal is to help you understand controller input basics and build a solid foundation for game, robot, or input-mapping projects.

## Features

- Read joystick movement values from left and right sticks
- Convert trigger input into 0–255 values
- Detect face button presses for A, B, X, and Y
- Read bumper inputs using button events
- Track D-pad presses and toggles
- Visualize live controller state in a terminal dashboard
- Easy-to-follow beginner-friendly scripts

## Project Structure

```text
GamepadLearning/
├── combined/
│   └── v2.py
├── seperate/
│   ├── bumper.py
│   ├── dPad-Both.py
│   ├── dPad-ClickOnOff.py
│   ├── Joystick.py
│   ├── trigger.py
│   └── XYAB.py
└── README.md
```

## Scripts Included

### combined/v2.py
This is the main controller dashboard. It reads:
- left/right stick values
- trigger values (LT/RT)
- face buttons (A/B/X/Y)
- bumpers (LB/RB)
- D-pad state

It displays a real-time terminal dashboard with live controller values and uses a deadzone to reduce noise.

### seperate/Joystick.py
Reads joystick axis data and prints vector-style values for the left and right sticks.

### seperate/trigger.py
Reads trigger pressure and scales it into a 0–255 range.

### seperate/XYAB.py
Reads A, B, X, and Y face buttons and prints their state.

### seperate/bumper.py
Reads left and right bumper button down/up events.

### seperate/dPad-Both.py
Tracks D-pad input in two modes:
- active hold mode
- toggle mode

### seperate/dPad-ClickOnOff.py
Demonstrates D-pad toggle behavior where each press flips a state on/off.

## Requirements

- Python 3.8+
- Pygame
- A compatible USB gamepad or controller

Install the dependency:

```bash
pip install pygame
```

## Setup

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/GamepadLearning.git
cd GamepadLearning
```

2. Install dependencies:

```bash
pip install pygame
```

3. Connect your controller.

4. Run any script:

```bash
python combined/v2.py
```

Or for individual examples:

```bash
python seperate/Joystick.py
python seperate/trigger.py
python seperate/XYAB.py
python seperate/bumper.py
python seperate/dPad-Both.py
python seperate/dPad-ClickOnOff.py
```

## Controller Notes

This project is built around typical XInput-style controllers, such as:
- Xbox controllers
- many third-party controllers that map similarly in Windows

Button and axis numbering can vary slightly depending on the controller and operating system. If your controller uses a different mapping, you may need to adjust the index values in the scripts.

## Typical Input Mapping

Common mapping used in these scripts:

- Left stick: axes 0 and 1
- Right stick: axes 2 and 3
- Left trigger: axis 4
- Right trigger: axis 5
- A: button 0
- B: button 1
- X: button 2
- Y: button 3
- Left bumper: button 4
- Right bumper: button 5
- D-pad: hat 0

## Deadzone

The project includes a deadzone value to ignore small joystick drift and prevent noise from overly sensitive input.

Example:

```python
DEADZONE = 0.15
```

This helps keep the controller values stable and makes terminal output cleaner.

## Troubleshooting

### No gamepad detected
- Make sure your controller is connected before running the script.
- Check whether the controller is recognized by Windows or your OS.
- Try unplugging and reconnecting the device.
- Confirm that the device is not being blocked by another application.

### Buttons or axes are mapped incorrectly
- Some controllers use different button numbering.
- You may need to inspect the mapping for your specific device.
- Try printing raw events for each button or axis to determine the correct index.

### Terminal output is noisy
- Use the included deadzone logic.
- Reduce the print frequency or update the loop speed.

## Use Cases

This project is useful for:
- learning input handling in Python
- building controller dashboards
- testing controller mapping before a game or robot project
- learning how to convert raw joystick and trigger values into useful ranges

## License

This repository is provided for educational and experimental purposes. Add an appropriate license if you plan to publish it publicly.

## Example GitHub Repository Info

Repository name:

```text
GamepadLearning
```

Short description:

```text
Python scripts to read and study joystick, trigger, button, and D-pad gamepad inputs with Pygame.
```

First commit message:

```bash
git commit -m "Initial commit: add Python gamepad input learning scripts"
```

## Future Ideas

- Add a GUI using Tkinter or PyQt
- Support multiple controllers
- Add calibration settings
- Save controller profiles
- Build robot control using gamepad input

## Conclusion

This repository is a beginner-friendly way to learn how controller inputs work and how to read them through Python. It is a good starting point for game development, automation, robotics, or custom input experiments.
