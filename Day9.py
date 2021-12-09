from UTILS import read_values

values = read_values('Day9_value')

lowpoints = 0
lowpoints_indexes = []  # Used for Part 2

for i in range(len(values)):
    for j in range(len(values[0])):
        current = int(values[i][j])
        if i != 0:
            if int(values[i - 1][j]) <= current:
                continue
        if i != len(values) - 1:
            if int(values[i + 1][j]) <= current:
                continue
        if j != 0:
            if int(values[i][j - 1]) <= current:
                continue
        if j != len(values[0]) - 1:
            if int(values[i][j + 1]) <= current:
                continue

        lowpoints += current + 1
        lowpoints_indexes.append((i, j))

print(lowpoints)


# Part 2

checked_current = []
highest_values = []


def check_neighbour(pos, value):
    global checked_current
    if pos in checked_current:
        return 0
    if value == 9:
        return 0

    checked_current.append(pos)
    neighbour_value = 0

    if pos[0] != 0:
        if value < int(values[pos[0] - 1][pos[1]]):
            neighbour_value += check_neighbour((pos[0] - 1, pos[1]), int(values[pos[0] - 1][pos[1]]))
    if pos[0] != len(values) - 1:
        if value < int(values[pos[0] + 1][pos[1]]):
            neighbour_value += check_neighbour((pos[0] + 1, pos[1]), int(values[pos[0] + 1][pos[1]]))
    if pos[1] != 0:
        if value < int(values[pos[0]][pos[1] - 1]):
            neighbour_value += check_neighbour((pos[0], pos[1] - 1), int(values[pos[0]][pos[1] - 1]))
    if pos[1] != len(values[0]) - 1:
        if value < int(values[pos[0]][pos[1] + 1]):
            neighbour_value += check_neighbour((pos[0], pos[1] + 1), int(values[pos[0]][pos[1] + 1]))

    return neighbour_value + 1


for lowpoint in lowpoints_indexes:
    checked_current = []
    highest_values.append(check_neighbour(lowpoint, int(values[lowpoint[0]][lowpoint[1]])))

highest_values = sorted(highest_values, reverse=True)

print(highest_values[0] * highest_values[1] * highest_values[2])
