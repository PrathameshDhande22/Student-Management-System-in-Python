import sys
from tkinter import *
from windows import loading, login_win
from PIL import Image, ImageTk
l = loading.loading()

# making the mainwindow


class gui(Tk):
    def __init__(self):
        super().__init__()
        self.minsize(width=1200, height=700)
        # self.state("zoomed")
        self.geometry("1400x790+60+10")
        self.resizable(False, False)
        self.title("Student Management System")
        self.iconbitmap("Images/student_icon.ico")
        self.load_images()

        self.img_list = [self.img1, self.img2, self.img3, self.img4,
                         self.img5, self.img6, self.img7, self.img8, self.img9]
        login_win.login(self, self.img_list)

    def load_images(self):
        self.img1 = Image.open("Images/back_img.png").resize((1400, 790))
        self.img1 = ImageTk.PhotoImage(self.img1)

        self.img2 = Image.open("Images/login.png").resize((140, 100))
        self.img2 = ImageTk.PhotoImage(self.img2)

        self.img3 = Image.open("Images/reset.png").resize((40, 40)).rotate(270)
        self.img3 = ImageTk.PhotoImage(self.img3)

        self.img4 = Image.open("Images/home.png").resize((30, 30))
        self.img4 = ImageTk.PhotoImage(self.img4)

        self.img5 = Image.open("Images/Superadmin.png").resize((200, 200))
        self.img5 = ImageTk.PhotoImage(self.img5)

        self.img6 = Image.open("Images/admin.png").resize((90, 90))
        self.img6 = ImageTk.PhotoImage(self.img6)

        self.img7 = Image.open("Images/search.png").resize((30, 30))
        self.img7 = ImageTk.PhotoImage(self.img7)

        self.img8 = Image.open("Images/faculty.png").resize((200, 200))
        self.img8 = ImageTk.PhotoImage(self.img8)

        self.img9 = Image.open("Images/student.png").resize((130, 130))
        self.img9 = ImageTk.PhotoImage(self.img9)


if __name__ == "__main__":

    g = gui()
    g.mainloop()
