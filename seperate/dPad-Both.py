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
# 2. STATE TRACKERS (Needed for Toggle Mode)
# ==========================================
dpad_toggles = {"UP": 0, "DOWN": 0, "LEFT": 0, "RIGHT": 0}
last_physical_state = {"UP": 0, "DOWN": 0, "LEFT": 0, "RIGHT": 0}

# ==========================================
# 3. MAIN LOOP
# ==========================================
print("\nReading D-Pad... Press Ctrl+C to quit.")

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

        # ------------------------------------------------------------------
        # --- MODE 1: ACTIVE WHILE PRESSED (Currently COMMENTED OUT) ---
        # To use this: Uncomment the block below, and comment out Mode 2.
        # ------------------------------------------------------------------
        
        # if any(current_physical_state.values()):
        #     print(f"HELD  -> UP: {current_physical_state['UP']} | DOWN: {current_physical_state['DOWN']} | LEFT: {current_physical_state['LEFT']} | RIGHT: {current_physical_state['RIGHT']}")
        

        # ------------------------------------------------------------------
        # --- MODE 2: TOGGLE / LIGHT SWITCH (Currently ACTIVE) ---
        # To use this: Leave this uncommented, and comment out Mode 1.
        # ------------------------------------------------------------------
        
        changed = False
        for direction in ["UP", "DOWN", "LEFT", "RIGHT"]:
            # Edge Detection: Pressed NOW, but wasn't LAST FRAME
            if current_physical_state[direction] == 1 and last_physical_state[direction] == 0:
                
                # Flip the toggle
                dpad_toggles[direction] = 1 if dpad_toggles[direction] == 0 else 0
                changed = True

        # Save this frame's physical state for the next time the loop runs
        last_physical_state = current_physical_state.copy()

        # Only print when a toggle actually flips
        if changed:
            print(f"TOGGLE -> UP: {dpad_toggles['UP']} | DOWN: {dpad_toggles['DOWN']} | LEFT: {dpad_toggles['LEFT']} | RIGHT: {dpad_toggles['RIGHT']}")
            
        # ------------------------------------------------------------------

        time.sleep(0.05) # Loop at 20 frames per second

except KeyboardInterrupt:
    print("\nExiting...")
finally:
    pygame.quit()