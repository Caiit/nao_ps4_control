# NAO PS4 Control

## Requirements
- python 2
- [pygame](https://www.pygame.org/news)
- [Pillow](https://pypi.org/project/Pillow/)
- [NaoQi](http://doc.aldebaran.com/2-1/dev/python/install_guide.html)

`pygame` and `Pillow` can be installed using pip or the requirements file: 

`pip install -r requirements.txt`

`NaoQi` cannot be installed using pip and should be installed following [this link](http://doc.aldebaran.com/2-1/dev/python/install_guide.html).

## Setup
Copy sounds files to the robot:

`scp -r sounds/ nao@<robot_name>.local:~/`

Connect with the robot and connect the ps4 controller to your laptop.

## Run 

`cd scripts/`
`python ps4.py -ip <robot_ip>`

## Controls
Left joystick: move in x/y direction

Right joystick: turn

X: wave

O: kick

△: elephant

□: saxophone

ps4: shutdown (robot will go to rest position and disconnect)


## Add new motions
- Create a new python file in `motions/`.
- Add the motion to the NAO class.
- Add the motion to a specific button in the PS4 class.

