import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("rootSolve")
root.geometry("1280x720")

root.mainloop()
root.configure(bg="#1e1e1e")

style = ttk.Style()
style.theme_use('clam')
style.configure("TLabel", background="#1e1e1e", foreground="white", font=("Segoe UI", 10))
style.configure("TButton", font=("Segoe UI", 10, "bold"))
style.configure("TLabelframe", background="#1e1e1e", foreground="#58a6ff")
style.configure("TLabelframe.Label", background="#1e1e1e", foreground="#58a6ff", font=("Segoe UI", 10, "bold"))

main_frame = ttk.Frame(root, padding = 20)
main_frame.pack(fill="both", expand=True)

input_frame = ttk.LabelFrame(main_frame, text="Inputs", padding=15)
input_frame.grid(row=0, column=0, sticky="n", padx=(0,20))