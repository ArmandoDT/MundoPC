from mundo_pc.dispositivo_entrada import DispositivoEntrada


class raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, marca, tipo_entrada):
        raton.contador_ratones += 1
        self._id_raton = raton.contador_ratones
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'Id: {self._id_raton}, Marca: {self._marca}, Tipo de entrada: {self._tipo_entrada}'


if __name__ == '__main__':
    raton1 = raton("HP", "USB")
    print(raton1)

    raton2 = raton("ACER", "Bluetooth")
    print(raton2)
