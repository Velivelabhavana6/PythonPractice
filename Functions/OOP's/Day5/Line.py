class Line:
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)
    
coor1=(3,2)
coor2=(2,8)
myLine=Line(coor1,coor2)
print(myLine.distance())  
print(myLine.slope())