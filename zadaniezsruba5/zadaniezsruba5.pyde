import random
add_library('pdf')
    
class Nos(): 
    uderz = 0 
    def __init__(self, arg_x, arg_y, arg_r):
        self.obrot = 0
        self.wcisniety = False
        self.x = arg_x
        self.y = arg_y
        self.r = arg_r
    def rysuj(self):
        arc(self.x, self.y, self.r, self.r, 0+radians(self.obrot+90), PI+ radians(self.obrot+90), PIE)
        arc(self.x, self.y, self.r, self.r, 0+radians(self.obrot+270), PI+ radians(self.obrot+270), PIE) 
    def obroc(self, stopnie):
        self.obrot += stopnie
    
    def kliknij(self): 
        Nos.uderz+=1 
        self.wcisniety = not self.wcisniety 
        if self.wcisniety:
            fill(200,100,0) 
        else:
            fill(0,100,200)
        
def setup():
    size(400, 400) 
    global nos 
    nos = Nos(width/2, height/2, 50)
        
def mouseClicked(): 
    nos.kliknij()
    
def mouseWheel(event): 
    nos.obroc(10) 
    print(nos.obrot) 
    
def draw(): 
    background(120)
    screw = createShape()
    screw.beginShape()
    screw.fill(255,20,30,100)
    screw.stroke(0,0,0,255)
    screw.vertex(90, 100)
    screw.vertex(90, 140)
    screw.vertex(120, 170)
    screw.vertex(180, 170)
    screw.vertex(210, 140)
    screw.vertex(210, 100)
    screw.vertex(180, 70)
    screw.vertex(120, 70)
    screw.vertex(90, 100)
    screw.endShape(CLOSE) 
    shape(screw, 50, 80)
    nos.rysuj() 
    print(Nos.uderz)  
    
