import math


# height_if:        H_0     H_F
# height_delta:     H_i     H_j
# time_interval:    t_i     t_j
# time_elapsed:     T_i     T_j

def displacement(typeof, height_if, height_delta, time_interval, time_elapsed):
    if typeof == 'Constant':
        if height_delta > 0:
            # Cam Follower Kinematics for Constant Velocity Motion: Rise
            pos = height_if + ((height_delta * time_interval) / time_elapsed)
        else:
            # Cam Follower Kinematics for Constant Velocity Motion: Fall
            pos = height_if - height_delta * (1 - (time_interval/time_elapsed))

    elif typeof == 'Cycloidal':
        # Cam Follower Kinematics for Cycloidal Motion: Rise
        if height_delta > 0:
            pos = (height_if +
                    height_delta * ((time_interval / time_elapsed) - (1/math.pi *
                    math.sin * (2 * math.pi * time_interval / time_elapsed))))
        else:
            # Cam Follower Kinematics for Cycloidal Motion: Fall
            pos = (height_if - height_delta * (1-(time_interval/time_elapsed) +
                1/(2*math.pi()) * math.sin(2*math.pi*time_interval/time_elapsed)))

    elif typeof == 'Harmonic':
        if height_delta > 0:
            # Cam Follower Kinematics for Harmonic Motion: Rise
            pos = height_if + (height_delta/2)*(1-math.cos(math.pi()*time_interval/time_elapsed))

        # Cam Follower Kinematics for Harmonic Motion: Fall
        else:
            pos = height_if - (height_delta/2)*(1+math.cos(math.pi()*time_interval/time_elapsed))

    else:
        raise ValueError

    return pos
