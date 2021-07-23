from world_pc.computadora import Computadora
from world_pc.monitor import Monitor
from world_pc.orden import Orden
from world_pc.raton import Raton
from world_pc.teclado import Teclado

teclado1 = Teclado('HP', 'USB')
raton1 = Raton('HP', 'USB')
monitor1 = Monitor('HP', 15)
computadora1 = Computadora('HP', monitor1, teclado1, raton1)


teclado2 = Teclado('Acer', 'Blueooth')
raton2 = Raton('Acer', 'Bluetooh')
monitor2 = Monitor('Acer', 27)
computadora2 = Computadora('Acer', monitor2, teclado2, raton2)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
print(orden1)


