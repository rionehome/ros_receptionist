from setuptools import setup

package_name = 'sound_system'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    py_modules=[
        'sound_system'
    ],
    install_requires=['setuptools'],
    data_files=[
        ('lib/' + package_name, ['package.xml']),
        ('lib/' + package_name+'/module',
         ['module/module_pico.py',
          'module/module_follow.py',
          'module/module_make_map.py',
          'module/module_beep.py',
          'module/module_information.py',
          'module/module_sit.py',
          'module/module_start.py'
          ]),
        ('lib/sound_system/dictionary/',
         ['dictionary/yes_no.dict',
          'dictionary/yes_no.gram',
          'dictionary/map_test.dict',
          'dictionary/map_test.gram',
          'dictionary/info_name.dict',
          'dictionary/info_name.gram',
          'dictionary/info_drink.dict',
          'dictionary/info_drink.gram',
          'dictionary/start_the_test.dict',
          'dictionary/start_the_test.gram'
          ]),
        ('lib/sound_system/beep/',
         ['beep/speech.wav',
          'beep/start.wav',
          'beep/stop.wav'
          ]),
        ('lib/sound_system/log',
            ['log/log.txt'])
    ],
    zip_safe=True,
    author='HiroseChihiro',
    author_email='rr0111fx@ed.ritsumei.ac.jp',
    maintainer='HiroseChihiro',
    maintainer_email='rr0111fx@ed.ritsumei.ac.jp',
    keywords=['ROS2'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='sound package for reseptionist',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sound_system = sound_system:main',
        ],
    },
)
