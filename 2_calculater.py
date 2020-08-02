i = 1

while i == 1:
    tanishq = input("please enter the number: ")
    swastik = input("please enter the operand: ")
    diwakar = input("please enter the number: ")
    pankaj = input("please enter the operand:")

    if '*' in swastik or pankaj:
        product = int(tanishq) * int(diwakar)

    if '/' in swastik or pankaj:
        quotient = int(tanishq) / int(diwakar)

    if '-' in swastik or pankaj:
        diffrence = int(tanishq) - int(diwakar)

    if '+' in swastik or pankaj:
        daksh = int(tanishq) + int(diwakar)

    if '=' in swastik or pankaj:
        print("multiplication:" , product)
        print("division:" , quotient)
        print("subtraction:" , diffrence)
        print("addition:" , daksh)
        i += 6
    else:
        continue
