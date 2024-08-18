import tkinter as tk
from tkinter import filedialog, Text
import os
import datetime

class MimicOS:
    def __init__(self, root):
        self.root = root
        self.root.title("sigmaOS")
        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>", lambda e: self.root.quit())
        
        self.file_list = []
        self.create_widgets()
        self.update_time()

    def create_widgets(self):
        self.frame = tk.Frame(self.root, bg='lightgray')
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.file_display = tk.Listbox(self.frame, bg='white', font=('Arial', 14))
        self.file_display.pack(fill=tk.BOTH, expand=True)

        self.create_button = tk.Button(self.frame, text="Create File", command=self.create_file)
        self.create_button.pack(side=tk.LEFT)

        self.open_button = tk.Button(self.frame, text="Open File", command=self.open_file)
        self.open_button.pack(side=tk.LEFT)

        self.time_label = tk.Label(self.frame, text="", bg='lightgray', font=('Arial', 12))
        self.time_label.pack(side=tk.BOTTOM)

        self.file_display.bind('<Double-Button-1>', self.view_file)

    def create_file(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if filename:
            with open(filename, 'w') as f:
                f.write("")
            self.file_list.append(filename)
            self.update_file_display()

    def open_file(self):
        filename = filedialog.askopenfilename(filetypes=[("All files", "*.*")])
        if filename:
            if filename.endswith('.exe'):
                os.startfile(filename)
            else:
                self.file_list.append(filename)
                self.update_file_display()

    def view_file(self, event):
        selected_file = self.file_display.get(self.file_display.curselection())
        with open(selected_file, 'r') as f:
            content = f.read()
        self.show_content_window(content)

    def show_content_window(self, content):
        content_window = tk.Toplevel(self.root)
        content_window.title("File Content")
        text_area = Text(content_window)
        text_area.insert(tk.END, content)
        text_area.pack(fill=tk.BOTH, expand=True)
        save_button = tk.Button(content_window, text="Save", command=lambda: self.save_file(content_window, text_area))
        save_button.pack()

    def save_file(self, window, text_area):
        selected_file = self.file_display.get(self.file_display.curselection())
        with open(selected_file, 'w') as f:
            f.write(text_area.get("1.0", tk.END))
        window.destroy()

    def update_file_display(self):
        self.file_display.delete(0, tk.END)
        for file in self.file_list:
            self.file_display.insert(tk.END, file)

    def update_time(self):
        now = datetime.datetime.now()
        self.time_label.config(text=now.strftime("%Y-%m-%d %H:%M:%S"))
        self.root.after(1000, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    app = MimicOS(root)
    root.mainloop()
