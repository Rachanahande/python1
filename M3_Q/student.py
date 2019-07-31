class A:
    def __init__(self):
        print(f"{self.__class__.__name__}")
class B(A):
    def __init__(self):
        print(f"{self.__class__.__name__}")

b=B()
    

