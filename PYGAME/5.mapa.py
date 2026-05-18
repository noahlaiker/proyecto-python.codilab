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


# --- BUCLE PRINCIPAL ---
control = True

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

  
    
    # 6. Dibujo
    pantalla.fill((0, 150, 255)) # Fondo azul
    
    # Sol
    pygame.draw.circle(pantalla, (255, 255, 0), (700, 80), 50)
    
    # Nubes
    for n in lista_nubes:
        nubes_dibujo(pantalla, n[0], n[1])
     
        
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
    
    

        
    dibujar_interfaz(pantalla, vida_actual)
    
    


    pygame.display.flip()
    reloj.tick(60)
    


pygame.quit()
