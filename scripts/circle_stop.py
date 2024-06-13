#!/usr/bin/env python3
import math
import rospy
from geometry_msgs.msg import Twist


def main():
    rospy.init_node("turtle-move")

    pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=1000)

    rate = rospy.Rate(10)
    vel = Twist()

    vel.linear.x = 2

    #vel.angular.z = 1
    # vel.angular.y=-1.54

    while not rospy.is_shutdown():
        vel.linear.x = 4
        vel.angular.z = 0
        pub.publish(vel)
        rospy.sleep(1)

        vel.linear.x = 0
        vel.angular.z = 135 * (math.pi/180)
        pub.publish(vel)
        rospy.sleep(1)

        vel.angular.z = 0
        vel.linear.x = 2
        pub.publish(vel)
        rospy.sleep(1)

        vel.linear.x = 0
        vel.angular.z = -90 * (math.pi/180)
        pub.publish(vel)
        rospy.sleep(1)

        vel.angular.z = 0
        vel.linear.x = 2
        pub.publish(vel)
        rospy.sleep(1)

        vel.linear.x = 0
        vel.angular.z = 135 * (math.pi/180)
        pub.publish(vel)
        rospy.sleep(1)

        vel.linear.x = 4
        vel.angular.z = 0
        pub.publish(vel)
        rospy.sleep(1)


if __name__ == "__main__":
    main()
