#tarea: generar una lista de pares e impares con los datos de la cola, generar una lista con los datos primos de la cola, buscar la mayor y menor elemento de la cola
class Nodo:
  def __init__(self, dato):
    self.info=dato             #estructura base de cada nodo de la cola
    self.sig=None

class Cola:
  def __init__(self):                         #crea la estructura completa de la cola lineal
    self.cab=Nodo(-1) #nodo centinela
    self.cab.sig=self.cab

  def sumar(self, dato):
    nuevo=Nodo(dato)
    nuevo.sig=self.cab.sig                 #inserta un nodo al final de la cola actualizando (cab)
    self.cab.sig=nuevo
    self.cab=nuevo

  def listar(self):
    if self.cab == self.cab.sig:       #recorre la cola desde el primer nodo hasta volver al centinela imprimiendo los datos que encuentre en su camino
      print("(cola vacia)")
      return
    q=self.cab.sig
    r=q.sig
    while r != q:
      print(r.info, end=" ")
      r=r.sig
    print()
    print("")

  def retirar(self):
    if self.cab == self.cab.sig:
      print("No hay datos para retirar")     #elimina el primer elemento ingresado
      return None
    q=self.cab.sig #centinela
    r=q.sig  #primer nodo real
    valor=r.info
    if r == self.cab:
      q.sig=q
      self.cab=q
    else:
      q.sig=r.sig
      if r == self.cab:
        self.cab=q
    print(f"dato retirado: {valor}")
    return valor
    print("")

  def obtener_lista(self):
    elementos=[]                                   #convierte la cola normal en una circular sin modificarla, para buscar de forma sensilla el dato solicitado
    if self.cab == self.cab.sig:
      return elementos
    q=self.cab.sig
    r=q.sig
    while r != q:
      elementos.append(r.info)
      r=r.sig
    return elementos

  def lista_pares(self):
    pares=[x for x in self.obtener_lista() if x%2==0]         #filtra los numeros pares
    print("Lista de pares: ", pares)
    print("")

  def lista_impares(self):
    impares=[x for x in self.obtener_lista() if x%2!=0]       #filtra los numeros impares
    print("Lista de impares: ", impares)
    print("")

  def es_primo(self, n):
    if n<2:
      return False
    for i in range(2, int(n ** 0.5) +1):                     #verifica si un numero es primo o no
      if n%i==0:
        return False
    return True

  def lista_primos(self):
    primos=[x for x in self.obtener_lista() if self.es_primo(x)]      #muestra todos los datos que encontro (es_primo) que sean primos
    print("Lista de primos: ", primos)
    print("")

  def mayor_elemento(self):
    elementos=self.obtener_lista()                                     #busca cual es el numero con mayor valor numerico de la lista
    if not elementos:
      print("La cola esta vacia")
    else:
      print("El mayor elemento es: ", max(elementos))
      print("")

  def menor_elemento(self):
    elementos=self.obtener_lista()                                    #busca cual es el numero con menor valor numerico de la lista
    if not elementos:
      print("La cola esta vacia")
    else:
      print("El menor elemento es: ", min(elementos))
      print("")

def menu():
  cola=Cola()        #controla la interaccion de cada funcion
  opcion=0

  while opcion != 9:
    print("===MENU DE COLA===")
    print("1. insertar dato")
    print("2. Retirar dato")
    print("3. Listar cola")
    print("4. Generar lista de pares")
    print("5. Generar lista de impares")
    print("6. Generar lista de primos")
    print("7. Buscar mayor elemento")
    print("8. Buscar menor elemento")
    print("9. Salir")
    print("===================")
    try:
      opcion=int(input("Seleccione una opcion: "))
    except ValueError:
      print("debe ingresar un numero")
      continue

    if opcion==1:
      try:
        dato=int(input("ingrese numero a insertar: "))
        cola.sumar(dato)
        print("dato insertado")
      except ValueError:
        print("entrada invalida")
    elif opcion==2:
      cola.retirar()
    elif opcion==3:
      print("Contenido de la cola: ", end="")
      cola.listar()
    elif opcion==4:
      cola.lista_pares()
    elif opcion==5:
      cola.lista_impares()
    elif opcion==6:
      cola.lista_primos()
    elif opcion==7:
      cola.mayor_elemento()
    elif opcion==8:
      cola.menor_elemento()
    elif opcion==9:
      print("Saliendo...")
      break
    else:
      print("Opcion invalida, intente nuevamente")

if __name__=="__main__":
  menu()