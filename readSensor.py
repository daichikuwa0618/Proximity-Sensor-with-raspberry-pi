# -*- coding: utf-8 -*-
#!/usr/bin/env python

# read analog photo reflector sensor by using MCP3208 which has 8-channel analog to digital converter
# move servo motor
# 1500us = 0deg 900us = -60deg 2400us = 60deg

from gpiozero import MCP3208
from time import sleep
import pigpio

adc = MCP3208(channel = 0)
pi = pigpio.pi()

# ========== 定数 =========
SERVO_PIN = 15
GET_OBJECT = 0.8
NEAR_OBJECT =0.3
TOUCH_OBJECT = 0.1

# ========== 変数 =========
command = 0 # 0: OPEN 1: CLOSE
state = 0 # distance between hand to object
degree = 0.0
microSec = 1500.0

# initialize
pi.set_servo_pulsewidth(SERVO_PIN, 1500)

# loop for infinite
try:
    while True:
        command = int(input("Type'1' to hand something: "))
        # OPEN(60deg wait)
        if command == 0:
            pi.set_servo_pulsewidth(SERVO_PIN, 2400)

        # CLOSE(hand object)
        else:
            # max speed
            while state == 0:
                degree -= 1
                microSec = 1500.0 + (degree * 10.0)
                # set limit
                if degree < -60.0:
                    degree = -60.0
                pi.set_servo_pulsewidth(SERVO_PIN, microSec)
                print(str(degree) + "[deg], ADC: " + str(adc.value) + "state: " + str(state))
                if adc.value < GET_OBJECT:
                    # next stage
                    state = 1
                sleep(0.1)

            # middle speed
            while state == 1:
                degree -= 0.2
                microSec = 1500.0 + (degree * 10.0)
                # set limit
                if degree < -60.0:
                    degree = -60.0
                pi.set_servo_pulsewidth(SERVO_PIN, microSec)
                print(str(degree) + "[deg], ADC: " + str(adc.value) + "state: " + str(state))
                if adc.value < NEAR_OBJECT:
                    # next stage
                    state = 2
                sleep(0.1)


            while state == 2:
                degree -= 1
                microSec = 1500.0 + (degree * 10.0)
                # set limit
                if degree < -60.0:
                    degree = -60.0
                pi.set_servo_pulsewidth(SERVO_PIN, microSec)
                print(str(degree) + "[deg], ADC: " + str(adc.value) + "state: " + str(state))
                if adc.value < TOUCH_OBJECT:
                    # touch
                    state = 0
                sleep(0.1)

except KeyboardInterrupt:
    pass pi.set_servo_pulsewidth(SERVO_PIN, 0)

# end of program
