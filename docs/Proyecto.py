import statistics
import math

def datos_no_agrupados(lista):
    n = len(lista)
    media = sum(lista) / n
    dato_mayor = max(lista)
    dato_menor = min(lista)
    moda = statistics.multimode(lista)  # Puede haber más de una moda
    varianza = sum((x - media) ** 2 for x in lista) / n
    desviacion_estandar = math.sqrt(varianza)
    
    print("Datos no agrupados:")
    print(f"Media aritmética: {media}")
    print(f"Dato mayor: {dato_mayor}")
    print(f"Dato menor: {dato_menor}")
    print(f"Moda(s): {moda}")
    print(f"Varianza: {varianza}")
    print(f"Desviación estándar: {desviacion_estandar}")

def datos_agrupados(intervalos, frecuencias):
    n = sum(frecuencias)
    puntos_medios = [(intervalo[0] + intervalo[1]) / 2 for intervalo in intervalos]
    
    # Media aritmética
    media = sum(punto * frec for punto, frec in zip(puntos_medios, frecuencias)) / n
    
    # Moda (el intervalo con mayor frecuencia)
    moda_intervalo = intervalos[frecuencias.index(max(frecuencias))]
    
    # Varianza
    varianza = sum(frec * (punto - media) ** 2 for punto, frec in zip(puntos_medios, frecuencias)) / n
    desviacion_estandar = math.sqrt(varianza)
    
    print("Datos agrupados:")
    print(f"Media aritmética: {media}")
    print(f"Moda: Intervalo {moda_intervalo}")
    print(f"Varianza: {varianza}")
    print(f"Desviación estándar: {desviacion_estandar}")

def main():
    num_elementos = int(input("Ingrese el número de elementos: "))
    
    if num_elementos < 30:
        # Datos no agrupados
        lista = []
        for i in range(num_elementos):
            num = int(input(f"Ingrese el elemento {i+1}: "))
            lista.append(num)
        datos_no_agrupados(lista)
    else:
        # Datos agrupados
        intervalos = []
        frecuencias = []
        num_intervalos = int(input("Ingrese el número de intervalos: "))
        for i in range(num_intervalos):
            limite_inferior = int(input(f"Ingrese el límite inferior del intervalo {i+1}: "))
            limite_superior = int(input(f"Ingrese el límite superior del intervalo {i+1}: "))
            frecuencia = int(input(f"Ingrese la frecuencia del intervalo {i+1}: "))
            intervalos.append((limite_inferior, limite_superior))
            frecuencias.append(frecuencia)
        datos_agrupados(intervalos, frecuencias)

if __name__ == "__main__":
    main()
