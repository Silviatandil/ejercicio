from enum import Enum

class TipoInstrumento(Enum):
    cat1 = "viento"
    cat2 = "cuerdas"
    cat3 = "percusion"

class Fabrica():
    def __init__(self):
        self.sucursales = []
    def crearSucursal(self):
        pass                                                            
    def listarInstrumentos(self):
        pass
    def listarTipoInstrumento(self):
        pass
    def borrarInstrumento(self):
        pass
    def porcInstrumentosPorTipo(self,sucursal):
        pass
    def agregarInstrumentos(self,sucursal,instrumentos):
        for instrumento in instrumentos:
            sucursal.agregarInstrumentos(instrumento)

class Sucursal():
    def __init__(self,nombre):
        self.nombre = nombre
        self.instrumentos = []

    def agregarInstrumentos(self,instrumento):
        self.instrumentos.append(instrumento)

    def listarInstrumentos(self):
        if self.instrumentos:
            print(f'instrumentos en la sucursal {self.nombre}')
            for instrumento in self.instrumentos:
                print(f'id: {instrumento.id}, tipo: {TipoInstrumento.value}')
        else:
            print(f'no hay instrumentos en la sucursal {self.nombre}')

class Instrumentos():
    def __init__(self,id,precio,TipoInstrumento):
        self.id = id
        self.precio = precio
        self.TipoInstrumento = TipoInstrumento 
        
#Instrumentos = [
  #  instrumento("1", 120000, TipoInstrumento.cat1)
 #   instrumento2("2",250000, TipoInstrumento.TipoInstrumento.cat2)
#]
mi_fabrica = Fabrica()
sucursal = Sucursal("sucursal A")
print(sucursal.nombre)

instrumento1 = Instrumentos("20", 100,TipoInstrumento.cat1)
sucursal.agregarInstrumentos(instrumento1)



#sucursal1.agregarInstrumentos(Instrumentos("violin","guitarra"))


