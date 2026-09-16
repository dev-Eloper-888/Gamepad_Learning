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

# Note: We completely deleted the 'last_bumpers' dictionary!

# ==========================================
# 2. MAIN LOOP (EVENT-DRIVEN)
# ==========================================
print("\nReading Bumpers using Event Queue... Press Ctrl+C to quit.")

try:
    while True:
        
        # INSTEAD OF pygame.event.pump(), WE READ THE ACTUAL EVENTS
        # This gives us a list of EVERYTHING that happened since the last loop.
        for event in pygame.event.get():
            
            # --- DETECT BUTTON PRESSES ---
            if event.type == pygame.JOYBUTTONDOWN:
                # event.button tells us exactly which button triggered this event
                if event.button == 4:
                    print("Left Bumper PRESSED!")
                elif event.button == 5:
                    print("Right Bumper PRESSED!")

            # --- DETECT BUTTON RELEASES ---
            elif event.type == pygame.JOYBUTTONUP:
                if event.button == 4:
                    print("Left Bumper RELEASED!")
                elif event.button == 5:
                    print("Right Bumper RELEASED!")


        # We can still sleep to save CPU power. 
        # Even while sleeping, the OS safely catches inputs into the queue!
        time.sleep(0.05) 

except KeyboardInterrupt:
    print("\nExiting...")
finally:
    pygame.quit()