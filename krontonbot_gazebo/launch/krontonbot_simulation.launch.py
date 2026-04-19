#!/usr/bin/env python3

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():

    krontonbot_description_pkg = get_package_share_directory('krontonbot_description')
    krontonbot_gazebo_pkg = get_package_share_directory('krontonbot_gazebo')



    robot_description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(krontonbot_description_pkg, 'launch', 'robot_description.launch.py')
        )
        )
    
    robot_world = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(krontonbot_gazebo_pkg, 'launch', 'krontonbot_home.launch.py')
        )
        )

    robot_spawner= IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(krontonbot_gazebo_pkg, 'launch', 'spawn_robot.launch.py')
        )
        )
    
    ld = LaunchDescription()

    ld.add_action(robot_description)
    ld.add_action(robot_world)
    ld.add_action(robot_spawner)


    return ld