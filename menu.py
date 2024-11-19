import pygame
import subprocess
import os
import time

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menú de Juegos")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
gray = (169, 169, 169)
blue = (0, 0, 255)

# Fuente
font = pygame.font.Font(None, 40)

# Variable para controlar si un juego está en ejecución
game_process = None

# Función para dibujar botones
def draw_button(text, x, y, width, height, color, action=None):
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

    # Detectar si el botón ha sido clicado
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        if click[0] == 1 and action is not None:
            action()

# Funciones para abrir los juegos
def abrir_juego_1():
    global game_process
    if game_process is None or game_process.poll() is not None:
        juego = 'snake.py'
        if os.path.exists(juego):
            print(f"Abriendo {juego}...")
            game_process = subprocess.Popen(['python', juego])
        else:
            print(f"El archivo {juego} no se encuentra en la ubicación esperada.")
    else:
        print("El juego ya está en ejecución.")

def abrir_juego_2():
    global game_process
    if game_process is None or game_process.poll() is not None:
        juego = 'juego2.py'
        if os.path.exists(juego):
            print(f"Abriendo {juego}...")
            game_process = subprocess.Popen(['python', juego])
        else:
            print(f"El archivo {juego} no se encuentra en la ubicación esperada.")
    else:
        print("El juego ya está en ejecución.")

# Función para salir del programa
def salir():
    global running
    running = False

# Bucle principal del menú
running = True
while running:
    screen.fill(white)

    # Dibujar los botones
    draw_button("Snake", 200, 100, 200, 50, red, abrir_juego_1)

    # Verificar si "Juego 2" existe, y cambiar color si no está disponible
    if os.path.exists('juego2.py'):
        draw_button("Juego 2", 200, 200, 200, 50, red, abrir_juego_2)
    else:
        draw_button("Juego 2 (No Disponible)", 200, 200, 200, 50, gray)

    # Mostrar un mensaje de advertencia si el juego 2 no está disponible
    if not os.path.exists('juego2.py'):
        warning_text = font.render("Juego 2 no está disponible.", True, black)
        screen.blit(warning_text, (200, 270))

    # Botón para salir
    draw_button("Salir", 200, 300, 200, 50, blue, salir)

    # Procesar los eventos del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
