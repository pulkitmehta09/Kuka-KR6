#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Float64
from sympy import sin, cos, Matrix, pi, symbols, simplify,diff
from sympy.interactive.printing import init_printing
from gazebo_ros_link_attacher.srv import Attach, AttachRequest, AttachResponse


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
    rospy.init_node('init_robot', anonymous=True)
    time = 0
    rate = rospy.Rate(loop_rate)
    while not rospy.is_shutdown():
        # home position
        if time < 3:
            # pose = [0, 0.2, -0.76, 0, -0.2, 0, 0, 0]
            pose = [1, 0, 0, 0, 0, 0, 0, 0]
        # bye
        else:
            break

        p_l1j.publish(pose[0])
        p_l2j.publish(pose[1])
        p_l3j.publish(pose[2])
        p_l4j.publish(pose[3])
        p_l5j.publish(pose[4])
        p_l6j.publish(pose[5])
        p_f1j.publish(pose[6])
        p_f2j.publish(pose[7])

        time += 1/loop_rate
        rate.sleep()
        # break

if __name__ == '__main__':

    try:
        pub()
    except rospy.ROSInterruptException:
        pass
    finally:
        rospy.loginfo("kr6 ready")
