#Superviviente (Juego de la Balsa)
# 🧟‍♂️ TAREA POO
# Objetivo: Usar Programación Orientada a Objetos para representar
# al jugador en el juego de supervivencia en la balsa.

# 📌 CONTEXTO DEL JUEGO:
# Estás en una balsa en medio del mar.
# Tu personaje tiene vida, hambre, sed y días sobrevividos.
# Algunas acciones te ayudan y otras te hacen perder vida.

# ============================
# 1) CREAR LA CLASE
# ============================
class Superviviente:
    def __init__(self,nombre,vida,hambre,sed,dia):
        self.nombre = nombre
        self.vida = vida
        self.hambre = hambre
        self.sed = sed
        self.dia = dia
 
    def estado(self):
        print("nombre : " + self.nombre)
        print("vida : " + str(self.vida))
        print("hambre : " + str(self.hambre))
        print("sed : " + str(self.sed))
        print("dia : " + str(self.dia))
        
    def pasar_dia(self):
        self.dia += 1
        self.hambre += 10
        self.sed = self.sed + 10
        if self.hambre >= 80:
            self.vida -=  10
        if self.sed >= 80:
            self.vida -= 10
        if self.vida < 0:
            self.vida = 0
            
    def beber_agua(self):
        self.sed = self.sed - 30
        if self.sed < 0:
            self.sed = 0
        
    def comer(self):
        self.hambre = self.hambre - 30
        if self.hambre < 0:
            self.hambre = 0
        
# - pasar_dia()
#   Cada vez que se llama:
#   - dia aumenta en 1
#   - hambre aumenta en 10
#   - sed aumenta en 10
#   - si hambre es mayor o igual a 80 → vida baja 10
#   - si sed es mayor o igual a 80 → vida baja 10

# - beber_agua()
#   Reduce la sed en 30 (no puede bajar de 0).

# - comer()
#   Reduce el hambre en 30 (no puede bajar de 0).

# ============================
# 3) CREAR UN PERSONAJE
# ============================
personaje = Superviviente("noah",100,0,0,1)   
        
# Crea un Superviviente llamado "Noah" con:
# vida = 100
# hambre = 0
# sed = 0
# dia = 1

# Mostrá su estado inicial usando el método estado().

personaje.estado()

# ============================
# 4) SIMULACIÓN SIMPLE
# ============================

personaje.pasar_dia()
personaje.estado()
personaje.pasar_dia()
personaje.beber_agua()
personaje.comer()
personaje.estado()

# Simulá lo siguiente, llamando a métodos:
# - Pasa 1 día
# - Pasa otro día
# - Noah bebe agua
# - Pasa otro día
# - Noah come
# - Pasa otro día

# Después de cada acción importante,
# mostrá el estado del personaje.

# ============================
# 5) CONDICIÓN FINAL
# ============================

# Al final del programa:
# - Si la vida de Noah es mayor a 0:
#     imprimir "Sobreviviste en la balsa"
# - Si la vida es 0 o menos:
#     imprimir "No sobreviviste…"

if personaje.vida > 0:
    print ("sobreviviste")
else:
    print ("no sobreviviste")

#print (personaje.nombre)

# ============================
# Parte final
# ============================

#noah.recibir_danio(25)
#print(noah)

# - Agregá un método recibir_danio(cantidad)
# - Usalo para simular que un tiburón ataca y hace 25 de daño
# - Mostrá el estado después del ataque
