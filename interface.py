from tkinter import *
from tkinter import ttk
#imports tkinter, the library the interface is based on
from render import *
#imports the function render, which is used to open '3D'
from sat_database import *
#allows the sat_dict to be accessed, and by extension, URL2
from attributes import *
#accesses the attribute_refresh() and attribute_clear() functions
from questiongenerator import *
#used for Learning Mode
import tkinter as tk

root = Tk()
#creates a window
root.title("Satellite Interface")
#changes the title of the window from 'tk'
root.minsize(400, 300)
#creates a minimum size, that can be expanded on when more items are added i.e. satsearch
title = Label(root, text="Welcome to the Satellite Interface!")
title.pack(pady=1)
#packs the introductory title with some padding
instruct = Label(root, text="Select A Satellite Database to Use, then select 'SELECT' to confirm.")
ions = Label(root, text="You can then select 'BEGIN' to see the satellites, or search for a satellite")
instruct.pack()
ions.pack(padx=3)
#packs the instructions with a little padding at the bottom
global entry
entry = tk.Entry(root)
#globalises entry so it's contents can be accessed easily from functions 
def openSatelliteAttributeDisplay(URL2):
    # Toplevel object which will 
    # be treated as a new window
    newWindow = Toplevel(root)
    newWindow.title("Satellite Attribute Display")
    # sets the geometry of toplevel
    newWindow.minsize(1000,400)
    # A Label widget to show in toplevel
    count_sat = 0
#A placeholder that shows which satellite we're "on"
    ts = load.timescale()
    t = ts.now()
#gets the current time in epochs
    temp_sat = ''
    height = len(attribute_list)
    #assigns the 'height' of the table to be the length of attribute_list, or the number of satellites
    width = 5
    tree = ttk.Treeview(newWindow, column=("c1", "c2","c3","c4","c5"), show='headings', height=len(attribute_list))
    #creates the tree
    tree.column("# 1", anchor='center',width=125)
    tree.heading("# 1", text="Name")
    #creates heading one, called Name
    tree.column("# 2", anchor='center',width=150)
    tree.heading("# 2", text="Epoch")
    #creates heading two, called 'Epoch'
    tree.column("# 3", anchor='center',width=300)
    tree.heading("# 3", text="Coordinates")
    #creates heading three, called 'Coordinates'
    tree.column("# 4",anchor='center',width=290)
    tree.heading("# 4",text="Velocity")
    #etc
    tree.column("# 5",anchor='center',width=135)
    tree.heading("# 5",text="Speed")
    #etc...
    for i in range(len(attribute_list)):
        tree.insert('', 'end', text=i, values=(attribute_list[i]))
        #inserts satellites in order of their index in attribute_list[]
    tree.pack()
    #adds the tree to the window


def sat_search(URL2):
    var = StringVar()
    #creates a stringvar that can be changed on the fly, will be used to
    #  assign data to
    returned = Label(root,textvariable=var)
    #creates a label with the textvariable var, when var updates, returned updates
    labels = Label(root,text='NAME, EPOCH, COORDINATES, VELOCITY, SPEED')
    #created a basic label that tells the user what 
    returned.forget()
    #makes sure the there is only one instance of the label
    search = satsearch.get()
    #'gets' the content of the Entry form
    tempsat = ''
    #creates a temporary variable to store a satellite
    bigData = load.tle_file(URL2,reload=True)
    #loads the data of the selected database
    for i in range(len(bigData)):
        #iterates through all satellites in bigData
        tempsat = bigData[i]
        #assigns the temporary variable as a satellite in bigData
        if search == tempsat.name:
            #if the search IS a satellite in bigData
            var.set(attribute_list[i+1])
            #gets the attributes of that satellite
            labels.pack()
            #returns the order of the attributes
            returned.pack() 
            #shows the attributes
            return
        else:
            next
    var.set('SATELLITE NOT FOUND')
    #when the whole database has been iterated through
    returned.pack()
    #packs the result
    return



def select():
    SAD = Button(root, text="Open SAD", command=lambda: openSatelliteAttributeDisplay(URL2))
    #creates a button that runs and opens SAD
    threedee = Button(root, text="Open 3D Map", command=lambda: render(URL2))
    #creates a button that runs and opens the 3D map
    search = Button(root, text="SEARCH SAT", command=lambda: sat_search(URL2))
    #creates the button that is used for sat_search
    SAD.forget()
    threedee.forget()
    #makes sure there is only one version of the SAD and threedee buttons at any one time
    global satsearch
    #makes satsearch global, so it can be accessed from other functions
    satsearch = tk.Entry(root)
    #creates an entry widget
    sat_select = satellite_filter.get(ANCHOR)
    #gets the User selected database in text
    if sat_select != '':
    #if the User actually has selected a database before selecting 'SELECT'
        filter_select.config(text=satellite_filter.get(ANCHOR))
        #gets the text of the selected database and changes the name of the button to be the database name
        satsearch.pack()
        search.pack()
        #packs the entry widget and the 'search sat' button
        URL2 = str(sat_dict[sat_select])
        #loads the corresponding url of the text
        bigData = load.tle_file(URL2, reload=True)
        #loads the Data
        tempVar = StringVar()
        #creates another StringVar
        Numb_sat = 'The Number of Satellites in this database is', len(bigData)
        #creates a temporary variable
        tempVar.set(Numb_sat)
        #assigns the text of Numb_sat [along with the length of bigData as a string] to tempVar
        sat_count = Label(root, textvariable=tempVar)
        #creates a label that uses tempVar as a textvariable
        sat_count.pack()
        #packs sat_count
        attribute_refresh(len(bigData),URL2)
        #refreshes the database with the URL that is specified
        SAD.pack()
        threedee.pack()
        #packs the buttons

