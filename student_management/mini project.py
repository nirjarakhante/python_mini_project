'''import tkinter as tk
root = tk.Tk()
root.title("Introduction")
root.geometry("900x400")

label = tk.Label(root,text = "Hello, My name is Nirjara Khante", font=("calibri",40),fg = "purple")

label.pack()
root.mainloop()
'''
#import tkinter as tk

from tkinter import *

# Global list 
students = []

def add_student():
    global students
    name = name_entry.get()
    roll = roll_entry.get()
    dept = dept_entry.get()
    marks = marks_entry.get()

    if name == "" or roll == "" or dept == "" or marks == "":
        result_label.config(text="Please fill all fields!", fg="red")
    else:
        students.append({"name": name, "roll": roll, "dept": dept, "marks": marks})
        result_label.config(text="Student added!", fg="green")
        name_entry.delete(0, END)
        roll_entry.delete(0, END)
        dept_entry.delete(0, END)
        marks_entry.delete(0, END)

def show_students():
    display.delete(1.0, END)
    if not students:
        display.insert(END, "No records found.")
    else:
        for s in students:
            display.insert(END, f"Name: {s['name']}, Roll: {s['roll']}, Dept: {s['dept']}, Marks: {s['marks']}\n")

root = Tk()
root.title("Student Management")
root.geometry("800x500")

Label(root, text="Student Management System", font=("calibri", 14, "bold")).pack()

Label(root, text="Name:").pack()
name_entry = Entry(root); name_entry.pack()

Label(root, text="Roll No:").pack()
roll_entry = Entry(root); roll_entry.pack()

Label(root, text="Department:").pack()
dept_entry = Entry(root); dept_entry.pack()

Label(root, text="Marks:").pack()
marks_entry = Entry(root); marks_entry.pack()

Button(root, text="Add Student", command=add_student, bg="lightgreen").pack(pady=8)
Button(root, text="Show Students", command=show_students, bg="lightblue").pack(pady=8)

result_label = Label(root, text="")
result_label.pack()

display = Text(root, height=8, width=40)
display.pack(pady=10)

root.mainloop()
