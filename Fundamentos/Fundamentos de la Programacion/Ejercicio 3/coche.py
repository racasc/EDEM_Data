	
from automovil import Automovil
 
class Coche(Automovil):
        numero_plazas: int
        litros_maletero: float
        sistema_abs: bool
        mm_llantas: float
        nota_seguridad: int
        caballos: int
 
        def __init__(self, marca, modelo, color, 
                        matricula, id_seguro, titular, carburante, 
                        numero_plazas, litros_maletero, sistema_abs,
                     	mm_llantas, nota_seguridad, caballos):
                super(Coche, self).__init__(marca, modelo, color, matricula,
                                            id_seguro, titular, carburante)
                self.numero_plazas = numero_plazas
                self.litros_maletero = litros_maletero
                self.sistema_abs = sistema_abs
                self.mm_llantas = mm_llantas
                self.nota_seguridad = nota_seguridad
                self.caballos = caballos
