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

pi.set_servo_pulsewidth(15, 1500)
degree = 0
microSec = 1500
# loop for infinite
while True:
    # 障害物に追従する
    if adc.value > 0.5:
        degree -=
    elif adc.value < 0.5:
        degree +=

    if degree > 60:
        degree = 60
    elif degree < -60:
        degree = -60

    microSec = 1500 + (degree * 10)
    pi.set_servo_pulsewidth(15, microSec)

    print(str(degree) + "[deg], ADC: " + str(adc.value))

    sleep(0.1)


# end of program
