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

def snake():
    print(f"{Y}JUEGO DE LA SERPIENTE - Usa WASD + Enter (o escribe 'salir'){R}")
    width, height = 30, 15
    snake = [(15, 7)]
    food = (random.randint(0,width-1), random.randint(0,height-1))
    dx, dy = 1, 0
    score = 0
    while True:
        # Dibujar tablero
        print("\033[2J\033[H", end="")  # limpia pantalla
        for y in range(height):
            line = ""
            for x in range(width):
                if (x,y) in snake:
                    line += "█" if (x,y) == snake[0] else "▓"
                elif (x,y) == food:
                    line += "♥"
                else:
                    line += "·"
            print(line)
        print(f"Puntos: {score}   (w/a/s/d + Enter para mover)")
        
        move = input().strip().lower()
        if move in "wasd":
            if move == "w": dx, dy = 0, -1
            if move == "s": dx, dy = 0, 1
            if move == "a": dx, dy = -1, 0
            if move == "d": dx, dy = 1, 0
        if move == "salir":
            print(f"{Y}¡Juego terminado! Puntos: {score}{R}")
            return
            
        # Mover serpiente
        head = snake[0]
        new = ((head[0] + dx) % width, (head[1] + dy) % height)
        if new in snake:
            print(f"{Y}¡Game Over! Puntos finales: {score}{R}")
            return
        snake.insert(0, new)
        if new == food:
            score += 1
            food = (random.randint(0,width-1), random.randint(0,height-1))
        else:
            snake.pop()    

# Bucle principal
while True:
    cmd = input(f"{Y}MiSO> {R}").strip().lower()
    if cmd == "matrix":
        matrix()
    elif cmd in ["snake", "serpiente"]:
        snake()
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