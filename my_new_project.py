# class Meta(type):
#     def create_local_attrs(self, *args, **kwargs):
#         for key, value in self.class_attrs.items():
#             self.__dict__[key] = value
#
#     def __init__(cls, name, bases, attrs):
#
#         cls.class_attrs = attrs
#         cls.__init__ = Meta.create_local_attrs()
#
#
# class FootballPlayer(metaclass=Meta):
#     title = 'Title'
#     content = 'Content'
#     photo = 'Photo'
#
# LM = FootballPlayer()
# # print(LM.__dict__)
#
# MyClass = type('MyPukClass', (), {})
# print(MyClass)

# class Point:
#     def __new__(cls, *args, **kwargs):
#         print('start execution '+str(cls))
#         return super().__new__(cls)
#
#     def __init__(self, x=0,y=0):
#         print('init'+str(self))
#         self.x = x
#         self.y = y
#
# pt = Point(1,2)
# # print(pt)

class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None
    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'connection with DB: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('closing the connection with DB')

    def read(self):
        return 'data from DB'

    def write(self, data):
        print(f'write in DB {data}')

# d1 = DataBase('Yauhen', 202020, 2021)
#
# d2 = DataBase('Yauheni', 225020, 2051)
# print(id(d1), id(d2))

lst = [1,2,3,4,5,6]
it = iter(lst)
print(next(it))