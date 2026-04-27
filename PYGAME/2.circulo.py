import pygame 

pygame.init()
ANCHO,ALTO = 800,600
pantalla = pygame.display.set_mode((ANCHO,ALTO))

pygame.display.set_caption("hola:D")

reloj = pygame.time.Clock()

control = True

#vamos a guarda la posicion del circulo
x = ANCHO//2
y = ALTO//2


while control:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            control = False
    
    #vamos a crear una variable tecla que va a guardar el metodo get_pressed() del objeto key del modulo pygame        
    tecla = pygame.key.get_pressed()
    
    #movimiento con WASD
    if tecla[pygame.K_w]:
        y = y - 3
    elif tecla[pygame.K_s]:
        y = y + 3
    elif tecla[pygame.K_a]:
        x -= 3
    elif tecla[pygame.K_d]:
        x += 3
            
    #               R    V   A
    pantalla.fill((100,100,100))
    
    #Dibujar el circulo
    #usando el metodo circle del objeto draw del modulo pygame
    #el metodo circle lleva 4 parametros,el primero es la superficie donde se va a dibujar
    #el segundo es el color,el tercero es la posicion y el cuarto es el tamaño y el radio
    pygame.draw.circle(pantalla,(200,100,100),(x,y),35)
        
    pygame.display.flip()
    reloj.tick(60)
            
            
            
            
            
            
            
            
            
            
pygame.quit()      