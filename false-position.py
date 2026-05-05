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
    elif ra*rc < 0:
        b = c
    else:
        a = c


print(f"The root is = {c:.4f}")




