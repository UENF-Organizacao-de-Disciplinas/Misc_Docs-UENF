
""" 
  4) Desenvolva um software que tera duas threads.
  Uma thread chamada Produtora que sorteia um numero aleatorio e coloca na variavel shared.
  Este sorteio acontece em um tempo tambem aleatorio.
  A segunda thread chamada monitor devera imprimir na tela sempre que houver um valor novo em shared.
 """

import threading
import random
import time

# Sorteia um numero aleatorio e guarda na variavel shared
def RandomShuffle (shared, oldShared):
  print("Sorteando")
  for i in range (random.randint(2,7)):
    print(".")
    time.sleep(1)
  oldShared[0] = shared[0]
  shared[0] = random.randint(1,10)

# Mostra na tela sempre que houver um valor novo em shared
def printResult (shared, oldShared):
  print("shared: {}, Old: {}".format(shared,oldShared))
  if (shared[0] != oldShared[0]):
    print("O resultado do sorteio eh: "+ str(shared[0]))
  else:
    print("Repetido")

# Funcao que realiza N sorteios 
def Sorteios(n):
  shared = [0]
  oldShared  = [-1]
  for i in range(n):
    print("sorteio: {}".format(i+1))
    produtora = threading.Thread(target=RandomShuffle,args=(shared, oldShared)) # devine a thread produtora
    produtora.start()   # Inicia a execução em uma thread     
    produtora.join()    # Pausa o programa ate o fim execucao na thread 

    monitor   = threading.Thread(target=printResult  ,args=(shared, oldShared)) # devine a thread monitor
    monitor.start()     # Inicia a execução em uma thread
    monitor.join()      # Pausa o programa ate o fim execucao na thread 

def Q4 ():
  Sorteios(10)

Q4 ()

