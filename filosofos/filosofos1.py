import threading
import random
import time

NUMERO_FILOSOFOS = 5

TIEMPO_PENSAR = 10
TIEMPO_COMER = 10

ROJO = "\033[1;31m"
VERDE = "\033[1;32m"
AZUL = "\033[1;34m"
ROSADO = "\033[1;35m"
AMARILLO = "\033[1;36m"
ORIGINAL = "\033[0m"



tenedores = []

#Agregamos 5 locks a la lista tenedores
for i in range(NUMERO_FILOSOFOS):
     tenedores.append(threading.Lock())

#creamos nuestra clase FILOSOFO
#creamos nuestra clase FILOSOFO
class FILOSOFO(threading.Thread):

    id_filosofo = 0
    nombre = ''
    tenedor_izquierdo=0
    tenedor_derecho=0
    COLOR = ""

    #metodo constructor
    def __init__(self, id_filosofo, nombre_filosofo, color_filosofo):
        threading.Thread.__init__(self)
        self.COLOR = color_filosofo
        self.id_filosofo = id_filosofo
        self.nombre = nombre_filosofo
        self.tenedor_derecho = tenedores[id_filosofo]
        self.tenedor_izquierdo = tenedores[(id_filosofo+1)%NUMERO_FILOSOFOS]

        

    def pensar(self):
        tiempo = random.random() * TIEMPO_PENSAR #NUMERO ALEATORIO ENTRE 1 Y TIEMPO_PENSAR
        print(f"{self.COLOR}el filosofo {self.nombre} ({self.id_filosofo}) va a pensar durante {tiempo} segundos")
        time.sleep(tiempo)
        print(f"el filosofo {self.nombre} a terminado de pensar.{ORIGINAL}")        

    def comer(self):
    
        pass


primer_filosofo = FILOSOFO(0, "Platon", ROJO)
segundo_filosofo = FILOSOFO(1, "Socrates", VERDE)
primer_filosofo.pensar()
segundo_filosofo.pensar()


