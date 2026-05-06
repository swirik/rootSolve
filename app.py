import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math

def f(eq, val):
    conversion = {
        "x": val,  # key:value pairs
        "log": math.log, 
        "sqrt": math.sqrt }
    return eval(eq.replace("^", "**"), conversion)

def get_f_prime(eq, x): 
    h = 1e-7 # approximation to up to 6-7 decimal places
    return (f(eq, x + h) - f(eq, x)) / h # derive

def hide_g_input(*args):
    if methods.get() == "Fixed Point":
        label_g.grid(row=4, column=0, sticky="w")
        user_input_g.grid(row=5, column=0, pady=(0, 10))
    else:
        label_g.grid_remove()
        user_input_g.grid_remove()

def solve(event=None):
    try:
        eq_f = user_input_equation.get()
        eq_g = user_input_g.get()
        method = methods.get()
        
        if not eq_f:
            messagebox.showwarning("Input Error", "Equation must not be empty")
            return

        for widget in results_inner_frame.winfo_children():
            widget.destroy()

        valid, a, b = a_and_b(eq_f)
        if not valid: return

        headers = f"{'N':<5} {'A':<10} {'B':<10} {'C':<10} {'F(C)':<10}"
        if method in ["Fixed Point", "Newton Raphson"]:
            headers = f"{'N':<5} {'X_old':<10} {'F(X)':<10} {'X_new':<10}"
        
        ttk.Label(results_inner_frame, text=headers, font=mono_font, foreground="#58a6ff").grid(column=0, row=0, sticky="w")

        curr_a, curr_b = a, b
        x_val = (a + b) / 2

        for n in range(1, 25):
            if method == "Bisection":
                c = (curr_a + curr_b) / 2
                fc = f(eq_f, c)
                row_output = f"{n:<5} {curr_a:<10.4f} {curr_b:<10.4f} {c:<10.4f} {fc:<10.4f}"
                if f(eq_f, curr_a) * fc < 0: curr_b = c
                else: curr_a = c
                conv_val = fc

            elif method == "Secant":
                fa, fb = f(eq_f, curr_a), f(eq_f, curr_b)
                if fb - fa == 0: break
                c = curr_b - (fb * (curr_b - curr_a)) / (fb - fa)
                fc = f(eq_f, c)
                row_output = f"{n:<5} {curr_a:<10.4f} {curr_b:<10.4f} {c:<10.4f} {fc:<10.4f}"
                curr_a, curr_b = curr_b, c
                conv_val = fc

            elif method == "Fixed Point":
                if not eq_g:
                    messagebox.showwarning("Input Error", "Fixed Point requires g(x)")
                    return
                dg = (f(eq_g, x_val + 1e-7) - f(eq_g, x_val)) / 1e-7
                if n == 1 and abs(dg) >= 1:
                    messagebox.showwarning("Warning", f"|g'(x)| = {abs(dg):.4f} >= 1. May diverge.")
                x_new = f(eq_g, x_val)
                row_output = f"{n:<5} {x_val:<10.4f} {f(eq_f, x_val):<10.4f} {x_new:<10.4f}"
                conv_val = f(eq_f, x_new)
                x_val = x_new

            elif method == "False Position":
                fa, fb = f(eq_f, curr_a), f(eq_f, curr_b)
                c = (curr_a * fb - curr_b * fa) / (fb - fa)
                fc = f(eq_f, c)
                row_output = f"{n:<5} {curr_a:<10.4f} {curr_b:<10.4f} {c:<10.4f} {fc:<10.4f}"
                if fa * fc < 0: curr_b = c
                else: curr_a = c
                conv_val = fc

            elif method == "Newton Raphson":
                fx = f(eq_f, x_val)
                dfx = get_f_prime(eq_f, x_val)
                if dfx == 0: break
                x_new = x_val - (fx / dfx)
                row_output = f"{n:<5} {x_val:<10.4f} {fx:<10.4f} {x_new:<10.4f}"
                conv_val = fx
                x_val = x_new

            ttk.Label(results_inner_frame, text=row_output, font=mono_font).grid(column=0, row=n, sticky="w")
            
            if abs(conv_val) < 0.0005:
                res_val = x_val if method in ["Fixed Point", "Newton Raphson"] else c
                root_msg = f"Root is approximately: {res_val:.4f}"
                ttk.Label(results_inner_frame, text=root_msg, font=("Consolas", 11, "bold"), foreground="#afff33").grid(column=0, row=n+2, sticky="w")
                break

    except Exception as e:
        messagebox.showerror("Math Error", str(e))

def a_and_b(equation):
    try:
        av, bv = user_input_a.get(), user_input_b.get()
        if not av or not bv:
            messagebox.showwarning("Input Error", "Fill A and B")
            return False, 0, 0
        a, b = float(av), float(bv)
        if methods.get() in ["Bisection", "False Position"]:
            if f(equation, a) * f(equation, b) >= 0:
                messagebox.showerror("Error", "f(a) and f(b) must have opposite signs!")
                return False, 0, 0
        return True, a, b
    except ValueError:
        messagebox.showwarning("Input Error", "Enter Numeric Values")
        return False, 0, 0



root = tk.Tk()
root.bind('<Return>', solve)
root.title("rootSolve")
root.geometry("1200x800")
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

input_frame = ttk.LabelFrame(main_frame, text=" Inputs ", padding=15)
input_frame.grid(row=0, column=0, sticky="n", padx=(0,20))

ttk.Label(input_frame, text="Method").grid(row=0, column=0, sticky="w")

methods = tk.StringVar()
methods.trace_add("write", hide_g_input)

method_selector = ttk.Combobox(input_frame, textvariable=methods, values=["Bisection", "Secant", "Fixed Point", "False Position", "Newton Raphson"], state="readonly")
method_selector.current(0)
method_selector.grid(row=1, column=0, pady=(0, 10), sticky="ew")

ttk.Label(input_frame, text="f(x) Equation").grid(row=2, column=0, sticky="w")
user_input_equation = ttk.Entry(input_frame, width=30)
user_input_equation.grid(row=3, column=0, pady=(0, 10))

label_g = ttk.Label(input_frame, text="g(x)")
user_input_g = ttk.Entry(input_frame, width=30)

ttk.Label(input_frame, text="A (Lower Limit)").grid(row=6, column=0, sticky="w")
user_input_a = ttk.Entry(input_frame, width=30)
user_input_a.grid(row=7, column=0, pady=(0, 10))

ttk.Label(input_frame, text="B (Upper Limit)").grid(row=8, column=0, sticky="w")
user_input_b = ttk.Entry(input_frame, width=30)
user_input_b.grid(row=9, column=0, pady=(0, 15))    

ttk.Button(input_frame, text="CALCULATE", command=solve).grid(row=10, column=0, pady=5, sticky="ew")
ttk.Button(input_frame, text="EXIT", command=root.destroy).grid(row=11, column=0, pady=5, sticky="ew")

results_container = ttk.LabelFrame(main_frame, text=" Output ", padding=15)
results_container.grid(row=0, column=1, sticky="nsew")
main_frame.columnconfigure(1, weight=1)

results_inner_frame = ttk.Frame(results_container)
results_inner_frame.pack(fill="both", expand=True)

hide_g_input()

root.mainloop()