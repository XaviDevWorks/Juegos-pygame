# 24-25-python-game-XavierFarrus

Este repositorio contiene un menú interactivo desarrollado en **Python** y **Pygame** que incluye dos opciones principales: un **juego de la serpiente** y una **calculadora interactiva**. Cada uno de estos proyectos está diseñado para demostrar habilidades de programación y diseño gráfico con Python.

------------------------------------------------------------------------------------

## Menú Principal

Al ejecutar el programa principal (`menu.py`), se muestra un menú interactivo desde el cual puedes seleccionar entre las siguientes opciones:

1. **Juego de la Serpiente**  
2. **Calculadora Interactiva**  

El menú tiene un diseño sencillo y funcional para facilitar la navegación.

------------------------------------------------------------------------------------

## 🐍 Juego de la Serpiente

Este es un clásico juego de **Snake**, programado completamente en **Python** utilizando **Pygame**. Controla una serpiente que debe comer manzanas mientras evita chocar contra las paredes o su propio cuerpo.

### 🎮 Controles:
- **Flechas del teclado**: Para mover la serpiente en las direcciones **arriba**, **abajo**, **izquierda** o **derecha**.

### 🚀 Cómo jugar:
1. **Inicio**: La serpiente comienza con tres bloques de longitud.
2. **Objetivo**: Come manzanas (comida roja) para aumentar la longitud de la serpiente.
3. **Reglas**:
   - Si chocas con las paredes o contigo mismo, el juego termina.
   - El objetivo es lograr la puntuación más alta posible antes de perder.

### ✨ Características:
- **Aumento de longitud**: Cada vez que comes una manzana, la serpiente crece.
- **Puntuación**: El puntaje se muestra en pantalla y aumenta con cada manzana comida.
- **Gráficos personalizados**: Imágenes únicas para la cabeza, el cuerpo y la cola de la serpiente.
- **Sonidos**: Efecto de sonido al comer (crunch.wav).

------------------------------------------------------------------------------------

## 🔢 Calculadora en Pygame

Un proyecto sencillo que simula una calculadora gráfica utilizando **Pygame**. Este programa permite realizar operaciones matemáticas básicas a través de una interfaz interactiva.

### 📋 Características:
1. **Interfaz gráfica**:
   - Botones interactivos para números y operaciones.
   - Diseño visual sencillo y funcional.
2. **Operaciones básicas**:
   - **Suma (`+`)**
   - **Resta (`-`)**
   - **Multiplicación (`*`)**
   - **División (`/`)**
3. **Otras funciones**:
   - Botón para borrar (`C`).
   - Botón para calcular el resultado (`=`).
4. **Navegación desde el menú principal**.

### 🤖 Uso:
- Selecciona la calculadora en el menú principal.
- Utiliza los botones para realizar cálculos interactivos.

------------------------------------------------------------------------------------

## 🛠️ Requisitos para ejecutar el proyecto

Asegúrate de tener instalados los siguientes elementos:

1. **Python**: Versión 3.8 o superior.
2. **Pygame**: Una biblioteca para gráficos y sonido. Instálala con `pip install pygame`.

------------------------------------------------------------------------------------

## 🚀 Cómo ejecutar el proyecto

Sigue estos pasos para ejecutar el programa:

1. Clona este repositorio:
   git clone https://github.com/XavierFarrus/24-25-python-game-XavierFarrus.git


2. Navega al directorio del proyecto:
    cd 24-25-python-game-XavierFarrus

3. Crea y activa un entorno virtual:
    python -m venv venv
    venv/Scripts/activate     # En Windows
    source venv/bin/activate  # En macOS/Linux

4. Instala las dependencias:
    pip install pygame

5. Ejecuta el menú principal:
    python menu.py

------------------------------------------------------------------------------------

## 🖼️ Imágenes del proyecto

- **Menú principal**  
  *Pantalla inicial con opciones para seleccionar entre el juego y la calculadora.*

- **Juego de la Serpiente**  
  *Vista del juego en acción, con la serpiente comiendo una manzana.*

- **Calculadora Interactiva**  
  *Interfaz gráfica mostrando botones para las operaciones.*
