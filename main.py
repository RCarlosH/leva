from displacement import displacement
import math
import matplotlib.pyplot as plt
import numpy as np

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
step_abs = 0
for m in motions:
    total_time += m['interval']

angular_vel = 1 / total_time
current_height = 0.0
heights = list()
for m in motions:
    # Divide interval by calculation intervals
    h_o = current_height    # Save height before motion calculation
    if m['displacement'] < 0:
        h_o += m['displacement']
    h_i = m['displacement'] #+ current_height
    steps = int(m['interval']/interval_calc)    # how many times to loop
    count = 0
    for i in range(steps):                      # in current motion
        count += 1
        step_abs += 1
        time_abs = step_abs * interval_calc
        step = count * interval_calc            # current point in time
        
        # Apply Formula
        current_height = displacement(m['typeof'], h_o, h_i, step, m['interval'])

        # Get angular position in radians
        rads = time_abs * angular_vel * 2 * math.pi
        # Get X and Y points
        x_coord = current_height * math.cos(rads)
        y_coord = current_height * math.sin(rads)

        heights.append([time_abs, rads, current_height, x_coord, y_coord])

# Print results table -----------------------------
print('\n', 'Time', 3*' ', 'Rads', 3*' ', 'Displac.', 'X', 6*' ', 'Y')
for lis in heights:
    for i in lis:
        print(' {:<8}'.format(round(i, 3)), end='')
    print('')

# Save to csv file
with open('leva.csv', 'w') as csv:
    csv.write('Time, Theta (rads), Displacement, RX, RY\n')
    for lis in heights:
        for i in lis:
            csv.write(str(i) + ',')
        csv.write('\n')


# Generate graphs ---------------------------------
ts = list()
hs = list()
xs = list()
ys = list()
for height in heights:
    ts.append(height[0])
    hs.append(height[2])
    xs.append(height[3])
    ys.append(height[4])

times_arr = np.array(ts)
heights_arr = np.array(hs)
xs_arr = np.array(xs)
ys_arr = np.array(ys)

plt.plot(times_arr, heights_arr)
plt.grid()
plt.savefig('heights.png')
plt.clf()

plt.scatter(xs_arr, ys_arr)
plt.savefig('profile.png')
