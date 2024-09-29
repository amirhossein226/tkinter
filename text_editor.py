import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = tk.Tk()
window.title("Text Editor")
window.rowconfigure(0, weight=1, minsize=800)
window.columnconfigure(1, weight=1, minsize=800)


def open_file():

    file_path = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not file_path:
        return

    text_box.delete("1.0", tk.END)

    with open(file_path, "r") as f:
        text = f.read()
        text_box.insert(tk.END, text)
    window.title(f"Text Editor - {file_path}")


def save_file():
    file_path = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not file_path:
        return
    with open(file_path, "w") as output_file:
        text = text_box.get("1.0", tk.END)
        output_file.write(text)

    window.title(f"Text Editor {file_path}")
    print(file_path)


btn_frame = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=5)

open_btn = tk.Button(master=btn_frame, text="Open", command=open_file)
save_btn = tk.Button(master=btn_frame, text="Save As...", command=save_file)

open_btn.grid(row=0, column=0, sticky="ew", pady=5, padx=5)
save_btn.grid(row=1, column=0, sticky="ew", padx=5)

text_box = tk.Text(master=window, relief=tk.RAISED, borderwidth=5)

btn_frame.grid(row=0, column=0, sticky="ns")
text_box.grid(row=0, column=1, sticky="wens")


window.mainloop()
