import tkinter as tk
from parse import parser
from lexical import lexical

def parse():
    parser(string.get())
    
def lex():
    lexical(string.get())

root = tk.Tk()
root.title("TUBES TBA")

# Mengatur ukuran jendela
window_width = 700
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width // 2) - (window_width // 2)
y_position = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Membuat label dan entry untuk inputan
input_label = tk.Label(root, text="Masukkan string:")
input_label.grid(row=0, column=0, sticky=tk.W)
string = tk.Entry(root, width= 60)
string.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

# Membuat tombol "Hitung"
parse_button = tk.Button(root, text="Parse", command=parse)
parse_button.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

# Membuat label untuk menampilkan hasil
parse_label = tk.Label(root, text="Hasil Parse:")
parse_label.grid(row=2, column=0, padx=5, sticky=tk.W)  # Menempatkan di baris 1, kolom 0 dengan penempelan di sebelah kiri
parse_output_text = tk.Text(root, height=5, width=60)  # Mengatur tinggi dan lebar area output
parse_output_text.grid(row=2, column=1, padx=5, sticky=tk.W)

# Membuat label untuk menampilkan hasil
la_label = tk.Label(root, text="Hasil Lexical Analysis:")
la_label.grid(row=3, column=0, padx=5, sticky=tk.W)  # Menempatkan di baris 1, kolom 0 dengan penempelan di sebelah kiri


# Menjalankan loop utama Tkinter
root.mainloop()

# def main():
    

# if __name__ == "__main__":
#     main()