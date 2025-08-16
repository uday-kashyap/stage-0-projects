from tkinter import *
import tkinter.messagebox as tmb
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

class Notepad(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x500")
        self.title("Untitled - Notepad")
        self.iconbitmap("notepad.ico")
        self.last_saved_file = None
        self.setup_editor()
        self.features_panel()

    @staticmethod
    def myfunc():
        print("Still to be developed")

    def openFile(self):
        file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file:
            try:
                with open(file) as f:
                    content = f.read()
            except Exception as e:
                print(e)
            else:
                self.title(f"{os.path.basename(file)} - Notepad")
                self.mainframe.delete(1.0, END)
                self.mainframe.insert(1.0, content)

    def newFile(self):
        self.title("Untitled - Notepad")
        self.mainframe.delete("1.0", END)

    def saveFile(self):
        file = asksaveasfilename(initialfile="Untitled.txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file:
            self.last_saved_file = file
            with open(file, "w") as f:
                f.write(self.mainframe.get(1.0, END))
            self.title(f"{os.path.basename(file)} - Notepad")

    def cut(self):
        self.mainframe.event_generate(("<<Cut>>"))

    def copy(self):
        self.mainframe.event_generate(("<<Copy>>"))

    def paste(self):
        self.mainframe.event_generate(("<<Paste>>"))

    def on_exit(self):
        if not self.last_saved_file:
            if tmb.askyesno("Quit", "Do you really want to exit without saving?"):
                self.destroy()
        else:
            self.destroy()

    def about(self):
        tmb.showinfo("About", "Created by - Uday Kashyap\n(as one of the project for Stage 0 projects)")

    def appversion(self):
        tmb.showinfo("App Version", "Version: ∞")

    def undo(self):
        try:
            self.mainframe.edit_undo()
        except TclError:
            pass  # No more actions to undo

    def redo(self):
        try:
            self.mainframe.edit_redo()
        except TclError:
            pass  # No more actions to redo



    def features_panel(self):

        main_panel = Menu(self)
        self.config(menu=main_panel)

        # 'File' feature 
        file_panel = Menu(main_panel, tearoff=0)
        file_panel.add_command(label="Open", command=self.openFile)
        file_panel.add_command(label="New", command=self.newFile)
        file_panel.add_separator()
        file_panel.add_command(label="Save", command=self.saveFile)
        file_panel.add_separator()
        file_panel.add_command(label="Exit", command=self.on_exit)
        main_panel.add_cascade(label="File", menu=file_panel)

        # 'Edit' feature
        edit_panel = Menu(main_panel, tearoff=0)
        edit_panel.add_command(label="Undo", command=self.undo, accelerator="Ctrl+Z")
        self.bind("<Control-z>", lambda e: self.undo())
        edit_panel.add_command(label="Redo", command=self.redo, accelerator="Ctrl+Y")
        self.bind("<Control-y>", lambda e: self.redo())
        edit_panel.add_separator()
        edit_panel.add_command(label="Cut", command=self.cut)
        edit_panel.add_command(label="Copy", command=self.copy)
        edit_panel.add_command(label="Paste", command=self.paste)
        main_panel.add_cascade(label="Edit", menu=edit_panel)

        # 'View' feature
        view_panel = Menu(main_panel, tearoff=0)
        view_panel.add_command(label="About", command=self.about)
        view_panel.add_separator()
        view_panel.add_command(label="Version", command=self.appversion)
        main_panel.add_cascade(label="View", menu=view_panel)

    def setup_editor(self):
        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.mainframe = Text(self, yscrollcommand= scrollbar.set, undo=True, autoseparators=True, maxundo=-1)
        self.mainframe.pack(fill=BOTH, expand=True)
        scrollbar.config(command=self.mainframe.yview)

if __name__ == '__main__':
    Notepad().mainloop()