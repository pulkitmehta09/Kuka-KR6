#!/usr/bin/env python
# license removed for brevity
import math
import rospy
from std_msgs.msg import String, Float64

p_l1j = rospy.Publisher('/c_l1j/command', Float64, queue_size=2)
p_l2j = rospy.Publisher('/c_l2j/command', Float64, queue_size=2)
p_l3j = rospy.Publisher('/c_l3j/command', Float64, queue_size=2)
p_l4j = rospy.Publisher('/c_l4j/command', Float64, queue_size=2)
p_l5j = rospy.Publisher('/c_l5j/command', Float64, queue_size=2)
p_l6j = rospy.Publisher('/c_l6j/command', Float64, queue_size=2)
p_f1j = rospy.Publisher('/c_f1j/command', Float64, queue_size=2)
p_f2j = rospy.Publisher('/c_f2j/command', Float64, queue_size=2)

loop_rate = 20

def pub():
    rospy.init_node('pub_node', anonymous=True)
    rate = rospy.Rate(loop_rate)

    # t1 = 0
    # t2 = 0.9
    # t3 = -0.3
    # t4 = 0
    # t5 = -1
    # t6 = 0
    # f1 = 0
    # f2 = 0

    t1 = 0
    t2 = 0
    t3 = 0
    t4 = 0
    t5 = 0
    t6 = 0
    f1 = 0
    f2 = 0


    while not rospy.is_shutdown():

        p_l1j.publish(t1)
        p_l2j.publish(t2)
        p_l3j.publish(t3)
        p_l4j.publish(t4)
        p_l5j.publish(t5)
        p_l6j.publish(t6)
        p_f1j.publish(f1)
        p_f2j.publish(f2)

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
        p_l4j.publish(0)
        p_l5j.publish(0)
        p_l6j.publish(0)
        p_f1j.publish(0)
        p_f2j.publish(0)
