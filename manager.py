from contants import *
import random
from math import sqrt
from R1 import get_r1
from R2 import get_r2

def generate_lap():

    # Generate y-intercepts
    c1 = random.randint(INTERCEPT_LOWER_LIMIT, INTERCEPT_UPPER_LIMIT)
    c2 = random.randint(INTERCEPT_LOWER_LIMIT, INTERCEPT_UPPER_LIMIT)

    # Generate slopes
    # These need a check i.e. m1!=m2 coz parallel lines meet at infinity
    m1 = random.randint(INTERCEPT_LOWER_LIMIT, INTERCEPT_UPPER_LIMIT)
    m2 = random.randint(INTERCEPT_LOWER_LIMIT, INTERCEPT_UPPER_LIMIT)
    while(m1==m2):
        m2 = random.randint(INTERCEPT_LOWER_LIMIT, INTERCEPT_UPPER_LIMIT)

    lap = []
    # A list having information about r1, r2 and starting position
    r1 = (m1, c1)
    r2 = (m2, c2)
    lap.append(r1)
    lap.append(r2)

    # Find intersection and append to lap
    lap.append(find_intersection(lap=lap))

    return lap

def find_intersection(lap=None):

    m1 = lap[0][0]
    c1 = lap[0][1]
    m2 = lap[1][0]
    c2 = lap[1][1]

    # Find x co-ordinate
    x = (c2-c1)/(m1-m2)
    # Find y co-ordinate
    y = m1*x + c1

    return (x,y)

def _get_distance(x1, y1, x2, y2):
    return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

if __name__=='__main__':

    # Keep a count of the laps
    lap_count = 1

    while(lap_count<=10):

        lap = generate_lap()
        origin_x = lap[2][0]
        origin_y = lap[2][1]
        r1_x = origin_x
        r1_y = origin_y
        r2_x = origin_x
        r2_y = origin_y
        m1   = lap[0][0]
        c1   = lap[0][1]
        m2   = lap[1][0]
        c2   = lap[1][1]

        lap_details = []

        while(_get_distance(r1_x, r1_y, r2_x, r2_y) <= 10):

            r1_x = get_r1(r1_x, m1, c1)[0]
            r1_y = get_r1(r1_y, m2, c2)[1]
            r2_x = get_r2(r2_x, m1, c1)[0]
            r2_y = get_r2(r2_y, m2, c2)[1]

            lap_details.append((r1_x, r1_y, r2_x, r2_y))

        # Lap completion
        # Increment lap count
        lap_count += 1
        print(lap_details)
