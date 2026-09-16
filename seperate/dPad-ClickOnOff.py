import pygame
import time

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
print(f"Controller Connected: {gamepad.get_name()}")

# ==========================================
# 2. TOGGLE STATE TRACKERS
# ==========================================
# This holds the actual "Light Switch" states you will use for your project
dpad_toggles = {
    "UP": 0, 
    "DOWN": 0, 
    "LEFT": 0, 
    "RIGHT": 0
}

# This remembers the physical controller state from the previous loop 
# so we can detect the exact moment you push down.
last_physical_state = {
    "UP": 0, 
    "DOWN": 0, 
    "LEFT": 0, 
    "RIGHT": 0
}

# ==========================================
# 3. MAIN LOOP
# ==========================================
print("\nReading D-Pad Toggles... Press Ctrl+C to quit.")

try:
    while True:
        pygame.event.pump()

        # Read the raw physical Hat data
        dpad_x, dpad_y = gamepad.get_hat(0)

        # Map what your thumb is doing RIGHT NOW
        current_physical_state = {
            "UP": 1 if dpad_y == 1 else 0,
            "DOWN": 1 if dpad_y == -1 else 0,
            "LEFT": 1 if dpad_x == -1 else 0,
            "RIGHT": 1 if dpad_x == 1 else 0
        }

        # Check all four directions for a "new" press
        changed = False
        for direction in ["UP", "DOWN", "LEFT", "RIGHT"]:
            
            # EDGE DETECTION: Is it pressed NOW, but wasn't LAST FRAME?
            if current_physical_state[direction] == 1 and last_physical_state[direction] == 0:
                
                # Flip the toggle (If 0 make it 1, if 1 make it 0)
                if dpad_toggles[direction] == 0:
                    dpad_toggles[direction] = 1
                else:
                    dpad_toggles[direction] = 0
                
                changed = True # Flag that we updated something

        # Save this frame's physical state for the next time the loop runs
        last_physical_state = current_physical_state.copy()

        # Only print when a toggle actually flips
        if changed:
            print(f"Toggles -> UP: {dpad_toggles['UP']} | DOWN: {dpad_toggles['DOWN']} | LEFT: {dpad_toggles['LEFT']} | RIGHT: {dpad_toggles['RIGHT']}")

        time.sleep(0.05) # Loop at 20 frames per second

except KeyboardInterrupt:
    print("\nExiting...")
finally:
    pygame.quit()