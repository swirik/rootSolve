import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# import sv_ttk 

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
            ttk.Label(results_inner_frame, text=column_headers, font=mono_font, foreground="#58a6ff").grid(column=0, row=0, sticky="w")
            
            for n in range(1, 25):
                c = (a + b) / 2
                fc = f(eq, c)
                fb = f(eq, b)
                fa = f(eq, a)
                row_output= f"{n:<5} {a:<10.4f} {b:<10.4f} {c:<10.4f} {fa:<10.4f} {fb:<10.4f} {fc:<10.4f}"
                
                ttk.Label(results_inner_frame, text=row_output, font=mono_font).grid(column=0, row=n, sticky="w")
                
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
            return False, 0, 0
        if f(equation, a) * f(equation, b) >= 0:
            messagebox.showerror("Error", "f(a) and f(b) must have opposite signs!")
            return False, 0, 0
        if abs(b - a) > 10:
            response = messagebox.askyesno("Are you sure?", "Large Interval detected. Continue?" )
            if not response:
                return False, 0, 0
        return True, a, b
    except ValueError:
        messagebox.showwarning("Input Error", "Please Enter Numeric Values")
        return False, 0, 0
    except ZeroDivisionError:
        return False, 0, 0

root = tk.Tk()
root.bind('<Return>', equation)
root.title("rootSolve Pro")
root.geometry("1100x700")
root.configure(bg="#1e1e1e") # Dark background

style = ttk.Style()
style.theme_use('clam') 
style.configure("TFrame", background="#1e1e1e")
style.configure("TLabel", background="#1e1e1e", foreground="white", font=("Segoe UI", 10))
style.configure("TButton", font=("Segoe UI", 10, "bold"))
style.configure("TLabelframe", background="#1e1e1e", foreground="#58a6ff")
style.configure("TLabelframe.Label", background="#1e1e1e", foreground="#58a6ff", font=("Segoe UI", 10, "bold"))

mono_font = ("Consolas", 11)

# Main container
main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill="both", expand=True)

# Left Side: Inputs
input_container = ttk.LabelFrame(main_frame, text=" Parameters ", padding=15)
input_container.grid(row=0, column=0, sticky="n", padx=(0, 20))

ttk.Label(input_container, text="Equation (use 'x')").grid(row=0, column=0, sticky="w", pady=(0, 5))
user_input_equation = ttk.Entry(input_container, width=30)
user_input_equation.grid(row=1, column=0, pady=(0, 15))

ttk.Label(input_container, text="Lower Bound (A)").grid(row=2, column=0, sticky="w", pady=(0, 5))
user_input_a = ttk.Entry(input_container, width=30)
user_input_a.grid(row=3, column=0, pady=(0, 15))

ttk.Label(input_container, text="Upper Bound (B)").grid(row=4, column=0, sticky="w", pady=(0, 5))
user_input_b = ttk.Entry(input_container, width=30)
user_input_b.grid(row=5, column=0, pady=(0, 20))

calc_btn = ttk.Button(input_container, text="CALCULATE", command=equation)
calc_btn.grid(row=6, column=0, pady=5, sticky="ew")

exit_btn = ttk.Button(input_container, text="EXIT", command=root.destroy)
exit_btn.grid(row=7, column=0, pady=5, sticky="ew")

# Right Side: Results
results_container = ttk.LabelFrame(main_frame, text=" Bisection Iterations ", padding=15)
results_container.grid(row=0, column=1, sticky="nsew")
main_frame.columnconfigure(1, weight=1)

results_inner_frame = ttk.Frame(results_container)
results_inner_frame.pack(fill="both", expand=True)

# Optional: If you want the "sv_ttk" modern look, uncomment below:
# sv_ttk.set_theme("dark")

root.mainloop()