def setup():
    size(400, 400)
    textSize(70)
      
def draw():
    clear()
    s = createShape()
    s.beginShape()
    s.fill(15,60,157,255)
    s.stroke(15,60,157,255)
    s.vertex(100, 100)
    s.vertex(100, 250)
    s.vertex(300, 250)
    s.vertex(300, 100)
    s.endShape(CLOSE)
    shape(s, 0, 0)
    
    s2 = createShape()
    s2.beginShape()
    s2.fill(8,18,40,255)
    s2.stroke(8,18,40,255)
    s2.vertex(120, 120)
    s2.vertex(120, 230)
    s2.vertex(280, 230)
    s2.vertex(280, 120)
    s2.endShape(CLOSE)
    shape(s2, 0, 0)

    fill(240, 180, 10)
    text("A", width/2-50, height/2)
    a = (hex(get(mouseX, mouseY)))
    if a == "FFF0B40A":
        fill(70, 230, 10)
        text("A", width/2-50, height/2)
        
    fill(240, 180, 10)
    text("S", width/2+10, height/2)
    a = (hex(get(mouseX, mouseY)))
    if key == "s" and keyPressed:
        fill(70, 230, 10)
        text("S", width/2+10, height/2) 
                 # proszę o wyrozumiałość, w stusunku do mnie i Aleksandry Sierhej, ponieważ obie komunikujemy się jeśli chodzi o wykonywanie zadań, dlatego niektóre aspekty mogą być identyczne. Pozdrawiam cielputko

    
  
    
