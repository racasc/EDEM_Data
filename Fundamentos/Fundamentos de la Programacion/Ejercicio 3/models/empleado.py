from persona import Persona

class Empleado(Persona):
  puesto:str
  pHoras:float
  hTrabajadas:int = 0
  cobro: float = 0.0

  def __init__(self, nombre, apellidos, edad, puesto, pHoras):
    #llamamos al cosntructir  del padre (persona)
    super (Empleado,self).__init__(nombre, apellidos, edad)
    #inicializar los atributos propios de Empleado
    self.puesto = puesto
    self.pHoras= pHoras

  def trabajar (self, horass:int):
    sel.hTrabajadas += 1
    print(f'{self.nombre} ha trabajado {horas} horas. En total lleva trabajasas: {self.hTrabajadas}horas)


  def cobrar(self):
    self.cobro = self.pHoras*self.hTrabajadas
    print(f'{self.nombre} cobra: {self.cobro}€)








