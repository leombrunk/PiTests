#!/usr/bin/python3

"""
Make an LED blink on a Raspberry Pi
See Hardware.png for hardware connections
"""

import time
import RPi.GPIO as GPIO

# Output GPIO pin
LED_PIN = 11

def setup():
    """Initialize the board"""
    print("Starting...")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.LOW)

def light_led():
    """Light up the led"""
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)

if __name__ == '__main__':
    setup()
    try:
        light_led()
    except KeyboardInterrupt:
        print("Ending...")
    finally:
        # Using finally to ensure this always runs
        GPIO.cleanup()
