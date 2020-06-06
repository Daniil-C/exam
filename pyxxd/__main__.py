import os
import tkinter
from tkinter.filedialog import askopenfilename

FILENAME = ""


def openb():  
    FILENAME = askopenfilename()
    window.master.title(os.path.basename(FILENAME))
    btnsv.config(state = tkinter.NORMAL)
    text.config(state = tkinter.NORMAL)
    with open(FILENAME, "r") as fin:
        src_text = fin.read();
    text.insert("1.0", src_text)

def saveb():
    new_text = text.get('1.0', 'end')
    with open(FILENAME, "w") as fout:
        fout.write(new_text)

if __name__ == "__main__":
    window = tkinter.Frame()
    window.master.rowconfigure(0, weight=1)
    window.master.columnconfigure(0, weight=1)
    window.grid(row=0, column=0, sticky="NEWS")
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)

    btns = tkinter.Frame(master = window)
    btns.grid(row=0, column=0, sticky="NEWS")
    btnop = tkinter.Button(btns, text="Open", command=openb)
    btnop.grid(column=0, row=0, sticky="NW")

    btnsv = tkinter.Button(btns, text="Save", command=saveb, state = tkinter.DISABLED)
    btnsv.grid(column=1, row=0, sticky="NW")

    text = tkinter.Text(window, width=80, height=20, state = tkinter.DISABLED)
    text.grid(column=0, row=1, sticky="NEWS")
    scroll = tkinter.Scrollbar(window)
    scroll.config(command=text.yview)
    scroll.grid(column=1, row=1, sticky="NS")
    text.config(yscrollcommand=scroll.set)
    tkinter.mainloop();
