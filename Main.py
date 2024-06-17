import tkinter as tk
from SentenceParser import parser

def check_sentence():
    structure_output.delete("1.0", tk.END)
    status_output.delete("1.0", tk.END)

    sentence = input_text.get("1.0", tk.END).strip()
    
    is_valid, structure = parser(sentence)
    
    structure_output.insert(tk.END, ' - '.join(structure))
    status_output.insert(tk.END, 'Accepted ✅' if is_valid else 'Rejected ❌')

# Setup GUI
root = tk.Tk()
root.title("Tubes TBA - Sentence Parser")

window_width = 600
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width // 2) - (window_width // 2)
y_position = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

input_label = tk.Label(root, text="Input Kalimat:")
input_label.grid(row=0, column=0, sticky=tk.W)
input_text = tk.Text(root, height=5, width=60)
input_text.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

process_button = tk.Button(root, text="Check", command=check_sentence)
process_button.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

structure_label = tk.Label(root, text="Struktur:")
structure_label.grid(row=2, column=0, padx=5, sticky=tk.W)
structure_output = tk.Text(root, height=5, width=60)
structure_output.grid(row=2, column=1, padx=5, sticky=tk.W)

status_label = tk.Label(root, text="Status:")
status_label.grid(row=3, column=0, padx=5, sticky=tk.W) 
status_output = tk.Text(root, height=5, width=60)
status_output.grid(row=3, column=1, padx=5, sticky=tk.W)

root.mainloop()
