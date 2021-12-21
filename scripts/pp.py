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

attach_srv = rospy.ServiceProxy('/link_attacher_node/attach', Attach)
attach_srv.wait_for_service()
rospy.loginfo("Created ServiceProxy to /link_attacher_node/attach")

detach_srv = rospy.ServiceProxy('/link_attacher_node/detach', Attach)
detach_srv.wait_for_service()
rospy.loginfo("Created ServiceProxy to /link_attacher_node/detach")


loop_rate = 20
playback_speed = 5

# pose
# ------------
# t1 = 1
# t2 = 0.2
# t3 = -0.76
# t4 = 0
# t5 = -0.2
# t6 = 0
# f1 = 0
# f2 = 0

def pub():
    time = 0
    rospy.init_node('pub_node', anonymous=True)
    rate = rospy.Rate(loop_rate)

    

    while not rospy.is_shutdown():
        rospy.loginfo(time)

        # home position
        if time < 10:
            pose = [0, 0.2, -0.76, 0, -0.2, 0, 0, 0]

        # pick position
        elif time < 20:
            pose = [0, 1.05, -0.4, 0, -1.4, 0.2, -1, 1]

        # grip position
        elif time < 30:
            pose = [0, 1.05, -0.4, 0, -1.4, 0.2, 0, 0]

        # home position
        elif time < 40:
            pose = [0, 0.2, -0.76, 0, -0.2, 0, 0, 0]

            rospy.loginfo("attaching pick box to gripper base")

            req = AttachRequest()
            req.model_name_1 = "kr6_v5"
            req.link_name_1 = "l6"
            req.model_name_2 = "pick_box"
            req.link_name_2 = "link"

            attach_srv.call(req)

        # rotate home position
        elif time < 50:
            pose = [1.57, 0.2, -0.76, 0, -0.2, 0, 0, 0]

        # drop position
        elif time < 60:
            pose = [1.57, 1.05, -0.4, 0, -1.4, 0.2, 0, 0]

        # release grip position
        elif time < 70:
            pose = [1.57, 1.05, -0.4, 0, -1.4, 0.2, -1, 1]

        # rotated home position
        elif time < 80:
            pose = [1.57, 0.2, -0.76, 0, -0.2, 0, 0, 0]

            rospy.loginfo("detaching pick box to gripper base")

            req = AttachRequest()
            req.model_name_1 = "kr6_v5"
            req.link_name_1 = "l6"
            req.model_name_2 = "pick_box"
            req.link_name_2 = "link"

            detach_srv.call(req)

        # release grip position
        elif time < 90:
            pose = [0, 0.2, -0.76, 0, -0.2, 0, 0, 0]

        # bye
        elif time < 100:
            break


        p_l1j.publish(pose[0])
        p_l2j.publish(pose[1])
        p_l3j.publish(pose[2])
        p_l4j.publish(pose[3])
        p_l5j.publish(pose[4])
        p_l6j.publish(pose[5])
        p_f1j.publish(pose[6])
        p_f2j.publish(pose[7])

        time += playback_speed/loop_rate
        rate.sleep()
        # break

if __name__ == '__main__':

    try:
        pub()
    except rospy.ROSInterruptException:
        pass
    finally:
        rospy.loginfo("later bud!")
        # p_l1j.publish(0)
        # p_l2j.publish(0)
        # p_l3j.publish(0)
        # p_l4j.publish(0)
        # p_l5j.publish(0)
        # p_l6j.publish(0)
        # p_f1j.publish(0)
        # p_f2j.publish(0)
