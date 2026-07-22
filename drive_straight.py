#!/usr/bin/env python3
# module 1.2 
import time
from sparkybotmini import SparkyBotMini

try:
    robot = SparkyBotMini(port="/dev/ttyUSB0")
    robot.connect()
    robot.set_motor(50, 50, 50, 50)
    time.sleep(5)
    robot.set_motor(0, 0, 0, 0)
    robot.disconnect()
except Exception as e:
    print(f"Error occurred: {e}")
finally:
    try:
        robot.disconnect()
    except:
        pass
