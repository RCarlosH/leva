import math


# height_if:        H_0     H_F
# height_delta:     H_i     H_j
# time_interval:    t_i     t_j
# time_elapsed:     T_i     T_j

def displacement(typeof, height_if, height_delta, time_interval, time_elapsed):
    # Cam Follower Kinematics for Constant Velocity Motion: Rise
    if typeof == 'Constant':
        if height_delta > 0:
            print('rise') #debug
            pos = height_if + ((height_delta * time_interval) / time_elapsed)
        else:
            # Cam Follower Kinematics for Constant Velocity Motion: Fall
            print('fall') #debug
            pos = height_if + height_delta * (1 - (time_interval / time_elapsed))

    elif typeof == 'Cycloidal':
        # Cam Follower Kinematics for Cycloidal Motion: Rise
        pos = (height_if +
                height_delta * ((time_interval / time_elapsed) - (1/math.pi *
                math.sin * (2 * math.pi * time_interval / time_elapsed))))

        # Cam Follower Kinematics for Cycloidal Motion: Fall
        pass

    elif typeof == 'Harmonic':
        # Cam Follower Kinematics for Harmonic Motion: Rise
        pass

        # Cam Follower Kinematics for Harmonic Motion: Fall
        pass

    else:
        raise ValueError

    return pos
