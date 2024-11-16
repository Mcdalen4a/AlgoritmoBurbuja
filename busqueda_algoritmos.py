import time
import random


def busqueda_lineal(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def busqueda_binaria(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def medir_tiempo_busqueda(algoritmo, lista, valor):
    start_time = time.time()
    resultado = algoritmo(lista, valor)
    end_time = time.time()
    return end_time - start_time, resultado

tamano_lista = 1000  
lista = [random.randint(1, 10000) for _ in range(tamano_lista)]


valor_buscado = random.choice(lista)

# Probar las búsquedas
print(f"Búsqueda Lineal: Tiempo = {medir_tiempo_busqueda(busqueda_lineal, lista, valor_buscado)[0]}s, Índice = {medir_tiempo_busqueda(busqueda_lineal, lista, valor_buscado)[1]}")
print(f"Búsqueda Binaria: Tiempo = {medir_tiempo_busqueda(busqueda_binaria, sorted(lista), valor_buscado)[0]}s, Índice = {medir_tiempo_busqueda(busqueda_binaria, sorted(lista), valor_buscado)[1]}")
