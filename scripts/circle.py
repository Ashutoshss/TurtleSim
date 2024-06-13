#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist


def main():
    rospy.init_node("turtle-move")

    pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=1000)

    rate = rospy.Rate(10)
    vel = Twist()



    while not rospy.is_shutdown():

        vel.linear.x = 1  # Linear velocity in x- Direction 1m/s
        vel.angular.z = 1 # Angular Velocity about z- Axis 1rad/s

        pub.publish(vel)

       # rate.sleep()

if __name__ == "__main__":
    main(   )
