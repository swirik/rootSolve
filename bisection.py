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
        

print ("root is = ", root)