## Receptionist

### sound_system
- turtlebot_button2.py
  - Subscriber
    - std_msgs/Bool, 'turtlebot2/button2'
  - Publisher
    - rione_msgs/Command, 'sound2/speak1'

- sound_system.py
  - Subscriber
    - rione_msgs/Command, 'sound_system/command'
  - Publisher
    - rione_msgs/Command, 'cerebrum/command'

- sound2_speak1.py
  - Subscriber
    - rione_msgs/Command, 'sound2/speak1'
  - Publisher
    - rione_msgs/Command, 'sound2/speak2'

- sound2_speak2.py
  - Subscriber
    - rione_msgs/Command, 'sound2/speak2'
  - Publisher
    - rione_msgs/Command, '/signal'

- sound2_speak3.py
  - Subscriber
    - rione_msgs/Command, 'sound2/speak3'
  - Publisher
    - rione_msgs/Command, '/signal2'

- sound2_speak4.py
  - Subscriber
    - rione_msgs/Command, 'sound2/speak4'
  - Publisher
    - rione_msgs/Command, '/signal3'
