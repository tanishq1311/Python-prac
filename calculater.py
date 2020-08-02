tanishq = input("enter the number: ")
swastik = input("enter the operande: ")
diwakar = input("enter the number: ")

if '+' in swastik:
    sum = int(tanishq) + int(diwakar)
    print("adition:" , sum)

if 'x' in swastik:
    sum = int(tanishq) * int(diwakar)
    print("multiplication:" , sum)

if '/' in swastik:
    sum = int(tanishq) / int(diwakar)
    print("division:" , sum)

if '-' in swastik:
    sum = int(tanishq) - int(diwakar)
    print("subtraction:" , sum)

