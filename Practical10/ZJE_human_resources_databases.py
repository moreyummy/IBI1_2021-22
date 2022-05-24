class Staff(object):
    def __init__(self, f, l, h, r):
        self.first = f
        self.last = l
        self.home = h
        self.role = r
    def __str__(self):
        return("%s %s  %s  %s"%(self.first, self.last, self.home, self.role))

#give an example
print(Staff('Li', 'Jackon', 'queen_road', 'leader'))
