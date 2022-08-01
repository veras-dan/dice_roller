def main():
  import random
  dice_rolls = int(input('Quantos dados deseja jogar? '))
  dice_size = int(input('quantos lados tem o dado? '))
  dice_sum = 0
  
  for i in range(0,dice_rolls):
    roll = random.randint(1,dice_size)
    dice_sum += roll
    
    if roll == 1:
      print(f'Você tirou {roll}! Falhou no crítico!')
    
    elif roll == dice_size:
      print(f'Você tirou {roll}! Acertou um Crítico!!! Parabéns!')
    
    else:
      print(f'Você tirou {roll}')
  print(f'Você tirou um total de {dice_sum}')


if __name__== "__main__":
  main()
  
input()