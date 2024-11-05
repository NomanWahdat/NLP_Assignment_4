import tkinter as tk
from tkinter import ttk, messagebox
from tasks import (edit_distance, traceback_operations, weighted_edit_distance, 
                   phonetic_edit_distance, needleman_wunsch, traceback_nw)

def run_edit_distance():
    s1 = str1_entry.get()
    s2 = str2_entry.get()
    if not s1 or not s2:
        messagebox.showwarning("Input Error", "Please enter both strings.")
        return
    dp, traceback_matrix = edit_distance(s1, s2)
    operations = traceback_operations(traceback_matrix, s1, s2)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Edit Distance Operations:\n")
    for op in operations:
        result_text.insert(tk.END, op + "\n")

def run_weighted_edit_distance():
    s1 = str1_entry.get()
    s2 = str2_entry.get()
    if not s1 or not s2:
        messagebox.showwarning("Input Error", "Please enter both strings.")
        return
    try:
        insert_cost = int(insert_cost_entry.get())
        delete_cost = int(delete_cost_entry.get())
        substitute_cost = int(substitute_cost_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Costs must be integers.")
        return
    dp = weighted_edit_distance(s1, s2, insert_cost, delete_cost, substitute_cost)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Weighted Edit Distance Table:\n")
    for row in dp:
        result_text.insert(tk.END, str(row) + "\n")

def run_phonetic_distance():
    s1 = str1_entry.get()
    s2 = str2_entry.get()
    if not s1 or not s2:
        messagebox.showwarning("Input Error", "Please enter both strings.")
        return
    distance = phonetic_edit_distance(s1, s2)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"Phonetic Edit Distance: {distance}\n")

def run_needleman_wunsch():
    s1 = str1_entry.get()
    s2 = str2_entry.get()
    if not s1 or not s2:
        messagebox.showwarning("Input Error", "Please enter both strings.")
        return
    dp, traceback_matrix = needleman_wunsch(s1, s2)
    alignment1, alignment2 = traceback_nw(traceback_matrix, s1, s2)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Needleman-Wunsch Alignment:\n")
    result_text.insert(tk.END, alignment1 + "\n")
    result_text.insert(tk.END, alignment2 + "\n")

# GUI setup
root = tk.Tk()
root.title("Edit Distance and Sequence Alignment")
root.geometry("800x600")  # Set a fixed window size
root.configure(bg='black')

# Styling
style = ttk.Style()
style.configure("TFrame", background="black")
style.configure("TLabel", background="black", foreground="white", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))
style.configure("TText", font=("Arial", 12))

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Input fields
ttk.Label(frame, text="String 1:").grid(row=0, column=0, sticky=tk.W)
str1_entry = ttk.Entry(frame, width=40)
str1_entry.grid(row=0, column=1)

ttk.Label(frame, text="String 2:").grid(row=1, column=0, sticky=tk.W)
str2_entry = ttk.Entry(frame, width=40)
str2_entry.grid(row=1, column=1)

# Buttons
button_frame = ttk.Frame(frame, padding=(0, 5))
button_frame.grid(row=2, columnspan=2)

ttk.Button(button_frame, text="Run Edit Distance", command=run_edit_distance).grid(row=0, column=0, sticky=tk.W, padx=5)
ttk.Button(button_frame, text="Run Weighted Edit Distance", command=run_weighted_edit_distance).grid(row=0, column=1, sticky=tk.W, padx=5)
ttk.Button(button_frame, text="Run Phonetic Distance", command=run_phonetic_distance).grid(row=0, column=2, sticky=tk.W, padx=5)
ttk.Button(button_frame, text="Run Needleman-Wunsch", command=run_needleman_wunsch).grid(row=0, column=3, sticky=tk.W, padx=5)

# Custom weights input
weight_frame = ttk.Frame(frame, padding=(0, 10))
weight_frame.grid(row=3, columnspan=2)

ttk.Label(weight_frame, text="Insert Cost:").grid(row=0, column=0, sticky=tk.W)
insert_cost_entry = ttk.Entry(weight_frame, width=5)
insert_cost_entry.insert(0, "1")
insert_cost_entry.grid(row=0, column=1, sticky=tk.W)

ttk.Label(weight_frame, text="Delete Cost:").grid(row=1, column=0, sticky=tk.W)
delete_cost_entry = ttk.Entry(weight_frame, width=5)
delete_cost_entry.insert(0, "1")
delete_cost_entry.grid(row=1, column=1, sticky=tk.W)

ttk.Label(weight_frame, text="Substitute Cost:").grid(row=2, column=0, sticky=tk.W)
substitute_cost_entry = ttk.Entry(weight_frame, width=5)
substitute_cost_entry.insert(0, "1")
substitute_cost_entry.grid(row=2, column=1, sticky=tk.W)

# Output area
result_text = tk.Text(frame, height=15, width=80, wrap=tk.WORD, bg='white', fg='black')
result_text.grid(row=4, column=0, columnspan=2, pady=10)

# Padding around the window
for i in range(5):
    frame.grid_rowconfigure(i, weight=1)

# Run the GUI loop
root.mainloop()
