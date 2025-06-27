class Test(object):
    def __init__(self):
        print("I am from constructor") # constructor is callled when object is created 

    def m1(self):
        print("Hello World")
    
x = Test()
x.m1()