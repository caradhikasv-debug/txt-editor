from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
window=Tk()
window.title("Text Editor")
window.geometry("600x500")
txtbox=Text(window)
txtbox.grid(row=0,column=1,sticky="nsew")
frame=Frame(window,relief="raised",bd=2)
frame.grid(row=0,column=0,sticky="ns")
def openfile():
    filepath=askopenfilename(filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if not filepath:
        return
    txtbox.delete(1.0,END)
    with open(filepath,"r") as inputfile:
        text=inputfile.read()
        txtbox.insert(END,text)
        inputfile.close()
    window.title(f"Text Editor - {filepath}")
btnopen=Button(frame,text="Open",command=openfile)
btnopen.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
def savefile():
    filepath=asksaveasfilename(defaultextension="txt",filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if not filepath:
        return
    with open(filepath,"w") as outputfile:
        text=txtbox.get(1.0,END)
        outputfile.write(text)
        outputfile.close()
    window.title(f"Text Editor - {filepath}")
btnsave=Button(frame,text="Save",command=savefile)
btnsave.grid(row=1,column=0,sticky="ew",padx=5)
window.mainloop()