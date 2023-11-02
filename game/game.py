import os
import random

OPTIONS = ['piedra', 'papel', 'tijeras']
PLAYER_OPTIONS = {
  'o': 'piedra',
  'd': 'papel',
  'x': 'tijeras'
}

def game():
  tries = 0
  machine = random.choice(OPTIONS)
  player = input('''Seleccione una de las siguientes opciones: 
piedra (O)
papel (D)
tijeras (X)
''')
  os.system('cls')
  option = PLAYER_OPTIONS.get(player.lower())
  if option:
    if option == machine:
      print('¡Empate! tuvimos la misma jugada')
      return False
    elif option == 'piedra' and machine == 'tijera' or option == 'papel' and machine == 'piedra' or option == 'tijera' and machine == 'papel':
      print(f'Ganaste esta ronda!, con {option}, y yo jugue con {machine}')
      return True

    else:
      print(f'Te gane con {machine}')
      return False


def play():
  wanna_play = 's'
  while wanna_play.lower() == 's':  
    rounds = 0
    wins = 0
    while rounds < 3:
      win = game()
      if win:
        wins += 1
      rounds += 1
      
    if wins == 2:
      print("Ganaste el juego")
    else:
      print("Looseeeer")
    wanna_play = input("Quieres seguir jugando? (s/n)")



play()