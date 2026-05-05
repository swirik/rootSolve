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


print("The root is = ", c)




