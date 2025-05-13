import threading

NUMERO_FILOSOFOS = 5

TIEMPO_PENSAR = 10
TIEMPO_COMER = 10

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

    def __init__(self, id_filosofo, nombre_filosofo):
        self.id_filosofo = id_filosofo
        self.nombre = nombre_filosofo
        self.tenedor_derecho = tenedores[id_filosofo]
        self.tenedor_izquierdo = tenedores[(id_filosofo+1)%NUMERO_FILOSOFOS]

    def pensar(self):
        pass

    def comer(self):
        pass


primer_filosofo = FILOSOFO(0, "Platon")
segundo_filosofo = FILOSOFO(1, "Socrates")
tercer_filosofo = FILOSOFO(2, "Aristoteles")
cuarto_filosofo = FILOSOFO(3, "Kanth")
quinto_filosofo = FILOSOFO(4, "Confucio")


