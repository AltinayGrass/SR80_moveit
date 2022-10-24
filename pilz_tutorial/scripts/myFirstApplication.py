#!/usr/bin/env python3
from geometry_msgs.msg import Pose, Point
from pilz_robot_programming import *
import math
import rospy
__REQUIRED_API_VERSION__ = "1"  # API version
__ROBOT_VELOCITY__ = 0.5        # velocity of the robot
# main program
def start_program():

    #record_pose=r.get_current_pose()
    #print(record_pose) # print the current position of thr robot in the terminal
    pos= Point(1.5,-0.5,0.5)
    ori= from_euler(0,math.radians(180),0)
    cartesian_goal= Pose(position=pos,orientation=ori)
    r.move(Ptp(goal=cartesian_goal, vel_scale=__ROBOT_VELOCITY__, target_link="flange",reference_frame="base_link"))
    r.move(Lin(goal=Pose(position=Point(0,0,-0.1)), relative= True,vel_scale=__ROBOT_VELOCITY__, target_link="flange",reference_frame="base_link"))
    r.move(Lin(goal=Pose(position=Point(0,0,0.2)), relative= True,vel_scale=__ROBOT_VELOCITY__, target_link="flange",reference_frame="base_link"))
    #r.move(Ptp(goal=record_pose, vel_scale=__ROBOT_VELOCITY__,planning_group= "SR80", target_link="sr80_tcp",reference_frame="base_link"))


if __name__ == "__main__":
    # init a rosnode
    rospy.init_node('robot_program_node')

    # initialisation
    r = Robot(__REQUIRED_API_VERSION__)  # instance of the robot

    # start the main program
    start_program()