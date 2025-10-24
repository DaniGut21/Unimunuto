#Peaje
import random        #importar la librería random de numeros aleatorios

class Nodo:
  def __init__(self, dato):
    self.info = dato             #inicializa el nodo con (info y sig)
    self.sig = None

class Cola:
  def __init__(self):
    self.cab = Nodo(-1)  # nodo centinela
    self.cab.sig = self.cab                           #asigna la cabeza de la cola al nodo
    # Contadores de control
    self.total_autos = 0
    self.total_camionetas = 0
    self.recaudo_autos = 0
    self.recaudo_camionetas = 0

  def agregar(self, tipo):
    """Agrega un vehículo a la cola"""                #agrega un vehículo a la cola
    nuevo = Nodo(tipo)
    nuevo.sig = self.cab.sig
    self.cab.sig = nuevo
    self.cab = nuevo

  def listar(self):
    """Muestra la cola actual"""
    if self.cab == self.cab.sig:
      print("(no hay vehículos en la cola)\n")
      return                                       #muestra los datos que se encuentran en la cola
    q = self.cab.sig
    r = q.sig
    print("Vehículos en la cola:")
    while r != q:
      print(f" - {r.info}")
      r = r.sig
    print("")

  def retirar(self):
    """Atiende el siguiente vehículo en la cola"""
    if self.cab == self.cab.sig:                               #atiende el siguiente vehículo en la cola
      print("No hay vehículos para atender.\n")
      return

    q = self.cab.sig  # centinela
    r = q.sig         # primer vehículo real             #elimina el primer vehículo (si es el mismo que el centinela, se vuelve a poner en la cabeza)
    tipo = r.info

    if r == self.cab:
      q.sig = q
      self.cab = q
    else:                      #elimina el primer vehículo
      q.sig = r.sig
      if r == self.cab:
        self.cab = q

    if tipo == "automóvil":
      self.total_autos += 1
      self.recaudo_autos += 50
    elif tipo == "camioneta":              #procesar cobro
      self.total_camionetas += 1
      self.recaudo_camionetas += 70

    print(f"Vehículo atendido: {tipo}")
    self.mostrar_estadisticas()

  def agregar_aleatorio(self, n):
    """Agrega n vehículos de forma aleatoria"""
    tipos = ["automóvil", "camioneta"]                        #agrega n vehículos aleatoriamente
    for _ in range(n):
      tipo = random.choice(tipos)
      self.sumar(tipo)
    print(f"{n} vehículos agregados aleatoriamente.\n")

  def mostrar_estadisticas(self):
    """Muestra totales actuales"""
    total_vehiculos = self.total_autos + self.total_camionetas
    total_recaudo = self.recaudo_autos + self.recaudo_camionetas

    print("\n--- ESTADÍSTICAS ---")                                                              #muestra estadísticas de la cola
    print(f"Automóviles: {self.total_autos} | Recaudo: ${self.recaudo_autos}")
    print(f"Camionetas: {self.total_camionetas} | Recaudo: ${self.recaudo_camionetas}")
    print(f"TOTAL vehículos: {total_vehiculos} | Recaudo total: ${total_recaudo}")
    print("----------------------\n")

def menu():                                                                                                #menu principal
  cola = Cola()
  opcion = 0

  while opcion != 6:
    print("=== MENÚ PEАJE ===")
    print("1. Agregar vehículo manualmente")
    print("2. Agregar vehículos aleatorios")
    print("3. Listar cola")
    print("4. Atender vehículo")                                                                    #menu de operaciones
    print("5. Mostrar estadísticas")
    print("6. Salir")
    print("===================")

    try:
      opcion = int(input("Seleccione una opción: "))
    except ValueError:
      print("Debe ingresar un número\n")
      continue

    if opcion == 1:
      tipo = input("Ingrese tipo (automóvil/camioneta): ").strip().lower()
      if tipo in ["automóvil", "camioneta"]:
        cola.agregar(tipo)
        print(f"Vehículo '{tipo}' agregado.\n")
      else:
        print("Tipo inválido.\n")

    elif opcion == 2:
      try:
        n = int(input("¿Cuántos vehículos desea agregar?: "))
        cola.agregar_aleatorio(n)                                                                    #parte logica y de desicion
      except ValueError:
        print("Entrada inválida.\n")

    elif opcion == 3:
      cola.listar()

    elif opcion == 4:
      cola.retirar()

    elif opcion == 5:
      cola.mostrar_estadisticas()

    elif opcion == 6:
      print("Saliendo del sistema de peaje...")
      break
    else:
      print("Opción inválida.\n")

if __name__ == "__main__":               #repite el menu hasta que se seleccione salir
  menu()
 