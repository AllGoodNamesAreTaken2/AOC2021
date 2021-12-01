from UTILS import read_values

values = read_values('Day1_value', only_ints=True)

larger = 0

three_sums = {}
value = values.pop(0)
three_sums[0] = value
value = values.pop(0)
three_sums[0] += value
three_sums[1] = value

index = 0
for value in values:
    three_sums[index] += value
    three_sums[index + 1] += value
    three_sums[index + 2] = value
    index += 1

prev = three_sums[0]

for i in range(len(three_sums.values()) - 2):
    if three_sums[i] > prev:
        larger += 1
    prev = three_sums[i]

print(larger)
