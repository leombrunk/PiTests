#!/usr/bin/python3

"""
Light up an LED based on motion sensor
"""

import sys
import RPi.GPIO as GPIO

# Output GPIO pin
ledPin = 12

# Input GPIO pin
sensorPin = 11

def setup():
    """Initialize the board"""
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(ledPin, GPIO.OUT)
	GPIO.setup(sensorPin, GPIO.IN)
	
def loop():
    """Light the LED when motion detected"""
	while True:
		if GPIO.input(sensorPin) == GPIO.HIGH:
			GPIO.output(ledPin, GPIO.HIGH)
			print('led on')
		else:
			GPIO.output(ledPin, GPIO.LOW)
			print('led off')
	
def destroy():
    """Cleanup GPIOs"""
	GPIO.output(ledPin, GPIO.LOW)
	GPIO.cleanup()
	
if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
				
