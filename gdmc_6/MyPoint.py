class MyPoint():
    def __init__(self, x, z, gn, hn, father=None):
        self.x = x
        self.z = z
        self.gn = gn
        self.hn = hn
        self.fn = gn + hn
        self.father = father
        self.son = None

    def getInList(self, pointList):
        for p in pointList:
            if self.x == p.x and self.z == p.z:
                return p
        return None
