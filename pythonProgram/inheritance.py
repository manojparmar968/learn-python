class abc:
    def __init__(self,name,age):
        self.name=name
        self.age = age

    def printname(self):
        print(self.name,self.age)

class Person(abc):
    def __init__(self,name,age):
        super().__init__(name,age)


x=Person("manoj",89)
x.printname()

y=abc("person",78)
y.printname()   