import os
import tkinter
import subrocess
from tkinter.filedialog import askopenfilename

FILENAME = ""

def openb():
    global FILENAME
    FILENAME = askopenfilename()
    window.master.title(os.path.basename(FILENAME))
    btnsv.config(state = tkinter.NORMAL)
    text.config(state = tkinter.NORMAL)
    out = subrocess.run(["xxd", "-g1", FILENAME], capture_output=True, shell=True)
    text.insert("1.0", out.stdout)

def saveb():
    pass
    # new_text = text.get('1.0', 'end')
    # with open(FILENAME, "w") as fout:
    #     fout.write(new_text)
    # text.delete('1.0', 'end')
    # window.master.title("pyxxd")
    # btnsv.config(state = tkinter.DISABLED)
    # text.config(state = tkinter.DISABLED)


if __name__ == "__main__":
    window = tkinter.Frame()
    window.master.rowconfigure(0, weight=1)
    window.master.columnconfigure(0, weight=1)
    window.master.title("pyxxd")
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
