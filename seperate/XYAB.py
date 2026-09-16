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
# 2. MAIN LOOP - ACTION BUTTONS ONLY
# ==========================================
print("\nReading A, B, X, Y buttons... Press Ctrl+C to quit.")

try:
    while True:
        pygame.event.pump() # Update physical sensors

        # Read the four main face buttons
        buttons = {
            "A": gamepad.get_button(0),
            "B": gamepad.get_button(1),
            "X": gamepad.get_button(2),
            "Y": gamepad.get_button(3)
        }

        # Check if ANY button in our dictionary is currently a 1
        if any(buttons.values()):
            # Print the current state of all four buttons
            print(f"A: {buttons['A']}  |  B: {buttons['B']}  |  X: {buttons['X']}  |  Y: {buttons['Y']}")

            # You can also trigger specific events easily like this:
            if buttons["X"] == 1:
                pass # Replace 'pass' with your robot's attack/horn/action code!

        time.sleep(0.05) # Run at 20 frames per second

except KeyboardInterrupt:
    print("\nExiting...")
finally:
    pygame.quit()