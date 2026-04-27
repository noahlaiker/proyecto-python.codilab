import pygame
import random

# ==========================
# 1) INICIALIZACIÓN BÁSICA
# ==========================

# Siempre hay que inicializar Pygame antes de usarlo
pygame.init()

# Tamaño de la ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Supervivencia en la Balsa - Demo")

# Reloj para controlar la velocidad del juego (frames por segundo)
clock = pygame.time.Clock()
FPS = 60  # intentaremos dibujar 60 veces por segundo

# ==========================
# 2) COLORES (R, G, B)
# ==========================

AZUL_AGUA    = (20, 80, 160)
MARRON_BALSA = (139, 69, 19)
BLANCO       = (255, 255, 255)
ROJO         = (200, 50, 50)
VERDE        = (50, 200, 80)
AMARILLO     = (230, 230, 50)
AZUL_CLARO   = (0, 180, 255)
GRIS_OSCURO  = (60, 60, 60)
NEGRO        = (0, 0, 0)

# Fuente para dibujar texto
fuente = pygame.font.SysFont(None, 24)

# ==========================
# 3) MUNDO DEL JUEGO
# ==========================

# La balsa: un rectángulo grande en el centro del mar
balsa_ancho, balsa_alto = 500, 350
balsa_rect = pygame.Rect(
    ANCHO // 2 - balsa_ancho // 2,
    ALTO // 2 - balsa_alto // 2,
    balsa_ancho,
    balsa_alto
)

# El jugador: un cuadrado blanco que se mueve sobre la balsa
jugador_tamano = 30
jugador_rect = pygame.Rect(
    ANCHO // 2 - jugador_tamano // 2,
    ALTO // 2 - jugador_tamano // 2,
    jugador_tamano,
    jugador_tamano
)
velocidad_jugador = 5  # píxeles por frame

# ==========================
# 4) VARIABLES DE ESTADO
# ==========================

vida   = 100   # 100 = perfecto, 0 = muerto
comida = 100   # 100 = lleno, 0 = muerto de hambre
agua   = 100   # 100 = sin sed, 0 = deshidratado
dia    = 1

# Usamos frames para contar días (cada pocos segundos sumamos 1)
contador_frames_dia = 0

# Cajas de recursos que aparecerán sobre la balsa
cajas = []
CAJA_TAMANO = 25
probabilidad_nueva_caja = 0.02  # 2% de probabilidad por frame de crear una caja


# ==========================
# 5) FUNCIONES AUXILIARES
# ==========================

def crear_caja():
    """
    Crea una caja de recursos en una posición aleatoria
    dentro del área de la balsa.
    """
    x = random.randint(balsa_rect.left + 10, balsa_rect.right - CAJA_TAMANO - 10)
    y = random.randint(balsa_rect.top + 10, balsa_rect.bottom - CAJA_TAMANO - 10)
    return pygame.Rect(x, y, CAJA_TAMANO, CAJA_TAMANO)


def dibujar_barra(x, y, valor, color, etiqueta):
    """
    Dibuja una barra de estado (vida, comida o agua) en la pantalla.
    valor va de 0 a 100.
    """
    ancho_max = 200
    alto_barra = 18

    # Aseguramos que el valor esté entre 0 y 100
    valor = max(0, min(100, valor))

    # Fondo gris de la barra
    pygame.draw.rect(ventana, GRIS_OSCURO, (x, y, ancho_max, alto_barra))

    # Parte rellena según el porcentaje
    ancho_valor = int(ancho_max * (valor / 100))
    pygame.draw.rect(ventana, color, (x, y, ancho_valor, alto_barra))

    # Texto encima de la barra
    texto = fuente.render(f"{etiqueta}: {int(valor)}", True, BLANCO)
    ventana.blit(texto, (x, y - 22))


# ==========================
# 6) BUCLE PRINCIPAL DEL JUEGO
# ==========================

corriendo = True

