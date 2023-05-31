class UndergroundSystem:

    def __init__(self):
        self.dict1 = {}
        self.dict2 = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.dict1[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        s, st = self.dict1[id]
        del self.dict1[id]
        if (s, stationName) in self.dict2.keys():
            a, b = self.dict2[(s, stationName)]
            self.dict2[(s, stationName)] = (a + 1, b + (t - st))
        else:
            self.dict2[(s, stationName)] = (1, t - st)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        a, b = self.dict2[(startStation, endStation)]
        return b / a
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)