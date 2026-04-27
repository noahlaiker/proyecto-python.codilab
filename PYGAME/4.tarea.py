import pygame #IMPORTAMOS la libreria pygame

pygame.init()#INICIAMOS pygame

#creamos la ventana "pantalla"
#-accedemos primero al modulo pygame
#-luego al objeto display
#-luego al metodo set_mode()
#-y le pasamos una tupla (ancho,alto)
pantalla = pygame.display.set_mode((800,700))

#pongamos un titulo al juego
pygame.display.set_caption("practica de lineas")

#creamos un reloj para controlar los fps
reloj = pygame.time.Clock()

#creamos una variable de control
control = True



#creamos el gameloop (el corazon del juego)
while control:
    #escuchamos lo que pasa con el teclado y con el mouse
    for evento in pygame.event.get():
        #si el usuario toca la X cerramos la ventana
        if evento.type == pygame.QUIT:
            control = False

    #color de fondo
    pantalla.fill((100,100,100))
    
    #========================================
# TAREA:
# 1- vas a dibujar 3 lineas usando pygame.draw.line()
# 2- una linea debe ser horizontal
# 3- otra linea debe ser vertical
# 4- otra linea debe ser diagonal
# 5- cada linea tiene que tener un color distinto
# 6- investiga cuantos parametros recibe draw.line()
# 7- prueba cambiar el ultimo parametro para hacer la linea mas gruesa
#
# pista:
# pygame.draw.line(superficie,color,(x1,y1),(x2,y2),grosor)
#========================================

# pygame.draw.line() recibe 4 parametros obligatorios y 1 opcional

# 1) superficie -> donde se va a dibujar la linea
# 2) color -> el color de la linea
# 3) punto_inicial -> donde empieza la linea (x1,y1)
# 4) punto_final -> donde termina la linea (x2,y2)
# 5) grosor -> es opcional, sirve para cambiar el ancho de la linea

# ejemplo:
# pygame.draw.line(pantalla,(255,0,0),(100,100),(300,100),5)
    


 #   pygame.draw.line(pantalla,(0,0,100),(0,100),(20,10),20)
 #   pygame.draw.line(pantalla,(0,100,0),(100,200),(200,900),20)
  #  pygame.draw.line(pantalla,(100,0,0),(100,100),(10,1800),20)
  #LETRA N                     RGB   origen   destino  ancho
    pygame.draw.line(pantalla,(0,0,0),(50,450),(50,150),8)
    pygame.draw.line(pantalla,(0,0,0),(50,150),(180,450),8)
    pygame.draw.line(pantalla,(0,0,0),(180,450),(180,150),8)

    pygame.draw.line(pantalla,(100,0,0),(300,500),(400,500),8)
    pygame.draw.line(pantalla,(100,0,0),(300,500),(300,200),8)
    pygame.draw.line(pantalla,(100,0,0),(400,500),(400,200),8)
    pygame.draw.line(pantalla,(100,0,0),(300,200),(400,200),8)
    
    pygame.draw.line(pantalla,(0,0,100),(400,500),(500,200),8)
    pygame.draw.line(pantalla,(0,0,100),(500,200),(600,500),8)
    pygame.draw.line(pantalla,(0,0,100),(605,300),(400,300),8)
    
    pygame.draw.line(pantalla,(0,100,0),(605,500),(600,200),8)
    pygame.draw.line(pantalla,(0,100,0),(700,500),(700,200),8)
    pygame.draw.line(pantalla,(0,100,0),(600,300),(700,300),8)
    
    #ahora vamos a dibujar circulos lo vamos a
    #con el metodo circle
    #el metodo circle lleva
    #parametros el primero es para la superficie donde se dibuja
    #tupla con x,y
    #el segundo es para el color del circulo
    #el tercero es el centro del circulo
    #el cuarto es el tamaño
    #y el quinto es el grosor(opcional)
    #SOL                           R G B
    pygame.draw.circle(pantalla,(120,90,0),(700,90),100,100)
    #vamos a dibujar un rectangulo
    #el metodo es .rect()
    #y lleva 4 parametros
    #el primero es la superficie
    #el segundo es el color
    #el tercero es una tupla con 4 elementos
    #-el primero es la posicion horizontal
    #el segundo es la posicion vertical
    #-el tercero es cuanto mide el ancho
    #-el cuarto es cuanto mide de alto
    #el cuarto y ultimo parametro de rect es el grosor(opcional)
    pygame.draw.rect(pantalla,(0,0,100),(100,50,50,50),100)
    #triangulo
    #vamos a usar el metodo polygon
    #este tiene 4 parametros
    #el primero es la superficie
    #el segundo es el color
    #el tercero es una lista
    #-la lista esta compuesta por 3 elementos cada uno de ellos es una tupla con 2 numeros
    #-el primero rpresenta al eje X y el segundo al eje Y
    #y el cuarto es el grosor(opcional)
    pygame.draw.polygon(pantalla,(0,100,0),[(40,100),(100,50),(10,50)],100)
    #LETRA O
    #ACA VAS A DIBUJAR TUS LINEAS

    #actualizamos la pantalla
    pygame.display.flip()

    #limitamos los fps
    reloj.tick(60)

#cerramos pygame correctamente
pygame.quit()