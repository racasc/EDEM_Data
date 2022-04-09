class Automovil:
    marca: str
    modelo: str
    color: str
    matricula: str
    id_seguro: str
    titular: str
    velocidad_actual: float = 0
    carburante: str
    
    def __init__(self, marca, modelo, color, matricula, id_seguro, titular, carburante):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.matricula = matricula
        self.id_seguro = id_seguro
        self.titular = titular
        self.carburante = carburante
    
    def arrancar(self):
        self.velocidad_actual = 10
        print('El automóvil ha arrancado')
    
    def frenar(self, presion: float):
        self.velocidad_actual -= (presion - 10)
        print(f'El automóvil ha frenado. Su velocidad ahora es de {self.velocidad_actual}')
    
    def acelerar(self, presion: float):
        self.velocidad_actual += (presion + 10)
        print(f'El automóvil ha acelerado. Su velocidad ahora es de {self.velocidad_actual}')
