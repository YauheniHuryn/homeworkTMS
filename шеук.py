# def create_new_metaclass(name, base, attrs):
#     return type(name,base,attrs)
#
#
# cl1 = create_new_metaclass('Popka',(), {"method1": 1*4, "method2": 7*7})
# print()
# class Popka(metaclass=create_new_metaclass):
#     def method3(self):
#         return 5*4


# pop1 = Popka(  )
#
# class Meta(type):
#     def __init__(cls, name, base, attrs):
#         super().__init__(name, base, attrs)


# def foo1():
#     print('STARTED EXECUTION')
#     count = 1999
#     a = int(input())
#     for _ in range(a):
#         count+=1
#         yield count
#
# f = foo1()
# print(next(f))
# print(next(f))
# print(next(f))

# def foo_():
#     print('POVIDLOOOOOOOOOOOOOOOOOOOOOOO')
#     b = 23
#     a = yield
#     print(a)
#     yield b * 2
#
# f = foo_()
# next(f)
# c = f.send(30)
# print(c)
def producer(sentence, next_coroutine):
    tokens = sentence.split(' ')
    for token in tokens:
        next_coroutine.send(token)
    next_coroutine.close()

def pattern_filter(pattern='hi', next_coroutine = None):
    print(f'Searching for {pattern}')
    try:
        while True:
            token = (yield)
            if pattern in token:
                next_coroutine.send(token)
    except GeneratorExit:
        print('Filtering is done')

def print_token():
    print('Print tokens')
    try:
        while True:
            token = (yield)
            print(token)
    except GeneratorExit:
        print('Done printing')

pt = print_token()
next(pt)
pf = pattern_filter(next_coroutine=pt)
next(pf)

sentence = 'Hey lohi ya ebu kartohi i liking'
# producer(sentence, pf)