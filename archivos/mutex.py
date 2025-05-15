import threading  # Importamos la librería para trabajar con hilos

#  Variable compartida entre los hilos
contador = 0

#  Mutex (candado) para evitar condiciones de carrera
mutex = threading.Lock()

#  Función que incrementa la variable compartida de forma segura
def incrementar_contador(nombre_hilo):
    """
    Esta función incrementa la variable 'contador' 10,000 veces.
    Usa un mutex para evitar que varios hilos la modifiquen al mismo tiempo.
    """
    global contador  # Indicamos que vamos a modificar la variable global

    for i in range(10000):
        # 🔹 Bloqueamos el acceso con el mutex
        with mutex:  
            contador += 1  # Incrementamos la variable compartida

        # 🔹 Opcional: Mostrar cada 2500 iteraciones (para ver progreso)
        if i % 2500 == 0:
            print(f"{nombre_hilo}: Iteración {i}, contador parcial: {contador}")

    print(f"{nombre_hilo} ha terminado.")  # Mensaje final de cada hilo

#  Crear dos hilos
hilo_1 = threading.Thread(target=incrementar_contador, args=("Hilo-1",))
hilo_2 = threading.Thread(target=incrementar_contador, args=("Hilo-2",))

#  Iniciar los hilos
print("Iniciando los hilos...")
hilo_1.start()
hilo_2.start()

#  Esperar a que ambos hilos terminen
hilo_1.join()
hilo_2.join()

#  Mostrar el resultado final
print(f"\n Valor final del contador: {contador} (debería ser 20000)")
