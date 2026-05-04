import pygame 

# Inicialización
pygame.init()

# Configuración de pantalla
pantalla = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Tarea: Obstáculo y Vida")
reloj = pygame.time.Clock()

# --- VARIABLES ---
# Nubes
lista_nubes = [[230, 150], [500, 120], [900, 170]]
velocidad_nubes = 2

# Personaje
x = 380
y = 420
velocidad = 5
salto = False
velocidad_salto = 15
gravedad = 1

# Vida y Obstáculo
vida_actual = 100
caja_x = 900
caja_y = 540
caja_velocidad = 7

# --- FUNCIONES ---
def dibujar_personaje(pantalla, X, Y):
    # CARA
    pygame.draw.rect(pantalla,(255, 220, 177),(X,Y,40,40))
    # GORRO
    pygame.draw.line(pantalla,(100,0,0),(X+20,Y-10),(X+20,Y),60)
    pygame.draw.rect(pantalla,(100,0,0),(X+3,Y-40,35,35))
    # BIGOTE, OJOS Y ROPA
    pygame.draw.rect(pantalla,(100,50,0),(X + 3,Y + 25,35,5))
    pygame.draw.rect(pantalla,(0,0,0),(X + 3,Y + 9,5,10))
    pygame.draw.rect(pantalla,(0,0,0),(X + 30,Y + 9,5,10))
    pygame.draw.rect(pantalla,(100,0,0),(X + 0,Y + 40,40,20))
    pygame.draw.rect(pantalla,(0,0,100),(X + 0,Y + 40,10,40))
    pygame.draw.rect(pantalla,(0,0,100),(X + 30,Y + 40,10,40))
    pygame.draw.rect(pantalla,(0,0,100),(X + 0,Y + 60,40,50))
    # ZAPATOS Y BRAZOS
    pygame.draw.rect(pantalla,(0,0,0),(X + 0,Y + 110,15,15))
    pygame.draw.rect(pantalla,(0,0,0),(X + 25,Y + 110,15,15))
    pygame.draw.rect(pantalla,(10,10,100),(X - 10,Y + 40,10,40))
    pygame.draw.rect(pantalla,(10,10,100),(X + 40,Y + 40,10,40))
    pygame.draw.rect(pantalla,(255, 220, 177),(X - 10,Y + 80,10,10))
    pygame.draw.rect(pantalla,(255, 220, 177),(X + 40,Y + 80,10,10))

def nubes_dibujo(pantalla, X, Y):    
    pygame.draw.circle(pantalla,(250,250,250),(X, Y), 40)
    pygame.draw.circle(pantalla,(250,250,250),(X-50, Y), 40)
    pygame.draw.circle(pantalla,(250,250,250),(X-25, Y-30), 40)
    pygame.draw.circle(pantalla,(250,250,250),(X-25, Y-30), 40)
    pygame.draw.circle(pantalla,(250,250,250),(X-60, Y-30), 40)
    pygame.draw.circle(pantalla,(250,250,250),(X-80, Y-3), 40)

def dibujar_interfaz(pantalla, vida):
    # --- Elegir color ---
    color = (0, 255, 0)
    if vida < 35: color = (255, 0, 0)
    elif vida < 65: color = (255, 255, 0)
    # Dibujar barra
    pygame.draw.rect(pantalla, (50, 50, 50), (20, 20, 200, 25))
    pygame.draw.rect(pantalla, color, (20, 20, vida * 2, 25))

# --- BUCLE PRINCIPAL ---
control = True
# ============================================================ 
# NOAH: ARREGLEMOS TU JUEGO PASO A PASO
# No borres todo. La idea es encontrar qué está fallando y corregirlo.
# ============================================================

# 1) Primero mirá esta parte:
#    Hay un choque entre rect_jugador y rect_caja,
#    pero el problema es que esos rectángulos todavía no existen.
#    O sea: Python no puede revisar un choque si antes no le dijiste
#    dónde está el jugador y dónde está la caja.

# 2) El orden correcto debería ser:
#    - mover al personaje
#    - mover la caja
#    - crear rect_jugador y rect_caja
#    - revisar si chocaron

# 3) Buscá si tenés un:
#    if rect_jugador.colliderect(rect_caja):
#    antes de haber creado rect_jugador y rect_caja.
#    Si está antes, ese bloque está en el lugar incorrecto.

