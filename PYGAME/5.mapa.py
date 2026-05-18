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
muerto = False  

# Vida y Obstáculo
vida_actual = 100
caja_x = 900
caja_y = 540
caja_velocidad = 7

# ========================================
# DESAFÍO: VARIABLES PARA REINICIAR EL JUEGO
# ========================================
# Cuando el personaje pierda, el juego no debería cerrarse de inmediato.
# Podés usar la variable muerto para saber si el jugador perdió.
# Pensá qué valores tendrían que volver al inicio cuando se reinicia:
# posición del personaje, vida, posición de la caja, salto y velocidad del salto.
# Más adelante podés crear una función llamada reiniciar_juego()
# para guardar todos esos valores iniciales en un solo lugar.

# ========================================
# DESAFÍO: VARIABLES PARA LOS NIVELES
# ========================================
# Necesitás saber en qué nivel está el jugador.
# Podrías crear una variable llamada nivel que empiece en 1.
# También necesitás contar cuántas cajas logró saltar el personaje.
# Podrías usar una variable llamada cajas_saltadas.
# Cuidado: una misma caja no debería contarse muchas veces.
# Para eso podrías usar una variable booleana que indique si esa caja ya fue contada.

# ========================================
# DESAFÍO: VARIABLES PARA FAROLAS DEL NIVEL 3
# ========================================
# En el nivel 3 aparecen farolas que iluminan partes del escenario.
# Podrías crear una lista con posiciones de farolas, por ejemplo:
# lista_farolas = [[150, 0], [460, 0], [770, 0]]
# Cada farola podría moverse hacia la izquierda igual que las nubes y las cajas.
# Cuando una farola salga de la pantalla, debería volver a aparecer por la derecha.

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

def personaje_saltando(pantalla, X, Y):
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
    pygame.draw.rect(pantalla,(0,0,100),(X + 40,Y + 10,20,30))
    pygame.draw.rect(pantalla,(0,0,100),(X + 0,Y + 60,40,50))
    # ZAPATOS Y BRAZOS                 x = 380 y = 420
    pygame.draw.rect(pantalla,(0,0,0),(X + 0,Y + 120,15,15))
    pygame.draw.rect(pantalla,(0,0,0),(X + 25,Y + 110,15,15))
    pygame.draw.rect(pantalla,(10,10,100),(X - 10,Y + 40,10,40))
    pygame.draw.rect(pantalla,(10,10,100),(X + 50,Y + 5,10,3))
    pygame.draw.rect(pantalla,(255, 220, 177),(X - 10,Y + 80,10,10))
    pygame.draw.rect(pantalla,(255, 220, 177),(X + 50,Y + 5,10,10))

def personaje_muerto(pantalla, X, Y):# x = 380   y = 420
    # CARA
    pygame.draw.rect(pantalla,(255, 220, 177),(X + 90,Y + 70,40,40))
    # GORRO
    pygame.draw.line(pantalla,(100,0,0),(X + 130,Y + 80),(X + 140,Y + 80),60)#
    pygame.draw.rect(pantalla,(100,0,0),(X + 140,Y + 70,35,40))
    # BIGOTE, OJOS Y ROPA
    # pygame.draw.rect(pantalla,(100,50,0),(X + 3,Y + 25,35,5))
    # pygame.draw.rect(pantalla,(0,0,0),(X + 3,Y + 9,5,10))
    # pygame.draw.rect(pantalla,(0,0,0),(X + 30,Y + 9,5,10))
    # pygame.draw.rect(pantalla,(100,0,0),(X + 0,Y + 40,40,20))
    # pygame.draw.rect(pantalla,(0,0,100),(X + 0,Y + 40,10,40))
    # pygame.draw.rect(pantalla,(0,0,100),(X + 30,Y + 40,10,40))
    pygame.draw.rect(pantalla,(0,0,100),(X + 40,Y + 70,50,40))
    # ZAPATOS Y BRAZOS
    # pygame.draw.rect(pantalla,(0,0,0),(X + 0,Y + 110,15,15))
    # pygame.draw.rect(pantalla,(0,0,0),(X + 25,Y + 110,15,15))
    # pygame.draw.rect(pantalla,(10,10,100),(X - 10,Y + 40,10,40))
    # pygame.draw.rect(pantalla,(10,10,100),(X + 40,Y + 40,10,40))
    # pygame.draw.rect(pantalla,(255, 220, 177),(X - 10,Y + 80,10,10))
    # pygame.draw.rect(pantalla,(255, 220, 177),(X + 40,Y + 80,10,10))

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

