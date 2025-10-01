class Nodo:
  def __init__(self, datico):
    self.dato=datico
    self.sig=None

def insertar(cab):
    i=int(input("ingrese numero "))
    nuevo=Nodo(i)
    nuevo.sig=cab
    cab=nuevo
    print("")
    return cab

def imprimir(cab):
    while (cab!=None):
      print(cab.dato)
      cab=cab.sig
    print("")

def retirar(cab):
  if cab==None:
    print("lista vacia, no hay datos para retirar")
  else:
    cab=cab.sig
    print("")
  return cab

def buscar(cab):
  if cab==None:
    print("Lista vacia, no hay datos para buscar")
  else:
    pos=int(input("Ingresa la posicion a buscar: "))
    i=1
    aux=cab
    while (aux!=None) and (i<pos):
      aux=aux.sig
      i+=1
    if aux==None:
      print("La posicion no existe en la lista")
    else:
      print("El dato del la posicion", pos, "es:", aux.dato)
print("")

def tamaño(cab):
  if cab==None:
    print("La lista esta esta vacia, tamaño = 0")
  else:
    i=0
    aux=cab
    while aux!=None:
      i+=1
      aux=aux.sig
    print("El tamaño actual de la lista es:", i)
print("")

def contar_pares(cab):
  if cab==None:
    print("La lista esta esta vacia, No hay datos para contar")
  else:
    i=1
    aux=cab
    while aux!=None:
      if aux.dato %2==0:
        i+=1
      aux=aux.sig
    print("Cantidad de datos pares:", i)
print("")

def contar_impares(cab):
  if cab==None:
    print("La lista esta esta vacia, No hay datos para contar")
  else:
    i=0
    aux=cab
    while aux!=None:
      if aux.dato %2!=0:
        i+=1
      aux=aux.sig
    print("Cantidad de datos impares:", i)
print("")

cabecera=None
while True:
  print("===========================================")
  print("Menu lista - pila")
  print("1. Insertar numero")
  print("2. Imprimir lista")
  print("3. Retirar numero")
  print("4. Buscar por posicion")
  print("5. Tamaño de la lista")
  print("6. Contar pares")
  print("7. Contar impares")
  print("8. Salir")
  op=int(input("Ingrese opcion "))
  print("===========================================")
  if op==1:
    cabecera=insertar(cabecera)
  elif op==2:
    imprimir(cabecera)
  elif op==3:
    cabecera=retirar(cabecera)
  elif op==4:
    buscar(cabecera)
  elif op==5:
    tamaño(cabecera)
  elif op==6:
    contar_pares(cabecera)
  elif op==7:
    contar_impares(cabecera)
  elif op==8:
    break