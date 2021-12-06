from UTILS import read_values, Base

values = read_values('Day6_value', split_on=',')

tests = []


class Test(Base):
    def __init__(self, value):
        self.value = int(value)

    def day(self):
        self.value -= 1
        if self.value < 0:
            self.value = 6
            new_fish = Test(8)
            tests.append(new_fish)


for v in values[0]:
    tests.append(Test(v))

day_counter = 0
for i in range(256):
    day_counter += 1
    print(day_counter)
    print('----')
    for t in tests.copy():
        t.day()

    print(len(tests))


