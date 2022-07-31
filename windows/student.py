from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Combobox, Treeview
from windows import login_win, backend


class Student:
    def __init__(self, win, img_list, user):
        self.win = win
        self.img_list = img_list
        self.user_tuple = user
        self.__s_gui()

    def __s_gui(self):
        # main frame
        self.frame1 = Frame(self.win, width=1400,
                            height=790, background="#ff7236")
        self.frame1.place(x=0, y=0)
        # menu frame
        self.frame2 = Frame(self.frame1, bg="#5800fc",
                            width=1400, height=150, bd=3, relief="solid")
        # home frame
        self.frame3 = Frame(self.frame1, bg="#ff7236", width=1380, height=630)
        # fees frame
        self.frame4 = Frame(self.frame1, bg="#ff7236", width=1380, height=630)
        # attendance frame
        self.frame5 = Frame(self.frame1, bg="#ff7236", width=1380, height=630)
        self.frame2.place(x=0, y=0)
        self.__home_gui()
        Label(self.frame2, image=self.img_list[8], bg="#5800fc").place(
            x=10, y=10)
        Label(self.frame2, text=f"Logined as : {self.user_tuple[1]}", bg="#5800fc", fg="white", font=(
            "Verdana", 13, "bold")).place(x=130, y=120)
        Button(self.frame2, text="HOME", bg="#ecfc05", font=("Verdana", 16, "bold"), relief="solid", bd=3,
               fg="black", activebackground="#05fc2a", width=14, command=self.__home_gui).place(x=210, y=40, height=60)
        Button(self.frame2, text="FEES", bg="#ecfc05", font=("Verdana", 16, "bold"), relief="solid", bd=3,
               fg="black", activebackground="#05fc2a", width=14, command=self.fees_frame).place(x=450, y=40, height=60)
        Button(self.frame2, text="Attendance", bg="#ecfc05", font=("Verdana", 16, "bold"), relief="solid", bd=3,
               fg="black", activebackground="#05fc2a", width=14, command=self.attendance_frame).place(x=690, y=40, height=60)
        Button(self.frame2, text="Logout", bg="#ecfc05", font=("Verdana", 16, "bold"), relief="solid", bd=3,
               fg="black", activebackground="#05fc2a", width=14, command=self.logout).place(x=930, y=40, height=60)

    def logout(self):
        a = mb.askyesno("Confirmation", "Are You Sure, You want to logout ?")
        if a:
            mb.showinfo("Done", "Successfully Logout !")
            login_win.login(self.win, self.img_list)

    def __home_gui(self):
        self.__remove_frames(3)
        self.frame3.place(x=10, y=160)
        data = self.get_student_details()
        Label(self.frame3, text="PROFILE", font=("Verdana", 20,
              "bold", "underline"), bg="#ff7236").place(x=630, y=0)
        Label(self.frame3, text="Personal Details", font=(
            "Verdana", 14, "bold"), bg="#b1fc03").place(x=0, y=50)
        Label(self.frame3, text="Academic Details", font=(
            "Verdana", 14, "bold"), bg="#b1fc03").place(x=700, y=50)
        Label(self.frame3, text=f"ID : {data[0][0]}", font=(
            "Verdana", 16), bg="#ff7236").place(x=740, y=90)
        Label(self.frame3, text=f"Standard : {data[0][9]}", font=(
            "Verdana", 16), bg="#ff7236").place(x=670, y=130)
        Label(self.frame3, text=f"Divison : {data[0][5]}", font=(
            "Verdana", 16), bg="#ff7236").place(x=690, y=170)
        Label(self.frame3, text=f"Roll NO : {data[0][4]}", font=(
            "Verdana", 16), bg="#ff7236").place(x=690, y=210)
        Label(self.frame3, text=f"Date Of Admission : {data[0][12]}", font=(
            "Verdana", 16), bg="#ff7236").place(x=576, y=250)
        Label(self.frame3, text=f"Username : {self.user_tuple[1]}", font=(
            "Verdana", 16), bg="#ff7236").place(x=665, y=290)
        if len(data[1]) == 0:
            Label(self.frame3, text=f"No Class Teacher Assign", font=(
                "Verdana", 16), bg="#ff7236").place(x=626, y=330)
        else:
            Label(self.frame3, text=f"Class Teacher : {data[1][0][0]}", font=(
                "Verdana", 16), bg="#ff7236").place(x=626, y=330)
        Label(self.frame3, text=f"First Name : {data[0][1]}", font=(
            "Verdana", 16), bg="#ff7236").place(x=25, y=90)
        Label(self.frame3, text=f"Middle Name : {data[0][2]}", font=(
            "Verdana", 16), bg="#ff7236").place(x=0, y=130)
        Label(self.frame3, text=f"Last Name : {data[0][3]}", font=(
            "Verdana", 16), bg="#ff7236").place(x=25, y=170)
        Label(self.frame3, text=f"Father Name : {data[0][7]}", font=(
            "Verdana", 16), bg="#ff7236").place(x=0, y=210)
        Label(self.frame3, text=f"Mother Name : {data[0][8]}", font=(
            "Verdana", 16), bg="#ff7236").place(x=0, y=250)
        Label(self.frame3, text=f"Date Of Birth : {data[0][10]}", font=(
            "Verdana", 16), bg="#ff7236").place(x=0, y=290)
        Label(self.frame3, text=f"Address : {data[0][6]}", font=(
            "Verdana", 16), bg="#ff7236").place(x=50, y=330)
        Label(self.frame3, text=f"Blood Grp : {data[0][11]}", font=(
            "Verdana", 16), bg="#ff7236").place(x=30, y=390)
        Label(self.frame3, text=f"Gender : {data[0][16]}", font=(
            "Verdana", 16), bg="#ff7236").place(x=220, y=390)
        Label(self.frame3, text=f"Father Occupation : {data[0][13]}", font=(
            "Verdana", 16), bg="#ff7236").place(x=0, y=430)
        Label(self.frame3, text=f"Mother Occupation : {data[0][14]}", font=(
            "Verdana", 16), bg="#ff7236").place(x=0, y=470)
        Label(self.frame3, text=f"Phone No.: {data[0][15]}", font=(
            "Verdana", 16), bg="#ff7236").place(x=26, y=510)

    def get_student_details(self):
        id = self.user_tuple[0]
        data = backend.fetch_details(
            'select * from student where id=%s;', (id,))
        faculty = backend.fetch_details(
            'select concat_ws(" ",f.first_name,f.middle_name,f.last_name) from div_details d inner join faculty f on d.faculty_id=f.id where d.divison=%s and d.std=%s;', (data[0][5], data[0][9]))
        data.append(faculty)
        return data

    def __remove_frames(self, no):
        try:
            if no == 3:
                self.frame4.place_forget()
                self.frame5.place_forget()
                self.month_label.place_forget()

            elif no == 4:
                self.frame3.place_forget()
                self.frame5.place_forget()
                self.month_label.place_forget()

            elif no == 5:
                self.frame4.place_forget()
                self.frame3.place_forget()
                self.month_label.place_forget()

        except:
            pass

    def fees_frame(self):
        self.__remove_frames(4)
        self.frame4.place(x=10, y=160)
        Label(self.frame4, text="FEES RECORD", font=("Verdana", 20,
              "bold", "underline"), bg="#ff7236").place(x=600, y=0)
        Label(self.frame4, text=f"View Record By Year ", font=(
            "lucida", 14), bg="#84fa92").place(x=10, y=50)
        data = backend.fetch_details(
            'select * from fees where id=%s', (self.user_tuple[0],))
        yearlist = []
        for y in data:
            yearlist.append(y[2])
        self.year_box = Combobox(self.frame4, background="white", values=yearlist, font=(
            "Times New Roman", 15), state="readonly", width=6)
        self.year_box.place(x=10, y=80)
        self.year_box.bind("<<ComboboxSelected>>",
                           lambda e: self.__fees_by_year(self.user_tuple[0]))

    def __fees_by_year(self, id):
        self.month_label = Label(
            self.frame4, bg="#ff7236", height=300, width=300)
        self.month_label.place(x=10, y=120)
        self.Mfees_details = ""
        self.Yfees_details = ""
        self.win.update()
        data = backend.fetch_details(
            'select * from fees where id=%s and year_=%s;', (id, self.year_box.get()))[0]
        data = list(data)

        for i in range(len(data)):
            if data[i] == "N":
                data[i] = "Not Paid"
            elif data[i] == "Y":
                data[i] = "Paid"
        f_details = backend.fetch_details(
            'select * from store_fees where year_=%s;', (self.year_box.get(),))[0]
        Label(self.month_label, text=f"{self.year_box.get()} Details", font=(
            "lucida", 16, "underline"), bg="#ff7236").place(x=10, y=0)
        self.Mfees_details = f_details[1]
        self.Yfees_details = f_details[2]
        self.month_f_label = Label(
            self.month_label, text=f"Monthly Fees : {self.Mfees_details}", font=("lucida", 16), bg="#ff7236")
        self.month_f_label.place(x=10, y=30)
        self.year_f_label = Label(
            self.month_label, text=f"Year Fees : {self.Yfees_details}", font=("lucida", 16), bg="#ff7236")
        self.year_f_label.place(x=10, y=60)
        if data[1] == "Paid":
            Label(self.month_label, text=f"Full Year Fees : Paid",
                  font=("Verdana", 20), bg="#ff7236").place(x=10, y=180)
        else:
            monthlist = ["January : ", "February : ", "March : ", "April : ", "May : ", "June : ",
                         "July : ", "August : ", "September : ", "October : ", "November : ", "December : "]
            Label(self.month_label, text=f"{monthlist[0]}{data[3]}", font=(
                "lucida", 14), bg="#ff7236").place(x=400, y=50)
            Label(self.month_label, text=f"{monthlist[1]}{data[4]}", font=(
                "lucida", 14), bg="#ff7236").place(x=390, y=80)
            Label(self.month_label, text=f"{monthlist[2]}{data[5]}", font=(
                "lucida", 14), bg="#ff7236").place(x=415, y=110)
            Label(self.month_label, text=f"{monthlist[3]}{data[6]}", font=(
                "lucida", 14), bg="#ff7236").place(x=428, y=140)
            Label(self.month_label, text=f"{monthlist[4]}{data[7]}", font=(
                "lucida", 14), bg="#ff7236").place(x=433, y=170)
            Label(self.month_label, text=f"{monthlist[5]}{data[8]}", font=(
                "lucida", 14), bg="#ff7236").place(x=427, y=200)
            Label(self.month_label, text=f"{monthlist[6]}{data[9]}", font=(
                "lucida", 14), bg="#ff7236").place(x=433, y=230)
            Label(self.month_label, text=f"{monthlist[7]}{data[10]}", font=(
                "lucida", 14), bg="#ff7236").place(x=407, y=260)
            Label(self.month_label, text=f"{monthlist[8]}{data[11]}", font=(
                "lucida", 14), bg="#ff7236").place(x=370, y=290)
            Label(self.month_label, text=f"{monthlist[9]}{data[12]}", font=(
                "lucida", 14), bg="#ff7236").place(x=395, y=320)
            Label(self.month_label, text=f"{monthlist[10]}{data[13]}", font=(
                "lucida", 14), bg="#ff7236").place(x=378, y=350)
            Label(self.month_label, text=f"{monthlist[11]}{data[14]}", font=(
                "lucida", 14), bg="#ff7236").place(x=378, y=380)

    def attendance_frame(self):
        self.__remove_frames(5)
        self.frame5.place(x=10, y=160)
        Label(self.frame5, text="ATTENDANCE", font=("Verdana", 20,
              "bold", "underline"), bg="#ff7236").place(x=600, y=0)
        self.table = Treeview(self.frame5, columns=[
                              "m", "p", 'a'], selectmode="none", show="headings", height=10)
        self.table.place(x=10, y=40, height=500)
        self.table.heading("m", text="Month")
        self.table.heading("p", text="Present Days")
        self.table.heading("a", text="Attended Days")
        self.table.column("m", anchor="center", width=100)
        self.table.column("p", anchor="center", width=100)
        self.table.column("a", anchor="center", width=100)
        self.sc = Scrollbar(
            self.frame5, command=self.table.yview, bd=2, relief="solid")
        self.table.configure(yscrollcommand=self.sc.set)
        self.sc.place(x=315, y=40, height=500)

        self.table1 = Treeview(self.frame5, columns=[
                               "m", "p", 'a', 'b'], selectmode="none", show="headings", height=10)
        self.table1.place(x=600, y=60, height=500)
        self.table1.heading("m", text="Month")
        self.table1.heading("p", text="Date")
        self.table1.heading("a", text="Day")
        self.table1.heading("b", text="Attended")
        self.table1.column("m", anchor="center", width=100)
        self.table1.column("p", anchor="center", width=100)
        self.table1.column("a", anchor="center", width=100)
        self.table1.column("b", anchor="center", width=100)
        self.sc1 = Scrollbar(
            self.frame5, command=self.table1.yview, bd=2, relief="solid")
        self.table1.configure(yscrollcommand=self.sc1.set)
        self.sc1.place(x=1004, y=60, height=500)
        self.__add_month_attend()
        self.__add_full_attend()

    def __add_full_attend(self):
        query = '''select monthname(date_attend),date_format(date_attend,"%d/%m/%Y"),dayname(date_attend),get_presentee(attended) from attendance where id=%s;'''
        for data in backend.fetch_details(query, (self.user_tuple[0],)):
            self.table1.insert("", END, values=data)

    def __add_month_attend(self):
        query1 = '''select monthname(p.present_date),count(p.present_date) from present p inner join attendance a on p.present_date=a.date_attend where a.id=%s group by monthname(p.present_date);'''
        query2 = "select count(id),monthname(date_attend) from attendance where id=%s and attended='Y' group by monthname(date_attend);"
        data1 = backend.fetch_details(query1, (self.user_tuple[0],))
        data2 = backend.fetch_details(query2, (self.user_tuple[0],))
        i = 0
        total = len(data1)
        while i < total:
            try:
                lst = []
                row1 = data1[i]
                row2 = data2[i]
                if row1[0] == row2[1]:
                    lst.append(row1[0])
                    lst.append(row1[1])
                    lst.append(row2[0])
                else:
                    lst.append(row1[0])
                    lst.append(row1[1])
                    lst.append(0)
                self.table.insert("", END, values=lst)

            except IndexError:
                pass
            i = i+1
