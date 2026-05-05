def bisection():
    def f(x):
        return x**3 - x - 2

    while True:
        a = int(input("Enter your a: "))
        b = int(input("Enter your b: "))
        if (a > b):
            print("a must be less than b")
        else:
            break

    while True:
        c = (a + b) / 2

        ra = f(a)
        rb = f(b)
        rc = f(c)

        if abs(rc) < 0.0005:
            root = c
            break
        elif (ra*rc < 0):
            b = c
        else:
            a = c

    return root

def secant():
    def f(x):
        return x**3 - x - 2

    while True:
        a = float(input("a: "))    
        b = float(input("b: "))    

        if (a > b):
            print("bro just quit math fr")
        else:
            break

    while True:

        ra = f(a) 
        rb = f(b)
        c = ((a * rb) - (b * ra)) / (rb - ra)
        rc = f(c) 

        if abs(rc) < 0.0005:
            root = c
            break
        else:
            a = b
            b = c

    return root

while True:
    print("What u wanna do?")
    user_input = int(input("1. Bisection \n2. Secant \nSelect: "))
    if user_input == 1:
        ans = bisection()
        print("Using Bisection Method!\n")
        print(f"Result = {ans:.4f}")
        break
    else:
        ans = secant()
        print("Using Secant Method!\n")
        print(f"Result = {ans:.4f}")
        break

            