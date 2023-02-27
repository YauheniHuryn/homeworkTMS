class Counter:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def increment(self):
        if self.start < self.stop:
            self.start+=1
            return self.start
        else:
            print('Maximal value is reached')
    def get(self):
        return self.start


c = Counter(2,5)
