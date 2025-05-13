import time
from datetime import datetime
COLOR_ROJO = "\033[1;31m"
COLOR_AZUL = "\033[1;34m"
COLOR_ROSADO = "\033[1;35m"
COLOR_AMARILLO = "\033[1;36m"
COLOR_ORIGINAL = "\033[0m"

def MostrarSaludo(nombre, color):
    for i in range(1,11):
        print(f"{color}hola {nombre}, bienvenido :)")
        time.sleep(0.05)

if __name__ == "main_":
    inicio=datetime.now()

    print(f"{COLOR_ROJO}INICIO DEL PROGRAMA A LAS {inicio}")

    MostrarSaludo("Jean", COLOR_ROSADO)
    MostrarSaludo("Merl", COLOR_AZUL)
    MostrarSaludo("UPEU", COLOR_AMARILLO)
    MostrarSaludo("C6 G1", COLOR_ROJO)
    final=datetime.now()
    total=(final-inicio).total_seconds()
    print(f"EL PROGRAMA A FINALIZADO A LAS {round(total,1)} segundos")