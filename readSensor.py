# -*- coding: utf-8 -*-
#!/usr/bin/env python

# read analog photo reflector sensor by using MCP3208 which has 8-channel analog to digital converter

from gpiozero import MCP3208
from time import sleep
adC = MCP3208(channel = 0)

# loop for infinite
while True:
    print(adc.value)
    sleep(0.5)

# end of program
