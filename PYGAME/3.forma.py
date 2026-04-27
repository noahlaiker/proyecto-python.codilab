import pygame #IMPORTAMOS la libreria pygame

pygame.init()#INICIAMOS pygame

#creamos la ventana "pantalla"
#-accedemos primero al modulo pygame
#-luego al objeto display
#-luego al metodo set_mode() 
#-y le pasamos una tupla (ancho,alto)
pantalla = pygame.display.set_mode((800,600))

#pogamos un titulo al juego
#esto se hace con el metodo set_caption()
#no hace falta crear una variable
#lo que hay que hacer es
#-1 accerder al modulo pygame
#-2accerder al objeto display
#-3 accerder al metodo set_caption()
#-4 escribi dentro del metodo el nombre del juego
pygame.display.set_caption("hola:D")

# pygame.Rect() se usa para crear un rectángulo.
# Recibe 4 parámetros:
# 1) posición en X
# 2) posición en Y
# 3) ancho
# 4) alto
#
# O sea:
# pygame.Rect(x, y, ancho, alto)
#
# Primero se crea el rectángulo
# y después se puede dibujar en pantalla.
cuadrado = pygame.Rect(200,200,100,100)

#creamos un reloj para controlar los fps
#-paso 1 crear una variable reloj
#-paso 2 dentro de esta variable vamos a acceder al metodo Clock() del objeto time
reloj = pygame.time.Clock()

#creamos un a variable de control (mientras sea True el juego sigue corriendo)
control = True

#creamos el gameloop (el corazon del juego)
while control:
    #escuchamos lo que pasa con el teclado y con el mause
    #lo hacemos con un bucle for y un iterador "evento" atraves del metodo get() del objeto event del modulo pygame
    for evento in pygame.event.get():
        #si el usuario toca la X cerramos la ventana
        if evento.type == pygame.QUIT:
            control = False
    #Vamos a ponerle color de fondo al juego
    #usaremos el metodo fill aplicado sobre la variable pantalla
    #               R    V   A
    pantalla.fill((100,100,100))
    
    #vamos a aprender a dibujar formas
    #para esto usaremos el objeto draw,y sus metodos rect() para rectangulos
    #metodo line() para lineas, circle() para circulos
    #polygon() esto es para poligonos
    #ellipse() para ellipses
    
    #rect() tiene 3 parametros,el primero es donde lo vamos a mostrar,
    #el segundo es el color y el tecero es datos de forma
    pygame.draw.rect(pantalla,(0,0,0),cuadrado)
    #actualizamos la pantalla
    #usando el meto flip(sin parametro) que pertenece al objeto display que pertene al modulo pygame
    pygame.display.flip()
    #vamos a limitar los fps
    reloj.tick(60)
            
            
            
            
            
            
            
            
            
            
#cerramos pygame correctamente
pygame.quit()      