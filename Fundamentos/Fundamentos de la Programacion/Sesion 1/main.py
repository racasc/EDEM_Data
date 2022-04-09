'''
Reto 1

Operacion aritmetica que realice 

((6-2)/5)^2
'''
resultado_operacion:float = (((6-2)/5)**2)
print(resultado_operacion)
print(resultado_operacion.__round__(2))

'''
Producto: 14,99€
los que no son de temporada tendran 30% de descuento

reciba un numero de productos en temporada
otro numero de productos de la temporada pasada y aplicar el descuento para obtener el gasto total.
'''
venta = 14.99
descuento = 0.3

temporada = int(input("Numero de productos que son de temporada: "))

noTemporada = int(input("Numeor de productos que no son de temporada: "))

total = round((temporada*venta) + (noTemporada*venta*(1-descuento)),2)

print("El precio total de la venta seria: ", total)


'''
se piede al usuario un año y tiene que salir si es bisiesto o no
'''

año = int(input("Introduzca un año: "))
if año % 4:
  print ("Exito")
elif :
  print ("no exito")




'''
que el ususario escriba años hasta que salga un numero bisiesto y darle un mensaje de exito
'''


