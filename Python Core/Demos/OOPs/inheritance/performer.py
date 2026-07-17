from singer import Singer
from dancer import Dancer

class Performer(Singer,Dancer):
    def __init__(self,song_type,dance_style,exp):
        Singer.__init__(self,song_type)
        Dancer.__init__(self,dance_style)
        self.exp= exp
    def show(self):
        print("Display method of Performer")

p1 = Performer('Clasical','Kathak',2)
p1.display()