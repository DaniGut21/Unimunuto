# start.py - MiSO v1.0 - MATRIX DURA 15 SEGUNDOS Y PARA SOLO
import time
import random

# Colores
G = "\033[92m" # verde
Y = "\033[93m" # amarillo
R = "\033[0m" # reset

print(f"{Y}═"*60)
print(f"{G} ★★★ MiSO v1.0 - SISTEMA OPERATIVO EN PYTHON ★★★")
print(f" Daniel + Angelita Silva + Daniel Roldan + Santiago Campo 2025")
print(f"═"*60 + f"{R}")

def matrix():
    print(f"{G}Iniciando efecto Matrix... (duración: 15 segundos){R}")
    cols = 80
    drops = [0] * cols
    start_time = time.time()
    
    while time.time() - start_time < 15: # ← DURA EXACTAMENTE 15 SEGUNDOS
        line = ""
        for i in range(cols):
            if drops[i] == 0 and random.random() < 0.12:
                drops[i] = random.randint(20, 50)
            if drops[i] > 0:
                line += random.choice("01アイウエオカキクケコサシスセソタチツテト")
                drops[i] -= 1
            else:
                line += " "
        print(f"{G}{line}{R}")
        time.sleep(0.06)
    
    print(f"{Y}\n¡Efecto Matrix finalizado automáticamente! (15s){R}")

# Bucle principal
while True:
    cmd = input(f"{Y}MiSO> {R}").strip().lower()
    if cmd == "matrix":
        matrix()
    elif cmd in ["snake", "serpiente"]:
        print("¡Snake disponible! (pídemelo y te lo paso completo)")
    elif cmd == "hola":
        print("¡Hola desde nuestro kernel en Python!")
    elif cmd == "equipo":
        print("¡Daniel G, tambien Angelita S, ademas Daniel R, y por ultimo Santiago C!")
    elif cmd == "reloj":
        print(f"Hora: {time.strftime('%H:%M:%S')}")    
    elif cmd == "clear":
        print("\033[2J\033[H", end="")
    elif cmd in ["salir", "exit", "adios"]:
        print(f"{Y}¡Apagando MiSO... Gracias por usar nuestro sistema!{R}")
        break
    else:
        print("Comandos: hola, equipo, matrix, snake, clear, salir")