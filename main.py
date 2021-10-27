
class Asiento:
    def __init__(self,color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    def cambiarColor(self,color):
         if color=='rojo' or color=='verde' or color=='amarillo' or color=='negro' or color=='blanco':
            self.color = color
class Auto:
    cantidadCreados=0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=list(asientos)
        self.marca=marca
        self.motor=motor
        self.registro=registro

    def cantidadAsientos(self):
        asientos = 0
        for i in self.asientos:
            if type(i) == Asiento :
                asientos += 1
        return asientos

    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for i in self.asientos:
                if type(i)== Asiento:
                    if i.registro == self.registro:
                        continue
                    else:
                        return 'Las piezas no son originales'
        else:
            return 'Las piezas no son originales'
        return 'Auto original'


class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
    def CambiarRegistro(self,registro):
        self.registro = registro
    def asignarTipo(self, tipo):
        pass
        if tipo == 'electrico' or tipo == 'gasolina':
            self.tipo = tipo
