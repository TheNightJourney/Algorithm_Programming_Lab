x = int(input("Enter the number: "))

variable = True

if x > 1:
    for i in range(2,x):
        if (x % i) == 0:
            variable = False
            break

if variable:
    print(bool(x))
else:
    print(bool(variable))