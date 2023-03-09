from mundo_pc.monitor import Monitor
from mundo_pc.raton import raton
from mundo_pc.teclado import Teclado


class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
        {self._nombre} : {self._id_computadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        '''


if __name__ == '__main__':
    Teclado1 = Teclado('HP', 'USB')
    Raton1 = raton('HP', 'USB')
    monitor1 = Monitor('HP', 15)
    computadora = Computadora('HP', monitor1, Raton1, Teclado1)
    print(computadora)