#nombre1 = input("introdusca su nombre: ")

#edad1 = int(input("introdusca su edad"))

#nombre2 = input("introdusca su edad: ")

#edad2 = int(input("introdusca su edad"))


#print(f"{nombre1}es mayor") if edad1 > edad2 else print(f"{nombre2} mayor")


class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario


    def __str__(self):
        return "{} que trabajo como {} tiene un salario de RD${} peso".format(self.nombre, self.cargo, self.salario)
    

listaEmpleado = [
    Empleado("juan", "Director", 175000),
     Empleado("ana", "presidente", 125000),
      Empleado("antonio", "Administrado", 85000),
       Empleado("sara", "secretaria", 75000),
       Empleado("mario", "mantanimiento", 50000),
 ]

#crear una funcion
def calculo_comision(Empleado):
    Empleado.salario = Empleado.salario 
    return Empleado

listaEmpleadocomision = map(calculo_comision, listaEmpleado)
for Empleado in listaEmpleadocomision:
    print(Empleado)


#aplicar una comicion solo a los trabajadores con salarios bajos
def calculo_comision(empleado):
    if(Empleado.salario <= 50000):
        Empleado.salario = empleado.salario *20
    return Empleado


listaEmpleadocomision = map(calculo_comision,listaEmpleado)

#for empleado in listaEmpleadocomision:
    #print(f"El empleado {empleado.nombre} ha ganado una comisión en este mes. Nuevo salario: RD${empleado.salario} pesos")


print(f"El empleado {Empleado} ha ganado una comisión en este mes. Nuevo salario: RD${Empleado.salario:6f} pesos")




