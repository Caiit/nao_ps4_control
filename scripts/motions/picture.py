from PIL import Image
import os
import threading
import time
import vision_definitions

# Current path
PATH = os.getcwd()


def save_image(camera_proxy):
    camera_id = camera_proxy.subscribe("camera", vision_definitions.k4VGA, vision_definitions.kRGBColorSpace, 30)
    nao_image = camera_proxy.getImageRemote(camera_id)

    image = Image.frombytes("RGB", (nao_image[0], nao_image[1]), nao_image[6])
    image.save(PATH + "/../pictures/" + time.ctime() + ".png")


def take_picture(motion_proxy, audio_player_proxy, camera_proxy):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.52, 1, 1.8, 2.4, 3.16, 3.8])
    keys.append([[0.118682, [3, -0.186667, 0], [3, 0.16, 0]], [-0.0568, [3, -0.16, 0.0318523], [3, 0.266667, -0.0530871]], [-0.136136, [3, -0.266667, 0], [3, 0.2, 0]], [-0.0982179, [3, -0.2, -0.0331099], [3, 0.253333, 0.0419392]], [0.0890118, [3, -0.253333, 0], [3, 0.213333, 0]], [-0.174919, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([1, 1.8, 2.4, 3.8])
    keys.append([[-0.0429939, [3, -0.346667, 0], [3, 0.266667, 0]], [-0.04913, [3, -0.266667, 0.00175314], [3, 0.2, -0.00131486]], [-0.0521979, [3, -0.2, 0], [3, 0.466667, 0]], [-0.019984, [3, -0.466667, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([0.44, 0.92, 2.36, 2.72, 3.2, 3.84])
    keys.append([[0.0858622, [3, -0.16, 0], [3, 0.16, 0]], [0.0689882, [3, -0.16, 0], [3, 0.48, 0]], [0.0733038, [3, -0.48, 0], [3, 0.12, 0]], [0.0733038, [3, -0.12, 0], [3, 0.16, 0]], [0.0858622, [3, -0.16, -0.00354718], [3, 0.213333, 0.00472958]], [0.0981341, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([0.44, 0.92, 2.36, 2.72, 3.2, 3.84])
    keys.append([[-0.128814, [3, -0.16, 0], [3, 0.16, 0]], [-0.151824, [3, -0.16, 0], [3, 0.48, 0]], [-0.116542, [3, -0.48, 0], [3, 0.12, 0]], [-0.116542, [3, -0.12, 0], [3, 0.16, 0]], [-0.128814, [3, -0.16, 0], [3, 0.213333, 0]], [-0.115008, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([0.44, 0.92, 1.72, 2.16, 2.56, 3.12, 3.72])
    keys.append([[-0.940732, [3, -0.16, 0], [3, 0.16, 0]], [-1.54462, [3, -0.16, 0], [3, 0.266667, 0]], [-1.54462, [3, -0.266667, 0], [3, 0.146667, 0]], [-1.54462, [3, -0.146667, 0], [3, 0.133333, 0]], [-1.53242, [3, -0.133333, -0.0121929], [3, 0.186667, 0.01707]], [-1.4207, [3, -0.186667, -0.111725], [3, 0.2, 0.119706]], [-0.444818, [3, -0.2, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0.92, 1.72, 2.16, 2.56, 3.72])
    keys.append([[-0.679603, [3, -0.32, 0], [3, 0.266667, 0]], [-0.475581, [3, -0.266667, -0.0167329], [3, 0.146667, 0.00920312]], [-0.466378, [3, -0.146667, -0.00241049], [3, 0.133333, 0.00219136]], [-0.461776, [3, -0.133333, 0], [3, 0.386667, 0]], [-1.16742, [3, -0.386667, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([0.44, 0.92, 1.72, 2.16, 2.28, 2.4, 2.56, 3.72])
    keys.append([[1, [3, -0.16, 0], [3, 0.16, 0]], [1, [3, -0.16, 0], [3, 0.266667, 0]], [1, [3, -0.266667, 0], [3, 0.146667, 0]], [0.9096, [3, -0.146667, 0.0904], [3, 0.04, -0.0246545]], [0.45, [3, -0.04, 0], [3, 0.04, 0]], [0.91, [3, -0.04, 0], [3, 0.0533333, 0]], [0.9092, [3, -0.0533333, 0.000800014], [3, 0.386667, -0.0058001]], [0.3024, [3, -0.386667, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([0.44, 0.92, 2.36, 2.72, 3.2, 3.84])
    keys.append([[-0.303691, [3, -0.16, 0], [3, 0.16, 0]], [0.176453, [3, -0.16, -0.00102218], [3, 0.48, 0.00306655]], [0.179519, [3, -0.48, 0], [3, 0.12, 0]], [0.179519, [3, -0.12, 0], [3, 0.16, 0]], [-0.303691, [3, -0.16, 0], [3, 0.213333, 0]], [0.136568, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([0.44, 0.92, 2.36, 2.72, 3.2, 3.84])
    keys.append([[0.0966839, [3, -0.16, 0], [3, 0.16, 0]], [0.159578, [3, -0.16, 0], [3, 0.48, 0]], [0.121228, [3, -0.48, 0], [3, 0.12, 0]], [0.121228, [3, -0.12, 0], [3, 0.16, 0]], [0.0966839, [3, -0.16, 0], [3, 0.213333, 0]], [0.115092, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([0.44, 0.92, 2.36, 2.72, 3.2, 3.84])
    keys.append([[-0.239262, [3, -0.16, 0], [3, 0.16, 0]], [-0.174835, [3, -0.16, -0.00102294], [3, 0.48, 0.00306881]], [-0.171766, [3, -0.48, 0], [3, 0.12, 0]], [-0.171766, [3, -0.12, 0], [3, 0.16, 0]], [-0.239262, [3, -0.16, 0], [3, 0.213333, 0]], [-0.171766, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([0.44, 0.92, 2.36, 2.72, 3.2, 3.84])
    keys.append([[0.246933, [3, -0.16, 0], [3, 0.16, 0]], [-0.0828778, [3, -0.16, 0.00315003], [3, 0.48, -0.00945009]], [-0.0923279, [3, -0.48, 0], [3, 0.12, 0]], [-0.0923279, [3, -0.12, 0], [3, 0.16, 0]], [0.246933, [3, -0.16, 0], [3, 0.213333, 0]], [-0.090548, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0.92, 1.72, 2.16, 2.56, 3.72])
    keys.append([[-0.262356, [3, -0.32, 0], [3, 0.266667, 0]], [-0.357464, [3, -0.266667, 0], [3, 0.146667, 0]], [-0.285367, [3, -0.146667, -0.00675023], [3, 0.133333, 0.00613657]], [-0.27923, [3, -0.133333, -0.00613657], [3, 0.386667, 0.0177961]], [1.50635, [3, -0.386667, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0.44, 0.92, 1.72, 2.16, 2.56, 3.72])
    keys.append([[0.654498, [3, -0.16, 0], [3, 0.16, 0]], [0.291418, [3, -0.16, 0], [3, 0.266667, 0]], [0.699462, [3, -0.266667, -0.0864636], [3, 0.146667, 0.047555]], [0.747017, [3, -0.146667, 0], [3, 0.133333, 0]], [0.728609, [3, -0.133333, 0.018408], [3, 0.386667, -0.0533831]], [0.116542, [3, -0.386667, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0.44, 0.92, 1.72, 2.16, 2.56, 3.72])
    keys.append([[-1.16064, [3, -0.16, 0], [3, 0.16, 0]], [-0.521602, [3, -0.16, 0], [3, 0.266667, 0]], [-0.702614, [3, -0.266667, 0], [3, 0.146667, 0]], [-0.684206, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.690342, [3, -0.133333, 0], [3, 0.386667, 0]], [0.130348, [3, -0.386667, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([0.44, 0.92, 2.36, 2.72, 3.2, 3.84])
    keys.append([[0.14884, [3, -0.16, 0], [3, 0.16, 0]], [0.073674, [3, -0.16, 0.000123396], [3, 0.48, -0.000370188]], [0.0733038, [3, -0.48, 0], [3, 0.12, 0]], [0.0733038, [3, -0.12, 0], [3, 0.16, 0]], [0.14884, [3, -0.16, 0], [3, 0.213333, 0]], [0.099752, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([0.44, 0.92, 2.36, 2.72, 3.2, 3.84])
    keys.append([[0.11049, [3, -0.16, 0], [3, 0.16, 0]], [0.0874801, [3, -0.16, 0.00204535], [3, 0.48, -0.00613606]], [0.081344, [3, -0.48, 0], [3, 0.12, 0]], [0.081344, [3, -0.12, 0], [3, 0.16, 0]], [0.11049, [3, -0.16, 0], [3, 0.213333, 0]], [0.0767419, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0.36, 0.84, 1.64, 2.16, 2.56, 3.12, 3.64])
    keys.append([[1.03673, [3, -0.133333, 0], [3, 0.16, 0]], [1.54462, [3, -0.16, 0], [3, 0.266667, 0]], [1.54462, [3, -0.266667, 0], [3, 0.173333, 0]], [1.54462, [3, -0.173333, 0], [3, 0.133333, 0]], [1.53251, [3, -0.133333, 0.0121091], [3, 0.186667, -0.0169528]], [1.43466, [3, -0.186667, 0.0978467], [3, 0.173333, -0.0908576]], [0.418823, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0.84, 1.64, 2.16, 2.56, 3.64])
    keys.append([[0.656511, [3, -0.293333, 0], [3, 0.266667, 0]], [0.467829, [3, -0.266667, 0], [3, 0.173333, 0]], [0.498508, [3, -0.173333, 0], [3, 0.133333, 0]], [0.475497, [3, -0.133333, 0], [3, 0.36, 0]], [1.15353, [3, -0.36, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0.36, 0.84, 1.64, 2.16, 2.28, 2.4, 2.56, 3.64])
    keys.append([[1, [3, -0.133333, 0], [3, 0.16, 0]], [0.9004, [3, -0.16, 0], [3, 0.266667, 0]], [0.9012, [3, -0.266667, 0], [3, 0.173333, 0]], [0.8996, [3, -0.173333, 0.00159997], [3, 0.04, -0.000369223]], [0.37, [3, -0.04, 0], [3, 0.04, 0]], [0.9, [3, -0.04, -0.000300005], [3, 0.0533333, 0.000400007]], [0.9004, [3, -0.0533333, 0], [3, 0.36, 0]], [0.3052, [3, -0.36, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([0.44, 0.92, 2.36, 2.72, 3.2, 3.84])
    keys.append([[-0.265424, [3, -0.16, 0], [3, 0.16, 0]], [0.174835, [3, -0.16, -0.00153356], [3, 0.48, 0.00460069]], [0.179436, [3, -0.48, 0], [3, 0.12, 0]], [0.179436, [3, -0.12, 0], [3, 0.16, 0]], [-0.265424, [3, -0.16, 0], [3, 0.213333, 0]], [0.133416, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([0.44, 0.92, 2.36, 2.72, 3.2, 3.84])
    keys.append([[-0.061318, [3, -0.16, 0], [3, 0.16, 0]], [-0.05058, [3, -0.16, 0], [3, 0.48, 0]], [-0.075124, [3, -0.48, 0], [3, 0.12, 0]], [-0.075124, [3, -0.12, 0], [3, 0.16, 0]], [-0.061318, [3, -0.16, 0], [3, 0.213333, 0]], [-0.06592, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("RHipYawPitch")
    times.append([0.44, 0.92, 3.2])
    keys.append([[-0.239262, [3, -0.16, 0], [3, 0.16, 0]], [-0.174835, [3, -0.16, 0], [3, 0.76, 0]], [-0.239262, [3, -0.76, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([0.44, 0.92, 2.36, 2.72, 3.2, 3.84])
    keys.append([[0.142704, [3, -0.16, 0], [3, 0.16, 0]], [-0.0904641, [3, -0.16, 0], [3, 0.48, 0]], [-0.0904641, [3, -0.48, 0], [3, 0.12, 0]], [-0.0904641, [3, -0.12, 0], [3, 0.16, 0]], [0.142704, [3, -0.16, 0], [3, 0.213333, 0]], [-0.091998, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0.84, 1.64, 2.16, 2.56, 3.64])
    keys.append([[-0.251533, [3, -0.293333, 0], [3, 0.266667, 0]], [-0.358915, [3, -0.266667, 0], [3, 0.173333, 0]], [-0.291418, [3, -0.173333, -0.00797527], [3, 0.133333, 0.00613482]], [-0.285283, [3, -0.133333, -0.00613482], [3, 0.36, 0.016564]], [1.5049, [3, -0.36, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0.36, 0.84, 1.64, 2.16, 2.56, 3.64])
    keys.append([[-0.640536, [3, -0.133333, 0], [3, 0.16, 0]], [-0.420357, [3, -0.16, 0], [3, 0.266667, 0]], [-0.785451, [3, -0.266667, 0], [3, 0.173333, 0]], [-0.767043, [3, -0.173333, -0.00398878], [3, 0.133333, 0.00306829]], [-0.763974, [3, -0.133333, -0.00306829], [3, 0.36, 0.00828439]], [-0.127364, [3, -0.36, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0.36, 0.84, 1.64, 2.16, 2.56, 3.64])
    keys.append([[0.994838, [3, -0.133333, 0], [3, 0.16, 0]], [0.547595, [3, -0.16, 0], [3, 0.266667, 0]], [0.751617, [3, -0.266667, 0], [3, 0.173333, 0]], [0.736278, [3, -0.173333, 0], [3, 0.133333, 0]], [0.736278, [3, -0.133333, 0], [3, 0.36, 0]], [0.177901, [3, -0.36, 0], [3, 0, 0]]])

    audio_thread = threading.Thread(target=audio_player_proxy.playFile, args=(PATH + "/../sounds/camera1.ogg", ))
    motion_thread = threading.Thread(target=motion_proxy.angleInterpolationBezier, args=(names, times, keys, ))
    camera_thread = threading.Thread(target=save_image, args=(camera_proxy, ))
    motion_thread.start()
    time.sleep(2)
    audio_thread.start()
    camera_thread.start()
    audio_thread.join()
    motion_thread.join()
