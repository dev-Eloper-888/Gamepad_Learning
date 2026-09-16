import pygame
import time

# ==========================================
# 1. HARDWARE SETUP
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
# 2. THE 0-255 MATH CONVERTER
# ==========================================
def read_single_direction_axis(axis_id, is_trigger=True):
    """
    Reads an axis and forces it into a single-direction 0 to 255 range.
    """
    raw_val = gamepad.get_axis(axis_id)
    
    if is_trigger:
        # Pygame Triggers rest at -1.0 and fully press to 1.0.
        # We shift this math so resting is 0, and fully pressed is 255.
        pull_amount = (raw_val + 1.0) / 2.0
        
        if pull_amount < 0.05: # Ignore tiny physical jitters
            return 0
            
        return int(pull_amount * 255)
        
    else:
        # If you are using a standard Joystick instead of a Trigger:
        # It rests at 0.0. We only care if you push it in ONE positive direction.
        if raw_val > 0.15: # 0.15 is the deadzone
            return int(raw_val * 255)
        return 0

# ==========================================
# 3. MAIN LOOP
# ==========================================
print("\nReading single-direction axis (0 to 255)... Press Ctrl+C to quit.")

try:
    while True:
        pygame.event.pump() # Update physical sensors

        # Read the Triggers (Usually Axis 4 and Axis 5)
        left_throttle = read_single_direction_axis(4, is_trigger=True)
        right_throttle = read_single_direction_axis(5, is_trigger=True)

        # Only print when you are actually pressing it
        if left_throttle > 0 or right_throttle > 0:
            print(f"Left Throttle: {left_throttle:3}  |  Right Throttle: {right_throttle:3}")
            
            # Example of how you would send this to hardware:
            # serial_link.write(f"<SPEED:{right_throttle}>\n".encode('utf-8'))

        time.sleep(0.05) # Run at 20 frames per second to save CPU

except KeyboardInterrupt:
    print("\nExiting...")
finally:
    pygame.quit()