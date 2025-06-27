class Father:
    def showf(self):
        print("Parent class Instance Method")


class Son(Father):
    def shows(self):
        print("Child clss Instance Methosd")

class GrandSon(Son):
    def showg(self):
        print("Grand Child class Instance Method")

s = GrandSon()
s.showf()
s.shows()
s.showg()
