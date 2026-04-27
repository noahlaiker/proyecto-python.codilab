class Personaje:
    def __init__ (self,nombre,vida):
        self.nombre = nombre
        self.vida = vida
        
    def saludar (self):
        print("hola, soy " + self.nombre + " y tengo " + str(self.vida) + " de vida")
        
    def recibir_dano (self,cantidad):
        self.vida = self.vida - cantidad
        if self.vida < 0 :
            self.vida = 0

p1 = Personaje("noah",100)
p2 = Personaje("tiburon",150)

p1.saludar()
p2.saludar()

print(p1.nombre)
print(p2.vida)

dano = 30
p1.recibir_dano(dano)

print(p1.vida)

p1.saludar()
# TAREA POO – CLASE Personaje
# ============================
# 1) Crea DOS personajes usando la clase Personaje:
#    - uno que se llame "Noah" con 100 de vida
#    - otro que se llame "Tiburón" con 150 de vida
#
# 2) Haz que cada personaje salude usando el método saludar().
#
# 3) Haz que el tiburón le haga daño a Noah:
#    - llama al método recibir_daño(cantidad) sobre el objeto de Noah
#    - el daño puede ser 30 (por ejemplo)
#
# 4) Imprime en pantalla la vida final de Noah usando print(...)
#
# 5) EXTRA:
#    - Crea un tercer personaje llamado "Jefe final" con 300 de vida
#    - Haz que el jefe final reciba daño dos veces
#    - Muestra su vida después de cada golpe



