#multiprocesamiento (Ejecucion de varios procesos a la vez)
import time
import threading


def for1():

    for i in range(1,21):
        print(i,end=",")
        time.sleep(1)

def for2():
    for i in range(10, 31):
        print(i, end=",")
        time.sleep(1)

def for3():
    for i in range(10,200,10):
        print(i, end=",")
        time.sleep(1)

def suma():
    a = int(input("primer numero: "))
    b = int(input("segundo numero: "))
    suma = a + b
    print("la suma es : ", suma)


#creamos los hilos para cada funcion y luego lanzarems en paralelo
hilo1 = threading.Thread(target=for1)
hilo2 = threading.Thread(target=for2)
hilo3 = threading.Thread(target=for3)
hilo4 = threading.Thread(target=suma)


hilo1.start()
hilo2.start()
hilo3.start()
hilo4.start()



hilo1.join()
print("\n-------")
hilo2.join()
print("\n-------")
hilo3.join()
print("\n-------")
hilo4.join()


print("\nprograma terminado")