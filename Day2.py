from UTILS import read_values, Base

values = read_values('Day2_value', split_on=' ')


class Test(Base):
    def __init__(self, input_value):
        self.value = input_value


tests = []

for value in values:
    tests.append(Test(value))


depth = 0
forward = 0
aim = 0

for test in tests:
    if test.value[0] == 'down':
        aim += int(test.value[1])
    if test.value[0] == 'up':
        aim -= int(test.value[1])
    if test.value[0] == 'forward':
        forward += int(test.value[1])
        depth += int(test.value[1]) * aim


print(depth)
print(forward)
print(aim)
print(forward*depth)
