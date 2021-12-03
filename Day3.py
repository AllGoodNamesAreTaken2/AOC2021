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
most_common_bit_array = ''
lest_common_bit_array = ''

for i in range(size):
    one = 0
    zero = 0
    for test in tests:
        if test.value[i] == '0':
            zero += 1
        else:
            one += 1
    if one > zero:
        most_common_bit_array += '1'
        lest_common_bit_array += '0'
    else:
        most_common_bit_array += '0'
        lest_common_bit_array += '1'

print(most_common_bit_array)
print(lest_common_bit_array)

common = 0
least = 0

for i in range(size):
    common += (math.pow(2, i)) * int(most_common_bit_array[-i - 1])
    least += (math.pow(2, i)) * int(lest_common_bit_array[-i - 1])

print(common)
print(least)
print(common * least)
