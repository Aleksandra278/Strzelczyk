from abc import ABCMeta, abstractmethod
class Pet():
    __metaclass__=ABCMeta 
    @abstractmethod 
    def speak(self): 
        super().__init__()
        return 'no sound'
    
class Panda(Pet):  
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('myyyyy', random(50, width-70), random(50, height-50))
        return 'myyyyy'
    
class Cat(Pet): 
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('meow', random(50, width-70), random(50, height-50))
        return 'meow'
class Dog(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('woof', random(50, width-70), random(50, height-50))
        return 'woof'
    def gimmePaw(self):
        image(loadImage("lapa.png"), random(50, width-70), random(50, height-100))
    def __add__(self, other): 
        return self.name[0]+ ' i ' + other.name[0]
    def __sub__(self,other):   
        print(self.name)   

class Bunny():
    pass
    
def setup():
    size(400,400)
    textSize(20)
    atos=Panda('Atos')  
    portos=Dog('Portos') 
    rex = Dog('Rex') 
    benio = Dog('Benio')
    skrypcik = Cat('Skrypcik') 
    janusz = Bunny() 
    global list_of_pets
    list_of_pets = [rex, benio, skrypcik, portos, atos] 
    print(isinstance(skrypcik, Pet)) 
    print(rex+benio) 
    print(portos-rex)   
def draw():
    pass
    
def mouseClicked():
    for pet in list_of_pets:
        pet.speak()
        if isinstance(pet, Dog): 
            pet.gimmePaw()
# 2pkt
        
