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

DEADZONE = 0.15

# ==========================================
# 2. VECTOR MATH & SCALING
# ==========================================
def get_vector(axis_x_id, axis_y_id, invert_y=True):
    """Reads X and Y axes, applies deadzone, and maps to vectors from -255 to 255."""
    
    # 1. Get raw float values from Pygame (-1.0 to 1.0)
    raw_x = gamepad.get_axis(axis_x_id)
    raw_y = gamepad.get_axis(axis_y_id)
    
    # 2. Invert Y-axis so Up is Positive (+255) and Down is Negative (-255)
    if invert_y:
        raw_y = -raw_y

    def scale_to_range(raw_value):
        """Converts the raw float into an integer between -255 and 255"""
        if abs(raw_value) < DEADZONE:
            return 0
        
        # Remember if we are going positive or negative
        sign = 1 if raw_value > 0 else -1
        
        # Smoothly scale the remaining range (0.15 to 1.0) into (0.0 to 1.0)
        adjusted_val = (abs(raw_value) - DEADZONE) / (1.0 - DEADZONE)
        
        # Multiply by 255 and apply the sign
        return int(adjusted_val * 255) * sign

    # Return a dictionary representing the vector
    return {
        "x": scale_to_range(raw_x),
        "y": scale_to_range(raw_y)
    }

# ==========================================
# 3. MAIN LOOP
# ==========================================
print("\nReading Joystick Vectors (-255 to 255)... Press Ctrl+C to quit.")

try:
    while True:
        pygame.event.pump()

        # XInput Standard Joystick Axes:
        # Left Stick: X = Axis 0, Y = Axis 1
        # Right Stick: X = Axis 2, Y = Axis 3
        
        left_joystick = get_vector(axis_x_id=0, axis_y_id=1)
        right_joystick = get_vector(axis_x_id=2, axis_y_id=3)

        # Only print when the sticks are actually moving to keep the terminal clean
        if left_joystick["x"] != 0 or left_joystick["y"] != 0 or \
           right_joystick["x"] != 0 or right_joystick["y"] != 0:
            
            # Formatting to align the negative signs and numbers neatly in the console
            print(f"Left Stick (X, Y): ({left_joystick['x']:4}, {left_joystick['y']:4})  |  "
                  f"Right Stick (X, Y): ({right_joystick['x']:4}, {right_joystick['y']:4})")

        time.sleep(0.05) # 20 Hz update rate

except KeyboardInterrupt:
    print("\nExiting...")
finally:
    pygame.quit()