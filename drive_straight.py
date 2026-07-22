#!/usr/bin/env python3
# module 1.2 
import time
from sparkybotmini import SparkyBotMini

robot = SparkyBotMini(port="/dev/ttyUSB0")
robot.connect()
robot.set_motor(50, 50, 50, 50)
time.sleep(5)
robot.set_motor(0, 0, 0, 0)
robot.disconnect()
