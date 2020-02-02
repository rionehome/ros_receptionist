from . import module_pico

# Start the test
def start():

    module_pico.speak('I will start game, please open the door!')
    return 1

if __name__ == '__main__':
    start()