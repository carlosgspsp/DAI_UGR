n = int(input("Ingrese un numero: "))
lista = list(range(2, n+1))

i = 0
while(lista[i]*lista[i] <= n):
    # Mientras el cuadrado del elemento actual sea menor que el ultimo elemento
    for j in lista:
        if j <= lista[i]:
            # Cada iteracion del while hace que el for comience desde el primer elemento. 
            # Esto es para omitir los numeros primos ya encontrados
            continue
        elif j % lista[i] == 0:
            # Si un numero es divisible entre el elemento actual del while
            # de ser asi, entonces eliminarlo de la lista (esto altera la lista)
            lista.remove(j)
        else:
            # Si no es divisible, entonces omitirlo (no hacer nada)
            pass
    i += 1 # Incrementa al siguiente elemento de la lista (que ha sido alterada)

print(lista)