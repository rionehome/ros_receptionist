from launch import LaunchDescription
import launch_ros.actions

def generate_launch_description():
    return LaunchDescription([
    
        launch_ros.actions.Node(
            package="sound_system",
            node_executable="turtlebot_button2",
            output="screen"
        ),

        launch_ros.actions.Node(
            package="sound_system",
            node_executable="sound_system",
            output="screen"

        ),
        
        launch_ros.actions.Node(
            package="sound_system",
            node_executable="sound2_speak1",
            output="screen"

        ),

        launch_ros.actions.Node(
            package="sound_system",
            node_executable="sound2_speak2",
            output="screen"

        ),

        launch_ros.actions.Node(
            package="sound_system",
            node_executable="sound2_speak3",
            output="screen"

        ),

        launch_ros.actions.Node(
            package="sound_system",
            node_executable="sound2_speak4",
            output="screen"

        )
    ])
