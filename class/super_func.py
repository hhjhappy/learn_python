'''
演示super函数的继承功能,super函数可以继承父类的单独函数
'''
class Cla(object):
    """docstring for class"""
    def __init__(self, arg):
        self.arg = arg

    def echo_message(self):
        print(self.arg)

class Clb(Cla):
    def __init__(self,par):
        super().__init__(par)

    def test_super(self):
        super().echo_message(self.par)


ccc = Clb('ffasdf')
ccc.echo_message()





        