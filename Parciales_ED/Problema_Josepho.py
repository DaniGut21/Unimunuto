#problema de Josephus
class Nodo:
  def __init__(self, dato):
    self.info = dato             #inicializa el nodo con (info y sig)
    self.sig = None

class Cola:
  def __init__(self):
    self.cab = Nodo(-1)  # nodo centinela       #asigna la cabeza de la cola al nodo
    self.cab.sig = self.cab

  def agregar(self, dato):
    nuevo = Nodo(dato)
    nuevo.sig = self.cab.sig     #inserta un nodo al final de la cola actualizando (cab)
    self.cab.sig = nuevo
    self.cab = nuevo

  def listar(self):
    if self.cab == self.cab.sig:
      print("(cola vacía)")          #muestra los datos que se encuentran en la cola
      return
    q = self.cab.sig
    r = q.sig
    while r != q:
      print(r.info, end=" ")
      r = r.sig
    print("\n")

  def obtener_lista(self):
    elementos = []
    if self.cab == self.cab.sig:        #convierte la cola normal en una circular sin modificarla, para buscar de forma sensible el dato solicitado
      return elementos
    q = self.cab.sig
    r = q.sig
    while r != q:
      elementos.append(r.info)
      r = r.sig
    return elementos

  def josephus(self, salto):
    """Simula el problema de Josephus"""
    elementos = self.obtener_lista()                                  #inicializa el problema de Josephus
    if not elementos:
      print("La cola está vacía, agrega elementos primero.")
      return
    if salto < 1:
      print("El salto debe ser mayor que 0.")
      return

    print(f"\nSimulando Josephus con {len(elementos)} personas y salto de {salto}...")
    idx = 0
    while len(elementos) > 1:
      idx = (idx + salto - 1) % len(elementos)
      eliminado = elementos.pop(idx)
      print(f"Eliminado: {eliminado} -> Quedan: {elementos}")
    print(f"\nSobreviviente: {elementos[0]}\n")

def menu():
  cola = Cola()        #inicializa la cola
  opcion = 0

  while opcion != 10:
    print("=== MENU DE COLA ===")
    print("1. Insertar dato")
    print("2. Listar cola")                    #menu de operaciones
    print("3. Resolver Josephus")
    print("4. Salir")
    print("====================")
    try:
      opcion = int(input("Seleccione una opción: "))
    except ValueError:
      print("Debe ingresar un número\n")
      continue

    if opcion == 1:
      try:
        dato = int(input("Ingrese número a insertar: "))
        cola.agregar(dato)
        print("Dato insertado\n")
      except ValueError:
        print("Entrada inválida\n")

    elif opcion == 2:
      print("Contenido de la cola:", end=" ")
      cola.listar()                                        #parte logica y de desicion

    elif opcion == 3:
      try:
        salto = int(input("Ingrese el salto: "))
        cola.josephus(salto)
      except ValueError:
        print("Entrada inválida\n")

    elif opcion == 4:
      print("Saliendo...")
      break
    else:
      print("Opción inválida\n")

if __name__ == "__main__":
  menu()                                 #repite el menu hasta que se seleccione salir
