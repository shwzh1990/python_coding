
from tkinter import *
import json
from tkinter import messagebox
from turtle import st

root = Tk()

student_info_msg = ["ID","Name","Gender","Chinese", "Math", "English"]
student_gui_widget = {}
def Add_Student():
    add_student_window = Toplevel()
    add_student_window.title("Add student screen")
    for info in student_info_msg:
        student_gui_widget[info] = []
        
        student_label = Label(add_student_window, text=info)
        student_label.pack()
        student_gui_widget[info].append(student_label)

        student_msg_input = Entry(add_student_window, width=20)
        student_msg_input.pack()
        student_gui_widget[info].append(student_msg_input)
    def save(student_info_list):
        with open("student_info.txt", 'r+') as fd:
            data = fd.read();
        student_info = json.loads(data)
        if student_info_list[0] in student_info:
            messagebox.showinfo("ID exist!","Please check the student ID!!"); 
        elif student_info_list[0] == '':
            messagebox.showinfo("No ID!","Please check type student ID!!"); 
        elif student_info_list[0].isdecimal() == FALSE:
            messagebox.showinfo("No ID!","please check ID format!!"); 
        else:
            student_info[student_info_list[0]] = {}
            print(student_info)
            for smsg,msg in zip(student_info_list[1:],student_info_msg[1:]):
                student_info[student_info_list[0]][msg] = smsg
            print(student_info)
            final_data = json.dumps(student_info,indent=4)
            with open("student_info.txt", 'w') as fd:
                fd.write(final_data)
            #messagebox.showinfo("student saved", "student info saves in the file!!")
        student_gui_widget.clear()
    Add_Button = Button(add_student_window, text="Add student info", command = lambda: save([student_gui_widget[msg][1].get() for msg in student_info_msg])).pack()
    EXIT_Button = Button(add_student_window, text="exit", command = add_student_window.destroy).pack()




def Remove_Student():
    Remove_student_window = Toplevel()
    Remove_student_window.title("Remove student screen")
    with open("student_info.txt",'r') as fd:
        student_data = fd.read()
    
    student_label = Label(Remove_student_window, text="Enter student ID:").pack()
    student_ID_Entry = Entry(Remove_student_window, width=20)
    student_ID_Entry.pack()
   
    def delete(ID):
        student_data_load = json.loads(student_data)
        if ID in student_data_load:
            del student_data_load[ID]
        else:
            messagebox.showinfo("No ID", "Cannot find ID!!")
        final_result = json.dumps(student_data_load, indent=4)
        with open("student_info.txt", 'w') as fd:
            fd.write(final_result)

    Remove_Button = Button(Remove_student_window, text="Remove",command = lambda:delete(student_ID_Entry.get())).pack()
    EXIT_Button = Button(Remove_student_window, text="exit", command = Remove_student_window.destroy).pack()
def Modify_student():
    modify_student_window = Toplevel()
    modify_student_window.title("Add student screen")
    for info in student_info_msg:
        student_gui_widget[info] = []
        
        student_label = Label(modify_student_window, text=info)
        student_label.pack()
        student_gui_widget[info].append(student_label)

        student_msg_input = Entry(modify_student_window, width=20)
        student_msg_input.pack()
        student_gui_widget[info].append(student_msg_input)
    def modify(student_info_list):
        with open("student_info.txt",'r') as fd:
            student_data = fd.read()
        student_info = json.loads(student_data)
        if student_info_list[0] in student_info:
            for msg,smsg in zip(student_info_msg,student_info_list):
                student_info[msg] = smsg
        else:
            messagebox.showinfo("NO ID!!", "No this ID in the database!!") 
        student_data = json.dumps(student_info)
        with open("student_info.txt", 'w') as fd:
            fd.write(student_data)
        student_gui_widget.clear()
    Modify_Button = Button(modify_student_window, text="Modify student info", command = lambda: modify([student_gui_widget[msg][1].get() for msg in student_info_msg])).pack()
    EXIT_Button = Button(modify_student_window, text="exit", command = modify_student_window.destroy).pack()


def Check_One_Student():
    Check_Student_Window = Toplevel()
    Check_Student_Window.title("Check one Student info")
    textBox = Text(Check_Student_Window, height = 30, width = 50)
    Check_Student_Label = Label(Check_Student_Window, text="Student ID").pack()
    Student_ID_Entry = Entry(Check_Student_Window, width=20)
    Student_ID_Entry.pack()
    with open("student_info.txt", 'r') as fd:
        student_data = fd.read()
    student_info_dict = json.loads(student_data)
    def check(student_ID):
        if student_ID in student_info_dict.keys():
            textBox.pack()
            present_str = 'ID: '
            print(student_info_dict[student_ID])
            present_str += student_ID
            present_str += '\n'
            for msg in student_info_msg[1:]:
                present_str += msg
                present_str += ': '
                present_str += student_info_dict[student_ID][msg]
                present_str += '\n'
            textBox.insert(END,present_str)                     
        else:
            messagebox.showinfo("NO ID", "Cannot find the ID in the database")

    textBox.delete("1.0","end")
    Check_Student_Button = Button(Check_Student_Window, text="Check", command = lambda: check(Student_ID_Entry.get())).pack()
    EXIT_Button = Button(Check_Student_Window, text="exit", command = Check_Student_Window.destroy).pack()
def List_Student():
    List_Student_Window = Toplevel()
    List_Student_Window.title("List all Students info")
    List_Student_Label = Label(List_Student_Window, text="Student ID").pack()
    textBox = Text(List_Student_Window, height = 30, width = 50)
    textBox.pack()
    with open("student_info.txt", 'r') as fd:
        student_data = fd.read()
    student_info_dict = json.loads(student_data)
    present_str = ''
    for key,val in student_info_dict.items():
        present_str += "ID: "
        present_str += key
        present_str += '\n'
        present_str += json.dumps(val, indent = 4)
        present_str += '\n'

    textBox.insert(END, present_str)
        
    EXIT_Button = Button(List_Student_Window, text="exit", command = List_Student_Window.destroy).pack()
def help():
    mylabel = Label(root, text="jfdsklafjdskaljfkl")
    mylabel.pack()

menu = {"Add Student":Add_Student, "Remove Student":Remove_Student, "Modify Students info":Modify_student, "Check One Student info":Check_One_Student, "list student info": List_Student,"help":help}
buttons = {}
def Button_Creat(menu_dict):
    for key, func in menu_dict.items():
        buttons[key] = Button(root, text = key,  command = func, padx = 20, pady = 40)
        buttons[key].pack()





    





root.geometry("400x600")
Welcome_Lable = Label(root, text="Welcome To My Student transcript manager!!")

Welcome_Lable.pack()
Button_Creat(menu)

root.mainloop()
