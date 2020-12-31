class dog():

    def __init__(self, name):
        self.name = name
        print(name)

    def add(self,x):
        return x+1
    def bark(self):
        print("bark")
d=dog("Tim")
d.bark()
a=d.add(5)
print(a)
print(type(d))