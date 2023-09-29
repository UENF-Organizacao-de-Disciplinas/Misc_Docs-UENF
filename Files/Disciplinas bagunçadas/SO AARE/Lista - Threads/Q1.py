""" 
  1) Escreva um programa que realize o calculo das somas dos valores das linhas de uma matriz
  qualquer de numeros inteiros e imprima o resultado na tela.
  Faca com que o calculo do somatorio de cada linha seja realizado em paralelo por uma thread.
"""
import threading
import time

 # Realiza a soma da linha
def somaLinha(matriz, numDaLinha):
  acumulador = 0
  for i in range (len(matriz[0])):
    acumulador += matriz[numDaLinha][i]
  print(acumulador)

 # Realiza a soma das linhas da matriz em threads diferentes 
def padrao(matriz):
  print(matriz)

  for i in range(len(matriz)):   
    x = threading.Thread(target=somaLinha, args=(matriz,i)) # Envia a funcao somaLinha e seus parametros que sao a matriz e a linha 
                                                            # para uma thresh onde serao realizadas as somas dessa linha em paralelo  
    x.start() # Inicia a execução em uma thread 
  x.join()    #Pausa o programa ate o fim da thread  
  print("\n")
  

def Q1():
  A = [[1,2,3], [4,5,6], [7,8,9]] 
  B = [[1,1,1], [2,2,2], [3,3,3]] 

  padrao(A)     
  padrao(B)   
 
Q1()