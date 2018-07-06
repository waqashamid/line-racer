

def get_r1(x=None, m1=None, c1=None):

    # # De-referencing lines from the lap
    # m1 = lap[0][0]
    # c1 = lap[0][1]
    # # De-referencing intersection points from the lap
    # x = lap[2][0]
    # y = lap[2][1]
    #
    # current_lap_points.append((x, y))
    # # Store all the current lap co-ordinates
    # current_x = current_lap_points[-1][0] + 1
    # current_y = m1*current_x + c1
    #
    # current_lap_points.append((current_x, current_y))
    #
    # return ((current_x, current_y))
    return (x+1, m1*x + c1)
#
# while(True):
#     print(get_position(1, 2, 5))
# # print(convey_position([(4, -5), (-3, 4), (1.2857142857142858, 0.14285714285714324)]))