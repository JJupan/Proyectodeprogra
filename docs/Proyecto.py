def calcular_media(lista):
    return sum(lista) / len(lista)

def calcular_moda(lista):
    frecuencia = {}
    for num in lista:
        if num in frecuencia:
            frecuencia[num] += 1
        else:
            frecuencia[num] = 1
    max_frecuencia = max(frecuencia.values())
    modas = [key for key, value in frecuencia.items() if value == max_frecuencia]
    return modas, max_frecuencia

def calcular_varianza(lista, media):
    varianza = sum((x - media) ** 2 for x in lista) / len(lista)
    return varianza

def calcular_desviacion_estandar(varianza):
    desviacion_estandar = varianza ** 0.5
    return desviacion_estandar

def datos_no_agrupados(lista):
    n = len(lista)
    media = calcular_media(lista)
    dato_mayor = max(lista)
    dato_menor = min(lista)
    moda, frecuencia_moda = calcular_moda(lista)
    varianza = calcular_varianza(lista, media)
    desviacion_estandar = calcular_desviacion_estandar(varianza)
    
    print("Datos no agrupados:")
    print(f"Media aritmética: {media}")
    print(f"Dato mayor: {dato_mayor}")
    print(f"Dato menor: {dato_menor}")
    print(f"Moda(s): {moda} con frecuencia: {frecuencia_moda}")
    print(f"Varianza: {varianza}")
    print(f"Desviación estándar: {desviacion_estandar}")

def calcular_puntos_medios(intervalos):
    return [(intervalo[0] + intervalo[1]) / 2 for intervalo in intervalos]

def calcular_media_agrupados(puntos_medios, frecuencias):
    total_frecuencia = sum(frecuencias)
    media = sum(punto * frec for punto, frec in zip(puntos_medios, frecuencias)) / total_frecuencia
    return media

def calcular_varianza_agrupados(puntos_medios, frecuencias, media):
    total_frecuencia = sum(frecuencias)
    varianza = sum(frec * (punto - media) ** 2 for punto, frec in zip(puntos_medios, frecuencias)) / total_frecuencia
    return varianza

def datos_agrupados(intervalos, frecuencias):
    puntos_medios = calcular_puntos_medios(intervalos)
    media = calcular_media_agrupados(puntos_medios, frecuencias)
    
    # Moda (el intervalo con mayor frecuencia)
    moda_intervalo = intervalos[frecuencias.index(max(frecuencias))]
    
    # Varianza
    varianza = calcular_varianza_agrupados(puntos_medios, frecuencias, media)
    desviacion_estandar = calcular_desviacion_estandar(varianza)
    
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
