from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.raton import raton
from mundo_pc.teclado import Teclado

Teclado1 = Teclado('HP', 'USB')
Raton1 = raton('HP', 'USB')
monitor1 = Monitor('HP', 15)
computadora1 = Computadora('HP', monitor1, Raton1, Teclado1)

Teclado2 = Teclado('ACER', 'USB')
Raton2 = raton('ACER', 'USB')
monitor2 = Monitor('ACER', 32)
computadora2 = Computadora('ACER', monitor2, Raton2, Teclado2)

Teclado3 = Teclado('GAMER', 'Bluethoh')
Raton3 = raton('GAMER', 'Bluethoh')
monitor3 = Monitor('GAMER', 12763)
computadora3 = Computadora('GAMER', monitor1, Raton1, Teclado1)

computadoras1 = [computadora1, computadora2]

orden1 = Orden(computadoras1)
print(orden1)
orden1.agregar_computadora(computadora3)
print(orden1)