from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

"""
Se definen los parámetros: 
Borderless: Para que salga sin botones de manejo de ventana
Nota: Vec3 quiere decir generar en 3D

Otras librerías: GODOT (más potente, muy similar a Python)
"""
app = Ursina(borderless=False)

Sky()  # Se genera un cielo por defecto.

# Definimos la semilla. Si se pone un valor, será siempre el mismo. Util para testing.
random.seed(random.randint(0, 65535))
window.size = 800, 600  # Se define el tamaño de pantalla, alto por ancho en píxeles.
window.update_aspect_ratio()

player = FirstPersonController()  # Definimos la función de primera persona.
# Creamos el texto de fin y de reset, pero deshabilitado.
end_txt = Text(text="End", color=color.black, scale=5, origin=(0, 0), parent=camera.ui)
reset_btn = Button(text="Reset", color=color.black, scale=(4, 0), origin=(-0.05, 0), parent=camera.ui)
end_txt.disable()
reset_btn.disable()


def spawn():
    player.position = Vec3(0, 0.25, 0)  # Definimos donde va a salir el jugador.
    player.enable()  # Activamos el control del jugador.
    end_txt.disable()
    reset_btn.disable()


# Creamos un método para generar cubos:
def cube_generator(pos):
    # Definición de una entidad en 3D
    return Entity(
        position=pos,  # Posición inicial del objeto.
        model='cube',  # Modelo geométrico
        scale=Vec3(1, 1, 1),  # Escala
        color=color.olive,  # Color del objeto.
        collider='box'  # "Hitbox"
    )


# Creamos un suelo.
floor = Entity(
    position=Vec3(0, -10, 0),
    model="plane",
    scale=60,
    color=color.black10,
    collider="box"
)
# Generamos el cubo de salida
cube_generator(Vec3(0, 0, 0))
rd_val = 10

for i in range(10):
    # Llamamos al método para generar cubos, y los mostramos de forma aleatoria.
    cube_generator(Vec3(0, 0, random.randint(0, i)))

# Definimos una meta pintando un cubo verde al final de la pasarela.
finish = cube_generator(Vec3(0, 0, 10))
finish.color = color.rgba(0, 255, 128, 255)  # Se puede configurar el color en RGB-A.


# Este código se va a ejecutar siempre.
def update():
    if player.position.y < -9.9:
        player.position = Vec3(0, 10, 0)
# Trazamos una línea invisible para detectar una posición.
    finish_marker = raycast(player.position, direction=Vec3(0, -1, 0), distance=2, ignore=[player])
    # Detectamos si hemos llegado a la meta.
    if finish_marker.entity == finish:
        # Generamos un texto al llegar. El parent es un elemento anidado que destruye todos los hijos, si hubiera.
        player.disable()
        end_txt.enable()
        reset_btn.enable()
        reset_btn.on_click = spawn  # Volvemos a la posición inicial.


# Este método siempre se tiene que llamar input porque si no, no funciona.
def input(key):
    if key == "escape":
        quit()


app.run()
