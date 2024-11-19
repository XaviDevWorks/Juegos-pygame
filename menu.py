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
GRAY = (169, 169, 169)
BLUE = (0, 0, 255)

# Fuente
font = pygame.font.Font(None, 40)

# Variable para controlar el proceso de juego
game_process = None

# Dibujar un botón
def draw_button(text, x, y, width, height, color, action=None):
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, text_surface.get_rect(center=(x + width // 2, y + height // 2)))
    
    # Acciones al hacer clic
    if pygame.mouse.get_pressed()[0]:
        if pygame.Rect(x, y, width, height).collidepoint(pygame.mouse.get_pos()) and action:
            action()

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
    screen.fill(WHITE)

    # Botones
    draw_button("Snake", 200, 100, 200, 50, RED, lambda: open_game('snake.py'))
    draw_button("Juego 2", 200, 200, 200, 50, RED if os.path.exists('juego2.py') else GRAY, 
                lambda: open_game('juego2.py') if os.path.exists('juego2.py') else None)
    draw_button("Salir", 200, 300, 200, 50, BLUE, salir)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir()

    pygame.display.flip()
