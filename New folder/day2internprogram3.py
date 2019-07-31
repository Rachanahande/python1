import random as r
num = []
for n in range(20):
    num.append(r.randint(1,50))
res=[max(num),min(num)]
print(res)