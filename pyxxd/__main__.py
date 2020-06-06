from tkinter import Tk
from tkinter.filedialog import askopenfilename

FILENAME = ""

def clicked():  
    Tk().withdraw()
	FILENAME = askopenfilename()


if __name__ == "__main__":
	window = Frame()
	window.master.rowconfigure(0, weight=1)
	window.master.columnconfigure(0, weight=1)
	window.grid(sticky="NEWS", row=0, column=0)
	window.rowconfigure(0, weight=1)
	window.columnconfigure(0, weight=1)
	btn = Button(window, text="Open", command=clicked)  
	btn.grid(column=0, row=1, sticky=NEWS)
	print(FILENAME)
	mainloop();
