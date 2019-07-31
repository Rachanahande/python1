lb = int(input("enter the lower bound "))
ub = int(input("enter the upper bound"))
res  = " ".join([i for i in range(lb,ub+1) if i%9 == 0 and i %5 !=0])
print(res)