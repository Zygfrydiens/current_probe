from tkinter import *
#from pubsub import *


class View:
    def __init__(self, parent):
        self.root = parent
        self.root.resizable(False, False)

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.f1 = Frame(self.root, highlightbackground="#a5a5ad", highlightthickness=1, width=100, height=100)
        self.f2 = Frame(self.root, highlightbackground="#a5a5ad", highlightthickness=1, width=900, height=400)
        self.f3 = Frame(self.root, highlightbackground="#a5a5ad", highlightthickness=1, width=900, height=400)
        self.import_button = Button(self.f1, text="Import", command=self.import_pressed, width=10, height=1)
        self.export_button = Button(self.f1, text="Export", command=self.export_pressed, width=10, height=1)


    def setup_layout(self):
        self.f1.grid(row=0, column=0)
        self.f2.grid(row=1, column=0)
        self.f3.grid(row=2, column=0)
        self.import_button.grid(row=0, column=0)
        self.export_button.grid(row=1, column=0)

    def import_pressed(self):
        print("Import pressed")

    def export_pressed(self):
        print("Print notes pressed")




# Testing
if __name__ == "__main__":
    print("running view")
    root = Tk()
    view = View(root)
    view.setup()
    root.mainloop()