# 4) También tenés dos partes que revisan el choque.
#    Dejá una sola.
#    Si dejás las dos, el código queda más confuso y puede restar vida mal.

# 5) Después de mover la caja, ahí sí creá los rectángulos:
#    uno para el jugador y otro para la caja.
#    Pensá que el rectángulo es como una "zona invisible" que usa el juego
#    para saber si dos cosas se tocaron.

# 6) La caja mide 50 por 50 cuando la dibujás.
#    Entonces rect_caja también debería medir 50 por 50.

# 7) El personaje es más alto que la cara.
#    Tiene gorro, cuerpo, piernas y zapatos.
#    Por eso el rectángulo del jugador tiene que cubrir casi todo el personaje,
#    no solamente la cabeza.

# 8) Cuando haya choque:
#    - restá vida
#    - mandá la caja hacia la derecha otra vez
#    - asegurate de que la vida no baje de 0

# 9) Ahora mirá las nubes.
#    Ya hiciste una función para dibujarlas, pero no la estás usando.
#    La función se llama nubes_dibujo().

# 10) En la parte donde dice "# Nubes",
#     en vez de volver a moverlas, tenés que dibujarlas.
#     Las nubes se mueven en la parte de lógica.
#     Las nubes se dibujan en la parte de dibujo.

# 11) Regla para acordarte:
#     Primero se calcula qué pasa en el juego.
#     Después se dibuja todo en pantalla.

# 12) Cuando lo termines, probá esto:
#     - el juego no debería tirar error
#     - la caja debería moverse hacia la izquierda
#     - si la caja toca al personaje, baja la vida
#     - la vida no debería bajar de 0
#     - las nubes deberían verse
#     - los rectángulos rojos deberían marcar las zonas de choque
while control:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            control = False


    # 1. Controles
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]: x -= velocidad
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]: x += velocidad
    if not salto and (teclas[pygame.K_SPACE] or teclas[pygame.K_w]):
        salto = True

    # 2. Física de Salto
    if salto:
        y -= velocidad_salto
        velocidad_salto -= gravedad
        if y >= 420:
            y = 420
            salto = False
            velocidad_salto = 15

    # 3. Mover Nubes
    for n in lista_nubes:
        n[0] -= velocidad_nubes
        if n[0] < -100: n[0] = 850

    # 4. Mover Caja
    caja_x -= caja_velocidad
    if caja_x < -50:
        caja_x = 900

    # 5. Colisión (Detección de choque)
    rect_jugador = pygame.Rect(x, y, 40, 120)
    rect_caja = pygame.Rect(caja_x, caja_y, 50, 50)

    if rect_jugador.colliderect(rect_caja):
        vida_actual -= 20
        caja_x = 950 # Alejar la caja para que no golpee dos veces
        if vida_actual < 0: vida_actual = 0
        # El personaje mide unos 40 de ancho y 120 de alto aprox.
# Usamos (x, y - 40) para incluir la gorra que dibujaste arriba de la cabeza.
        rect_jugador = pygame.Rect(x, y - 40, 40, 160)
        # Si dibujas un rect de 50x50, el colisionador debe ser igual
        rect_caja = pygame.Rect(caja_x, caja_y, 50, 50)

    # 6. Dibujo
    pantalla.fill((0, 150, 255)) # Fondo azul
    
    # Sol
    pygame.draw.circle(pantalla, (255, 255, 0), (700, 80), 50)
    
    # Nubes
    for n in lista_nubes: 
     n[0] -= velocidad_nubes
     
        
    # Suelo (Línea verde gruesa)
    pygame.draw.line(pantalla, (0, 200, 0), (0, 600), (800, 600), 200)
    
    # Objetos y Personaje
    pygame.draw.rect(pantalla, (139, 69, 19), (caja_x, caja_y, 50, 50)) # La Caja
    dibujar_personaje(pantalla, x, y)
    dibujar_interfaz(pantalla, vida_actual)

    # Esto dibuja bordes rojos donde el juego "cree" que están los personajes
    pygame.draw.rect(pantalla, (255, 0, 0), rect_jugador, 2)
    pygame.draw.rect(pantalla, (255, 0, 0), rect_caja, 2)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
