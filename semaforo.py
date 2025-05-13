import threading  # Importamos la librería para trabajar con hilos
import time  # Importamos la librería para manejar el tiempo y simular retrasos

#  Semáforo con 3 "recursos" disponibles (pueden ser hilos que acceden a recursos limitados)
# Esto significa que hasta 3 hilos pueden acceder al recurso simultáneamente.
sem = threading.Semaphore(3)

#  Función que representa la tarea que realiza cada hilo
def acceder_recurso(nombre_hilo):
    """
    Esta función es ejecutada por cada hilo. Intenta acceder al recurso limitado.
    Cada hilo debe esperar su turno si los recursos están ocupados.
    """
    print(f"{nombre_hilo} esperando para acceder al recurso...")
    
    #  Intentamos "adquirir" el semáforo (es decir, disminuir el contador del semáforo)
    # Si el semáforo ya tiene 0, el hilo debe esperar a que otro hilo libere el recurso.
    sem.acquire()
    print(f"{nombre_hilo} ha accedido al recurso.")
    
    #  Simulamos el uso del recurso, lo que representa un proceso que lleva tiempo (2 segundos)
    time.sleep(2)
    
    #  Después de usar el recurso, liberamos el semáforo (aumentamos el contador)
    # Esto indica que otro hilo puede acceder al recurso.
    sem.release()
    print(f"{nombre_hilo} ha liberado el recurso.")

#  Creamos 5 hilos que intentarán acceder al recurso limitado
hilos = []
for i in range(5):
    hilo = threading.Thread(target=acceder_recurso, args=(f"Hilo-{i+1}",))  # Creamos el hilo
    hilos.append(hilo)  # Añadimos el hilo a la lista de hilos

#  Iniciamos todos los hilos
print("Iniciando los hilos...")
for hilo in hilos:
    hilo.start()

#  Esperamos a que todos los hilos terminen antes de finalizar el programa
# Usamos join() para bloquear el hilo principal hasta que todos los hilos terminen su ejecución
for hilo in hilos:
    hilo.join()

#  Mensaje final indicando que todos los hilos han terminado su ejecución
print("\nTodos los hilos han terminado su ejecución.")
