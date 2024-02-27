from enum import Enum
class direccion(Enum):
    norte = "norte"
    sur = "sur"
    este = "este"
    oeste = "oeste"

print("direcciones cardinales:")
for direccion in direccion:
    print(direccion.value)

jugador = direccion.este
print("el jugadore va hacia el", jugador.value)

from enum import Enum

class niveles(Enum):
    junior = "junior"
    senior = "senior"
    especialista = "especialista"

class persona():
    def __init__(self,nombre, edad, niveles):
        self.nombre = nombre
        self.edad = edad
        self.niveles = niveles



    def __str__(self):
        return f'self,nombre: {nombre}, edad: {edad}, niveles: {niveles}'

persona1 = persona("juan perez", "25", niveles.junior)
print(persona1.nombre)
print(persona1.edad)
print(persona1.niveles)




