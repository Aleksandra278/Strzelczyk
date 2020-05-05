import random
add_library('pdf')
 
def setup():
    size(400,550) # to nie do końca proporcja zdjęcia dokumentowego
    global obrazek_numer_1
    global obrazek_numer_2
    global obrazek_numer_3
    obrazek_numer_1 = loadImage("https://www.konradhudas.pl/portret/wp-content/uploads/2018/07/5D1_9336-PL-Dow%C3%B3d-Osobisty-102x152-mm_10x15-610x910.jpg")
    obrazek_numer_2 = loadShape("https://upload.wikimedia.org/wikipedia/commons/d/de/Natural-moustache_Simple_Black.svg")
    obrazek_numer_3 = loadShape ("https://upload.wikimedia.org/wikipedia/commons/f/f7/Tux_Paint_sunglasses_02.svg")
    beginRecord(PDF, "PDF.pdf")
    
def draw():
    image(obrazek_numer_1,0,0, 400, 550)
    fill(210,105,30)
    t1=text("1 - pokaz wasy", 10, 20)
    t2=text("2 - pokaz okulary", 10, 40)
    t3=text("<-  wybor opcji nr 1", 270, 20)
    t4=text("->  wybor opcji nr 2", 270, 40)
    # + do aktywności za podjęcie UI, bo prawie nikt tego nie zrobił
    
    if keyPressed: # tak jest czytelniej i mniej pisania, niż powtarzać co warunek - obowiązuje we wszystkich wytabowanych pod nim
        if (keyCode == LEFT) or (keyCode == RIGHT):
            fill(255,255,255)
            noStroke()
            # rect(0,0,135,50)
            # rect(269,0,135,50)
            image(obrazek_numer_1,0,0, 400, 550) # narysowanie tła ponownie zakryłoby teksty lepiej niż prostokąty
    
        if key=='1':
            shape(obrazek_numer_2,110, 355, 180, 40)
        elif keyCode == LEFT: # do else if używa się elif :)
                shape(obrazek_numer_2,110, 350, 180, 40)
                endRecord()
                exit()
        
        if key=='2':
            shape(obrazek_numer_3,35, 100, 340, 290)
    
        elif keyCode == RIGHT:
                shape(obrazek_numer_3,35, 100, 340, 290)
                endRecord()
                exit()

# 1,75 +
