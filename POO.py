#programacion orentiada a objetos
#el primer paso es crear la plantilla
class Personaje:
    #detro de la plantilla,lo primero que hay que hacer es usar
    #el metodo constructor (__init__()) para indicar
    #que atributos va a tener el objeto
    def __init__(self, nombre, vida):
        self.nombre = nombre #atributo/propiedad
        self.vida = vida #atributo
        
    #los segundo es escribir los metodos/funciones del objeto
    def saludar(self): #metodo
        print("hola, soy " + self.nombre)
        
    def recibir_dano(self, cantidad):
        self.vida -= cantidad
        print(self.nombre + " ahora tine " + self.vida + " de vida")
        
#ahora creamos un objeto a partir de esta plantilla
p1 = Personaje("noah",100)
p2 = Personaje("tiburon",150)

p1.saludar()
p2.saludar()

p1.recibir_dano(5)
print(p1.vida)

#name = p1.nombre
#name = "pedro"
        
#print (p1)