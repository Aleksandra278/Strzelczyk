def setup():
    size(600,600)
    global img
    img=loadImage("Gejsza.jpg") 
def draw():
    global img
    zaladowanoObrazek = None
    try:
        image(img, 100, 100, 400, 400)
        stroke(30,144,255)
    except:
        fill(0,0,0)
        textSize(20)
        text("Nieprawidlowy plik", 200, 300)
        stroke(255,0,0)
        strokeWeight(2)
    noFill()
    square(100, 100, 400)
