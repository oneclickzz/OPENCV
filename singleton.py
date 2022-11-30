
# __new__()
# __init__()

import time


class Foo(object):
    def __new__(cls, *args, **kwargs):
        # print("__new__ is called: cls: ", cls) #1

        instance = super().__new__(cls)
        # print('instance: ', instance)

        # instance.bar = 10
        return instance

    def __init__(self):
        # print("__init__ is called self: ", self) #2
        # print("self.bar: ", self.bar)
        pass

# ins = object.__new__(Class)
# object.__init__(ins)

s = Foo()
print(s) #3


# 클래스 변수, 인스턴스 변수, 객체 변수
class ClassVar():
    foo = 'foo'
    pass

# 인스턴스, 객체 x, 클래스 o

print('ClassVar.foo: ',  ClassVar.foo)

ClassVar.foo = 'foo2'
print('ClassVar.foo: ',  ClassVar.foo)

cv = ClassVar()
print('cv.foo: ',  cv.foo)

print(f'ClassVar.foo: {id(ClassVar.foo)}, cv.foo: {id(cv.foo)}')


# 클래스 메서드

class ClassMethod():

    count = 100
    _protectVar = 'protect'
    __privateVar = 'private'

    @classmethod
    def print_count(cls):
        print('print_count: count: ', cls.count)
        # print('print_count _protectVar: ', cls._protectVar)
        print('print_count __privateVar: ', cls.__privateVar)

    pass

# ClassMethod.print_count()
# ClassMethod.__privateVar


class Singleton(object):
    def __new__(cls, *args, **kwargs):

        # 속성이 존재할때는 이미 존재하는 속성을 리턴
        if hasattr(cls, "_instance"):
            return cls._instance

        # 클래스, 인스턴스(사례), 객체(오브젝트)

        #  obj = JkonClass()

        # cls (클래스 설계)를 토대로 인스턴스 생성
        cls._instance = super().__new__(cls)
        cls._instance.figures = []

        return cls._instance

    def __init__(self):
        # if not hasattr(self, 'figures'):
        #     self.figures = []
        pass

    @classmethod
    def figure(cls):
        fig = time.time()
        cls().figures.append(fig)
        return fig

    @classmethod
    def figureClear(cls):
        cls().figures.clear()
        return cls().figures

    @staticmethod
    def staticMethod(a, b):
        print('total: ', a + b)
        # Singleton()



s1 = Singleton()
# print('s1: ', s1)

s2 = Singleton()
# print('s2: ', s2)

# print('s1: ', s1)
# print('Singleton._instance: ', Singleton._instance)

# Singleton.staticMethod()


fig1 = Singleton.figure()
time.sleep(3)
fig2 = Singleton.figure()

print('fig1: ', fig1)
print('fig2: ', fig2)

print('s1 figures: ', s1.figures)
print('s2 figures: ', s2.figures)

figures = Singleton.figureClear()

print('figures: ', figures)
print('s1 figures: ', s1.figures)
print('s2 figures: ', s2.figures)







