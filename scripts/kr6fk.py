#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Float64
from sympy import sin, cos, Matrix, pi, symbols, simplify,diff
from sympy.interactive.printing import init_printing


# symbols
theta1 = symbols('theta1')
theta2 = symbols('theta2')
theta3 = symbols('theta3')
theta4 = symbols('theta4')
theta5 = symbols('theta5')
theta6 = symbols('theta6')
theta7 = symbols('theta7')
d1 = symbols('d1')
d3 = symbols('d3')
d5 = symbols('d5')
d7 = symbols('d7')

# symbolic matrix function
def transformation_matrix(a_in, alpha_in, d_in, theta_in):
    return Matrix([[cos(theta_in), -(sin(theta_in)*cos(alpha_in)), sin(theta_in)*sin(alpha_in), a_in*cos(theta_in)],
                [sin(theta_in), cos(theta_in)*cos(alpha_in), -(cos(theta_in)*sin(alpha_in)), a_in*sin(theta_in)],
                [0, sin(alpha_in), cos(alpha_in), d_in],
                [0, 0, 0, 1]])


# Intermediate Transformation Matrix Calculation


# D-H Table
# -------------------------------------
# A         Alpha       d       Theta
# 0.350     -90         815     theta1
# 0.850     0           0       theta2
# 0.145     90          0       theta3
# 0.0       -90         820     theta4
# 0.0       90          0       theta5
# 0.0       0           170     theta6


# 0->1
# A1 = transformation_matrix(0.350, -pi/2, 0.815, theta1)
# # 1->2
# A2 = transformation_matrix(0.850, 0, 0, theta2)
# # 2->3
# A3 = transformation_matrix(0.145, pi/2, 0, theta3)
# # 3->4 
# A4 = transformation_matrix(0, -pi/2, 0.820, theta4)
# # 4->5
# A5 = transformation_matrix(0, pi/2, 0, theta5)
# # 5->6
# A6 = transformation_matrix(0, 0, 0.170, theta6)

A1 = transformation_matrix(0.350, -pi/2, 0.815, theta1)
A2 = transformation_matrix(0.850, 0, 0, theta2)
A3 = transformation_matrix(0.145, pi/2, 0, theta3)
A4 = transformation_matrix(0, -pi/2, 0.820, theta4)
A5 = transformation_matrix(0, pi/2, 0, theta5)
A6 = transformation_matrix(0, 0, 0.170, theta6)

# Transformation Matrix w.r.t. base

T01 = 1   * A1
T02 = T01 * A2
T03 = T02 * A3
T04 = T03 * A4
T05 = T04 * A5
T06 = T05 * A6



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
    # t6 = 0.2
    # f1 = 0
    # f2 = 0

    # home position
    t1 = 0
    t2 = 0.2
    t3 = -0.76
    t4 = 0
    t5 = -0.2
    t6 = 0.2
    f1 = 0
    f2 = 0

    # pick position
    t1 = 0
    t2 = 1.05
    t3 = -0.4
    t4 = 0
    t5 = -1.4
    t6 = 0.2
    f1 = -1
    f2 = 1

    # lift position
    # t1 = 0
    # t2 = 0.2
    # t3 = -0.76
    # t4 = 0
    # t5 = -0.2
    # t6 = 0.2
    # f1 = -1
    # f2 = 1


    # squeeze position
    # t1 = 0
    # t2 = 1.05
    # t3 = -0.4
    # t4 = 0
    # t5 = -1.2
    # t6 = 0.2
    # f1 = 0
    # f2 = 0

    # exp
    # t1 = 0
    # t2 = 0.2
    # t3 = -0.76
    # t4 = 0
    # t5 = -1
    # t6 = 0.2
    # f1 = 0
    # f2 = 0

    while not rospy.is_shutdown():
        rospy.loginfo_once(T06.subs({
            'theta1': 0,
            'theta2': 0,
            'theta3': 0,
            'theta4': 0,
            'theta5': 0,
            'theta6': 0
        }))
        p_l1j.publish(t1)
        p_l2j.publish(t2)
        p_l3j.publish(t3)
        p_l4j.publish(t4)
        p_l5j.publish(t5)
        p_l6j.publish(t6)
        p_f1j.publish(f1)
        p_f2j.publish(f2)
        
        rate.sleep()
        # break

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
