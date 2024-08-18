import tkinter as tk
from tkinter import filedialog, messagebox

def upload_file():
    file_path = filedialog.askopenfilename(title="Select an Image File", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        entry_file_name.delete(0, tk.END)
        entry_file_name.insert(0, file_path.split('/')[-1])

def save_file():
    file_name = entry_file_name.get()
    if not file_name:
        messagebox.showerror("Error", "Please enter a file name.")
        return
    
    save_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=file_name)
    if save_path:
        with open(save_path, 'w') as f:
            if text_input.get("1.0", tk.END).strip():
                f.write(text_input.get("1.0", tk.END).strip())
            else:
                messagebox.showerror("Error", "No text input provided.")
        messagebox.showinfo("Success", f"File saved as {save_path}")

app = tk.Tk()
app.title("Image and Text File Packager")

text_input = tk.Text(app, height=10, width=40)
text_input.pack(pady=10)

entry_file_name = tk.Entry(app, width=40)
entry_file_name.pack(pady=10)

btn_upload = tk.Button(app, text="Upload Image", command=upload_file)
btn_upload.pack(pady=5)

btn_save = tk.Button(app, text="Pack and Download", command=save_file)
btn_save.pack(pady=5)

app.mainloop()
