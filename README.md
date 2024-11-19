# 24-25-python-game-XaviDevWorks

# Menu
Creado el menu de juego, donde actualmente se pueden selecionar dos juegos.

# Primer Juego: la Serpiente

Este juego está programado en **Python** utilizando la biblioteca **Pygame**. Es una implementación clásica del juego **Snake**, en la cual el jugador controla una serpiente que se mueve por la pantalla para recoger manzanas (o "comida"). A medida que la serpiente come más manzanas, su tamaño (o longitud) aumenta. El objetivo del juego es evitar que la serpiente choque contra las paredes o contra su propio cuerpo, mientras se trata de obtener la mayor puntuación posible.

## Controles:
- **W**: Mover hacia arriba.
- **S**: Mover hacia abajo.
- **A**: Mover hacia la izquierda.
- **D**: Mover hacia la derecha.

## Cómo jugar:
- Comienzas con una serpiente pequeña.
- Al comer las manzanas (comida roja), la serpiente crecerá.
- Si la serpiente choca con los bordes de la pantalla o con su propio cuerpo, el juego terminará.
- Tu objetivo es obtener el puntaje más alto posible.

## Características:
- **Puntuación**: A medida que la serpiente come manzanas, tu puntaje aumenta.
- **Puntación más alta**: El puntaje más alto alcanzado se guarda y muestra durante la partida.
- **Velocidad variable**: Cuantas más manzanas comas, más rápido se moverá la serpiente.

# Comandos para poner en bash (en la terminal en visual)
python -m venv venv 

venv/Scripts/activate

pip install pygame

python menu.py






# Calculadora en Pygame

Una calculadora gráfica básica creada utilizando [Pygame](https://www.pygame.org/), diseñada para practicar interfaces gráficas en Python. Incluye funcionalidades para realizar operaciones matemáticas básicas (suma, resta, multiplicación y división) y un pequeño menú para salir de la aplicación.

## Características

- Interfaz gráfica simple y amigable.
- Operaciones básicas: suma, resta, multiplicación, división.
- Botón para borrar (`C`) y calcular el resultado (`=`).
- Menú con un botón para salir de la aplicación.

## Requisitos

- Python 3.8 o superior.
- Pygame 2.0 o superior.

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu-usuario/calculadora-pygame.git
   cd calculadora-pygame

