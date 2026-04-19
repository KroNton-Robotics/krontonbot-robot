from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    
    #call other launches inside the main launch
    krontonbot_amcl_launch = os.path.join(get_package_share_directory('krontonbot_localization'),'launch','krontonbot_localization.launch.py')
    krontonbot_nav2_launch = os.path.join(get_package_share_directory('krontonbot_navigation'),'launch','krontonbot_nav2.launch.py')
    
    amcl_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            krontonbot_amcl_launch
        )
    )

    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            krontonbot_nav2_launch
        )
    )


    return LaunchDescription([   
        amcl_launch, 
        nav2_launch
    ])