import tkinter
def button_press():
    print("test")

window = tkinter.Tk()
window.title("My program")
window.geometry("800x800")
window.configure(background="blue")
label = tkinter.Label(window, text="Hello", background="blue")
button = tkinter.Button(window, text="click me", command=button_press)
label.pack()
button.pack()
window.mainloop()