satellite_filter = Listbox(root, height= 8, width=23)
satellite_filter.pack(pady=10)
#creates the lisbox that the database names go in

def drop():
    title.forget()
    satellite_filter.forget()
    filter_select.forget()
    instruct.forget()
    ions.forget()
    learningmode.forget()
    #'drops' or forgets everything on the main interface screen
    


for item in sat_dict:
    satellite_filter.insert(END, item)
#appends items from satellite types into the dropdown list
filter_select = Button(root, text='SELECT', command=select)
#creates the 'SELECT' button with function select
filter_select.pack(pady=2)
learningmode = Button(text='Click Here for Learning Mode',command=lambda: learningmode_SAD())
#creates a button that initiates learningmode
learningmode.pack(pady=1)

def validate(question_count):
    tempvar = StringVar()
    temp_q = question_list[question_count]
    tempvar.set(temp_q[1])
    #sets tempvar to the solution
    incorrect1 = tk.Label(text='Sorry, that is incorrect, the correct answer is ',fg='red')
    incorrect2 = tk.Label(textvariable=tempvar,fg='red')
    #prints the actual soluton
    correct = tk.Label(text='Correct!',fg='green')
    attempt = entry.get()
    #gets the users attempt, when 'validate' is selected
    
    if attempt == temp_q[1]:
        correct.pack()
        entry.delete(0, tk.END)
        #if correct, return correct and clear the entry widget
    else:
        incorrect1.pack()
        incorrect2.pack()
        entry.delete(0, tk.END)
        #if incorrect, return incorrect with the correct answer, clear the entry widget
    
    if question_count == 0:
        var.set(question_full[question_count + 1])
        validate0.forget()
        validate1.pack()
    elif question_count == 1:
        var.set(question_full[question_count + 1])
        question.pack()
        validate1.forget()
        validate2.pack()
    elif question_count == 2:
        var.set(question_full[question_count + 1])
        question.pack()
        validate2.forget()
        validate3.pack()
    elif question_count == 3:
        var.set(question_full[question_count + 1])
        question.pack()
        validate3.forget()
        validate4.pack()

        #these 4 question numbers just set the var to the new solution, unpack the previous validation
        #and pack the new one
    elif question_count == 4:
        question.forget()
        entry.forget()
        validate4.forget()
        tryagain = tk.Button(text='You have finished your 5 questions: do get some more!',command=lambda: learningmode_SAD())
        tryagain.pack()
        #this creates a new button that re-initialises the learning mode
             
           
def learningmode_SAD():
    question_formulate()
    #formulates the questions
    drop()
    #gets rid of everything on the interface screent
    title = tk.Label(text="WELCOME TO LEARNING MODE")
    info = tk.Label(text='Learning Mode is a great way to improve your circular motion and gravitational field question technique. Each example is taken from real-time satellites in orbit.')
    info2 = tk.Label(text='All questions can be answered by using the OCR A A Level Physics Formula Booklet')
    title.pack()
    info.pack(pady=1)
    info2.pack(pady=1)
    #packs all of the instructions with a little padding
    global validate0, validate1,validate2,validate3,validate4,question,var
    #allows all of the validate commands to be accessed by the validate() function
    validate0 = tk.Button(root,text='Validate Answer 1',command=lambda: validate(0))
    validate1 = tk.Button(root,text='Validate Answer 2',command=lambda: validate(1))
    validate2 = tk.Button(root,text='Validate Answer 3',command=lambda: validate(2))
    validate3 = tk.Button(root,text='Validate Answer 4',command=lambda: validate(3))
    validate4 = tk.Button(root,text='Validate Answer 5',command=lambda: validate(4))
    var = StringVar()
    var.set(question_full[0])
    #creates var, sets it to the first question
    question = tk.Label(root,textvariable= var)
    #creates a label with var as a textvariable
    question.pack()
    entry.pack()
    #packs the entries
    for i in range(5):
        temp = question_list[i]
        #iterates through the questions
        print(temp[1])
        #prints the answers in the console for testing
    validate0.pack()
    root.mainloop()

root.mainloop()
