# MiSO v2.0 - Sistema Operativo Mejorado
# Mejoras incluidas:
# - Sistema de ayuda mejorado
# - Colores centralizados
# - Manejo de errores más sólido
# - Comandos organizados en un diccionario
# - Juego Snake optimizado con límites configurables
# - Función "info" para mostrar información del sistema
# - Mensajes más limpios y consistentes

import time
import random
import os

# ==========================
# COLORES
# ==========================
class Color:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"
    RED = "\033[91m"
    MAG = "\033[95m"

c = Color

# ==========================
# ENCABEZADO
# ==========================
def header():
    print(f"{c.YELLOW}═" * 60)
    print(f"{c.GREEN} ★★★ MiSO v2.0 - SISTEMA OPERATIVO EN PYTHON ★★★")
    print(f" Equipo: Daniel G · Angelita S · Daniel R · Santiago C · 2025")
    print(f"═" * 60 + f"{c.RESET}")

header()

# ==========================
# EFECTO MATRIX
# ==========================
def matrix():
    print(f"{c.GREEN}Iniciando efecto Matrix mejorado... (15 segundos){c.RESET}")
    columnas = 80
    gotas = [0] * columnas
    inicio = time.time()

    while time.time() - inicio < 15:
        linea = ""
        for i in range(columnas):
            if gotas[i] == 0 and random.random() < 0.10:
                gotas[i] = random.randint(15, 45)
            if gotas[i] > 0:
                linea += random.choice("01アカサタナマアイウエオ012345")
                gotas[i] -= 1
            else:
                linea += " "
        print(c.GREEN + linea + c.RESET)
        time.sleep(0.05)

    print(f"{c.YELLOW}\nEfecto finalizado.{c.RESET}")

# ==========================
# SNAKE
# ==========================
def snake():
    print(f"{c.YELLOW}JUEGO: Snake (W A S D para mover, 'salir' para terminar){c.RESET}")

    ancho, alto = 25, 12
    snake = [(ancho // 2, alto // 2)]
    comida = (random.randint(0, ancho - 1), random.randint(0, alto - 1))
    dx, dy = 1, 0
    puntos = 0

    while True:
        os.system("cls" if os.name == "nt" else "clear")

        for y in range(alto):
            linea = ""
            for x in range(ancho):
                if (x, y) == snake[0]:
                    linea += "█"  # cabeza
                elif (x, y) in snake:
                    linea += "▓"  # cuerpo
                elif (x, y) == comida:
                    linea += "♥"
                else:
                    linea += "."
            print(linea)
        print(f"Puntos: {puntos}")

        mov = input().lower().strip()

        if mov == "salir":
            print(f"{c.YELLOW}Juego terminado. Puntos: {puntos}{c.RESET}")
            return
        elif mov == "w": dx, dy = 0, -1
        elif mov == "s": dx, dy = 0, 1
        elif mov == "a": dx, dy = -1, 0
        elif mov == "d": dx, dy = 1, 0

        cabeza = snake[0]
        nueva = ((cabeza[0] + dx) % ancho, (cabeza[1] + dy) % alto)

        if nueva in snake:
            print(f"{c.RED}Game Over. Puntos finales: {puntos}{c.RESET}")
            return

        snake.insert(0, nueva)

        if nueva == comida:
            puntos += 1
            comida = (random.randint(0, ancho - 1), random.randint(0, alto - 1))
        else:
            snake.pop()

# ==========================
# INFORMACIÓN DEL SISTEMA
# ==========================
def info():
    print(f"{c.CYAN}MiSO v2.0 — Información del sistema:{c.RESET}")
    print(f"- Intérprete de comandos mejorado")
    print(f"- Procesos: Matrix, Snake")
    print(f"- Comandos del sistema disponibles")
    print(f"- Creado como proyecto educativo en Python")

# ==========================
# AYUDA
# ==========================
def help_menu():
    print(f"{c.MAG}Comandos disponibles:{c.RESET}")
    for cmd in comandos.keys():
        print(f" - {cmd}")

# ==========================
# MAPA DE COMANDOS
# ==========================
def youtube():
    query = input("Ingresa el nombre del video a buscar: ").strip().replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)
    print(f"{c.YELLOW}Abriendo YouTube...{c.RESET}")

comandos = {
    "matrix": matrix,
    "snake": snake,
    "serpiente": snake,
    "youtube": youtube,
    "hola": lambda: print("¡Hola desde MiSO v2!"),
    "equipo": lambda: print("Daniel G, Angelita S, Daniel R, Santiago C"),
    "reloj": lambda: print("Hora actual:", time.strftime("%H:%M:%S")),
    "info": info,
    "help": help_menu,
    "ayuda": help_menu,
    "clear": lambda: os.system("cls" if os.name == "nt" else "clear"),
    "salir": lambda: exit(print(f"{c.YELLOW}Apagando MiSO v2...{c.RESET}")),
}

# ==========================
comandos = {
    "matrix": matrix,
    "snake": snake,
    "serpiente": snake,
    "hola": lambda: print("¡Hola desde MiSO v2!"),
    "equipo": lambda: print("Daniel G, Angelita S, Daniel R, Santiago C"),
    "reloj": lambda: print("Hora actual:", time.strftime("%H:%M:%S")),
    "info": info,
    "help": help_menu,
    "ayuda": help_menu,
    "clear": lambda: os.system("cls" if os.name == "nt" else "clear"),
    "salir": lambda: exit(print(f"{c.YELLOW}Apagando MiSO v2...{c.RESET}")),
}

# ==========================
# BUCLE PRINCIPAL DEL SISTEMA
# ==========================
while True:
    cmd = input(f"{c.YELLOW}MiSO>{c.RESET} ").strip().lower()

    if cmd in comandos:
        try:
            comandos[cmd]()
        except Exception as e:
            print(f"{c.RED}[ERROR] {e}{c.RESET}")
    else:
        print(f"{c.RED}Comando no reconocido.{c.RESET}")
        print("Escribe 'help' para ver los comandos disponibles.")
