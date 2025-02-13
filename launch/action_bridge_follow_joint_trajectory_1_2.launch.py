from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="action_bridge",
            name="action_bridge_follow_joint_trajectory_1_2",
            executable="action_bridge_follow_joint_trajectory_1_2",
            output="screen",
            respawn="true")
    ])
