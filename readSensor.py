# -*- coding: utf-8 -*-
#!/usr/bin/env python

# read analog photo reflector sensor by using MCP3208 which has 8-channel analog to digital converter

from gpiozero import MCP3208
adC = MCP3208(channel = 0)

# end of program
