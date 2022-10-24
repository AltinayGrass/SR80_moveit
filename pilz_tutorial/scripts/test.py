#!/usr/bin/env python3
from geometry_msgs.msg import Pose, Point
from pilz_robot_programming import *
import math
import rospy

__REQUIRED_API_VERSION__ = "1"  # API version 
__ROBOT_VELOCITY__ = 0.5        # velocity of the robot

# main program
def start_program():
  print(r.get_current_pose(target_link="flange",base="base_link")) # print the current position of thr robot in the terminal
  for count in range(1):
    r.move(Ptp(goal=[ 0.333,-0.547,-0.185,0.063,-0.650,-0.404],  vel_scale=0.2, target_link="flange",reference_frame="base_link"))
    r.move(Ptp(goal=[ 0.847,-1.504,-0.621,-0.000,-0.883,-0.847],  vel_scale=0.5, target_link="flange",reference_frame="base_link"))
    r.move(Ptp(goal=[ -0.000,-0.000,0.000,0.000,0.000,-0.000],  vel_scale=0.5, target_link="flange",reference_frame="base_link"))
    r.move(Ptp(goal=[ 0.333,-0.547,-0.185,0.063,-0.650,-0.404],  vel_scale=0.5, target_link="flange",reference_frame="base_link"))
    r.move(Ptp(goal=[ 0.409,0.694,1.033,-0.016,-0.886,0.419],  vel_scale=0.5, target_link="flange",reference_frame="base_link"))
    r.move(Ptp(goal=[ 1.117,-1.086,1.032,-0.000,-0.254,-2.117],  vel_scale=0.5, target_link="flange",reference_frame="base_link"))
  
if __name__ == "__main__":
    # init a rosnode
    rospy.init_node('robot_program_node')
    # initialisation
    r = Robot(__REQUIRED_API_VERSION__)  # instance of the robot
    # start the main program
    start_program()
