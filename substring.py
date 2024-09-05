import random


class structure:

    def __init__(self):
        self.items = list()

    def insert(self, value):
        if value not in self.items:
            self.items.append(value)
        else:
            print("Duplicate value ", value)

    def remove(self, value):
        self.items.remove(value)

    def getRandom(self):
        return self.items[random.randint(0, len(self.items) - 1)]


d = structure()

d.insert(4)
d.insert(6)
d.insert(4)
d.insert(9)

d.insert(4)
d.insert(16)
d.insert(14)

d.insert(9)
d.remove(14)


print(d.items, " ---> ", d.getRandom())
