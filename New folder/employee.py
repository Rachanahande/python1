class Employee:
    def __init__(self,empno,ename,qual,sal,dname):
        self.empno=empno
        self.ename=ename
        self.qual=qual
        self.sal=sal
        self.dname=dname
    def show_info(self):
        print(f"{self.empno} - {self.ename} - {self.qual} - {self.sal} - {self.dname}")
    
    def incr_sal(self,inc_amt):
        self.sal+=inc_amt
        print(f"{self.ename} after the increament {self.sal}")