import os
import random

OPTIONS = ['piedra', 'papel', 'tijeras']
PLAYER_OPTIONS = {
  'o': 'piedra',
  'd': 'papel',
  'x': 'tijeras'
}

def play():
  while True:
    machine = random.choice(OPTIONS)
    player = input('''Seleccione una de las siguientes opciones: 
piedra (O)
papel (D)
tijeras (X)
Presione cualquier otra tecla para terminar              
                  ''')
    os.system('cls')
    option = PLAYER_OPTIONS.get(player.lower())
    if option:
      if option == machine:
        print('¡Empate! tuvimos la misma jugada')
      elif option == 'piedra' and machine == 'tijera' or option == 'papel' and machine == 'piedra' or option == 'tijera' and machine == 'papel':
        print(f'¡Ganaste!, me ganaste con {option}, y yo jugue con {machine}, felicidades')
      else:
        print(f'Te gane con {machine}')
    else:
      break


play()