from UTILS import read_values, Base

values = read_values('Day6_value', split_on=',')

days = 256

my_d = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
}

for v in values[0]:
    f = int(v)
    my_d[f] += 1


for day in range(days):
    my_dd = my_d.copy()
    my_dd[0] = my_d[1]
    my_dd[1] = my_d[2]
    my_dd[2] = my_d[3]
    my_dd[3] = my_d[4]
    my_dd[4] = my_d[5]
    my_dd[5] = my_d[6]
    my_dd[6] = my_d[7] + my_d[0]
    my_dd[7] = my_d[8]
    my_dd[8] = my_d[0]
    my_d = my_dd


total = 0
for value in my_d.values():
    total += value

print(total)
