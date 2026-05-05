import math

def get_f(expr):
    return lambda x: eval(expr, {"x": x, "math": math, "sin": math.sin, "cos": math.cos, "exp": math.exp, "log": math.log, "sqrt": math.sqrt})

def get_f_prime(f):
    h = 1e-7
    return lambda x: (f(x + h) - f(x)) / h

while True:
    print("\n[1] Continue\n[2] Exit")
    if input("> ") != '1':
        break

    expr = input("Enter expression (use 'math.sin(x)' etc): ")
    a = float(input("Enter (a): "))
    b = float(input("Enter (b): "))
    
    f = get_f(expr)
    f_prime = get_f_prime(f)

    print("\n[1] Bisection\n[2] Secant\n[3] Fixed Point\n[4] False Position\n[5] Newton Raphson\n[6] Exit")
    method = input("> ")

    if method == '1':
        fa, fb = f(a), f(b)
        if fa * fb >= 0:
            print("Fail: No bracket.")
            continue
        print(f"{'N':<5} {'A':<10} {'B':<10} {'C':<10} {'f(C)':<10}")
        for n in range(1, 16):
            c = (a + b) / 2
            fc = f(c)
            print(f"{n:<5} {a:<10.4f} {b:<10.4f} {c:<10.4f} {fc:<10.4f}")
            if abs(fc) < 0.0005: break
            if f(a) * fc < 0: b = c
            else: a = c

    elif method == '2':
        print(f"{'N':<5} {'A':<10} {'B':<10} {'C':<10} {'f(C)':<10}")
        for n in range(1, 16):
            fa, fb = f(a), f(b)
            if fb - fa == 0: break
            c = b - (fb * (b - a)) / (fb - fa)
            fc = f(c)
            print(f"{n:<5} {a:<10.4f} {b:<10.4f} {c:<10.4f} {fc:<10.4f}")
            if abs(fc) < 0.0005: break
            a, b = b, c

    elif method == '3':
        x = (a + b) / 2
        print("Note: Using x = g(x) logic via user input needed for true Fixed Point.")
        print(f"{'N':<5} {'X':<10} {'f(X)':<10}")
        for n in range(1, 16):
            fx = f(x)
            print(f"{n:<5} {x:<10.4f} {fx:<10.4f}")
            if abs(fx) < 0.0005: break
            x = x - fx 

    elif method == '4':
        fa, fb = f(a), f(b)
        if fa * fb >= 0:
            print("Fail: No bracket.")
            continue
        print(f"{'N':<5} {'A':<10} {'B':<10} {'C':<10} {'f(C)':<10}")
        for n in range(1, 16):
            fa, fb = f(a), f(b)
            c = (a * fb - b * fa) / (fb - fa)
            fc = f(c)
            print(f"{n:<5} {a:<10.4f} {b:<10.4f} {c:<10.4f} {fc:<10.4f}")
            if abs(fc) < 0.0005: break
            if fa * fc < 0: b = c
            else: a = c

    elif method == '5':
        x = (a + b) / 2
        print(f"{'N':<5} {'X_old':<10} {'f(X)':<10} {'X_new':<10}")
        for n in range(1, 16):
            fx = f(x)
            dfx = f_prime(x)
            if dfx == 0: break
            x_new = x - (fx / dfx)
            print(f"{n:<5} {x:<10.4f} {fx:<10.4f} {x_new:<10.4f}")
            if abs(fx) < 0.0005: break
            x = x_new