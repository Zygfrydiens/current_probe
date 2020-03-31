import xlsxwriter
from tkinter import messagebox


class Model:
    def __init__(self):
        self.file_info = {}
        self.info = {}
        self.x = []
        self.y = []
        self.k = []
        self.y_current = []

    def read_file(self, file_path):
        if not file_path:
            print("No file has been chosen")
        else:
            self.file = open(file_path, "r")
            for index, line in enumerate(self.file):
                self.fields = line.split(";")
                if index <= 27:
                    self.info[self.fields[0]] = self.fields[1] + self.fields[2]
                else:
                    self.x.append((float(self.fields[0].replace(',', '.'))))
                    self.y.append((float(self.fields[1].replace(',', '.'))))
            self.k = [(0.614045364377758 + (923325.475889253 / (31283.7193617478 + x + 9.96874998835705
                            * (10 ** (-7)) * (x ** 2) + 1.42482554551897 * (10 ** (-11)) * (x ** 3))) - 4.05216298020406
                            * (10 ** (-9)) * x) for x in self.x]

            for i in range(0, len(self.y)):
                self.y_current = [self.k[c] + self.y[c] for c in range(len(self.y))]

            self.file_info[file_path] = self.info

    def export_file(self, x, y, y_current, info, file_path):
        if not file_path:
            print("No file has been chosen")
        else:
            try:
                self.workbook = xlsxwriter.Workbook(file_path)
                self.worksheet = self.workbook.add_worksheet("Data")
                self.worksheet.write("A1", "f [Hz]")
                self.worksheet.write("B1", "U [dBuV]")
                self.worksheet.write("C1", "I [dBuA]")
                for i, num in enumerate(x):
                    self.worksheet.write('A' + str(i+2), x[i])
                    self.worksheet.write('B' + str(i+2), y[i])
                    self.worksheet.write('C' + str(i+2), y_current[i])
                self.workbook.close()
            except xlsxwriter.exceptions.FileCreateError:
                messagebox.showerror("Error", "This file is being used. Before saving close the file!")

    def clear_all(self):
        self.file_info.clear()
        self.info.clear()
        self.x.clear()
        self.y.clear()
        self.k.clear()
        self.y_current.clear()


