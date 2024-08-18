import tkinter as tk
from tkinter import filedialog, messagebox
import os

class HTMLFileEditor:
    def __init__(self, master):
        self.master = master
        master.title("HTML File Editor")

        self.text_area = tk.Text(master, wrap='word')
        self.text_area.pack(expand=True, fill='both')

        self.load_button = tk.Button(master, text="Load HTML File", command=self.load_file)
        self.load_button.pack(side='left')

        self.done_button = tk.Button(master, text="Done", command=self.save_file)
        self.done_button.pack(side='right')

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("HTML files", "*.html")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)

    def save_file(self):
        edited_content = self.text_area.get(1.0, tk.END)
        save_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML files", "*.html")])
        if save_path:
            with open(save_path, 'w', encoding='utf-8') as file:
                file.write(edited_content)
            messagebox.showinfo("Success", "File saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    editor = HTMLFileEditor(root)
    root.mainloop()
