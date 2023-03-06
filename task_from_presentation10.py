class Calculator:

    @staticmethod
    def sum_(start, *args):
        sum_ = start
        for i in args:
            sum_+=i
        return sum_

    @staticmethod
    def subs_(start, *args):
        subs_ = start
        for i in args:
            subs_-=i
        return subs_

    @staticmethod
    def mult_(start, *args):
        mult_ = start
        for i in args:
            mult_ *= i
        return mult_

    @staticmethod
    def div_(start, *args):
        div_ = start
        for i in args:
            div_ *= i
        return div_

calc1 = Calculator()



