import time
from hal import hal_led as led
from hal import hal_input_switch as input_switch


def main():
    # Initialize LED and slide switch
    led.init()
    input_switch.init()

    right_timer_started = False
    start_time = 0

    print("PiLedTest running... Press Ctrl+C to stop.")

    try:
        while True:
            # Read slide switch position (0 = Left, 1 = Right)
            switch_pos = input_switch.read_slide_switch()

            if switch_pos == 1:
                # --- LEFT POSITION (Part b & c): Blink at 5 Hz continuously ---
                # 5 Hz = 0.2s period (0.1s ON, 0.1s OFF)
                right_timer_started = False  # Reset timer when switched back to Left
                
                led.set_output(0, 1)
                time.sleep(0.1)
                led.set_output(0, 0)
                time.sleep(0.1)

            else:
                # --- RIGHT POSITION (Part c & d): Blink at 10 Hz for 5s, then turn OFF ---
                if not right_timer_started:
                    start_time = time.time()
                    right_timer_started = True

                elapsed_time = time.time() - start_time

                if elapsed_time < 5.0:
                    # 10 Hz = 0.1s period (0.05s ON, 0.05s OFF)
                    led.set_output(0, 1)
                    time.sleep(0.05)
                    led.set_output(0, 0)
                    time.sleep(0.05)
                else:
                    # Turn off LED completely after 5 seconds
                    led.set_output(0, 0)
                    time.sleep(0.1)

    except KeyboardInterrupt:
        led.set_output(0, 0)
        print("\nProgram stopped.")


if __name__ == "__main__":
    main()