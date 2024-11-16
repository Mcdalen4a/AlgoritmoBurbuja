import time
import random


def generar_lista(tam):
    return [random.randint(1, 10000) for _ in range(tam)]


def burbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def seleccion(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insercion(arr):
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        while j >= 0 and clave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivote = arr[len(arr) // 2]
    izquierda = [x for x in arr if x < pivote]
    medio = [x for x in arr if x == pivote]
    derecha = [x for x in arr if x > pivote]
    return quicksort(izquierda) + medio + quicksort(derecha)


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        izquierda = arr[:mid]
        derecha = arr[mid:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                arr[k] = izquierda[i]
                i += 1
            else:
                arr[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            arr[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            arr[k] = derecha[j]
            j += 1
            k += 1


def medir_tiempo(algoritmo, lista):
    start_time = time.time()
    if algoritmo == quicksort:
        algoritmo(lista.copy())  
    else:
        algoritmo(lista)  
    end_time = time.time()
    return end_time - start_time


tam = 1000  
lista = generar_lista(tam)

print("Ordenación por Burbuja:", medir_tiempo(burbuja, lista.copy()))
print("Ordenación por Selección:", medir_tiempo(seleccion, lista.copy()))
print("Ordenación por Inserción:", medir_tiempo(insercion, lista.copy()))
print("Ordenación Rápida:", medir_tiempo(quicksort, lista.copy()))
print("Ordenación por Mezcla:", medir_tiempo(merge_sort, lista.copy()))
