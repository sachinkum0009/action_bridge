A package to bridge actions between ROS1 and ROS2. 

**NOTE:**   
- Currently supports forwarding goals from ROS1 (noetic) action client to ROS2 (humble) action server
- As an example, implemented interfaces for the action bridge for FibonacciAction   
  and FollowJointTrajectoryAction  





**How to build:**  

> Follow the below link to install dependencies
- [Using ROS1 Bridge Jammy Upstream](https://docs.ros.org/en/humble/How-To-Guides/Using-ros1_bridge-Jammy-upstream.html)

```
source /opt/ros/humble/setup.bash
colcon build --packages-select action_bridge
```

Now you are ready to run the `action_bridge`!  
Source this workspace to use the executeables built in the previous step. 
```
source <path-to-workspace>/install/setup.bash
```
4 example executables are available:
- `action_bridge_fibonacci_1_2`
- `action_bridge_fibonacci_2_1`
- `action_bridge_follow_joint_trajectory_1_2` and
- `action_bridge_follow_joint_trajectory_2_1`
You can start one of these nodes in the following manner:
```
ros2 run action_bridge action_bridge_fibonacci_1_2
```
OR
```
ros2 run action_bridge action_bridge_follow_joint_trajectory_1_2
```









