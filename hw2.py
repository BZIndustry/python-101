import tkinter as tk
from tkinter import ttk

# สร้างหน้าต่าง
window = tk.Tk()
window.title("My GUI")
window.geometry("400x400")

# Label
label = tk.Label(window, text="Hello, World!")
label.pack()

# Button
def on_click():
    print("Button clicked!")
button = tk.Button(window, text="Click me!", command=on_click)
button.pack()

# Entry (Textbox)
entry = tk.Entry(window)
entry.pack()

# Checkbutton (Checkbox)
checkbutton = tk.Checkbutton(window, text="I agree to the terms and conditions")
checkbutton.pack()

# Radiobutton (Radio)
radio_var = tk.StringVar()
radio_var.set("Option 1")
radio_button1 = tk.Radiobutton(window, text="Option 1", variable=radio_var, value="Option 1")
radio_button1.pack()
radio_button2 = tk.Radiobutton(window, text="Option 2", variable=radio_var, value="Option 2")
radio_button2.pack()

# Combobox
combobox_var = tk.StringVar()
combobox = tk.ttk.Combobox(window, textvariable=combobox_var)
combobox["values"] = ("Option 1", "Option 2", "Option 3")
combobox.pack()

# Listbox
listbox = tk.Listbox(window)
listbox.insert(1, "Option 1")
listbox.insert(2, "Option 2")
listbox.insert(3, "Option 3")
listbox.pack()

# Menu
menubar = tk.Menu(window)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=file_menu)
window.config(menu=menubar)

# Canvas
canvas = tk.Canvas(window, width=200, height=200, bg="white")
canvas.pack()
line = canvas.create_line(0, 0, 200, 200, fill="blue", width=2)
rectangle = canvas.create_rectangle(50, 50, 150, 150, fill="red")

# Scrollbar
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text = tk.Text(window, yscrollcommand=scrollbar.set)
text.insert(tk.END, "This is some text.")
text.pack()
scrollbar.config(command=text.yview)

window.mainloop()
