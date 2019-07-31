str = "In another two months time, I will be good at python programming"
for ch in str:
    if ch in ['a','e','i','o','u']:
        str = str.replace(ch ,' ')
print(str)