while corriendo:
    # 6.1) Controlar la velocidad del juego
    clock.tick(FPS)  # pausa lo necesario para ir a ~60 FPS

    # 6.2) Manejar eventos (teclado, ratón, cerrar ventana...)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False  # si tocan la X, salimos del bucle

    # 6.3) Leer teclas presionadas para mover al jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        jugador_rect.x -= velocidad_jugador
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        jugador_rect.x += velocidad_jugador
    if teclas[pygame.K_UP] or teclas[pygame.K_w]:
        jugador_rect.y -= velocidad_jugador
    if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
        jugador_rect.y += velocidad_jugador

    # 6.4) Evitar que el jugador salga de la balsa
    if jugador_rect.left < balsa_rect.left:
        jugador_rect.left = balsa_rect.left
    if jugador_rect.right > balsa_rect.right:
        jugador_rect.right = balsa_rect.right
    if jugador_rect.top < balsa_rect.top:
        jugador_rect.top = balsa_rect.top
    if jugador_rect.bottom > balsa_rect.bottom:
        jugador_rect.bottom = balsa_rect.bottom

    # 6.5) Actualizar recursos con el tiempo (simulamos el paso del tiempo)
    comida -= 0.05   # baja muy de a poco
    agua   -= 0.08   # el personaje tiene más sed que hambre

    # Si se queda sin comida o sin agua, comienza a perder vida
    if comida <= 0 or agua <= 0:
        vida -= 0.2

    # Evitamos que los valores se vayan de rango
    vida   = max(0, min(100, vida))
    comida = max(0, min(100, comida))
    agua   = max(0, min(100, agua))

    # 6.6) Contar días (cada 5 segundos = 1 día de juego)
    contador_frames_dia += 1
    if contador_frames_dia >= FPS * 5:  # 5 segundos * 60 FPS
        dia += 1
        contador_frames_dia = 0

    # 6.7) Crear nuevas cajas de recursos de vez en cuando
    if random.random() < probabilidad_nueva_caja:
        cajas.append(crear_caja())

    # 6.8) Revisar si el jugador toca alguna caja
    cajas_restantes = []
    for caja in cajas:
        if jugador_rect.colliderect(caja):
            # Al agarrar una caja, el jugador encuentra recursos:
            vida   += 5   # se cura un poquito
            comida += 20  # consigue comida
            agua   += 15  # consigue agua
        else:
            cajas_restantes.append(caja)
    cajas = cajas_restantes

    # Volvemos a limitar valores por las dudas
    vida   = max(0, min(100, vida))
    comida = max(0, min(100, comida))
    agua   = max(0, min(100, agua))

    # 6.9) Dibujar el fondo (mar) y la balsa
    ventana.fill(AZUL_AGUA)  # mar
    pygame.draw.rect(ventana, MARRON_BALSA, balsa_rect)  # balsa

    # Dibujar al jugador
    pygame.draw.rect(ventana, BLANCO, jugador_rect)

    # Dibujar las cajas de recursos
    for caja in cajas:
        pygame.draw.rect(ventana, VERDE, caja)

    # 6.10) Dibujar HUD (barras de vida/comida/agua y día)
    dibujar_barra(20, 20, vida, ROJO, "Vida")
    dibujar_barra(20, 70, comida, AMARILLO, "Comida")
    dibujar_barra(20, 120, agua, AZUL_CLARO, "Agua")

    texto_dia = fuente.render(f"Día: {dia}", True, BLANCO)
    ventana.blit(texto_dia, (ANCHO - 110, 20))

    instrucciones = fuente.render(
        "Mueve con flechas o WASD y agarra las cajas para sobrevivir.",
        True,
        BLANCO
    )
    ventana.blit(instrucciones, (40, ALTO - 40))

    # 6.11) Comprobar condición de fin de juego
    if vida <= 0:
        corriendo = False

    # 6.12) Actualizar la pantalla con todo lo que dibujamos
    pygame.display.flip()

# ==========================
# 7) PANTALLA FINAL (GAME OVER)
# ==========================

ventana.fill(NEGRO)

texto_fin = fuente.render("GAME OVER - La balsa no sobrevivió", True, ROJO)
texto_dias = fuente.render(f"Sobreviviste {dia} días", True, BLANCO)

ventana.blit(
    texto_fin,
    (ANCHO // 2 - texto_fin.get_width() // 2,
     ALTO // 2 - texto_fin.get_height())
)
ventana.blit(
    texto_dias,
    (ANCHO // 2 - texto_dias.get_width() // 2,
     ALTO // 2 + 10)
)

pygame.display.flip()

# Esperamos unos segundos para que pueda leer el mensaje
pygame.time.wait(4000)

# Cerramos Pygame
pygame.quit()
