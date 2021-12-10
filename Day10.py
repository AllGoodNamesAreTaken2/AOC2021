from UTILS import read_values, Base

values = read_values('Day10_value')


class Test(Base):
    def __init__(self, input_value):
        self.value = input_value


tests = []

for value in values:
    tests.append(Test(value))


translate = {
    '[': ']',
    '<': '>',
    '(': ')',
    '{': '}',
}

tracker = {  # Used for part 2
    '[': 0,
    '{': 0,
    '<': 0,
    '(': 0,
    ')': 0,
    '>': 0,
    '}': 0,
    ']': 0,
}

points = 0

for value in values.copy():
    opens = []
    for sign in value:
        if sign in '({[<':
            opens.append(sign)
        else:
            start = opens.pop(-1)
            if translate[start] != sign:
                # print('expected ' + translate[start] + ' but got ' + sign)
                if sign == ']':
                    points += 57
                    if value in values:
                        values.remove(value)  # For part 2
                elif sign == '>':
                    points += 25137
                    if value in values:
                        values.remove(value)
                elif sign == '}':
                    points += 1197
                    if value in values:
                        values.remove(value)
                elif sign == ')':
                    points += 3
                    if value in values:
                        values.remove(value)

print(points)

# Part 2
all_points = []
for value in values:
    opens = []
    for sign in value:
        if sign in '({[<':
            opens.append(sign)
        else:
            opens.pop(-1)
    closers = []
    for o in opens:
        closers.insert(0, translate[o])
    points = 0
    for i in range(len(closers)):
        value = 0
        if closers[i] == ')':
            value = 1
        if closers[i] == ']':
            value = 2
        if closers[i] == '}':
            value = 3
        if closers[i] == '>':
            value = 4
        points = points * 5 + value
    all_points.append(points)

all_points = sorted(all_points)
print(all_points[int(len(all_points) / 2)])

