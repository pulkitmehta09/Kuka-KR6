#!/usr/bin/env python
# license removed for brevity
import math
import rospy
from std_msgs.msg import String, Float64

p_l1j = rospy.Publisher('/c_l1j/command', Float64, queue_size=2)
p_l2j = rospy.Publisher('/c_l2j/command', Float64, queue_size=2)
p_l3j = rospy.Publisher('/c_l3j/command', Float64, queue_size=2)
loop_rate = 20

def pub():
    rospy.init_node('pub_node', anonymous=True)
    rate = rospy.Rate(loop_rate)

    angle = 0
    d_angle = 0.9

    while not rospy.is_shutdown():

        if angle > 6.28 or angle < -6.28:
            d_angle *= -1

        pos = math.sin(angle)
        # rospy.loginfo(angle)
        rospy.loginfo("commanding l1j %s" % pos)
        p_l1j.publish(pos)
        p_l2j.publish(pos/3)
        p_l3j.publish((pos-0.2)/2)

        angle += d_angle/loop_rate

        rate.sleep()

if __name__ == '__main__':

    try:
        pub()
    except rospy.ROSInterruptException:
        pass
    finally:
        p_l1j.publish(0)
        p_l2j.publish(0)
        p_l3j.publish(0)

