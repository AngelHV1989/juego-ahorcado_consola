from random import *

lista_palabras = ['comida','submarino','python', 'extraño']
palabra_aleatoria = choice(lista_palabras)
vidas = 8
letras_incorrectas = []

def pedir_letra(palabra,vidas):
    caracteres = len(palabra)
    palabra = list(palabra)
    palabra_escondida = list(palabra)
    palabra_escondida[0:caracteres] = '_' * caracteres
    letra = input(f"Ingresa una letra para adivinar la palabra: ").lower()
    valida_letra(letra,palabra,palabra_escondida,vidas)

def valida_letra(letra,palabra,palabra_escondida,vidas):
    abcedario = 'abcdfghijklmnñopqrstuvwxyz'
    if len(letra) > 1:
        print("Introduce solo una letra")
        juntando_letras(palabra_escondida,palabra,vidas)
    if letra not in abcedario:
        print("Solo se ademiten letras")
        juntando_letras(palabra_escondida, palabra, vidas)
    else:
        chequear_letra(letra,palabra,palabra_escondida,vidas)

def chequear_letra(letra,palabra,palabra_escondida,vidas):
    indice = -1
    if letra in palabra:
        for l in palabra:
            indice += 1
            if l == letra:
                palabra_escondida[indice] = letra
        if comprobar_solucion(palabra,palabra_escondida):
            print(f"Has Ganado! efectivamente la palabra era '{''.join(palabra)}'")
        else:
            print(f"Letras falladas: {letras_incorrectas}")
            juntando_letras(palabra_escondida,palabra,vidas)
    else:
        letras_incorrectas.append(letra)
        print(f"Letras falladas: {'-'.join(letras_incorrectas)}")
        vidas -= 1
        if vidas == 0:
            print(f"Has perdido, la palabra era '{''.join(palabra)}'")
        else:
            if vidas >= 2:
                print(f"Te quedan {vidas} vidas")
            else:
                print(f"Te queda {vidas} vida")
            juntando_letras(palabra_escondida,palabra,vidas)

def juntando_letras(palabra_escondida,palabra,vidas):
    print(palabra_escondida)
    letra = input(f"Ingresa una letra para adivinar la palabra: ")
    valida_letra(letra, palabra, palabra_escondida,vidas)

def comprobar_solucion(palabra,palabra_escondida):
    if(set(palabra)) == set(palabra_escondida):
        return True

pedir_letra(palabra_aleatoria,vidas)
