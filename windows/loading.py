import sys
from tkinter import *
from tkinter.ttk import Progressbar


class loading(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("460x100+500+300")
        # threading.Thread(target=self.screen).start()
        self.screen()
        self.mainloop()

    def screen(self):

        self.resizable(False, False)
        self.iconbitmap("Images/student_icon.ico")
        self.title("Student Management System")
        self.config(background="White")
        Label(text="Loading...", font=("Cambria", 17),
              background="white").place(x=20, y=10)
        self.progr = Progressbar(self, length=400, maximum=100)
        self.progr.place(x=20, y=50)
        self.progr.start(30)
        self.progr.after(3110, self.get)
        self.protocol("WM_DELETE_WINDOW", lambda: sys.exit())

    def get(self):
        # print(self.progr["value"])
        self.progr.stop()
        self.destroy()


if __name__ == "__main__":
    l = loading()
