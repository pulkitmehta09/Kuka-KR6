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
    a = a_in
    alpha = alpha_in
    d = d_in
    theta = theta_in

    A = Matrix([[cos(theta), -(sin(theta)*cos(alpha)), sin(theta)*sin(alpha), a*cos(theta)],
                [sin(theta), cos(theta)*cos(alpha), -(cos(theta)*sin(alpha)), a*sin(theta)],
                [0, sin(alpha), cos(alpha), d],
                [0, 0, 0, 1]])
    return A


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
A1 = transformation_matrix(0.350, -pi/2, 0.815, theta1)
# 1->2
A2 = transformation_matrix(0.850, 0, 0, theta2)
# 2->3
A3 = transformation_matrix(0.145, pi/2, 0, theta3)
# 3->4 
A4 = transformation_matrix(0, -pi/2, 0.820, theta4)
# 4->5
A5 = transformation_matrix(0, pi/2, 0, theta5)
# 5->6
A6 = transformation_matrix(0, 0, 0.170, theta6)

# Transformation Matrix w.r.t. base

# 0->1
T01 = 1   * A1
# 0->2
T02 = T01 * A2
# 0->3
T03 = T02 * A3
# 0->4
T04 = T03 * A4
# 0->5
T05 = T04 * A5
# 0->6
T06 = T05 * A6

# forward kinematics
def get_x(q):
    '''
    take q and return X
    '''
    a = T07.subs({
        'theta1': q[0],
        'theta2': q[1],
        'theta3': 0,
        'theta4': q[2],
        'theta5': q[3],
        'theta6': q[4],
        'theta7': q[5],
        'd1':0.3600,
        'd3':0.4200,
        'd5':0.3995,
        'd7':0.2055
    })
    return Matrix([a.col(3)[0], a.col(3)[1], a.col(3)[2], 0, 0, 0])



# method 2 jacobian

def get_z(htm):
    # returns a sympy matrix
    temp = htm.col(2)
    temp.row_del(3)
    return temp

htm_list = [T01, T02, T03, T04, T05, T06, T07]
# Zi_list = [Matrix([0, 0, 1])]
Zi_list = []

# for htm in htm_list[1:]:
for htm in htm_list:
    # make a list of Zi and Oi for easy processing
    Zi_list.append(get_z(htm))

# h(q) is parametric translation column in T07
h = T07.col(3)
# drop the padding
h.row_del(3)

theta_list = [theta1,theta2,theta3,theta4,theta5,theta6,theta7]

J = Matrix()
for index, th in enumerate(theta_list):
  J = J.row_join(Matrix([diff(h, th), Zi_list[index]]))

# drop joint 3 (theta 3) column
J.col_del(2)  



# inverse jacobian

def inverse_jacobian(jack, q):
    '''
    q should have 6 theta values
    jack should be the parametrized jacobian
    '''
    temp = jack.subs({
    'theta1': q[0],
    'theta2': q[1],
    'theta3': 0,
    'theta4': q[2],
    'theta5': q[3],
    'theta6': q[4],
    'theta7': q[5],
    'd1':0.360,
    'd3':0.420,
    'd5':0.3995,
    'd7':0.2055       
    })
    return temp.pinv()



# -----------------------------------------------------------------------------
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

    # home position
    t1 = 0
    t2 = 0.2
    t3 = -0.76
    t4 = 0
    t5 = -0.2
    t6 = 0
    f1 = 0
    f2 = 0

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
