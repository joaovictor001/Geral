class Super:
    def __init__(self):
        pass
    
    def hello(self):
        print("Salve salve sou a super classe")

class Sub(Super):
    def __init__(self):
        pass

    def hello(self):
        print("Salve salve sou a Sub classe")

class Subsub(Sub):
    def __init__(self):
        pass

    def hello(self):
        print("Salve salve sou a Subsub classe")

super1 = Super()

super1.hello()

sub1 = Sub()

sub1.hello()