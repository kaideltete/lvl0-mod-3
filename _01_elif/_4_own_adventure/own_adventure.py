from tkinter import simpledialog, messagebox, Tk

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story




import tkinter as tk
from tkinter import messagebox, simpledialog, Tk
from tkinter import simpledialog, Tk
from PIL import Image, ImageTk
from playsound import playsound
global window
window = None


def show_image(filename=None):
    try:
        image = Image.open(filename)
    except FileNotFoundError as fnf:
        print("ERROR: Unable to find file " + filename)
        return

    global window
    window.deiconify()
    image = ImageTk.PhotoImage(image)
    tk.Label(master=window, image=image).pack()

    window.mainloop()

    window = Tk()
    window.withdraw()

if __name__ == '__main__':
        window = Tk()
        window.withdraw()

        msg1 = simpledialog.askstring(title='quest', prompt="you are on a path, then it spits in two ways do you go left or right?(left to go left, right to go right)")

        if (msg1 == "go home" or msg1 == "go home."):
            messagebox.showinfo(message="you go home.")
        if (msg1 == "left" or msg1 == "left."):
            msg3 = simpledialog.askstring(title='quest', prompt="there is a cliff do you go back or jump, yes or no?")

            if (msg3 == "yes" or msg3 == "yes."):
                messagebox.showinfo(message="you die.")
            if (msg3 == "no" or msg3 == "no."):
                messagebox.showinfo(message="you go home.")

        if (msg1 == "right" or msg1 == "right."):
            print("inside")
            msg2 = simpledialog.askstring(title='quest',prompt="there is a bear, do you fight it, yes or no?")
            if (msg2 == "yes" or msg2 == "yes."):
                messagebox.showinfo(message="you die.")
            if (msg2 == "no" or msg2 == "no."):
                messagebox.showinfo(message="you go home.")

pass
