from . import module_pico

def follow():

    module_pico.speak('Please following me')
    return 1

if __name__ == '__main__':
    follow()