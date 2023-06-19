import RPi.GPIO as GPIO
from w1thermsensor import W1ThermSensor
import time

# The pin number where your relay is connected
relay_pin = 18

# Temperature threshold (in Fahrenheit)
temp_threshold = 60.0  # adjust this value to your needs
tolerance = 2.0  # temperature tolerance

# Use the Broadcom SOC channel, these are the GPIO pin numbers on the Broadcom SOC
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pin for output
GPIO.setup(relay_pin, GPIO.OUT)

# Initial state of the relay
relay_state = GPIO.LOW
GPIO.output(relay_pin, relay_state)

# Create a sensor object
sensor = W1ThermSensor()

# Function to get temperature in Fahrenheit
def get_temperature_fahrenheit():
    temperature_in_celsius = sensor.get_temperature()
    temperature_in_fahrenheit = (temperature_in_celsius * 9/5) + 32
    return temperature_in_fahrenheit

try:
    # Main program loop
    while True:
        current_temp = get_temperature_fahrenheit()
        print("Current temperature: {:.2f}°F".format(current_temp))

        if current_temp <= (temp_threshold - tolerance) and relay_state == GPIO.LOW:
            # Switch the relay on
            relay_state = GPIO.HIGH
            GPIO.output(relay_pin, relay_state)
        elif current_temp >= (temp_threshold + tolerance) and relay_state == GPIO.HIGH:
            # Switch the relay off
            relay_state = GPIO.LOW
            GPIO.output(relay_pin, relay_state)

        # Wait a bit before the next reading
        time.sleep(30)

# Clean up on exit
except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
