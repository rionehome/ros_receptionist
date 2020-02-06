import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data

from module import module_pico
from module import module_start
from module import module_information
from module import module_follow
from module import module_sit
from module import module_make_map


from rione_msgs.msg import Command

class SoundSystem(Node):
    def __init__(self):
        super(SoundSystem, self).__init__('SoundSystem')

        self.command = None

        self.create_subscription(
            Command, 'sound_system/command',
            self.command_callback,
            10
        )

        self.senses_publisher = self.create_publisher(
            Command,
            'cerebrum/command',
            10
        )


    # recieve a command {Command, Content}
    def command_callback(self, msg):

        # Speak a content
        if 'speak' == msg.command:
            if module_pico.speak(msg.content) == 1:
                self.cerebrum_publisher("speak")

        # Start the test
        if 'start' == msg.command:
            if module_start.start() == 1:
                self.cerebrum_publisher("start")

        # Get information
        if 'information' == msg.command:
            content = msg.content
            if content == "name":
                name = module_information.main(content)
                self.cerebrum_publisher("information_name", str(name))
            elif msg.content == "drink":
                drink = module_information.main(content)
                self.cerebrum_publisher("information_drink", str(drink))
            elif msg.content == "share":
                if module_information.main(content) == 1:
                    self.cerebrum_publisher("information_share")

        # Say please follow me
        if 'follow' == msg.command:
            if str(module_follow.follow()) == 1:
                self.cerebrum_publisher("follow")

        # Say please sit down
        if 'sit' == msg.command:
            if str(module_sit.sit()) == 1:
                self.cerebrum_publisher("sit", "restart")

        # Make map
        content = None
        if 'make_map' == msg.command:
            content = msg.content
            if content == "go":
                self.cerebrum_publisher("make_map_go",str(module_make_map.make_map(content)))
            else:self.cerebrum_publisher("make_map_else",(module_make_map.make_map()))

    # Publish a result of an action
    def cerebrum_publisher(self, command, content=""):

        _trans_message = Command()
        #_trans_message.flag = flag
        _trans_message.command = command
        _trans_message.content = content
        _trans_message.sender = "sound"

        self.senses_publisher.publish(_trans_message)
        # self.destroy_publisher(self.senses_publisher)


def main():
    rclpy.init()
    node = SoundSystem()
    rclpy.spin(node)


if __name__ == '__main__':
    main()
