from tkinter import simpledialog, messagebox, Tk
import webbrowser


# Use this function to play a video from the internet
def play_video(url):
    webbrowser.open(url)

# =================== DO NOT MODIFY THE CODE ABOVE ===========================


if __name__ == '__main__':
    # TODO 1) Make a new window variable, window = Tk()
    #      2) Hide the window using the window's .withdraw() method
    #      3) Ask the user how many cats they have
    #      4) If they have 3 or more cats, tell them they are a crazy cat lady
    #      5) If they have less than 3 cats AND more than 0 cats, call the
    #         play_video function below to show them a cat video
    #      6) If they have 0 cats, show them a video of A Frog Sitting on a
    #         Bench Like a Human
    window = Tk()
    window.withdraw()
    can_they = simpledialog.askstring(title='how many cats dpo you have?', prompt="cat")

    if (can_they=="0"):
        play_video(str("https://www.youtube.com/watch?v=umAyl9q9Gwg"))
    if (can_they=="1" or can_they=="2"):
        play_video(str("https://www.youtube.com/watch?v=QH2-TGUlwu4"))
    else:
        messagebox.showinfo(message="you are a crazy cat lady")

    if (can_they=="1234567890"):
        play_video(str("https://youtu.be/dQw4w9WgXcQ"))









    pass
