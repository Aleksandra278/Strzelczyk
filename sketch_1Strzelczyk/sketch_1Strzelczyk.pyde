def setup(): 
    size(1200,600)
def draw():
        print(height,width,mouseX,mouseY,mousePressed)
        rect(182,300,180,180)
        if mousePressed:
            print(height,width,mouseX,mouseY,mousePressed)
            rect(182,300,180,180)
            circle(mouseX,mouseY,25)
        else:
            print(height,width,mouseX,mouseY,mousePressed)
            rect(182,300,180,180)
        
 
