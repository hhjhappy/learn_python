class test_class(object):
    def __init__(self,pra,prab = {}):
        self.pra = pra
        self.prab = prab

    def sing_test(self):
        print(self.pra)
        print(self.prab.a)
        # print(self.prab)
        # print(type(self.prab))
        for k,v in self.prab.items():
            print(k,v)

class Animal(object):
    pass

class Dog(object):
    def __init__(self,name):
        self.name = name

class Cat(object):
    def __init__(self,name):
        self.name = name

class Person(object):
    def __init__(self,name):
        self.name = name
        print(self.name)
        # print(self.__name__)

    def echo_message(self,nameb):
        print(nameb)

class Employee(Person):
    def __init__(self,name):
        # self.name = name
        super().echo_message(name)
        # print(self.__name__())

Employee('fff')


# ff = test_class('aaaa',{'ff':1})
# ff.sing_test()