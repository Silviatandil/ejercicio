from enum import Enum

class tipoContrato(Enum):
    fijo = "salario fijo"
    comi = " salario por comision"

class antiguedad(Enum):
    cat1 = "menos de 2 años"
    cat2 = "entre 2 anios y 5 añios"
    cat3 = "mas de 5 anios"

class empleado():
    def __init__(self,dni,nombre,apellido,anioIngreso,tipoContrato):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.anioIngreso = anioIngreso
        self.tipoContrato = tipoContrato

    def __str__(self):
        return f'empleado: {self.nombre} {self.apellido} {self.anioIngreso} {self.tipoContrato}'
    
    def calcularSalario(self):
        pass

    #def mostrarSalario(self):
     #   pass
       # print(f'{self.nombre} {self.apellido}: no especificado ')
    

class empleadoComision(empleado):
    def __init__(self, dni, nombre, apellido, anioIngreso, tipoContrato,salarioMinimo,clientesCaptados,montoACobrar):
        super().__init__(dni, nombre, apellido, anioIngreso, tipoContrato)   
        self.salarioMinimo = salarioMinimo
        self.clientesCaptados = clientesCaptados
        self.montoACobrar = montoACobrar  

    def mostrarSalario (self):
        salario = self.clientesCaptados * self.montoACobrar
        if salario < self.salarioMinimo:
            return self.salarioMinimo
        else:
            return salario
        
        
    #def mostrarSalario(self):
     
     #   salario = self.calcularSalario()
        #return f'dni: {self.dni}, nombre: {self.nombre}, apellido: {self.apellido}, anio de ingreso: {self.anioIngreso}, tipo de contrato:{self.tipoContrato}, sueldo basico:{self.sueldoBasico}' 


class empleadoFijo(empleado):
    def __init__(self, dni, nombre, apellido, anioIngreso, tipoContrato,sueldoBasico,porcentajeAdicional):
        super().__init__(dni, nombre, apellido, anioIngreso, tipoContrato)
        self.sueldoBasico = sueldoBasico
        self.porcentajeAdicional = porcentajeAdicional
        #mostrar salario

    def calcularSalario(self):
        antiguedad = 2024 - self.anioIngreso
        porcentajeAdicional = 0
        if antiguedad >= 2 and antiguedad <=5:
            porcentajeAdicional = 0.05
        elif antiguedad > 5:
            porcentajeAdicional = 0.1
        salario = self.sueldoBasico * (1 + self.porcentajeAdicional/100 + porcentajeAdicional)
        print("el salario es: ", salario)

    #def calcularSalario(self):
     #   if self.anioIngreso in antiguedad.cat2.value:
      #      return "recibe 5% adicional" 
       # elif self.anioIngreso > antiguedad.cat2.value[-1]:
        #    return  "recibe 10% adicional"
        #else:
         #   return "no tiene adicional"
        
   
        

empleado1= empleadoFijo(36608285,"silvia", "camara",2023,"tipoContrato.fijo",250000,5)
empleado1.calcularSalario()
print(empleado1)


empleado2 = empleadoComision("34853019","juan","perez",2005,tipoContrato.comi,250000,6,5)
empleado2.mostrarSalario()



#print(empleado1.apellido)
#print(empleado1.dni)
#print(empleado1.anioIngreso)
#print(empleado1.tipoContrato)


        
