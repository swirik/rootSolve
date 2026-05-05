import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def f(equation, val):
    return eval(equation.replace("x", f"({val})"))

def equation(event=None):
    try:
        eq = user_input_equation.get().replace("^", "**")
        if not eq:
            messagebox.showwarning("Input Error", "Input must not be empty")
            return

        valid, a, b = a_and_b(eq)

        if valid:

            column_headers = f"{'n':<5} {'A':<10} {'B':<10} {'C':<10} {'F(A)':<10} {'F(B)':<10} {'F(C)':<10}"
            ttk.Label(frame, text=column_headers, font=mono_font).grid(column = 2, row = 0)

            for n in range(1, 25):
                c = (a + b) / 2
                fc = f(eq, c)
                fb = f(eq, b)
                fa = f(eq, a)
                row_output= f"{n:<5} {a:<10.4f} {b:<10.4f} {c:<10.4f} {fa:<10.4f} {fb:<10.4f} {fc:<10.4f}"
                
                ttk.Label(frame, text=row_output, font=mono_font).grid(column=2, row=n, padx=10, sticky="w")

                if abs(fc) < 0.0005: 
                    break
                if fa * fc < 0: 
                    b = c
                else: 
                    a = c
    except Exception as e:
        print(f"An unexpected error occured {e}")    

def a_and_b(equation):
    try:
        a = float(user_input_a.get())
        b = float(user_input_b.get())

        if not a or not b:
            messagebox.showwarning("Input Error", "Please fill in A and B")
            return False,0,0

        if f(equation, a) * f(equation, b) >= 0:
            messagebox.showerror("Error", "f(a) and f(b) must have opposite signs!")
            return False,0,0
        if abs(b - a) > 10:
            response = messagebox.askyesno("Are you sure?", "Large Interval detected. Continue?" )
            if not response:
                return False,0,0
        return True, a, b
    except ValueError:
        messagebox.showwarning("Input Error", "Please Enter Numeric Values")
        return False,0,0
    except ZeroDivisionError:
        print("Error: Division by zero")
        return False,0,0

root = tk.Tk()
root.bind('<Return>', equation)
root.title("rootSolve")
root.geometry("1280x720")
root.configure(bg="#1e1e1e")

style = ttk.Style()
style.theme_use('clam')
frame = ttk.Frame(root, padding=10)
frame.grid()
mono_font = ("Courier New", 10)

user_input_equation = ttk.Entry(frame)
ttk.Label(frame, text="Type Equation Here").grid(column=0, row=2)
user_input_equation.grid(column=0, row=3)

user_input_a = ttk.Entry(frame)
ttk.Label(frame, text="Enter A here").grid(column=0, row=4)
user_input_a.grid(column=0, row=5)

user_input_b = ttk.Entry(frame)
ttk.Label(frame, text="Enter B here").grid(column=0, row=6)
user_input_b.grid(column=0, row =7)
    
ttk.Button(frame, text="Calculate", command=equation).grid(column=0, row=9)
ttk.Button(frame, text="Exit",  command=root.destroy).grid(column=0, row=10)



root.mainloop()

