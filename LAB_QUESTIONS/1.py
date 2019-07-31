'''program to find simple interest'''

principle = int(input("enter the principal amount"))
rate = int(input("enter the rate"))
time = float(input("enter the time"))
si = (principle * rate * time)/100
print(f"simple interest is {si}")