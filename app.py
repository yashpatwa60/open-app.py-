import tkinter as tk 
from tkinter import filedialog, Text
import os


root = tk.Tk()

apps = []                                               #saving data in this array

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempapps = f.read()                             #Removing whitespace from array using x.strip()
        tempapps = tempapps.split(',')
        apps = [x for x in tempapps if x.strip()]

def addApp():

    for widget in frame.winfo_children():              # widget.destroy will clean the screen before adding a new app or exe file
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (('executables','*.exe'),("all files", '*.*')))
    apps.append(filename)
    print(filename)

    for app in apps:
        label = tk.Label(frame, text = app , bg = "gray")
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)                              #Running the application



canvas = tk.Canvas(root, height =700, width =700, bg = "#000")
canvas.pack()

frame = tk.Frame(root, bg = "white")
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

openFile = tk.Button(root, text = "Open file" , fg = "white", bg = "#263D42" ,command = addApp , padx = 10, pady = 5  )
openFile.pack()

runApps = tk.Button(root, text = "Run apps" , fg = "white", bg = "#263D42", padx = 10, pady = 5, command = runApps )
runApps.pack()

for app in apps:

    label = tk.Label(frame, text = app)
    label.pack()

root.mainloop()


with open("save.txt", 'w') as f:
    for app in apps:

        f.write(app + ',')
