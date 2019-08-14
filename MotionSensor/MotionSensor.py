#!/usr/bin/python3

"""
Light up an LED based on motion sensor
"""

import RPi.GPIO as GPIO

# Output GPIO pin
LED_PIN = 12

# Input GPIO pin
SENSOR_PIN = 11

def setup():
    """Initialize the board"""
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.setup(SENSOR_PIN, GPIO.IN)

def loop():
    """Light the LED when motion detected"""
    while True:
        if GPIO.input(SENSOR_PIN) == GPIO.HIGH:
            GPIO.output(LED_PIN, GPIO.HIGH)
            print('led on')
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
            print('led off')

def destroy():
    """Cleanup GPIOs"""
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
