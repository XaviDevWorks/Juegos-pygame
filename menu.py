import pygame
import subprocess
import os

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Menú de Juegos")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)
DARK_GRAY = (169, 169, 169)
BUTTON_HOVER = (255, 100, 100)  # Rojo claro para hover

# Fuente
font = pygame.font.Font(None, 50)
font_small = pygame.font.Font(None, 30)

# Variable para controlar el proceso de juego
game_process = None

# Dibujar un botón con efecto hover
def draw_button(text, x, y, width, height, color, hover_color, action=None):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    button_rect = pygame.Rect(x, y, width, height)

    # Cambiar el color si el mouse está sobre el botón
    if button_rect.collidepoint(mouse_x, mouse_y):
        pygame.draw.rect(screen, hover_color, button_rect)
        if pygame.mouse.get_pressed()[0] and action:
            action()
    else:
        pygame.draw.rect(screen, color, button_rect)

    # Dibujar el texto en el centro del botón
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, text_surface.get_rect(center=button_rect.center))

# Abrir juego
def open_game(file_name):
    global game_process
    if not game_process or game_process.poll() is not None:
        if os.path.exists(file_name):
            game_process = subprocess.Popen(['python', file_name])
        else:
            print(f"{file_name} no encontrado.")

# Salir del programa
def salir():
    pygame.quit()
    exit()

# Bucle principal
running = True
while running:
    screen.fill(LIGHT_BLUE)

    # Título de la aplicación
    title_text = font_small.render("Menú de Juegos", True, DARK_GRAY)
    screen.blit(title_text, (200, 30))

    # Botones con efectos hover
    draw_button("Snake", 200, 100, 200, 60, RED, BUTTON_HOVER, lambda: open_game('snake.py'))
    draw_button("Calculadora", 200, 200, 200, 60, GREEN if os.path.exists('calculadora.py') else DARK_GRAY, BUTTON_HOVER, 
                lambda: open_game('calculadora.py') if os.path.exists('calculadora.py') else None)
    draw_button("Salir", 200, 300, 200, 60, BLUE, BUTTON_HOVER, salir)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir()

    pygame.display.flip()

