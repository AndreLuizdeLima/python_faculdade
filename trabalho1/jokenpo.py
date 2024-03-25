print('*** [Jogo do Jokenpo] ***')
print('')
print('Nesse game dois jogadores vao informar sua jogadas e nos vamos julgar quem venceu')
print('Possiveis escolhas:')
print('1: Pedra')
print('2: Papel')
print('3: Tesoura')
print('')

#jogador 1

jogador1 = int(input('Escolha jogador 1: '))

if jogador1 == 1:
    print('Jogador 1 escolheu: Pedra')
    print('')
    
elif jogador1 == 2:
    print('Jogador 1 escolheu: Papel')
    print('')

elif jogador1 == 3:
    print('Jogador 1 escolheu: Tesoura') 
    print('')
    
else:
    print('Numero invalido:')
    print('')
    exit()

#jogador2

jogador2 = int(input('Escolha jogador 2: '))

if jogador2 == 1:
    print('Jogador 2 escolheu: Pedra')
    print('')
    
elif jogador2 == 2:
    print('Jogador 2 escolheu: Papel')
    print('')

elif jogador2 == 3:
    print('Jogador 2 escolheu: Tesoura') 
    print('')
    
else:
    print('Numero invalido:')
    exit()
    
#hora de julgar quem venceu
# Pedra empata com Pedra e ganha de Tesoura.
# Tesoura empata com Tesoura e ganha de Papel.
# Papel empata com Papel e ganha de Pedra.
    
if jogador1 == 1 and jogador2 == 1:
    print('Empate: Pedra empata com Pedra')
    
elif jogador1 == 1 and jogador2 == 3:
    print('Jogador 1 ganhou: Pedra vence tesoura')
    
elif jogador1 == 3 and jogador2 == 3:
    print('Empate: Tesoura empata com Tesoura')
    
elif jogador1 == 3 and jogador2 == 2:
    print('Jogador1 ganhou: Tesoura vence Papel')
    
elif jogador1 == 2 and jogador2 == 2:
    print('Empate: Papel empata com Papel')
    
elif jogador1 == 2 and jogador2 == 1:
    print('Jogador 1 venceu: Papel vence Pedra')    

#verificando segundo jogador
    
elif jogador2 == 1 and jogador1 == 1:
    print('Empate: Pedra empata com Pedra')
    
elif jogador2 == 1 and jogador1 == 3:
    print('Jogador 2 ganhou: Pedra vence Tesoura')
    
elif jogador2 == 3 and jogador1 == 3:
    print('Empate: Tesoura empata com Tesoura')
    
elif jogador2 == 3 and jogador1 == 2:
    print('Jogador 2 ganhou: Tesoura vence Papel')
    
elif jogador2 == 2 and jogador1 == 2:
    print('Empate: Papel empata com Papel')
    
elif jogador2 == 2 and jogador1 == 1:
    print('Jogador 2 venceu: Papel vence Pedra')