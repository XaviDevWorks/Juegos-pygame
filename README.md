# 24-25-python-game-XaviDevWorks

# Menu
Creado el menu de juego, donde actualmente se pueden selecionar dos juegos.

# Juego de la Serpiente

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

# Comandos
python -m venv venv 

venv/Scripts/activate

pip install pygame

python menu.py


