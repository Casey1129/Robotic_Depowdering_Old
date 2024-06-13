from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Paths
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_flexiv_rizon_gazebo = get_package_share_directory('flexiv_rizon_gazebo')

    # Launch Gazebo
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py')
        ),
    )

    # Spawn Robot
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-file', os.path.join(pkg_flexiv_rizon_gazebo, 'models', 'rizon.urdf'),
                   '-entity', 'rizon'],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        spawn_entity,
    ])

