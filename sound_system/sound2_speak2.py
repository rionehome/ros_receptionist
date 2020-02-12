import rclpy
from rclpy.node import Node

from module import module_information

from rione_msgs.msg import Command

class SoundSystem2(Node):
    def __init__(self):
        super(SoundSystem2, self).__init__('SoundSystem2')

        self.create_subscription(
            Command, 'sound2/speak2',
            self.command_callback,
            10
        )

        self.senses_publisher = self.create_publisher(
            Command,
            '/signal',
            10
        )

    # recieve a command {Command, Content}
    def command_callback(self, msg):

        # Start the test and start follow me
        if "information" == msg.command:
            content = msg.content
            if content == "drink":
                option = 0
                while True:
                    drink = module_information.information(content, option)
                    if drink == -1:
                        option = -1
                        pass
                    elif drink != -1:
                        self.main_publisher("START")
                        break


    # Publish a result of an action
    def main_publisher(self, command, content=""):

        _trans_message = Command()
        #_trans_message.flag = flag
        _trans_message.command = command
        _trans_message.content = content
        _trans_message.sender = "sound"

        self.senses_publisher.publish(_trans_message)
        # self.destroy_publisher(self.senses_publisher)

def main():
    rclpy.init()
    node = SoundSystem2()
    rclpy.spin(node)


if __name__ == '__main__':
    main()
