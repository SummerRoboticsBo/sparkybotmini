#!/usr/bin/env python3
# module 1.2 
import time
from sparkybotmini import SparkyBotMini

try:
    robot = SparkyBotMini(port="/dev/ttyUSB0")
    robot.connect()
    robot.set_auto_report(True)
    time.sleep(0.5)
    
    robot.set_motor(50, 50, 50, 50)
    
    # Read and print attitude every second while moving
    for i in range(5):
        roll, pitch, yaw = robot.get_attitude(degrees=True)
        print(f"Time {i+1}s - Roll: {roll:.1f}°, Pitch: {pitch:.1f}°, Yaw: {yaw:.1f}°")
        time.sleep(1)
    
    robot.set_motor(0, 0, 0, 0)
    robot.disconnect()
except Exception as e:
    print(f"Error occurred: {e}")
finally:
    try:
        robot.disconnect()
    except:
        pass
