def setup():
    size(600,600)
    global img
    img=loadImage("Gejsza.jpg")
    textSize(20)
    strokeWeight(2)
def draw():
    global img
    try:
        image(img, 100, 100, 400, 400) # tylko ten fragment jest neuralgiczny
    except:
        fill(0,0,0)
        text("Nieprawidlowy plik", 200, 300)
        stroke(255,0,0)
    else:
        stroke(30,144,255)
        noFill()
    finally:
        square(100, 100, 400)

# 1,5pkt
