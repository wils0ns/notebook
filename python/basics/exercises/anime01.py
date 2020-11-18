from time import sleep
from random import randint

x = 0  # position
step = 2  # speed
max_position = 10  # limits x value
animation_length = 60  # animation durantion (animation_length*sleep)
timeline = 0  # controls the timed events in the animation
offset = 20

while animation_length > 0:
    x += step  # Move `*` `step` times

    if timeline > offset:
        print('*'.rjust(x, '-'), end='')
        newStar = '*'*x
        print('', newStar)
    else:
        print('*'.rjust(x, '-'))

    if x >= max_position:
        # If x is at its maximum position, invert step
        step = -step

    if x <= 0:
        # To have finite runs, uncomment the line below
        animation_length -= 1
        print(animation_length)
        step = -step
    sleep(0.1)

    timeline += 1
