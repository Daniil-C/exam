import os
import tkinter
from tkinter.filedialog import askopenfilename

FILENAME = ""

def openb():  
    FILENAME = askopenfilename()
    window.master.title(os.path.basename(FILENAME))

def saveb():
    pass

if __name__ == "__main__":
    window = tkinter.Frame()
    window.master.rowconfigure(0, weight=1)
    window.master.columnconfigure(0, weight=1)
    window.grid(sticky="NEWS", row=0, column=0)
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)

    btnop = tkinter.Button(window, text="Open", command=openb)
    btnop.grid(column=0, row=0, sticky="NW")

    btnsv = tkinter.Button(window, text="Save", command=saveb)
    btnsv.grid(column=0, row=0, sticky="NW")

    text = tkinter.Text(window, width=80, height=20)
    text.grid(column=0, row=1, sticky="NEWS")
    scroll = tkinter.Scrollbar(window)
    scroll.config(command=text.yview)
    scroll.grid(column=1, row=1, sticky="NS")
    text.config(yscrollcommand=scroll.set)
    tkinter.mainloop();
