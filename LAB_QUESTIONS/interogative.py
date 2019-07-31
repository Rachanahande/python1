while True:
    inp = input("enter the string")
    if inp == 'done':
        break
    else:
        if inp.endswith('?'):
            print("interogative statements")
        else:
            print("assert")