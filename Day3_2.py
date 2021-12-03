from UTILS import read_values, Base
import math

values = read_values('Day3_value')


class Test(Base):
    def __init__(self, input_value):
        self.value = input_value


tests = []

for value in values:
    tests.append(Test(value))

size = len(tests[0].value)

for i in range(size):
    one = 0
    zero = 0

    for test in tests:
        if test.value[i] == '1':
            one += 1
        else:
            zero += 0

    for test in tests.copy():
        if one >= zero:
            if test.value[i] != '1':
                tests.remove(test)
        else:
            if test.value[i] != '0':
                tests.remove(test)


