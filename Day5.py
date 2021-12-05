from UTILS import read_values, Base

values = read_values('Day5_value', split_on=' ')


class Test(Base):
    def __init__(self, value):
        self.value = value
        self.generated_values = []
        self.produce_values()

    def produce_values(self):
        x1, y1 = [int(x) for x in self.value[0].split(',')]
        x2, y2 = [int(x) for x in self.value[2].split(',')]

        if x1 == x2:
            for i in range(y1, y2 + 1 * (y1 < y2) + -1 * (y1 > y2), 1 + -2 * (y1 > y2)):
                self.generated_values.append((x1, i))
        elif y1 == y2:
            for i in range(x1, x2 + 1 * (x1 < x2) + -1 * (x1 > x2), 1 + -2 * (x1 > x2)):
                self.generated_values.append((i, y1))
        else:  # Part 2
            for i in range(x1, x2 + (1 + -2 * (x1 > x2)), 1 + -2 * (x1 > x2)):
                self.generated_values.append((i, y1 + (i - x1) * (1 + -2 * ((
                        y1 < y2 and (i - x1) < 0) or (y1 > y2 and (i - x1) > 0)))))


tests = []


for v in values:
    tests.append(Test(v))

summs = {}
for t in tests:
    for v in t.generated_values:
        if v not in summs:
            summs[v] = 1
        else:
            summs[v] = summs[v] + 1

counter = 0
for key, value in summs.items():
    counter += 1 * (value > 1)

print(counter)
