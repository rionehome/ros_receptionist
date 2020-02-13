from . import module_pico
from time import sleep

# Start the test
def start():

    module_pico.speak('I will start game, please open the door!')
    sleep(5)
    return 1

if __name__ == '__main__':
    start()