# ========================================
# DESAFÍO: CARTEL DE "PERDISTE"
# ========================================
# Creá una función para dibujar el mensaje de derrota.
# Podés usar pygame.font.SysFont() para crear una fuente.
# Con fuente.render() podés convertir un texto en una imagen.
# Con get_rect(center=(400, 350)) podés centrar el texto en la pantalla.
# El mensaje principal debería decir "PERDISTE".
# También podés agregar un texto más pequeño que diga cómo reiniciar.

# ========================================
# DESAFÍO: EFECTO DE FONDO AL PERDER
# ========================================
# Cuando el jugador pierda, el escenario debe quedar quieto.
# Además, el fondo debería verse diferente.
# Una opción es crear una superficie transparente:
# velo = pygame.Surface((800, 700), pygame.SRCALPHA)
# Luego podés pintarla con un color semitransparente.
# Por último, dibujala sobre la pantalla con pantalla.blit().
# Eso puede crear un efecto de difuminado o de pantalla apagada.

# ========================================
# DESAFÍO: FUNCIÓN PARA CAMBIAR DE NIVEL
# ========================================
# Creá una función que revise cuántas cajas saltó el jugador.
# Si está en nivel 1 y saltó más de 10 cajas, debe pasar al nivel 2.
# Si está en nivel 2 y saltó 15 cajas, debe pasar al nivel 3.
# En cada cambio de nivel conviene reiniciar el contador de cajas saltadas.
# También podés cambiar la velocidad de la caja o el lugar donde reaparece.

# ========================================
# DESAFÍO: FONDOS SEGÚN EL NIVEL
# ========================================
# El nivel 1 puede mantener el cielo azul.
# El nivel 2 debería tener un cielo más amarillo o anaranjado.
# Eso simula que se está haciendo más tarde.
# El nivel 3 debería tener un cielo más oscuro.
# Podés resolverlo con condicionales:
# if nivel == 1:
#     pantalla.fill((0, 150, 255))
# elif nivel == 2:
#     pantalla.fill((245, 178, 70))
# else:
#     pantalla.fill((18, 25, 55))

# ========================================
# DESAFÍO: FAROLAS Y OSCURIDAD DEL NIVEL 3
# ========================================
# Dibujá farolas usando rectángulos, líneas y círculos.
# Cada farola debería tener una luz.
# Para oscurecer la pantalla podés crear una superficie negra transparente.
# Después, sobre esa superficie, podés dibujar zonas transparentes donde haya luz.
# La idea es que el personaje solo se vea cuando esté debajo de una farola.
# Pista: pygame.Surface((800, 700), pygame.SRCALPHA) permite usar transparencia.


# --- BUCLE PRINCIPAL ---
control = True

