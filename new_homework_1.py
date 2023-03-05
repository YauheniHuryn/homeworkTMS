class Iterator:
    def __init__(self, lst: list):
        self.lst = lst
        self.cursor = -2

    def __next__(self):
        if self.cursor + 2 >= len(self.lst):
            raise StopIteration
        self.cursor+=2
        return self.lst[self.cursor]**2


class MyList:
    def __init__(self, lst: list):
        self.lst = lst

    def __iter__(self):
        return Iterator(self.lst)

lst1 = MyList([1,2,3,4,5,6,7,8])

for i in lst1:
    print(i)



