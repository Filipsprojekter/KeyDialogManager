import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(initialdir="C:/Users/user/Documents/Noter", title="Vælg fil",
                                       filetypes=(("Text File", "*.txt"),))

with open(file_path) as txtfile:
    text = txtfile.read()
    print("Key:")
    print(text)

input("Click any button to quit")
