from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from windows import backend
# import backend


class Fees:
    def __init__(self, win):
        self.win = win
        self.__topwid()

    def __topwid(self):
        self.top = Toplevel(self.win)
        self.top.title("Fees Detail")
        self.top.iconbitmap("Images/student_icon.ico")
        self.top.geometry("290x220+500+300")
        self.top.config(bg="#fab6b1")
        self.top.resizable(False, False)
        Label(self.top, text="Add Fee Year Record", font=(
            "Verdana", 14, "bold", "underline"), bg="#fab6b1").place(x=10, y=0)
        Label(self.top, text="Year", font=("Verdana", 12),
              bg="#fab6b1").place(x=5, y=40)
        Label(self.top, text="Montly Fee", font=(
            "Verdana", 12), bg="#fab6b1").place(x=70, y=40)
        Label(self.top, text="Year Fee", font=(
            "Verdana", 12), bg="#fab6b1").place(x=175, y=40)
        self.year_f = IntVar()
        self.month_f = IntVar()
        self.year_fees = IntVar()
        self.search = StringVar(value="Search By Year")
        self.year_txt = Entry(self.top, textvariable=self.year_f, font=(
            "Times New Roman", 14), background="white", width=6, bd=2, relief="solid")
        self.year_txt.place(x=5, y=70)
        self.month_txt = Entry(self.top, textvariable=self.month_f, font=(
            "Times New Roman", 14), background="white", width=10, bd=2, relief="solid")
        self.month_txt.place(x=70, y=70)
        self.year_fees_txt = Entry(self.top, textvariable=self.year_fees, font=(
            "Times New Roman", 14), background="white", width=10, bd=2, relief="solid")
        self.year_fees_txt.place(x=175, y=70)
        Button(self.top, text="ADD Record", font=("Verdana", 12), bg="#05ff2f", relief="groove", bd=2, fg="white",
               activebackground="#ff0505", foreground="black", activeforeground="white", command=self.__add_record).place(x=20, y=110, height=40)
        Button(self.top, text="Update", font=("Verdana", 12), bg="#05ff2f", relief="groove", bd=2, fg="white", activebackground="#ff0505",
               foreground="black", activeforeground="white", width=10, command=self.__update_record).place(x=140, y=110, height=40)
        self.img = Image.open("Images/search.png").resize((30, 30))
        self.img = ImageTk.PhotoImage(self.img)
        self.search_txt = Entry(self.top, textvariable=self.search, font=(
            "Times New Roman", 14), background="white", width=16, bd=2, relief="solid")
        self.search_txt.place(x=10, y=170)
        Button(self.top, image=self.img, bg="black", relief="groove", bd=2, fg="white",
               activebackground="#fab6b1", command=self.__search_rec).place(x=160, y=162)
        self.search_txt.bind("<Button-1>", lambda e: self.search.set(""))

    def __search_rec(self):
        if self.search.get() == "":
            messagebox.showinfo("Error", "Enter any Year to search")
        else:
            data = backend.fetch_details(
                "select * from store_fees where year_=%s;", (self.search.get(),))
            if len(data) == 0:
                messagebox.showerror("Error", "No Record Found")
            else:
                self.year_f.set(data[0][0])
                self.year_fees.set(data[0][2])
                self.month_f.set(data[0][1])

    def __add_record(self):
        if self.year_f.get() == "" or len(str(self.year_f.get())) != 4:
            messagebox.showerror("Error", "Enter valid Year")
        else:
            query = 'insert into store_fees values (%s,%s,%s);'
            val = (self.year_f.get(), self.month_f.get(), self.year_fees.get())
            dat = backend.execute_query(query, val)
            if dat == True:
                messagebox.showinfo("Success", "Successfully Added the Record")
            elif "1062" in str(dat):
                messagebox.showinfo(
                    "Already Exist", "The Year you enter already exist")

    def __update_record(self):
        if self.year_f.get() == "" or len(str(self.year_f.get())) != 4:
            messagebox.showerror("Error", "Enter valid Year")
        else:
            query = 'update store_fees set monthly=%s,yearly=%s where year_=%s;'
            val = (self.month_f.get(), self.year_fees.get(), self.year_f.get())
            dat = backend.execute_query(query, val)
            if dat == True:
                messagebox.showinfo(
                    "Success", "Successfully Updated the Record")


if __name__ == "__main__":
    root = Tk()
    c = Fees(root)
    root.update()
    root.mainloop()
