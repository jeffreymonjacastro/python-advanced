## Raise Exception
def validar_x(x):
  if x < 1:
    raise Exception("La variable x debe ser mayor a 1")
  else:
    print("x es mayor a 1")

x = 2
# validar_x(x)


## Assert
def calcular_promedio(lista):
  assert len(lista) != 0, "La lista no puede estar vacía"
  return sum(lista) / len(lista)


promedio = calcular_promedio([1,2,3])
# print(promedio)


## Try - Except
def calcular_promedio(lista):
  assert len(lista) != 0, "La lista no puede estar vacía"
  return sum(lista) / len(lista)

try:
  promedio = calcular_promedio(["texto"])
  print(promedio)
except AssertionError as assert_error:
  print(assert_error)
except Exception as e:
  print("La función no calculó el promedio")
  print(e)