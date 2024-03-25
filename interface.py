from tkinter import *
from tkinter import ttk
from render import *
from sat_database import *
from attributes import *


root = Tk()
root.title("Satellite Interface")
root.minsize(600, 600)
title = Label(root, text="Welcome to the Satellite Interface!")
title.pack()
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
        #render(URL2)
    
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

for item in sat_dict:
    satellite_filter.insert(END, item)
#appends items from satellite types into the dropdown list
filter_select = Button(root, text='SELECT', command=select)
filter_select.pack(pady= 10)


root.mainloop()
