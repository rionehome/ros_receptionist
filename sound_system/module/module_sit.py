from . import module_pico

def sit():

    module_pico.speak('Please sit down this chair')
    return 1

if __name__ == '__main__':
    sit()