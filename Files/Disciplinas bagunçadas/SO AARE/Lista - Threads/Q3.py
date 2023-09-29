""" 
  3) Faca um programa que apresente o menu abaixo.
  Ao selecionar a opcao numero 2,
    o programa deve executar um funcao 'chamada_bloqueante'
      que espera tempo aleatorio entre 1 a 30 segundos e
      voltar imediatamente o menu principal.

  Isto e, o programa deve continuar responsivo
  mesmo quando a funcao esteja sendo executada.

  Caso, o usuario selecione novamente a opcao numero 2
  e a funcao "chamada_bloqueante" ja esteja sendo executada
  o software devera avisar o usuario que
  nao podera executar mais de uma instancia da funcao "chamada_bloqueante" concorrentemente.
 """
import threading
import time 
import random

# Pausa o programa por um tempo aleatorio entre 1 a 30 segundos
def chamada_bloqueante(bloqueado):
  sleep_time = random.randint(1, 30)
  bloqueado[0] = 1
  print("Bloqueando por {} segundos.".format(sleep_time))
  time.sleep(sleep_time)
  bloqueado[0] = 0 

# Menu que da opcoes para o usuario de sair do programa ou chamar a funcao
# chamada_bloqueante limitando as chamadas dessa funcao a uma por vez 
def Menu():
  bloqueado = [0] 
  while True:
    print("------------------------\n")
    print("1) Sair \n")
    print("2) Chamada Bloqueante\n")
    option = input ()
    #print(threading.active_count())
    if option == "1":
      print("Saindo.")
      quit()

    elif option == "2":
      if bloqueado[0] == 1: #threading.active_count() >= 2:
        print('\nVoce nao pode executar mais de uma instancia da funcao "chamada bloqueante" concorrentemente\n')
      else: 
          print("Executando chamada Bloqueante")
          bloqueio = threading.Thread(target=chamada_bloqueante, args=(bloqueado,)) # Envia a funcao chamada_bloqueante para uma thresh
          bloqueio.daemon = True
          bloqueio.start() # Inicia a execução em uma thread.
    else:
      print("Opcao invalida.")

def Q3 ():
  Menu()

Q3 ()
