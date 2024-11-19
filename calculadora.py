import pygame
import sys

# Inicializa Pygame
pygame.init()

# Dimensiones de la ventana
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Calculadora")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 100, 255)

# Fuentes
font = pygame.font.Font(None, 40)
result_font = pygame.font.Font(None, 60)

# Botones de la calculadora
buttons = [
    {'text': '7', 'pos': (50, 200)}, {'text': '8', 'pos': (150, 200)}, {'text': '9', 'pos': (250, 200)}, {'text': '/', 'pos': (350, 200)},
    {'text': '4', 'pos': (50, 300)}, {'text': '5', 'pos': (150, 300)}, {'text': '6', 'pos': (250, 300)}, {'text': '*', 'pos': (350, 300)},
    {'text': '1', 'pos': (50, 400)}, {'text': '2', 'pos': (150, 400)}, {'text': '3', 'pos': (250, 400)}, {'text': '-', 'pos': (350, 400)},
    {'text': '0', 'pos': (50, 500)}, {'text': 'C', 'pos': (150, 500)}, {'text': '=', 'pos': (250, 500)}, {'text': '+', 'pos': (350, 500)},
]

# Estado inicial de la calculadora
current_input = ""
result = ""

def draw_buttons():
    """Dibuja los botones de la calculadora en la pantalla."""
    for button in buttons:
        pygame.draw.rect(screen, GRAY, (*button['pos'], 80, 80), border_radius=10)
        text_surface = font.render(button['text'], True, BLACK)
        text_rect = text_surface.get_rect(center=(button['pos'][0] + 40, button['pos'][1] + 40))
        screen.blit(text_surface, text_rect)

def check_button_click(pos):
    """Verifica si el usuario hizo clic en algún botón."""
    for button in buttons:
        x, y = button['pos']
        if x <= pos[0] <= x + 80 and y <= pos[1] <= y + 80:
            return button['text']
    return None

def calculate(expression):
    """Evalúa la expresión matemática."""
    try:
        return str(eval(expression))
    except:
        return "Error"

# Bucle principal
running = True
while running:
    screen.fill(WHITE)

    # Dibuja la pantalla de entrada
    pygame.draw.rect(screen, BLUE, (20, 50, WIDTH - 40, 100), border_radius=10)
    input_surface = result_font.render(current_input, True, WHITE)
    input_rect = input_surface.get_rect(right=WIDTH - 40, centery=100)
    screen.blit(input_surface, input_rect)

    # Dibuja los botones
    draw_buttons()

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verifica si se hizo clic en un botón
            button_text = check_button_click(event.pos)
            if button_text:
                if button_text == "C":
                    current_input = ""
                elif button_text == "=":
                    result = calculate(current_input)
                    current_input = result
                else:
                    current_input += button_text

    # Actualiza la pantalla
    pygame.display.flip()

pygame.quit()
sys.exit()
