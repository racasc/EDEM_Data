class Animales ():
  edad:float
  nPatas:float
  nombre:str
  haceruido:str
  comida:float

  def __init__(self, edad, nPatas, nombre, haceruido):
    self.edad = edad
    self.nPatas = nPatas
    self.nombre = nombre
    self.haceruido = haceruido
  
  def dieta (self, kilos = float):
    self.comida += kilos 
    
class tAnimal ():
    tipo:str

class gAnimal(Animales, tAnimal):
  

  
    
  
  