from tkinter import *
from tkinter import filedialog
from pubsub import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure


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
        self.current_figure = Figure(figsize=(9, 5), dpi=100)
        self.voltage_figure = Figure(figsize=(9, 5), dpi=100)

    def setup_layout(self):
        self.f1.grid(row=0, column=0)
        self.f2.grid(row=1, column=0)
        self.f3.grid(row=2, column=0)
        self.import_button.grid(row=0, column=0)
        self.export_button.grid(row=1, column=0)

    def plot(self, title, y_label, x, y, frame, figure):
        self.ax = figure.add_subplot(111)
        self.ax.set_title(title)
        self.ax.set_xlabel("f [Hz]")
        self.ax.set_ylabel(y_label)
        self.ax.set_xscale("log")
        self.ax.grid(which='minor', color='#CCCCCC', linestyle=':')
        self.ax.grid(linestyle='-', linewidth=1)
        self.ax.plot(x, y)
        self.canvas = FigureCanvasTkAgg(figure, master=frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0)

    def open_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=(("Data files", ".dat"), ("Text files", ".txt"),
                                                           ("All files", "*.*")))
        print(self.file_path)

    def import_pressed(self):
        print("Import pressed")
        pub.sendMessage("Import button pressed")

    def export_pressed(self):
        print("Export pressed")
        pub.sendMessage("Export button pressed")


# Testing
if __name__ == "__main__":
    print("running view")
    root = Tk()
    view = View(root)
    view.setup()
    root.mainloop()
