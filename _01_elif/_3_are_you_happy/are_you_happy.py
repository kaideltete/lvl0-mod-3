
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

    # Put the image on the Tk window used by simpledialog so that when the
    # window with the image is closed, the interpreter moves to the next
    # line of code
    global window
    window.deiconify()
    image = ImageTk.PhotoImage(image)
    tk.Label(master=window, image=image).pack()

    # Blocks so picture can be shown--resumes when picture window is closed
    window.mainloop()

    # Regenerate a new window after closing so more simpledialogs and
    # images can be shown
    window = Tk()
    window.withdraw()










if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements


    window = Tk()
    window.withdraw()






    are_you = simpledialog.askstring(title='happy', prompt="are you happy? yes or no")

    if (are_you=="yes" or are_you=="yes."):
        messagebox.showinfo(message="keep doing what you are doing.")
    if (are_you=="no" or are_you=="no."):
        do_you = simpledialog.askstring(title='happy', prompt="do you want to be happy? yes or no")


    if (do_you=="no" or do_you=="no."):
        messagebox.showinfo(message="keep doing what you are doing.")


    if (do_you=="yes" or do_you=="yes."):
        messagebox.showinfo(message="change something.")


    if (do_you=="perhaps" or do_you=="perhaps."):
        show_image('crab.png')


pass
