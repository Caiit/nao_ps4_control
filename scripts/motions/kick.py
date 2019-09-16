def kick(motion_proxy):
    """
    Kick is a special case. TODO: COMMENT
    :param motion_proxy:
    :return:
    """
    names = ['LShoulderRoll', 'LShoulderPitch', 'RShoulderRoll', 'RShoulderPitch', 'LHipRoll', 'LHipPitch', 'LKneePitch', 'LAnklePitch', 'LAnkleRoll', 'RHipRoll', 'RHipPitch', 'RKneePitch', 'RAnklePitch', 'RAnkleRoll']
    angles = [[0.3], [0.4], [-0.5], [1.0], [0.0], [-0.4, -0.2], [0.95, 1.5], [-0.55, -1], [-0.2], [0.0], [-0.4], [0.95], [-0.55], [-0.2]]
    times =  [[0.5], [0.5], [ 0.5], [0.5], [0.5], [ 0.4,  0.8], [ 0.4, 0.8], [ 0.4, 0.8], [ 0.4], [0.5], [ 0.4], [0.4] , [0.4],   [0.4]]
    motion_proxy.angleInterpolation(names, angles, times, True)
    motion_proxy.angleInterpolation(['LShoulderPitch', 'LHipPitch', 'LKneePitch', 'LAnklePitch'], [1.0, -0.7, 1.05, -0.5], [[0.1], [0.1], [0.1], [0.1]], True)
    motion_proxy.angleInterpolation(['LHipPitch', 'LKneePitch', 'LAnklePitch'], [-0.5, 1.1, -0.65], [[0.25], [0.25], [0.25]], True)
