class Model:
    def __init__(self):
        self.info = {}
        self.x = []
        self.y = []
        self.k = []
        self.y_current = []

    def read_file(self, file_path):
        self.file = open(file_path, "r")
        for index, line in enumerate(self.file):
            self.fields = line.split(";")
            if index <= 28:
                self.info[self.fields[0]] = self.fields[1] + self.fields[2]
            else:
                self.x.append((float(self.fields[0].replace(',', '.'))))
                self.y.append((float(self.fields[1].replace(',', '.'))))
        self.k = [(0.614045364377758 + (923325.475889253 / (31283.7193617478 + x + 9.96874998835705
                        * (10 ** (-7)) * (x ** 2) + 1.42482554551897 * (10 ** (-11)) * (x ** 3))) - 4.05216298020406
                        * (10 ** (-9)) * x) for x in self.x]
        for i in range(0, len(self.y)):
            self.y_current = [self.k[c] + self.y[c] for c in range(len(self.y))]
