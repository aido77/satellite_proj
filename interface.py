from tkinter import *
from tkinter import ttk
from render import *
from sat_database import *
from attributes import *
from questiongenerator import *
import tkinter as tk
from tkinter import *
import time

root = Tk()
root.title("Satellite Interface")
root.minsize(600, 600)
title = Label(root, text="Welcome to the Satellite Interface!")
title.pack()
global entry
entry = tk.Entry(root)
#initialises the satellite 
def openSatelliteAttributeDisplay(URL2):
    # Toplevel object which will 
    # be treated as a new window
    newWindow = Toplevel(root)
    newWindow.title("Satellite Attribute Display")
    # sets the geometry of toplevel
    newWindow.geometry("1000x600")
    # A Label widget to show in toplevel
    count_sat = 0
#A placeholder that shows which satellite we're "on"
    ts = load.timescale()
    t = ts.now()
#gets the current time in epochs
    temp_sat = ''
    height = len(attribute_list)
    width = 5
    tree = ttk.Treeview(newWindow, column=("c1", "c2","c3","c4","c5"), show='headings', height=len(attribute_list))
    tree.column("# 1", anchor='center',width=125)
    tree.heading("# 1", text="Name")
    tree.column("# 2", anchor='center',width=150)
    tree.heading("# 2", text="Epoch")
    tree.column("# 3", anchor='center',width=300)
    tree.heading("# 3", text="Coordinates")
    tree.column("# 4",anchor='center',width=300)
    tree.heading("# 4",text="Velocity")
    tree.column("# 5",anchor='center',width=125)
    tree.heading("# 5",text="Speed")
    for i in range(len(attribute_list)):
        tree.insert('', 'end', text=i, values=(attribute_list[i]))
    tree.pack()
    time.sleep(10)
    render(URL2)
    
def select():
    init = Button(root, text="BEGIN", command=lambda: openSatelliteAttributeDisplay(URL2))
    init.pack_forget()
    filter_select.config(text=satellite_filter.get(ANCHOR))
    sat_select = satellite_filter.get(ANCHOR)
    print(sat_select)
    URL2 = str(sat_dict[sat_select])
    bigData = load.tle_file(URL2)
    print("numbsatlen=",len(bigData))
    attribute_refresh(len(bigData),URL2)
    print("bigdatalen =",len(bigData))
    print("coordslen =",len(coords))
    init.pack()

satellite_filter = Listbox(root)
satellite_filter.pack()

def drop():
    title.forget()
    satellite_filter.forget()
    filter_select.forget()


for item in sat_dict:
    satellite_filter.insert(END, item)
#appends items from satellite types into the dropdown list
filter_select = Button(root, text='SELECT', command=select)
filter_select.pack(pady= 10)

def validate(question_count):
    tempvar = StringVar()
    temp_q = question_list[question_count]
    tempvar.set(temp_q[1])
    incorrect1 = tk.Label(text='Sorry, that is incorrect, the correct answer is ',fg='red')
    incorrect2 = tk.Label(textvariable=tempvar,fg='red')
    correct = tk.Label(text='Correct!',fg='green')
    attempt = entry.get()
    correct.forget()
    incorrect1.forget()
    incorrect2.forget()

    if attempt == temp_q[1]:
        correct.pack()
        entry.delete(0, tk.END)
        if question_count == 0:
            var.set(question_full[question_count])
            validate0.forget()
            validate1.pack()
        elif question_count == 1:
            var.set(question_full[question_count])
            question.pack()
            validate1.forget()
            validate2.pack()
        elif question_count == 2:
            var.set(question_full[question_count])
            question.pack()
            validate2.forget()
            validate3.pack()
        elif question_count == 3:
            var.set(question_full[question_count])
            question.pack()
            validate3.forget()
            validate4.pack()
        elif question_count == 4:
            question.forget()
            entry.forget()
            validate4.forget()
            tryagain = tk.Button(text='You have finished your 5 questions: do get some more!')
            tryagain.pack()
    else:
        incorrect1.forget()
        incorrect2.forget()
        correct.forget()
        incorrect1.pack()
        incorrect2.pack()
        entry.delete(0, tk.END)
        if question_count == 0:
            var.set(question_full[question_count])
            question.pack()
            validate0.forget()
            validate1.pack()
        elif question_count == 1:
            var.set(question_full[question_count])
            question.pack()
            validate1.forget()
            validate2.pack()
        elif question_count == 2:
            var.set(question_full[question_count])
            question.pack()
            validate2.forget()
            validate3.pack()
            
        elif question_count == 3:
            var.set(question_full[question_count])
            question.pack()
            validate3.forget()
            validate4.pack()
        elif question_count == 4:
            question.forget()
            entry.forget()
            validate4.forget()
            tryagain = tk.Button(text='You have finished your 5 questions: do get some more!')
            tryagain.pack()
             
           
def learningmode_init():
    question_formulate()
    drop()
    print(question_list)
    title = tk.Label(text="WELCOME TO LEARNING MODE")
    info = tk.Label(text='Learning Mode is a great way to improve your circular motion and gravitational field question technique/nEach example is taken from real-time satellites in orbit.')
    title.pack()
    info.pack()
    global validate0, validate1,validate2,validate3,validate4,question,var
    validate0 = tk.Button(root,text='Validate Answer',command=lambda: validate(0))
    validate1 = tk.Button(root,text='Validate Answer',command=lambda: validate(1))
    validate2 = tk.Button(root,text='Validate Answer',command=lambda: validate(2))
    validate3 = tk.Button(root,text='Validate Answer',command=lambda: validate(3))
    validate4 = tk.Button(root,text='Validate Answer',command=lambda: validate(4))
    var = StringVar()
    var.set(question_full[0])
    question = tk.Label(root,textvariable= var)
    question.pack()
    entry.pack()
    validate0.pack()
    #validate0.pack()
    root.mainloop()
learningmode = Button(text='Click Here for Learning Mode',command=lambda: learningmode_init())
learningmode.pack()
root.mainloop()
