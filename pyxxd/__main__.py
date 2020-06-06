import os
import sys
import tkinter
import subprocess
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox

FILENAME = ""
FILENMAEOUT = ""


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
    #chars = len(event.widget.get("1.0", "end-1c"))
    new_text = text.get('1.0', 'end')
    out = subprocess.run(["xxd", "-r", "-g1", "-", "-"], input=new_text.encode("UTF-8"), stdout=subprocess.PIPE)
    text.insert("1.0", out.stdout)

def openfile():
    window.master.title(os.path.basename(FILENAME))
    btnsv.config(state = tkinter.NORMAL)
    btnsvs.config(state = tkinter.NORMAL)
    text.config(state = tkinter.NORMAL)
    out = subprocess.run(["xxd", "-g1", FILENAME], stdout=subprocess.PIPE)
    if out.returncode == 0:
        text.insert("1.0", out.stdout)
    else:
        messagebox.showerror("Error", "Can`t open file")

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
    out = subprocess.run(["xxd", "-r", "-g1", "-", out_file], input=new_text.encode("UTF-8"), stdout=subprocess.PIPE)
    if out.returncode == 0:
        text.delete('1.0', 'end')
        window.master.title("pyxxd")
        btnsv.config(state=tkinter.DISABLED)
        btnsvs.config(state=tkinter.DISABLED)
        text.config(state=tkinter.DISABLED)
    else:
        messagebox.showerror("Error", "Can`t write to file")
    FILENAMEOUT = ""

def saveasb():
    new_file = asksaveasfilename()
    if new_file:
        new_text = text.get('1.0', 'end')
        out = subprocess.run(["xxd", "-r", "-g1", "-", new_file], input=new_text.encode("UTF-8"), stdout=subprocess.PIPE)
        if out.returncode == 0:
            text.delete('1.0', 'end')
            window.master.title("pyxxd")
            btnsv.config(state=tkinter.DISABLED)
            btnsvs.config(state=tkinter.DISABLED)
            text.config(state=tkinter.DISABLED)
        else:
            messagebox.showerror("Error", "Can`t write to file")
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
