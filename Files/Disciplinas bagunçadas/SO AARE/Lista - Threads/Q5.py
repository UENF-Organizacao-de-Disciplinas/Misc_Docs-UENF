""" 
  5) Crie um software que terá duas threads.
  Uma thread Produtora que sorteia um numero e 
    coloque este número no topo da pilha shared.
    Este sorteio deverá acontecer em um tempo aleatório.

  A segunda thread chamada de consumidor
  deverá remover o item do topo de pilha
  e imprimir na tela.

  Para evitar inconsistências no programa e possíveis travamentos
  as duas threads não podem acessar a pilha shared ao mesmo tempo. 
 """

import threading
import time
import random

# Sorteia um numero e coloca no topo da pilha shared.
def RandomShuffle (shared):
  print("Sorteando")
  for i in range (random.randint(0,5)):
    print(".")
    time.sleep(1)
  shared.append(random.randint(1,10))

# Remove o item do topo de pilha e imprimir na tela.
def printResult (shared):
    print("O resultado do sorteio eh: "+ str(shared.pop()))

# Funcao que realiza N sorteios
def Sorteios(n):
  shared = []
  for i in range(n):
    print("sorteio: {}".format(i+1))
    produtora = threading.Thread(target=RandomShuffle,args=(shared,)) # Define a thread produtora
    produtora.start()  # Inicia a execução de uma thread
    produtora.join()   # Pausa o programa ate o fim execucao na thread 
    
    
    consumidor = threading.Thread(target=printResult,args=(shared,))  # Define a thread consumidor
    consumidor.start() # Inicia a execução de uma thread
    consumidor.join()  # Pausa o programa ate o fim execucao na thread 

def Q5 ():
  Sorteios(10)

Q5()