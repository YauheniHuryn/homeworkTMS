from abc import abstractmethod, ABC


class Bird(ABC):

   def __init__(self, name):
       self.name = name

   @abstractmethod
   def walk(self):
        pass
   @abstractmethod
   def fly(self):
       pass


class Flying_bird(Bird):

    def walk(self):
        return print(f'{self.name} is walking')

    def fly(self):
        return print(f'{self.name} is flying')

    def eat(self):
        return print(f'{self.name} mostly eats worms and grains')

class Nonflying_bird(Bird):

    def walk(self):
        return print(f'{self.name} is walking')

    def fly(self):
        raise AttributeError('Penguin object has no attribute fly')

    def swim(self):
        return print(f'{self.name} can swim')
    def eat(self):
        return print(f'{self.name} mostly eats fish')


class Superbird(Flying_bird, Nonflying_bird):

    def eat(self):
        return print('eats everything')

bird1 = Flying_bird('Calibri')
bird1.walk()

# ping = Nonflying_bird('Pinguin')
# ping.fly()
sss = Superbird('Call')
sss.walk()