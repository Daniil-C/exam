import os
import tkinter
from tkinter.filedialog import askopenfilename

FILENAME = ""

def clicked():  
    FILENAME = askopenfilename()


if __name__ == "__main__":
    window = tkinter.Frame()
    window.master.rowconfigure(0, weight=1)
    window.master.columnconfigure(0, weight=1)
    window.grid(sticky="NEWS", row=0, column=0)
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    btn = tkinter.Button(window, text="Open", command=clicked)  
    btn.grid(column=0, row=0, sticky="NW")
    window.master.title(os.path.basename(FILENAME))
    tkinter.mainloop();
