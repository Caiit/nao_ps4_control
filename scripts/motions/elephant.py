import os
import threading

# Current path
PATH = os.getcwd()


def elephant(motion_proxy, audio_player_proxy):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.44, 0.84, 1.92, 3.32, 4.4, 5.72, 6.24, 6.76])
    keys.append([[-0.21293, [3, -0.16, 0], [3, 0.133333, 0]], [0.514872, [3, -0.133333, 0], [3, 0.36, 0]], [0.149268, [3, -0.36, 0], [3, 0.466667, 0]], [0.514872, [3, -0.466667, 0], [3, 0.36, 0]], [0.149268, [3, -0.36, 0], [3, 0.44, 0]], [0.514872, [3, -0.44, 0], [3, 0.173333, 0]], [0.274544, [3, -0.173333, 0.118544], [3, 0.173333, -0.118544]], [-0.196393, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([0.44, 0.84, 1.92, 3.32, 4.4, 5.72, 6.24, 6.76])
    keys.append([[-0.0453786, [3, -0.16, 0], [3, 0.133333, 0]], [-0.3735, [3, -0.133333, 0], [3, 0.36, 0]], [-0.370809, [3, -0.36, 0], [3, 0.466667, 0]], [-0.3735, [3, -0.466667, 0], [3, 0.36, 0]], [-0.370809, [3, -0.36, 0], [3, 0.44, 0]], [-0.3735, [3, -0.44, 0], [3, 0.173333, 0]], [0.0367741, [3, -0.173333, 0], [3, 0.173333, 0]], [-0.021518, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([0.84, 1.8, 3.2, 4.28, 5.6, 6.64])
    keys.append([[-0.030722, [3, -0.293333, 0], [3, 0.32, 0]], [-0.122762, [3, -0.32, 0.016016], [3, 0.466667, -0.0233567]], [-0.14884, [3, -0.466667, 0], [3, 0.36, 0]], [-0.122762, [3, -0.36, 0], [3, 0.44, 0]], [-0.14884, [3, -0.44, 0], [3, 0.346667, 0]], [0.0858622, [3, -0.346667, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([0.84, 1.8, 3.2, 4.28, 5.6, 6.64])
    keys.append([[-0.144154, [3, -0.293333, 0], [3, 0.32, 0]], [-0.147222, [3, -0.32, 0], [3, 0.466667, 0]], [-0.139552, [3, -0.466667, 0], [3, 0.36, 0]], [-0.147222, [3, -0.36, 0], [3, 0.44, 0]], [-0.139552, [3, -0.44, -0.00286001], [3, 0.346667, 0.00225334]], [-0.131882, [3, -0.346667, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([0.52, 0.92, 2, 3.4, 4.48, 5.8, 6.32, 6.84])
    keys.append([[-0.849975, [3, -0.186667, 0], [3, 0.133333, 0]], [-1.54462, [3, -0.133333, 0], [3, 0.36, 0]], [-1.54462, [3, -0.36, 0], [3, 0.466667, 0]], [-1.54462, [3, -0.466667, 0], [3, 0.36, 0]], [-1.54462, [3, -0.36, 0], [3, 0.44, 0]], [-1.54462, [3, -0.44, 0], [3, 0.173333, 0]], [-1.23023, [3, -0.173333, -0.186879], [3, 0.173333, 0.186879]], [-0.423342, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0.92, 2, 3.4, 4.48, 5.8, 6.32, 6.84])
    keys.append([[0, [3, -0.32, 0], [3, 0.36, 0]], [0.0280028, [3, -0.36, 0], [3, 0.466667, 0]], [0, [3, -0.466667, 0], [3, 0.36, 0]], [0.0280028, [3, -0.36, 0], [3, 0.44, 0]], [0, [3, -0.44, 0.0280028], [3, 0.173333, -0.0110314]], [-1.35763, [3, -0.173333, 0], [3, 0.173333, 0]], [-1.1981, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([0.52, 0.92, 2, 3.4, 4.48, 5.8, 6.32, 6.84])
    keys.append([[0.08, [3, -0.186667, 0], [3, 0.133333, 0]], [0.602755, [3, -0.133333, 0], [3, 0.36, 0]], [0.602755, [3, -0.36, 0], [3, 0.466667, 0]], [0.602755, [3, -0.466667, 0], [3, 0.36, 0]], [0.602755, [3, -0.36, 0], [3, 0.44, 0]], [0.602755, [3, -0.44, 0], [3, 0.173333, 0]], [0.1, [3, -0.173333, 0], [3, 0.173333, 0]], [0.3092, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([0.84, 1.8, 3.2, 4.28, 5.6, 6.64])
    keys.append([[-0.421808, [3, -0.293333, 0], [3, 0.32, 0]], [0.128898, [3, -0.32, 0], [3, 0.466667, 0]], [-0.697927, [3, -0.466667, 0], [3, 0.36, 0]], [0.128898, [3, -0.36, 0], [3, 0.44, 0]], [-0.697927, [3, -0.44, 0], [3, 0.346667, 0]], [0.1335, [3, -0.346667, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([0.84, 1.8, 3.2, 4.28, 5.6, 6.64])
    keys.append([[0.101286, [3, -0.293333, 0], [3, 0.32, 0]], [0.150374, [3, -0.32, 0], [3, 0.466667, 0]], [0.0874801, [3, -0.466667, 0], [3, 0.36, 0]], [0.150374, [3, -0.36, 0], [3, 0.44, 0]], [0.0874801, [3, -0.44, 0], [3, 0.346667, 0]], [0.0951499, [3, -0.346667, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([0.84, 1.8, 3.2, 4.28, 5.6, 6.64])
    keys.append([[-0.288349, [3, -0.293333, 0], [3, 0.32, 0]], [-0.184038, [3, -0.32, 0], [3, 0.466667, 0]], [-0.253067, [3, -0.466667, 0], [3, 0.36, 0]], [-0.184038, [3, -0.36, 0], [3, 0.44, 0]], [-0.253067, [3, -0.44, 0], [3, 0.346667, 0]], [-0.156426, [3, -0.346667, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([0.84, 1.8, 3.2, 4.28, 5.6, 6.64])
    keys.append([[0.486237, [3, -0.293333, 0], [3, 0.32, 0]], [0.271475, [3, -0.32, 0], [3, 0.466667, 0]], [0.76389, [3, -0.466667, 0], [3, 0.36, 0]], [0.271475, [3, -0.36, 0], [3, 0.44, 0]], [0.76389, [3, -0.44, 0], [3, 0.346667, 0]], [-0.092082, [3, -0.346667, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0.52, 0.92, 2, 3.4, 4.48, 5.8, 6.32, 6.84])
    keys.append([[0.195477, [3, -0.186667, 0], [3, 0.133333, 0]], [-0.403171, [3, -0.133333, 0.0765654], [3, 0.36, -0.206727]], [-0.654399, [3, -0.36, 0], [3, 0.466667, 0]], [-0.403171, [3, -0.466667, 0], [3, 0.36, 0]], [-0.654399, [3, -0.36, 0], [3, 0.44, 0]], [-0.403171, [3, -0.44, -0.251228], [3, 0.173333, 0.0989686]], [1.52936, [3, -0.173333, -0.00613659], [3, 0.173333, 0.00613659]], [1.53549, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0.92, 2, 3.4, 4.48, 5.8, 6.32, 6.84])
    keys.append([[0.139697, [3, -0.32, 0], [3, 0.36, 0]], [0.15506, [3, -0.36, 0], [3, 0.466667, 0]], [0.139697, [3, -0.466667, 0], [3, 0.36, 0]], [0.15506, [3, -0.36, 0], [3, 0.44, 0]], [0.139697, [3, -0.44, 0.0153633], [3, 0.173333, -0.00605219]], [0.00609397, [3, -0.173333, 0], [3, 0.173333, 0]], [0.116542, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0.52, 0.92, 2, 3.4, 4.48, 5.8, 6.32, 6.84])
    keys.append([[-0.7662, [3, -0.186667, 0], [3, 0.133333, 0]], [0, [3, -0.133333, 0], [3, 0.36, 0]], [0, [3, -0.36, 0], [3, 0.466667, 0]], [0, [3, -0.466667, 0], [3, 0.36, 0]], [0, [3, -0.36, 0], [3, 0.44, 0]], [0, [3, -0.44, 0], [3, 0.173333, 0]], [-0.30224, [3, -0.173333, 0], [3, 0.173333, 0]], [0.0889301, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([0.84, 1.8, 3.2, 4.28, 5.6, 6.64])
    keys.append([[-0.0383082, [3, -0.293333, 0], [3, 0.32, 0]], [-0.078192, [3, -0.32, 0.0235041], [3, 0.466667, -0.0342768]], [-0.211651, [3, -0.466667, 0], [3, 0.36, 0]], [-0.078192, [3, -0.36, 0], [3, 0.44, 0]], [-0.211651, [3, -0.44, 0], [3, 0.346667, 0]], [0.099752, [3, -0.346667, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([0.84, 1.8, 3.2, 4.28, 5.6, 6.64])
    keys.append([[0.179519, [3, -0.293333, 0], [3, 0.32, 0]], [0.216335, [3, -0.32, 0], [3, 0.466667, 0]], [0.12583, [3, -0.466667, 0], [3, 0.36, 0]], [0.216335, [3, -0.36, 0], [3, 0.44, 0]], [0.12583, [3, -0.44, 0], [3, 0.346667, 0]], [0.130432, [3, -0.346667, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0.44, 0.84, 1.4, 2.44, 3.32, 3.88, 4.92, 5.72, 6.24, 6.76])
    keys.append([[1.24791, [3, -0.16, 0], [3, 0.133333, 0]], [0.534071, [3, -0.133333, 0.168473], [3, 0.186667, -0.235862]], [0.0349066, [3, -0.186667, 0], [3, 0.346667, 0]], [0.884857, [3, -0.346667, 0], [3, 0.293333, 0]], [0.534071, [3, -0.293333, 0.173138], [3, 0.186667, -0.110179]], [0.0349066, [3, -0.186667, 0], [3, 0.346667, 0]], [0.884857, [3, -0.346667, 0], [3, 0.266667, 0]], [0.534071, [3, -0.266667, 0], [3, 0.173333, 0]], [1.29014, [3, -0.173333, 0], [3, 0.173333, 0]], [0.418823, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0.44, 0.84, 1.92, 3.32, 4.4, 5.72, 6.24, 6.76])
    keys.append([[1.42244, [3, -0.16, 0], [3, 0.133333, 0]], [1.2363, [3, -0.133333, 0], [3, 0.36, 0]], [1.24098, [3, -0.36, 0], [3, 0.466667, 0]], [1.2363, [3, -0.466667, 0], [3, 0.36, 0]], [1.24098, [3, -0.36, 0], [3, 0.44, 0]], [1.2363, [3, -0.44, 0], [3, 0.173333, 0]], [1.39743, [3, -0.173333, 0], [3, 0.173333, 0]], [1.19955, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0.44, 1.36, 2.44, 3.84, 4.92, 6.24, 6.76])
    keys.append([[0.66, [3, -0.16, 0], [3, 0.306667, 0]], [0.602465, [3, -0.306667, 0], [3, 0.36, 0]], [0.98, [3, -0.36, 0], [3, 0.466667, 0]], [0.602465, [3, -0.466667, 0], [3, 0.36, 0]], [0.98, [3, -0.36, 0], [3, 0.44, 0]], [0.1, [3, -0.44, 0], [3, 0.173333, 0]], [0.308, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([0.84, 1.8, 3.2, 4.28, 5.6, 6.64])
    keys.append([[-0.403483, [3, -0.293333, 0], [3, 0.32, 0]], [0.197844, [3, -0.32, 0], [3, 0.466667, 0]], [-0.705682, [3, -0.466667, 0], [3, 0.36, 0]], [0.197844, [3, -0.36, 0], [3, 0.44, 0]], [-0.705682, [3, -0.44, 0], [3, 0.346667, 0]], [0.125746, [3, -0.346667, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([0.84, 1.8, 3.2, 4.28, 5.6, 6.64])
    keys.append([[-0.124212, [3, -0.293333, 0], [3, 0.32, 0]], [-0.208583, [3, -0.32, 0], [3, 0.466667, 0]], [-0.0643861, [3, -0.466667, 0], [3, 0.36, 0]], [-0.208583, [3, -0.36, 0], [3, 0.44, 0]], [-0.0643861, [3, -0.44, 0], [3, 0.346667, 0]], [-0.0904641, [3, -0.346667, 0], [3, 0, 0]]])

    names.append("RHipYawPitch")
    times.append([0.84, 1.8, 3.2, 4.28, 5.6, 6.64])
    keys.append([[-0.288349, [3, -0.293333, 0], [3, 0.32, 0]], [-0.184038, [3, -0.32, 0], [3, 0.466667, 0]], [-0.253067, [3, -0.466667, 0], [3, 0.36, 0]], [-0.184038, [3, -0.36, 0], [3, 0.44, 0]], [-0.253067, [3, -0.44, 0], [3, 0.346667, 0]], [-0.156426, [3, -0.346667, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([0.84, 1.8, 3.2, 4.28, 5.6, 6.64])
    keys.append([[0.466378, [3, -0.293333, 0], [3, 0.32, 0]], [0.131966, [3, -0.32, 0], [3, 0.466667, 0]], [0.814596, [3, -0.466667, 0], [3, 0.36, 0]], [0.131966, [3, -0.36, 0], [3, 0.44, 0]], [0.814596, [3, -0.44, 0], [3, 0.346667, 0]], [-0.0827939, [3, -0.346667, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0.44, 0.84, 1.92, 3.32, 4.4, 5.72, 6.24, 6.76])
    keys.append([[0.79587, [3, -0.16, 0], [3, 0.133333, 0]], [0.53058, [3, -0.133333, 0.117297], [3, 0.36, -0.316703]], [-0.506132, [3, -0.36, 0], [3, 0.466667, 0]], [0.53058, [3, -0.466667, 0], [3, 0.36, 0]], [-0.506132, [3, -0.36, 0], [3, 0.44, 0]], [0.53058, [3, -0.44, -0.501073], [3, 0.173333, 0.197392]], [1.58927, [3, -0.173333, 0], [3, 0.173333, 0]], [1.53404, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0.84, 1.92, 3.32, 4.4, 5.72, 6.24, 6.76])
    keys.append([[0.219786, [3, -0.293333, 0], [3, 0.36, 0]], [0.190134, [3, -0.36, 0], [3, 0.466667, 0]], [0.219786, [3, -0.466667, 0], [3, 0.36, 0]], [0.190134, [3, -0.36, 0], [3, 0.44, 0]], [0.219786, [3, -0.44, 0], [3, 0.173333, 0]], [0.208528, [3, -0.173333, 0.0112574], [3, 0.173333, -0.0112574]], [-0.124296, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0.44, 0.84, 1.92, 3.32, 4.4, 5.72, 6.24, 6.76])
    keys.append([[0.493928, [3, -0.16, 0], [3, 0.133333, 0]], [-1.27409, [3, -0.133333, 0], [3, 0.36, 0]], [-1.27223, [3, -0.36, 0], [3, 0.466667, 0]], [-1.27409, [3, -0.466667, 0], [3, 0.36, 0]], [-1.27223, [3, -0.36, 0], [3, 0.44, 0]], [-1.27409, [3, -0.44, 0], [3, 0.173333, 0]], [0.883542, [3, -0.173333, 0], [3, 0.173333, 0]], [0.0858622, [3, -0.173333, 0], [3, 0, 0]]])

    audio_thread = threading.Thread(target=audio_player_proxy.playFile, args=(PATH + "/../sounds/elephant.ogg", ))
    motion_thread = threading.Thread(target=motion_proxy.angleInterpolationBezier, args=(names, times, keys, ))
    audio_thread.start()
    motion_thread.start()
    audio_thread.join()
    motion_thread.join()
