readme
------

1. extract the contents of the package 'kr6_v5' to catkin_ws. RENAME to kr6_v5 if necessary. the package needs to be named kr6_v5 to work.
2. clone the repository to your catkin_ws: https://github.com/pal-robotics/gazebo_ros_link_attacher.git. This is important for the gripper to work.
3. execute cd ~/catkin_ws/src/kr6_v5/scripts
4. execute sudo chmod +x pp.py init_robot.py spawn_models.py
5. execute python3 -m pip install rospkg sympy (so everything runs later on)
6. execute catkin clean && catkin build. 'catkin build' requires catkin tools to be installed (python3-catkin-tools) (from enpm809y).
7. source the catkin_ws with the command: source ~/catkin_ws/devel/setup.bash
8. from the root of the workspace, catkin_ws, execute roslaunch kr6_v5 l1.launch
9. from a new terminal execute the python script that performs pick and place. this can be found in kr6_v5/scripts/pp.py. the script must be executed using python3, not rosrun. this is because the program depends on sympy and there is a known issue with rosrun and sympy.
10. if the non reproducable error occurs whereby the robot does not spawn collision free, init_robot.py can be run the same way as pp.py to initialize the robot's position.
