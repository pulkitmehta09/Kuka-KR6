
1. Extract the contents of the package 'kr6_v5' to catkin_ws. RENAME to kr6_v5 if necessary. the package needs to be named kr6_v5 to work.
2. clone the repository to your catkin_ws: https://github.com/pal-robotics/gazebo_ros_link_attacher.git. This is important for the gripper to work.
3. Execute in terminal
 ```bash
$ cd ~/catkin_ws/src/kr6_v5/scripts
 ```
 
4. Execute 
```bash
$ sudo chmod +x pp.py init_robot.py spawn_models.py
```
6. Execute
```bash
$ python3 -m pip install rospkg sympy (so everything runs later on)
```
8. Execute in a new terminal 
```bash
$ catkin clean && catkin build. 'catkin build' requires catkin tools to be installed (python3-catkin-tools) (from enpm809y).
```
10. source the catkin_ws with the command: 
```bash
$ source ~/catkin_ws/devel/setup.bash
```
12. from the root of the workspace, catkin_ws, execute 
```bash
$ roslaunch kr6_v5 l1.launch
```
14. from a new terminal execute the python script that performs pick and place.
```bash
$ cd kr6_v5/scripts
$ python3 pp.py
```
