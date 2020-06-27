class Kwadrat():
    def __init__(self, bok):
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
class Kwadracik(Kwadrat):
    def rysujObiekt(self,x,y):
        self.sketch(x,y)
    def paski(self, x, y, paski):
        przestrzen = self.bok/paski
        xLinii = 0
        for pasek in range(0, paski):
            line(x+xLinii, y, x+xLinii, y+self.bok)
            xLinii +=przestrzen
    def malujkwadrat(self,a,b,c):
        fill(a,b,c)
        
def setup():
    size(140,150)
    background(255,255,255)
    malyKwadracik=Kwadracik(30)
    malyKwadracik.malujkwadrat(178,34,34)
    malyKwadracik.rysujObiekt(10,55)
    malyKwadracik.paski(10,55,5)
    duzyKwadracik=Kwadracik(60)
    duzyKwadracik.malujkwadrat(0,0,0)
    duzyKwadracik.rysujObiekt(60,40)
    
