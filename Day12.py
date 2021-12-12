from UTILS import read_values, Base

values = read_values('Day12_value', split_on='-')
answers = []
signs = {}
used_signs = []
current_sign = ''


class Test(Base):
    def __init__(self, sign):
        self.sign = sign
        self.visited = False
        self.connections = []

    def find_end(self):
        path = 'start'
        for connection in self.connections:
            connection.next(path)

    def next(self, path):
        if self.sign == 'end':
            path += ',' + self.sign
            global answers
            if path not in answers:
                answers.append(path)
            return
        if self.sign.lower() == self.sign:
            global current_sign
            if current_sign == self.sign:
                if path.count(self.sign) > 1:
                    return
            else:
                if path.count(self.sign) >= 1:
                    return
        path += ',' + self.sign
        for connection in self.connections:
            connection.next(path)


for value in values:
    for v in value:
        if v not in used_signs:
            used_signs.append(v)
            signs[v] = Test(v)

for value in values:
    signs[value[0]].connections.append(signs[value[1]])
    signs[value[1]].connections.append(signs[value[0]])

# signs['start'].find_end() // Part 1

for sign in used_signs:
    if sign == 'start':
        continue
    current_sign = sign
    signs['start'].find_end()

print(len(answers))
