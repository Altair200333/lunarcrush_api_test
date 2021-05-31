class Plot:
    def __init__(self):
        self.data = []

    def addPoint(self, data):
        if data is not None:
            self.data.append(data)
        else:
            if len(self.data) == 0:
                self.data.append(-1)
                print("bad point")
            else:
                self.data.append(self.data[len(self.data)-1])
            
    def getData(self):
        return self.data
    