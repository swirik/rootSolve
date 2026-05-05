import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math

def f(equation, val):

    safe_dict = {"x": val, "math": math, "sin": math.sin, "cos": math.cos, 
                 "exp": math.exp, "log": math.log, "sqrt": math.sqrt}
    return eval(equation.replace("^", "**"), safe_dict)

def get_f_prime(equation, x):
    h = 1e-7
    return (f(equation, x + h) - f(equation, x)) / h

def solve_logic(event=None):
    try:
        eq = user_input_equation.get()
        method = method_selector.get()
        
        if not eq:
            messagebox.showwarning("Input Error", "Input must not be empty")
            return

        for widget in results_inner_frame.winfo_children():
            widget.destroy()

        valid, a, b = a_and_b(eq)
        if not valid: return

        # Headers logic
        headers = f"{'N':<5} {'A':<10} {'B':<10} {'C':<10} {'F(C)':<10}"
        if method in ["Fixed Point", "Newton Raphson"]:
            headers = f"{'N':<5} {'X_old':<10} {'F(X)':<10} {'X_new':<10}"
        
        ttk.Label(results_inner_frame, text=headers, font=mono_font, foreground="#58a6ff").grid(column=0, row=0, sticky="w")

        for n in range(1, 25):
            if method == "Bisection":
                c = (a + b) / 2
                fc = f(eq, c)
                row_output = f"{n:<5} {a:<10.4f} {b:<10.4f} {c:<10.4f} {fc:<10.4f}"
                if f(eq, a) * fc < 0: b = c
                else: a = c

            elif method == "Secant":
                fa, fb = f(eq, a), f(eq, b)
                if fb - fa == 0: break
                c = b - (fb * (b - a)) / (fb - fa)
                fc = f(eq, c)
                row_output = f"{n:<5} {a:<10.4f} {b:<10.4f} {c:<10.4f} {fc:<10.4f}"
                a, b = b, c

            elif method == "Fixed Point":

                fx = f(eq, a)
                x_new = a - fx
                row_output = f"{n:<5} {a:<10.4f} {fx:<10.4f} {x_new:<10.4f}"
                fc = fx 
                a = x_new

            elif method == "False Position":
                fa, fb = f(eq, a), f(eq, b)
                c = (a * fb - b * fa) / (fb - fa)
                fc = f(eq, c)
                row_output = f"{n:<5} {a:<10.4f} {b:<10.4f} {c:<10.4f} {fc:<10.4f}"
                if fa * fc < 0: b = c
                else: a = c

            elif method == "Newton Raphson":
                fx = f(eq, a)
                dfx = get_f_prime(eq, a)
                if dfx == 0: break
                x_new = a - (fx / dfx)
                row_output = f"{n:<5} {a:<10.4f} {fx:<10.4f} {x_new:<10.4f}"
                fc = fx 
                a = x_new


            ttk.Label(results_inner_frame, text=row_output, font=mono_font).grid(column=0, row=n, sticky="w")
            
            if abs(fc) < 0.0005:
                root_msg = f"Root is approximately: {a if method in ['Fixed Point', 'Newton Raphson'] else c:.4f}"
                ttk.Label(results_inner_frame, text=root_msg, font=("Consolas", 11, "bold"), foreground="#afff33").grid(column=0, row=n+2, sticky="w")
                break

    except Exception as e:
        messagebox.showerror("Math Error", f"Check your equation syntax: {e}")

def a_and_b(equation):
    try:
        a_val = user_input_a.get()
        b_val = user_input_b.get()
        if not a_val or not b_val:
            messagebox.showwarning("Input Error", "Please fill in A and B")
            return False, 0, 0
        a, b = float(a_val), float(b_val)
        

        if method_selector.get() in ["Bisection", "False Position"]:
            if f(equation, a) * f(equation, b) >= 0:
                messagebox.showerror("Error", "f(a) and f(b) must have opposite signs!")
                return False, 0, 0
        return True, a, b
    except ValueError:
        messagebox.showwarning("Input Error", "Please Enter Numeric Values")
        return False, 0, 0


root = tk.Tk()
root.bind('<Return>', solve_logic)
root.title("rootSolve Pro")
root.geometry("1100x700")
root.configure(bg="#1e1e1e")

style = ttk.Style()
style.theme_use('clam')
style.configure("TFrame", background="#1e1e1e")
style.configure("TLabel", background="#1e1e1e", foreground="white", font=("Segoe UI", 10))
style.configure("TLabelframe", background="#1e1e1e", foreground="#58a6ff")
style.configure("TLabelframe.Label", background="#1e1e1e", foreground="#58a6ff", font=("Segoe UI", 10, "bold"))

mono_font = ("Consolas", 11)

main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill="both", expand=True)


input_frame = ttk.LabelFrame(main_frame, text=" Parameters ", padding=15)
input_frame.grid(row=0, column=0, sticky="n", padx=(0,20))

ttk.Label(input_frame, text="Method").grid(row=0, column=0, sticky="w")
method_selector = ttk.Combobox(input_frame, values=["Bisection", "Secant", "Fixed Point", "False Position", "Newton Raphson"], state="readonly")
method_selector.current(0)
method_selector.grid(row=1, column=0, pady=(0, 15), sticky="ew")

ttk.Label(input_frame, text="Equation (e.g., x**2 - 4)").grid(row=2, column=0, sticky="w")
user_input_equation = ttk.Entry(input_frame, width=30)
user_input_equation.grid(row=3, column=0, pady=(0, 15))

ttk.Label(input_frame, text="A (or Initial Guess)").grid(row=4, column=0, sticky="w")
user_input_a = ttk.Entry(input_frame, width=30)
user_input_a.grid(row=5, column=0, pady=(0, 15))

ttk.Label(input_frame, text="B").grid(row=6, column=0, sticky="w")
user_input_b = ttk.Entry(input_frame, width=30)
user_input_b.grid(row=7, column=0, pady=(0, 20))

ttk.Button(input_frame, text="CALCULATE", command=solve_logic).grid(row=8, column=0, pady=5, sticky="ew")
ttk.Button(input_frame, text="EXIT", command=root.destroy).grid(row=9, column=0, pady=5, sticky="ew")


results_container = ttk.LabelFrame(main_frame, text=" Output Log ", padding=15)
results_container.grid(row=0, column=1, sticky="nsew")
main_frame.columnconfigure(1, weight=1)

results_inner_frame = ttk.Frame(results_container)
results_inner_frame.pack(fill="both", expand=True)

root.mainloop()