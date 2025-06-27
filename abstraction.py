from abc import ABC, abstractmethod
class Father:
    @abstractmethod
    def disp(self):
        pass
    def show(self):
        print("Concrete method in Father class")

class Child(Father):
    def disp(self):
        print("Defining Abstract Method")

x = Child()
x.show()
x.disp()