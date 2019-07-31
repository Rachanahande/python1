class A:
    def __init__(self):
        print(f"A init")
    def show(self):
        print("show of A")
    

class B:
    def __init__(self):
        print(f"B init")
    def show(self):
        print("show of A")

''''class C(A,B):
    def __init__(self):
        print("C init")'''
class C(A,B):
    def showInfo(self):
        print("show info C")

obj = C()




    