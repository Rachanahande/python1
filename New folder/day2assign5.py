'''5.	Write a program to add the elements of 2 arrays that are of the same dimension'''
l1 = [1,2,3,4]
l2 = [5,6,7,8]
l3 = list(map(lambda x,y: x+y,l1,l2))
print(f"after adding l1{l1} and l2 {l2} is {l3}")
