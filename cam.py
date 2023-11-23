#!/usr/bin/python
import math


# height_initial:   H_0
# height_final:     H_i
# time_interval:    t_i
# time_elapsed:     T_i

# Cam Follower Kinematics for Constant Velocity Motion: Rise
def constant_rise_motion(height_initial, height_final, time_interval, time_elapsed):
    rise = height_initial + (height_final * time_interval) / time_elapsed
    return rise


# Cam Follower Kinematics for Constant Velocity Motion: Fall
def constant_fall_motion(height_initial, height_final, time_interval, time_elapsed):
    fall = height_initial + (height_final * time_interval) / time_elapsed
    return fall


# Cam Follower Kinematics for Cycloidal Motion: Rise
def cycloidal_rise_motion(height_initial, height_final, time_interval, time_elapsed):
    rise = (height_initial +
            height_final * (time_interval / time_elapsed - 1/math.pi *
            math.sin * (2 * math.pi * time_interval / time_elapsed)))
    return rise


# Cam Follower Kinematics for Cycloidal Motion: Fall
def cycloidal_fall_motion(height_initial, height_final, time_interval, time_elapsed):
    return fall


# Cam Follower Kinematics for Harmonic Motion: Rise
def harmonic_rise_motion(height_initial, height_final, time_interval, time_elapsed):
    return rise


# Cam Follower Kinematics for Harmonic Motion: Fall
def harmonic_fall_motion(height_initial, height_final, time_interval, time_elapsed):
    pass
