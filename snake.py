import turtle
import time
import random

# Configuración inicial
retraso = 0.1
puntuacion = 0
puntuacion_alta = 0

# Configuración de la pantalla
ventana = turtle.Screen()
ventana.title("Juego de la Serpiente por @XaviDevWorks")
ventana.bgcolor("black")
ventana.setup(width=600, height=600)
ventana.tracer(0)  # Desactiva la actualización automática de la ventana

# Texto para pantallas de Game Over
texto_inicio = turtle.Turtle()
texto_inicio.speed(0)
texto_inicio.color("white")
texto_inicio.penup()
texto_inicio.hideturtle()

# Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("darkgreen")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direccion = "detenida"

# Comida de la serpiente
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("yellow")
comida.penup()
comida.goto(0, 100)

segmentos = []

# Texto de puntuación
texto = turtle.Turtle()
texto.speed(0)
texto.shape("square")
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)

def actualizar_puntuacion():
    texto.clear()
    texto.write(f"Puntuación: {puntuacion}  Puntuación Más Alta: {puntuacion_alta}", align="center", font=("Courier", 24, "normal"))

actualizar_puntuacion()

# Funciones de movimiento
def mover_arriba():
    if cabeza.direccion != "abajo":
        cabeza.direccion = "arriba"

def mover_abajo():
    if cabeza.direccion != "arriba":
        cabeza.direccion = "abajo"

def mover_izquierda():
    if cabeza.direccion != "derecha":
        cabeza.direccion = "izquierda"

def mover_derecha():
    if cabeza.direccion != "izquierda":
        cabeza.direccion = "derecha"

def mover():
    if cabeza.direccion == "arriba":
        cabeza.sety(cabeza.ycor() + 20)
    if cabeza.direccion == "abajo":
        cabeza.sety(cabeza.ycor() - 20)
    if cabeza.direccion == "izquierda":
        cabeza.setx(cabeza.xcor() - 20)
    if cabeza.direccion == "derecha":
        cabeza.setx(cabeza.xcor() + 20)

# Funciones para los botones
def crear_boton(texto, color, x, y, funcion):
    boton = turtle.Turtle()
    boton.speed(0)
    boton.shape("square")
    boton.color(color)
    boton.penup()
    boton.goto(x, y)
    boton.shapesize(stretch_wid=2, stretch_len=6)
    
    # Escribir el texto en el botón
    texto_boton = turtle.Turtle()
    texto_boton.speed(0)
    texto_boton.color("white")
    texto_boton.penup()
    texto_boton.hideturtle()
    texto_boton.goto(x, y-10)
    texto_boton.write(texto, align="center", font=("Courier", 14, "bold"))

    # Asociar la función al botón
    ventana.onclick(lambda x, y: funcion())  # Hacer clic en el botón

    return boton, texto_boton

def pantalla_game_over():
    texto_inicio.clear()
    texto_inicio.goto(0, 50)
    texto_inicio.write("¡Game Over!", align="center", font=("Courier", 24, "bold"))
    texto_inicio.goto(0, -10)
    texto_inicio.write(f"Puntuación Final: {puntuacion}", align="center", font=("Courier", 16, "normal"))
    texto_inicio.goto(0, -50)
    texto_inicio.write("Haz clic en el botón para continuar o salir", align="center", font=("Courier", 16, "normal"))
    
    # Crear botones
    crear_boton("Seguir", "green", -100, -100, iniciar_juego)
    crear_boton("Salir", "red", 100, -100, salir_juego)

# Salir del juego
def salir_juego():
    ventana.bye()

# Iniciar el juego
def iniciar_juego():
    texto_inicio.clear()
    for segmento in segmentos:
        segmento.goto(1000, 1000)  # Mueve los segmentos fuera de la pantalla
    segmentos.clear()
    cabeza.goto(0, 0)
    cabeza.direccion = "detenida"
    global puntuacion, retraso
    puntuacion = 0
    retraso = 0.1
    actualizar_puntuacion()
    bucle_juego()

# Bucle principal del juego
def bucle_juego():
    mover()  # Mueve la serpiente cada vez que se actualiza
    # Colisión con bordes
    if cabeza.xcor() > 290 or cabeza.xcor() < -290 or cabeza.ycor() > 290 or cabeza.ycor() < -290:
        pantalla_game_over()
        return

    # Colisión con la comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        comida.goto(x, y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("forestgreen")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        global puntuacion, puntuacion_alta, retraso
        puntuacion += 10
        if puntuacion > puntuacion_alta:
            puntuacion_alta = puntuacion
        retraso -= 0.001
        actualizar_puntuacion()

    # Mover los segmentos del cuerpo
    for i in range(len(segmentos) - 1, 0, -1):
        x = segmentos[i - 1].xcor()
        y = segmentos[i - 1].ycor()
        segmentos[i].goto(x, y)

    if segmentos:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    # Colisión con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            pantalla_game_over()
            return

    ventana.ontimer(bucle_juego, int(retraso * 1000))  # Llama a la función después de un retraso

# Controles de teclado
ventana.listen()
ventana.onkeypress(mover_arriba, "w")
ventana.onkeypress(mover_abajo, "s")
ventana.onkeypress(mover_izquierda, "a")
ventana.onkeypress(mover_derecha, "d")

bucle_juego()  # Ejecuta el bucle principal de la ventana
ventana.mainloop()  # Mantiene la ventana abierta hasta que el jugador decida cerrarla
