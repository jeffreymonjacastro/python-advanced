class Persona:
  saludo = "Hola, soy una persona"  # Atributo de clase

  def __init__ (self, nombre, edad): 
    self.nombre = nombre # Atributo de instancia
    self.edad = edad

  # Método de instancia
  def cumplirAnios(self):
    self.edad += 1
    print(f"Feliz cumpleaños #{self.edad} {self.nombre}")


# Herencia de la clase Persona
class Empleado(Persona):
  def __init__(self, nombre, edad, horas_totales):
    super(Empleado, self).__init__(nombre, edad) # Llamada al constructor de la clase padre
    self.horas_totales = horas_totales

  def trabajar(self, horas_trabajadas):
    self.horas_totales += horas_trabajadas
    print(f"{self.nombre} trabajó {horas_trabajadas} horas")
    print(f"Total de horas trabajadas: {self.horas_totales}")


# Objeto paco de la clase Persona
paco = Empleado("Paco", 25, 30)
paco.trabajar(8)

