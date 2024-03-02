class Auto:
    def __init__(self, color, estado, paisOrigen):
        self.color = color
        self.estado = estado
        self.paisOrigen = paisOrigen

    def arrancar(self):
        print(f'el auto de color {self.color} arranco')
    
auto = Auto("negro", "activo", "china")
print(auto.color)                                                                                            
auto.arrancar()
#cuando pongo arrancar entre () lo q hago es ejecutar la funcion arrancar sobre el parametro auto instancia
#no sobre la clase Auto
#por eso pongo instancia.funcion()

