import math


# height_initial:   H_0
# height_final:     H_i
# time_interval:    t_i
# time_elapsed:     T_i

def displacement(typeof, height_initial, height_final, time_interval, time_elapsed):
    # Cam Follower Kinematics for Constant Velocity Motion: Rise
    if typeof == 'Constant':
        if height_final > 0:
            pos = height_initial + ((height_final * time_interval) / time_elapsed)
        else:
            # Cam Follower Kinematics for Constant Velocity Motion: Fall
            pos = (height_initial + height_final *
                (1 - time_interval / time_elapsed))

    elif typeof == 'Cycloidal':
        # Cam Follower Kinematics for Cycloidal Motion: Rise
        pos = (height_initial +
                height_final * ((time_interval / time_elapsed) - (1/math.pi *
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

# User input ----------------------------------------
# User input: Lenght of intervals
interval_calc = 0
while interval_calc == 0:
    try:
        interval_calc = float(input('Calculation interval length (t_i): '))
        if interval_calc == 0:
            print('Can\'t be 0')
            raise ValueError

    except ValueError:
        print('Must be a float ')

# User input: Create intervals list
motions = list()
motions_count = 0

while True:
    try:
        # Interval length
        motion_interval = input('''\n:: Press Return to stop adding intervals or type interval length (s):\n>> ''')
        if motion_interval == '': break
        # Displacement
        displ = input(':: Type the displacement (m) for the interval:\n>> ')
        # Type of motion
        motion_type = input(''':: Select type of motion:\
                            \n[1] Constant velocity motion\
                            \n[2] Cycloidal motion\
                            \n[3] Harmonic motion\n>> ''')

        # Validate input
        motion_interval = float(motion_interval)
        displ = float(displ)
        motion_type = int(motion_type)

        if motion_type == 1: motion_type = 'Constant'
        elif motion_type == 2: motion_type = 'Cycloidal'
        elif motion_type == 3: motion_type = 'Harmonic'
        else:
            print('Type of motion not valid')
            raise ValueError

        # Add motion to motions list
        motions.append(dict(interval=motion_interval,
                            displacement=displ,
                            typeof=motion_type))

    except ValueError:
        print('ValueError, motion not added')
        continue

print('\n\n:: Added motions:')
print(' Interval     | Displacement | Type of motion')
for motion in motions:
    for k, v, in motion.items():
        print(' {:<14}'.format(v), end='')
    print('')

# Processing --------------------------------------
total_time = 0
for m in motions:
    total_time += m['interval']

angular_vel = 2 * math.pi / total_time
current_height = 0.0
heights = list()
count = 0
for m in motions:
    # Divide interval by calculation intervals
    steps = int(m['interval']/interval_calc)    # how many times to loop
    for i in range(steps):                      # in current motion
        count += 1
        step = count * interval_calc            # current point in time
        # Apply Formula
        current_height += displacement(m['typeof'], current_height, m['displacement'], step, m['interval'])

        # Get angular position in radians
        rads = step * angular_vel
        # Get X and Y points
        x_coord = current_height * math.sin(rads)
        y_coord = current_height * math.cos(rads)

        heights.append([step, rads, current_height, x_coord, y_coord])

    # Generate displacement graph
    # Generate cam profile

print('')
for i in heights:
    print(i)
