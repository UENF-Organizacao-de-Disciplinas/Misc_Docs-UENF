""" 
  2) Faca um programa que imprima os numeros primos existentes entre 0 e 99999.
  UTILIZE THREADS.Dica: para cada faixa de mil valores crie um thread e dispare
  o processo para cada uma delas.
 """

import threading
import time

# Checa se o numero eh primo 
def checarPrimo (primo):
  
  if primo == 2:
    return True

  if primo%2 == 0: 
    return False
    
  for i in range(3,primo,2):
    if primo%i == 0:
      return False
  return True

# Realiza a checagem de uma lista de números 
def checarPrimoDaListaEntre (listaPrimos, inicio, fim):
  for i in range(inicio, fim):
    if(checarPrimo(i)):
      listaPrimos.append(i)

# Envia a funcao primosDe0a9999 e seus parametros para as threads 
# com intervalo especificos de parametros para cada uma delas
def primosDe0a9999 (lista):
  mil=1000
  for i in range(10):
    x = threading.Thread(target=checarPrimoDaListaEntre, args=(lista, i*mil,(i+1)*mil-1)) # Envia para uma thread a funcao primosDe0a9999 e seus parametros que sao o inicio e o fim de cada intervalo de mil números entre 0 e 9999. 
    x.start() # Inicia a execução em uma thread  
  print(lista)

def Q2():
  listaPrimos=[]
  primosDe0a9999(listaPrimos)

Q2()
