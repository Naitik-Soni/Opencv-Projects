import tkinter as tk

app = tk.Tk()
app.title("Color Manipulation")

try:
    icon = tk.PhotoImage(file=r"Assets\window-icon.png")
    app.iconphoto(False, icon)
except tk.TclError:
    print("Error: Could not load icon file.")

app.state('zoomed')

label = tk.Label(app, text = "Hello, User!")
label.pack()
label.grid(row=0, column=0)

app.mainloop()