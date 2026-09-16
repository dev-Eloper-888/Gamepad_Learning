import pygame
import time
import os
import sys

os.system("") # Enable ANSI escape sequences on Windows

# ==========================================
# 1. INITIALIZE GAMEPAD
# ==========================================
pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No gamepad found. Please plug in the dongle.")
    exit()

gamepad = pygame.joystick.Joystick(0)
gamepad.init()

os.system('cls' if os.name == 'nt' else 'clear')

DEADZONE = 0.15

# ==========================================
# 2. MASTER STATE TRACKERS
# ==========================================
state = {
    "LX": 0, "LY": 0, "RX": 0, "RY": 0,     
    "LT": 0, "RT": 0,                       
    "LB": 0, "RB": 0,                       
    "A": 0, "B": 0, "X": 0, "Y": 0,         
    "UP": 0, "DOWN": 0, "LEFT": 0, "RIGHT": 0 
}

# We add a tracker to remember exactly what the screen currently looks like
last_printed_state = None
last_physical_dpad = {"UP": 0, "DOWN": 0, "LEFT": 0, "RIGHT": 0}

# ==========================================
# 3. MATH HELPER
# ==========================================
def scale_axis(raw_val, is_trigger=False):
    if is_trigger:
        pull = (raw_val + 1.0) / 2.0
        return int(pull * 255) if pull >= 0.05 else 0
    else:
        if abs(raw_val) < DEADZONE: return 0
        sign = 1 if raw_val > 0 else -1
        adjusted = (abs(raw_val) - DEADZONE) / (1.0 - DEADZONE)
        return int(adjusted * 255) * sign

# ==========================================
# 4. THE LIVE DASHBOARD LOOP
# ==========================================
# Hide the blinking terminal cursor for a cleaner look
sys.stdout.write("\033[?25l")
sys.stdout.flush()

try:
    while True:
        pygame.event.pump()

        # Update Joysticks & Triggers
        state["LX"] = scale_axis(gamepad.get_axis(0))
        state["LY"] = scale_axis(-gamepad.get_axis(1)) 
        state["RX"] = scale_axis(gamepad.get_axis(2))
        state["RY"] = scale_axis(-gamepad.get_axis(3))
        state["LT"] = scale_axis(gamepad.get_axis(4), is_trigger=True)
        state["RT"] = scale_axis(gamepad.get_axis(5), is_trigger=True)

        # Update Buttons
        state["A"] = gamepad.get_button(0)
        state["B"] = gamepad.get_button(1)
        state["X"] = gamepad.get_button(2)
        state["Y"] = gamepad.get_button(3)
        state["LB"] = gamepad.get_button(4)
        state["RB"] = gamepad.get_button(5)

        # Update D-Pad Toggles
        dpad_x, dpad_y = gamepad.get_hat(0)
        current_dpad = {
            "UP": 1 if dpad_y == 1 else 0,
            "DOWN": 1 if dpad_y == -1 else 0,
            "LEFT": 1 if dpad_x == -1 else 0,
            "RIGHT": 1 if dpad_x == 1 else 0
        }

        for dir in ["UP", "DOWN", "LEFT", "RIGHT"]:
            if current_dpad[dir] == 1 and last_physical_dpad[dir] == 0:
                state[dir] = 1 if state[dir] == 0 else 0
        last_physical_dpad = current_dpad.copy()

        # ---------------------------------------------------------
        # FAST PRINTING LOGIC
        # ---------------------------------------------------------
        # ONLY redraw the screen if the controller inputs have actually changed
        if state != last_printed_state:
            
            dashboard = f"""\033[H=================================================
        COSMIC BYTE ARES - LIVE DASHBOARD
=================================================
 JOYSTICKS (-255 to 255)
 -----------------------
 Left Stick  ->  X: {state['LX']:4}  |  Y: {state['LY']:4}
 Right Stick ->  X: {state['RX']:4}  |  Y: {state['RY']:4}

 TRIGGERS (0 to 255)
 -------------------
 Left (LT)   ->  {state['LT']:3}      |  Right (RT) ->  {state['RT']:3}

 FACE BUTTONS & BUMPERS (Active Hold)
 ------------------------------------
 A: {state['A']}  |  B: {state['B']}  |  X: {state['X']}  |  Y: {state['Y']}
 LB: {state['LB']} |  RB: {state['RB']}

 D-PAD (Light-Switch Toggles)
 ----------------------------
 UP: {state['UP']} | DOWN: {state['DOWN']} | LEFT: {state['LEFT']} | RIGHT: {state['RIGHT']}
=================================================
 Press Ctrl+C to stop."""
            
            # Write directly to system buffer and flush instantly
            sys.stdout.write(dashboard)
            sys.stdout.flush()
            
            # Update our tracker
            last_printed_state = state.copy()

        # You can actually lower this sleep time now to make it highly responsive (60Hz)
        time.sleep(0.016) 

except KeyboardInterrupt:
    pass
finally:
    # Bring the terminal cursor back before exiting
    sys.stdout.write("\033[?25h\nShutting down...\n")
    sys.stdout.flush()
    pygame.quit()