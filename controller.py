from view import *
from model import *
from tkinter import *
from pubsub import pub

class Controller:
    def __init__(self, parent):
        self.parent = parent
        self.model = Model()
        self.view = View(parent)
        self.view.setup()

        pub.subscribe(self.load_file, "Import button pressed")
        pub.subscribe(self.export_file, "Export button pressed")

    def load_file(self):
        print("controller - loading file")
        self.view.open_file()
        self.model.read_file(self.view.file_path_open)
        self.view.plot("Voltage", "U [dBuV]", self.model.x, self.model.y, self.view.f2, self.view.voltage_figure)
        self.view.plot("Current", "I [dBua]", self.model.x, self.model.y_current, self.view.f3, self.view.current_figure)

    def export_file(self):
        self.view.save_file()
        self.model.export_file(self.model.x, self.model.y, self.model.y_current, self.model.info,
                               self.view.file_path_save)
        print("controller - exporting file")


if __name__ == "__main__":
    root = Tk()
    app = Controller(root)
    root.mainloop()