from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'ros1_action_name',
            default_value='follow_joint_trajectory',
            description='ROS1 action name'
        ),
        DeclareLaunchArgument(
            'ros2_action_name',
            default_value='follow_joint_trajectory',
            description='ROS2 action name'
        ),
        Node(
            package="action_bridge",
            name="action_bridge_follow_joint_trajectory_2_1",
            executable="action_bridge_follow_joint_trajectory_2_1",
            output="screen",
            arguments=["ros1_action_name", "ros2_action_name"],
            respawn=True
        )
    ])
