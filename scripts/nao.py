import math
from naoqi import ALProxy

# Motions
from motions import wave, kick, elephant, saxophone, picture


class NAO(object):
    def __init__(self, ip, port):
        print("Hi I am Nao")

        # Proxies
        self.motion_proxy = ALProxy("ALMotion", ip, port)
        self.posture_proxy = ALProxy("ALRobotPosture", ip, port)
        self.text_to_speech_proxy = ALProxy("ALTextToSpeech", ip, port)
        self.audio_player_proxy = ALProxy("ALAudioPlayer", ip, port)
        self.camera_proxy = ALProxy("ALVideoDevice", ip, port)
        self.auto_life_proxy = ALProxy("ALAutonomousLife", ip, port)

        # Last walking commands
        self.x = 0
        self.y = 0
        self.theta = 0
        
        # Turn off autonomous life and wake up
        self.auto_life_proxy.setAutonomousAbilityEnabled("All", False)
        self.motion_proxy.wakeUp()
        self.text_to_speech_proxy.say("Hi, I'm Nao")

    def walk(self, x, y, theta):
        if (self.x != 0 or self.y != 0 or self.theta != 0) and (x == 0 and y == 0 and theta == 0):
            # If not already stopped, but need to stop
            self.motion_proxy.stopMove()
            self.posture_proxy.goToPosture("StandInit", 0.5)
        else:
            self.motion_proxy.moveToward(round(-y, 2), round(-x, 2), round(theta / math.pi, 2))
        self.x = x
        self.y = y
        self.theta = theta

    def wave(self):
        wave.wave(self.motion_proxy, self.text_to_speech_proxy)
        self.posture_proxy.goToPosture("StandInit", 0.5)

    def kick(self):
        kick.kick(self.motion_proxy)
        self.posture_proxy.goToPosture("StandInit", 0.5)

    def elephant(self):
        elephant.elephant(self.motion_proxy, self.audio_player_proxy)
        self.posture_proxy.goToPosture("StandInit", 0.5)

    def saxophone(self):
        saxophone.saxophone(self.motion_proxy, self.audio_player_proxy)
        self.posture_proxy.goToPosture("StandInit", 0.5)

    def take_picture(self):
        picture.take_picture(self.motion_proxy, self.audio_player_proxy, self.camera_proxy)
        self.posture_proxy.goToPosture("StandInit", 0.5)
    
    def rest(self):
        self.text_to_speech_proxy.say("Bye bye")
        self.motion_proxy.rest()
