

class Person:
    # constructor:
    def __init__(self, name):
        self.name = name
        self.bat = 0
        self.hit = 0
        self.avg = 0

    def getname(self):
        return self.name

    def getBat(self):
        return self.bat

    def getHit(self):
        return self.hit

    def updateHit(self,hit):
        hit_old = self.hit
        self.hit = hit_old + float(hit)

    def updateBat(self,bat):
        bat_old = self.bat
        self.bat = bat_old + float(bat)

    def updateAve(self,avg):
        self.avg = avg

    def format_name(self):
        return "Gotta love to eat " + self.name