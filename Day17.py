x_max = 286
x_min = 257
y_max = -57
y_min = -101

s_pos = (0, 0)
s_vel_x = 6
s_vel_y = 9

highest_y = None
real_highest_y = 0


def do_step():
    global s_vel_y
    global s_vel_x
    global s_pos
    global highest_y

    s_pos = (s_pos[0] + s_vel_x, s_pos[1] + s_vel_y)

    s_vel_y -= 1
    if s_vel_x < 0:
        s_vel_x += 1
    elif s_vel_x > 0:
        s_vel_x -= 1

    if highest_y is None:
        highest_y = s_pos[1]
    else:
        if s_pos[1] > highest_y:
            highest_y = s_pos[1]


def check_inside_area():
    if s_pos[0] >= x_min and s_pos[0] <= x_max:
        if s_pos[1] >= y_min and s_pos[1] <= y_max:
            return True

    return False


def passed():
    if s_pos[0] > x_max or s_pos[1] < y_min:
        return True

    return False


counter = 0

for x in range(x_max + 50):
    print(x)
    for y in range(2000):
        highest_y = None

        s_vel_x = x
        s_vel_y = y - 1000
        s_pos = (0, 0)

        possible = False
        hit = False

        while not possible:
            do_step()
            if check_inside_area():
                hit = True
                possible = True
            else:
                possible = passed()

        if hit:
            print('IS HIT!')
            counter += 1
            print(highest_y)
            print((x, y))
            if real_highest_y is None:
                real_highest_y = highest_y
            else:
                if real_highest_y < highest_y:
                    real_highest_y = highest_y


print(real_highest_y)
print(highest_y)
print(counter)
