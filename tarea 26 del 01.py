# 🧟‍♂️ TAREA POO — Clase DiaEnLaBalsa
# Objetivo: Representar un día del juego usando Programación Orientada a Objetos,
# donde el clima y los eventos afectan al estado del jugador.

# CONTEXTO:
# Estás en una balsa en medio del mar.
# Cada día tiene un clima y puede pasar un evento.
# Ese día afecta la vida, el hambre, la sed y la fogata del jugador.

# ==================================================
# 1) CREAR LA CLASE DiaEnLaBalsa
# ==================================================

# Crear una clase llamada DiaEnLaBalsa.

# El constructor debe recibir:
# - numero_dia (número entero)
# - clima (texto: "calor", "lluvia" o "nieve")
# - evento (texto: "nada", "caja", "tiburon" o "mini_jefe")

class DiaEnLaBalsa:
    def __init__(self, numero_dia, clima, evento):
        self.numero_dia = numero_dia
        self.clima = clima
        self.evento = evento
    def descripcion(self):
        print("el numero de dia es " + str(self.numero_dia))
        print("el clima es " + self.clima)
        print("el evento es " + self.evento)
    def aplicar_efectos(self,vida,hambre,sed,fogata_encendida):
        hambre = hambre + 10
        sed = sed + 10
        if self.clima == "calor":
            sed = sed + 15
        elif self.clima == "lluvia":
            if fogata_encendida == True:
                fogata_encendida = False
        elif self.clima == "nieve":
            if fogata_encendida == False:
                vida = vida - 10
        if self.evento == "nada":
            pass
        elif self.evento == "caja":
            hambre = hambre - 10
        elif self.evento == "tiburon":
            vida = vida - 15
        elif self.evento == "mini_jefe":
            vida = vida - 30
        if hambre < 0:
            hambre = 0
        if sed < 0:
            sed = 0
        if vida < 0:
            vida = 0
        return vida,hambre,sed,fogata_encendida
    
semana = []
semana.append(DiaEnLaBalsa(1,"lluvia","nada"))
semana.append(DiaEnLaBalsa(2,"calor","caja"))
semana.append(DiaEnLaBalsa(3,"nieve","tiburon"))
semana.append(DiaEnLaBalsa(4,"lluvia","nada"))
semana.append(DiaEnLaBalsa(5,"nieve","mini_jefe"))  

vida = 100
sed = 0
hambre = 0
fogata_encendida = True 

for dia_semana in semana:
    dia_semana.descripcion()
    vida,hambre,sed,fogata_encendida = dia_semana.aplicar_efectos(vida,hambre,sed,fogata_encendida)
    print(vida = str(vida))
    print(sed = str(sed))
    print(hambre = str(hambre))
    print(fogata_encendida = (fogata_encendida))
    
if vida > 0:
    print("sobreviviste")
else:
    print("no sobreviviste")
    
# Guardar esos valores como atributos del objeto.

# ==================================================
# 2) MÉTODOS DE LA CLASE
# ==================================================

# Crear un método llamado descripcion()
# Este método debe mostrar un texto que diga:
# "Día X | Clima: ... | Evento: ..."

# Crear un método llamado aplicar_efectos(...)
# Este método debe:
# - Recibir como datos:
#     vida
#     hambre
#     sed
#     fogata_encendida
#
# - Devolver los valores nuevos de:
#     vida
#     hambre
#     sed
#     fogata_encendida

# REGLAS DEL DÍA (expresadas en lenguaje natural):

# A) Al comenzar el día:
#    - El hambre aumenta en 10
#    - La sed aumenta en 10

# B) Según el clima:
#    - Si el clima es "calor":
#         la sed aumenta en 15
#    - Si el clima es "lluvia":
#         si la fogata está encendida, la fogata se apaga
#    - Si el clima es "nieve":
#         si la fogata está apagada, la vida baja en 10
                
# C) Según el evento:
#    - Si el evento es "nada":
#         no pasa nada extra
#    - Si el evento es "caja":
#         el hambre baja en 10 (no puede quedar negativa)
#    - Si el evento es "tiburon":
#         la vida baja en 15
#    - Si el evento es "mini_jefe":
#         la vida baja en 30

# D) Límites importantes:
#    - El hambre no puede ser menor a 0
#    - La sed no puede ser menor a 0
#    - La vida no puede ser menor a 0

# ==================================================
# 3) CREAR LOS DÍAS DEL JUEGO
# ==================================================

# Crear una lista llamada semana.
# En esa lista, crear 5 objetos DiaEnLaBalsa.

# La semana debe tener:
# - Al menos un día con clima "lluvia"
# - Al menos un día con clima "nieve"
# - Un día con evento "caja"
# - Un día con evento "tiburon"
# - Un día con evento "mini_jefe" (idealmente el último)

# ==================================================
# 4) SIMULACIÓN DE LA SEMANA
# ==================================================

# Crear las variables iniciales del jugador (NO una clase):
# - vida empieza en 100
# - hambre empieza en 0
# - sed empieza en 0
# - fogata_encendida empieza como True

# Para cada día de la semana:
# - Llamar al método descripcion()
# - Llamar al método aplicar_efectos(...)
# - Guardar los valores nuevos que devuelve
# - Mostrar el estado del jugador al final del día:
#     Vida, Hambre, Sed y Fogata (True o False)
#
# IMPORTANTE:
# - Usar print con + y str()
# - No usar comas ni f-strings

# ==================================================
# 5) CONDICIÓN FINAL
# ==================================================

# Al terminar el último día:
# - Si la vida es mayor a 0:
#     mostrar "Sobreviviste varios días en la balsa"
# - Si la vida es igual a 0:
#     mostrar "No sobreviviste en la balsa…"

# ==================================================
# EXTRA (OPCIONAL)
# ==================================================

# Crear un método llamado encender_fogata(...)
# Este método debe:
# - Recibir si la fogata está encendida o apagada
# - Recibir cuánta madera hay
# - Solo permitir encender la fogata si hay al menos 2 de madera
# - Devolver el nuevo estado de la fogata y la madera restante
