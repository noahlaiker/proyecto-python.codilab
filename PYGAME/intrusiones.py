# El error pasa porque Python llega a esta pregunta:
#
# if rect_jugador.colliderect(rect_caja):
#
# pero todavía no sabe qué es rect_jugador ni qué es rect_caja.
#
# Es como preguntarle:
# "¿El jugador chocó con la caja?"
# antes de decirle:
# "El jugador está acá" y "la caja está acá".
#
# Entonces, antes de revisar el choque, hay que crear las dos zonas invisibles:
#
# rect_jugador = pygame.Rect(...)
# rect_caja = pygame.Rect(...)

# ============================================================
# ORDEN CORRECTO DENTRO DEL WHILE
# ============================================================

# 1) Primero se leen las teclas.
#    Acá se mueve el jugador a la izquierda o a la derecha.
#
#    Ejemplo:
#    si toca izquierda, x baja
#    si toca derecha, x sube

# 2) Después se calcula el salto.
#    Si el jugador está saltando, cambia la variable y.
#    Recordá:
#    x es la posición horizontal
#    y es la posición vertical

# 3) Después se mueven las nubes.
#    Esto no tiene que ver con el choque, pero forma parte de la lógica del juego.

# 4) Después se mueve la caja.
#    La caja cambia su posición porque viene desde la derecha hacia la izquierda.
#
#    Esto es importante:
#    NO crees rect_caja antes de mover la caja,
#    porque si lo hacés, el rectángulo queda con la posición vieja.

# 5) Recién después de mover al jugador y mover la caja,
#    creás los rectángulos de colisión.
#
#    El rectángulo del jugador tiene que usar la posición actual:
#
#    rect_jugador = pygame.Rect(x, y - 40, 40, 160)
#
#    Usamos y - 40 porque el personaje tiene gorro arriba de la cabeza.
#    Si usáramos solamente y, el rectángulo no cubriría todo el personaje.
#
#    El 40 es el ancho aproximado del personaje.
#    El 160 es la altura aproximada contando gorro, cuerpo y piernas.

# 6) Después creás el rectángulo de la caja:
#
#    rect_caja = pygame.Rect(caja_x, caja_y, 50, 50)
#
#    La caja se dibuja de 50 por 50.
#    Entonces su zona de choque también tiene que medir 50 por 50.

# 7) Ahora sí podés preguntar si chocaron:
#
#    if rect_jugador.colliderect(rect_caja):
#
#    En este punto Python ya sabe dónde está el jugador
#    y también sabe dónde está la caja.

# ============================================================
# COSA IMPORTANTE
# ============================================================

# No pongas esto al principio del while:
#
# if rect_jugador.colliderect(rect_caja):
#
# porque al principio del while todavía no creaste los rectángulos.

# Tampoco crees los rectángulos adentro del if del choque.
#
# Esto estaría mal:
#
# if rect_jugador.colliderect(rect_caja):
#     rect_jugador = pygame.Rect(...)
#     rect_caja = pygame.Rect(...)
#
# Está mal porque para entrar al if, Python ya necesitaba conocer
# rect_jugador y rect_caja desde antes.

# ============================================================
# RESUMEN SIMPLE
# ============================================================

# El orden final tiene que ser:
#
# 1. Mover personaje
# 2. Mover caja
# 3. Crear rect_jugador
# 4. Crear rect_caja
# 5. Revisar si chocaron
# 6. Dibujar todo en pantalla

# ============================================================
# MINI GUÍA PARA ARREGLARLO
# ============================================================

# Buscá el primer:
#
# if rect_jugador.colliderect(rect_caja):
#
# Si está antes de esta parte:
#
# rect_jugador = pygame.Rect(...)
# rect_caja = pygame.Rect(...)
#
# entonces ese if está mal ubicado y hay que borrarlo o moverlo.

# Después dejá una sola parte de choque.
# No hacen falta dos if revisando lo mismo.
#
# La parte de choque debería quedar después de crear rect_jugador y rect_caja.