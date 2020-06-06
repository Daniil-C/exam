import os
import sys
import tkinter
import subprocess
from tkinter.filedialog import askopenfilename, asksaveasfilename

FILENAME = ""
FILENMAEOUT = ""

def openfile():
    window.master.title(os.path.basename(FILENAME))
    btnsv.config(state = tkinter.NORMAL)
    btnsvs.config(state = tkinter.NORMAL)
    text.config(state = tkinter.NORMAL)
    out = subprocess.run(["xxd", "-g1", FILENAME], stdout=subprocess.PIPE)
    text.insert("1.0", out.stdout)

def openb():
    global FILENAME
    FILENAME = askopenfilename()
    if FILENAME:
        openfile();

def saveb():
    global FILENAMEOUT
    new_text = text.get('1.0', 'end')
    out_file = FILENAME
    if FILENAMEOUT != "":
        out_file = FILENAMEOUT
    print(FILE)
    out = subprocess.run(["xxd", "-r", "-g1", "-", out_file], input=new_text.encode("UTF-8"), stdout=subprocess.PIPE)
    text.delete('1.0', 'end')
    window.master.title("pyxxd")
    btnsv.config(state=tkinter.DISABLED)
    btnsvs.config(state=tkinter.DISABLED)
    text.config(state=tkinter.DISABLED)
    FILENAMEOUT = ""

def saveasb():
    new_file = asksaveasfilename()
    if new_file:
        new_text = text.get('1.0', 'end')
        out = subprocess.run(["xxd", "-r", "-g1", "-", new_file], input=new_text.encode("UTF-8"), stdout=subprocess.PIPE)
        text.delete('1.0', 'end')
        window.master.title("pyxxd")
        btnsv.config(state=tkinter.DISABLED)
        btnsvs.config(state=tkinter.DISABLED)
        text.config(state=tkinter.DISABLED)
        FILENAMEOUT = ""

if __name__ == "__main__":
    n = len(sys.argv)
    FILENAME = sys.argv[1] if n >= 2 else ""
    FILENAMEOUT = sys.argv[2] if n >= 3 else ""
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

    btnsv = tkinter.Button(btns, text="Save", command=saveb, state=tkinter.DISABLED)
    btnsv.grid(column=1, row=0, sticky="NW")

    btnsvs = tkinter.Button(btns, text="Save As", command=saveasb, state=tkinter.DISABLED)
    btnsvs.grid(column=2, row=0, sticky="NW")

    text = tkinter.Text(window, width=90, height=25, state=tkinter.DISABLED)
    text.grid(column=0, row=1, sticky="NEWS")
    scroll = tkinter.Scrollbar(window)
    scroll.config(command=text.yview)
    scroll.grid(column=1, row=1, sticky="NS")
    text.config(yscrollcommand=scroll.set)
    if (FILENAME != ""):
        openfile();
    tkinter.mainloop();
