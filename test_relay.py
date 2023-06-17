import RPi.GPIO as GPIO
import time

# The pin number where your relay is connected
relay_pin = 18

# Use the Broadcom SOC channel, these are the GPIO pin numbers on the Broadcom SOC
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pin for output
GPIO.setup(relay_pin, GPIO.OUT)

# Main program loop
try:
    while True:
        # Switch the relay on
        GPIO.output(relay_pin, GPIO.HIGH)
        time.sleep(1)

        # Switch the relay off
        GPIO.output(relay_pin, GPIO.LOW)
        time.sleep(1)

# Clean up on exit
except KeyboardInterrupt:
    print("Exiting...")
except Exception as e:
    print(e)
finally:
    GPIO.cleanup()