while control:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            control = False

        # ========================================
        # DESAFÍO: REINICIAR CON TECLA O CLICK
        # ========================================
        # Si el jugador perdió, debería poder reiniciar.
        # Revisá si muerto es True.
        # Luego detectá si el evento es pygame.KEYDOWN o pygame.MOUSEBUTTONDOWN.
        # Si pasa eso, llamá a una función que reinicie todas las variables.


    # ========================================
    # DESAFÍO: DETENER EL JUEGO AL PERDER
    # ========================================
    # Cuando muerto sea True, el juego debería dejar de moverse.
    # Para eso, podés encerrar los controles, la física,
    # el movimiento de nubes, el movimiento de caja y las colisiones
    # dentro de un if que solo se ejecute si muerto es False.

    # 1. Controles
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]: x -= velocidad
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]: x += velocidad
    if not salto and (teclas[pygame.K_SPACE] or teclas[pygame.K_w]):
        salto = True
    # Evitar que el personaje salga de la pantalla
    if x < 0:
        x = 0

    if x > 760:
        x = 760

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

    # ========================================
    # DESAFÍO: CONTAR CAJAS SALTADAS
    # ========================================
    # Una caja cuenta como saltada cuando ya pasó al personaje.
    # Podés comparar la posición de la caja con la posición x del jugador.
    # Por ejemplo: si caja_x + 50 es menor que x, la caja ya pasó.
    # Sumá 1 al contador de cajas saltadas.
    # Usá una variable booleana para no sumar muchas veces la misma caja.
    # Cuando la caja reaparece por la derecha, esa variable debería volver a False.
    # Después de sumar una caja, revisá si corresponde cambiar de nivel.

    # ========================================
    # DESAFÍO: MOVER FAROLAS EN NIVEL 3
    # ========================================
    # Si el nivel actual es 3, mové las farolas hacia la izquierda.
    # Si una farola sale de la pantalla, hacela reaparecer por la derecha.
    # Podés usar un for para recorrer la lista de farolas.
        


    # 5. Colisión (Detección de choque)

    # El personaje no empieza exactamente en x, y.
    # Tiene gorro arriba, brazos a los costados y zapatos abajo.
    # Por eso el rectángulo invisible tiene que cubrir todo el cuerpo.
    rect_jugador = pygame.Rect(x - 10, y - 40, 60, 165)

    # La caja se dibuja de 50x50, entonces su rectángulo también debe ser 50x50.
    rect_caja = pygame.Rect(caja_x, caja_y, 50, 50)

    if rect_jugador.colliderect(rect_caja):
        vida_actual -= 20

        # Mandamos la caja lejos para que no reste vida muchas veces seguidas.
        caja_x = 950

        # Evitamos que la vida baje de 0.
        if vida_actual <= 0:
            # vida_actual = 0
            muerto = True

    # ========================================
    # DESAFÍO: FINALIZAR LA PARTIDA
    # ========================================
    # Cuando la vida llegue a 0, la variable muerto debe pasar a True.
    # También conviene dejar vida_actual en 0 para que no muestre números negativos.
    # Recordá que el juego no debería cerrarse: debe quedar en pantalla
    # mostrando el cartel "PERDISTE" hasta que el jugador reinicie.

  
    
    # 6. Dibujo
    pantalla.fill((0, 150, 255)) # Fondo azul

    # ========================================
    # DESAFÍO: CAMBIAR EL COLOR DEL CIELO
    # ========================================
    # En vez de usar siempre el mismo fill(),
    # probá cambiar el color según el nivel.
    # Nivel 1: azul de día.
    # Nivel 2: amarillo/anaranjado de atardecer.
    # Nivel 3: azul oscuro o casi negro.
    
    # Sol
    pygame.draw.circle(pantalla, (255, 255, 0), (700, 80), 50)
    
    # Nubes
    for n in lista_nubes:
        nubes_dibujo(pantalla, n[0], n[1])

    # ========================================
    # DESAFÍO: DIBUJAR FAROLAS EN NIVEL 3
    # ========================================
    # En el nivel 3, además del fondo oscuro, dibujá farolas.
    # Podés reemplazar o acompañar las nubes con farolas.
    # Cada farola puede tener un poste, un brazo y un círculo amarillo de luz.
     
        
    # Suelo (Línea verde gruesa)
    pygame.draw.line(pantalla, (0, 200, 0), (0, 600), (800, 600), 200)
    
    # Objetos y Personaje
    pygame.draw.rect(pantalla, (139, 69, 19), (caja_x, caja_y, 50, 50)) # La Caja
    if salto:
        personaje_saltando(pantalla, x, y)
    elif muerto:
        personaje_muerto(pantalla, x, y) 
    else:    
        dibujar_personaje(pantalla, x, y)

    # ========================================
    # DESAFÍO: OSCURIDAD DEL NIVEL 3
    # ========================================
    # Después de dibujar el personaje y la caja,
    # podés dibujar una capa oscura encima de todo.
    # Luego hacé que las zonas cerca de las farolas queden iluminadas.
    # Así, cuando el personaje no esté bajo una luz, casi no se verá.

    # ========================================
    # DESAFÍO: MOSTRAR CARTEL DE DERROTA
    # ========================================
    # Si muerto es True, dibujá el efecto de fondo y el cartel "PERDISTE".
    # Este dibujo debe ir al final para que aparezca por encima del escenario.
    
        
    dibujar_interfaz(pantalla, vida_actual)
    
    


    pygame.display.flip()
    reloj.tick(60)
    


pygame.quit()
