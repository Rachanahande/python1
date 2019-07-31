from employee import Employee
lstemp = []
def load_emp():
    with open("empdata1.txt") as  f:
        fdata = f.readlines()
        for data in fdata:
            data = data.split(",")
            empno=int(data[0])
            ename=data[1]
            qual=data[2]
            sal=int(data[3])
            dname=data[4]
            emp = Employee(empno,ename,qual,sal,dname)
            lstemp.append(emp)
    print(f"total employee count: {len(lstemp)}")
def showDeptNames():
    dnames = set(map(lambda emp: emp.dname,lstemp))
    for name in dnames:
        print(name)
def showAllQualification():
    quali=set(map(lambda emp: emp.qual,lstemp))
    for qual in quali:
        print(qual)
def maxSalaryEmp():
        max_sal = max(list(map(lambda x:x.sal,lstemp)))
        lst = list(filter(lambda x:x.sal == max_sal,lstemp))
        for emp in lst:
            emp.show_info()

def showEmpCountByDeptName():
    pass
def showTotalSalByDeptName():
    pass
def showEmpCountByQual():
    pass

load_emp()
print("all department names:")
showDeptNames()
print("all qualifications:")
showAllQualification()
