import os
import sys
import tkinter
import subprocess
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox

FILENAME = ""
FILENMAEOUT = ""
MOD = False
FIRST = True

class CustomText(tkinter.Text):
    def __init__(self, *args, **kwargs):
        tkinter.Text.__init__(self, *args, **kwargs)
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, command, *args):
        cmd = (self._orig, command) + args
        result = self.tk.call(cmd)

        if command in ("insert", "delete", "replace"):
            self.event_generate("<<TextModified>>")
        return result

def onModification(event):
    global MOD
    print(MOD)
    pos = text.index("insert")
    if not MOD:
        MOD = True
        #chars = len(event.widget.get("1.0", "end-1c"))
        new_text = text.get('1.0', 'end')
        print(new_text[10:-16].split(" "))
        nul = False
        for i in new_text[10:-16].split(" "):
            print(len(i), nul)
            if len(i) == 0:
                nul = True
            if len(i) % 2 == 1 or (len(i) > 0 and nul):
                MOD = False
                return
        out = subprocess.run(["xxd", "-r", "-g1", "-", "-"], input=new_text[:-16].encode("UTF-8"), stdout=subprocess.PIPE)
        out = subprocess.run(["xxd", "-g1"], input=out.stdout, stdout=subprocess.PIPE)
        print(out.stdout, out.returncode)
        if out.returncode == 0:
            text.delete('1.0', 'end')
            text.insert("1.0", out.stdout)
        text.mark_set("insert", pos)
        MOD = False

def openfile():
    global FILENAMEOUT
    global FIRST
    if FIRST:
        FIRST = False
    else:
        FILENAMEOUT = ""
    global MOD
    window.master.title(os.path.basename(FILENAME))
    btnsv.config(state = tkinter.NORMAL)
    btnsvs.config(state = tkinter.NORMAL)
    text.config(state = tkinter.NORMAL)
    out = subprocess.run(["xxd", "-g1", FILENAME], stdout=subprocess.PIPE)
    if out.returncode == 0:
        MOD = True
        text.insert("1.0", out.stdout)
        Mod = False
    else:
        messagebox.showerror("Error", "Can`t open file")
    MOD = False

def openb():
    global FILENAME
    FILENAME = askopenfilename()
    if FILENAME:
        openfile();

def saveb():
    global FILENAMEOUT
    global MOD
    MOD = True
    new_text = text.get('1.0', 'end')
    out_file = FILENAME
    if FILENAMEOUT != "":
        out_file = FILENAMEOUT
    out = subprocess.run(["xxd", "-r", "-g1", "-", out_file], input=new_text.encode("UTF-8"), stdout=subprocess.PIPE)
    if out.returncode != 0:
        messagebox.showerror("Error", "Can`t write to file")
    MOD = False
    FILENAMEOUT = ""

def saveasb():
    global MOD
    MOD = True
    new_file = asksaveasfilename()
    if new_file:
        new_text = text.get('1.0', 'end')
        out = subprocess.run(["xxd", "-r", "-g1", "-", new_file], input=new_text.encode("UTF-8"), stdout=subprocess.PIPE)
        if out.returncode != 0:
            messagebox.showerror("Error", "Can`t write to file")
        FILENAMEOUT = ""
    MOD = False

def undo():
    try:
        text.edit_undo()
    else:
        pass

def redo():
    try:
        text.edit_redo()
    else:
        pass

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

    btnun = tkinter.Button(btns, text="Undo", command=undo, state=tkinter.DISABLED)
    btnun.grid(column=3, row=0, sticky="NW")

    btnre = tkinter.Button(btns, text="Redo", command=redo, state=tkinter.DISABLED)
    btnre.grid(column=4, row=0, sticky="NW")

    text = CustomText(window, width=90, height=25, state=tkinter.DISABLED, font="fixed")
    text.grid(column=0, row=1, sticky="NEWS")
    text.bind("<<TextModified>>", onModification)
    scroll = tkinter.Scrollbar(window)
    scroll.config(command=text.yview)
    scroll.grid(column=1, row=1, sticky="NS")
    text.config(yscrollcommand=scroll.set)
    if (FILENAME != ""):
        openfile();
    tkinter.mainloop();
