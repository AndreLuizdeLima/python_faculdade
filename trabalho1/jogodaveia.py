#realizar na criação de um jogo da velha

#variaves globais

tab = [
    ['=','A','B','C'],    
    ['1','0','0','0'],    
    ['2','0','0','0'],    
    ['3','0','0','0']    
]

condParada = 1

numJog = 0

quemJoga = 0

#funções

def printaTabFor():
    for i in tab:
        print(i)
        
def printaStart():
    print('=== Iniciando o Game jogo da velha ===')
    print('')    
    print('Jogador 1, será representado pelo numero X')
    print('Jogador 2, será representado pelo numero Y')
    print('')    
    printaRegras()
    print('')    
    printaTab()
    
def printaTab():
    print('')    
    print('Esse é o tabuleiro atual:')
    print('')    
    printaTabFor()
    print('')    
    print('')    
    
def printaRegras():
    print()
    print('Regras, para definir qual quadrado preenxer vocÊ deve')
    print('Na sua jogada você deve selecionar a coluna e a linha ex: A1')
    print()
    
def defineQuemJoga(jogadaNum):
    global quemJoga
    if jogadaNum % 2 == 0:
        quemJoga = 1
        return(quemJoga)
    else:
        quemJoga = 2
        return(quemJoga)

def jogada():
    global quemJoga
    print('')    
    print(f'Vez do jogador {quemJoga} Informe qual sua jogada')
    print('')
    columnsJog = input('Coluna: ')
    rowsJog = int(input('Linha: '))
    print('')
    print(f'Sua Jogada vai ser {columnsJog}{rowsJog}')
    pause = input()
    
    return(columnsJog,rowsJog)
    
def insertFormat(columnsJog,rownJog):
    global insertRown, insertColumns
    insertRown = None
    if rownJog == 1:
        insertRown = 1
    if rownJog == 2:
        insertRown = 2
    if rownJog == 3:
        insertRown = 3

    insertColumns = None
    if columnsJog == 'A' or columnsJog == 'a':
        insertColumns = 1
        
    if columnsJog == 'B' or columnsJog == 'b':
        insertColumns = 2
    if columnsJog == 'C' or columnsJog == 'c':
        insertColumns = 3     
        
    return(insertRown,insertColumns)

def insertTab(insertRown,insertColumns):
    global quemJoga, tab, numJog
    marcador = None

    if quemJoga == 1:
        marcador = 'X'
        
    if quemJoga == 2:
        marcador = 'Y'
        
    tab[insertRown][insertColumns] = marcador
    numJog += 1
    
def validaVencedor():
    global tab
    
    #vertical X
    if tab[1][1] == 'X' and tab[2][1] == 'X' and tab[3][1] == 'X':
        anuncioVencedor()
    if tab[1][2] == 'X' and tab[2][2] == 'X' and tab[3][2]== 'X':
        anuncioVencedor()
    if tab[1][3] == 'X' and tab[2][3] == 'X' and tab[3][3]== 'X':
        anuncioVencedor()
    
    #horizontal X
    if tab[1][1] == 'X' and tab[1][2] == 'X' and tab[1][3] == 'X':
        anuncioVencedor()
    if tab[2][1] == 'X' and tab[2][2] == 'X' and tab[2][3] == 'X':
        anuncioVencedor()
    if tab[3][1] == 'X' and tab[3][2] == 'X' and tab[3][3] == 'X':
        anuncioVencedor()
    
    #diagonal X
    
    if tab[1][1] == 'X' and tab[2][2] == 'X' and tab[3][3] == 'X':
        anuncioVencedor()
    if tab[1][3] == 'X' and tab[2][2] == 'X' and tab[3][1] == 'X':
        anuncioVencedor()
        
     #vertical Y
    if tab[1][1] == 'Y' and tab[2][1] == 'Y' and tab[3][1] == 'Y':
        anuncioVencedor()
    if tab[1][2] == 'Y' and tab[2][2] == 'Y' and tab[3][2] == 'Y':
        anuncioVencedor()
    if tab[1][3] == 'Y' and tab[2][3] == 'Y' and tab[3][3] == 'Y':
        anuncioVencedor()
    
    #horizontal Y
    if tab[1][1] == 'Y' and tab[1][2] == 'Y' and tab[1][3] == 'Y':
        anuncioVencedor()
    if tab[2][1] == 'Y' and tab[2][2] == 'Y' and tab[2][3] == 'Y':
        anuncioVencedor()
    if tab[3][1] == 'Y' and tab[3][2] == 'Y' and tab[3][3] == 'Y':
        anuncioVencedor()
    
    #diagonal Y
    
    if tab[1][1] == 'Y' and tab[2][2] == 'Y' and tab[3][3] == 'Y':
        anuncioVencedor()
    if tab[1][3] == 'Y' and tab[2][2] == 'Y' and tab[3][1] == 'Y':
        anuncioVencedor()
        
def anuncioVencedor():
    global quemJoga, condParada
    print('')
    print('=== Fim do Game ===')
    print('')
    print(f'O vencedor foi o jogador {quemJoga}')
    print('')
    condParada+=1

#game em si

printaStart()

while condParada <= 1:
    defineQuemJoga(numJog)
    columnsJog, rowsJog = jogada()
    insertRown, insertColumns = insertFormat(columnsJog,rowsJog)
    insertTab(insertRown,insertColumns)
    printaTab()
    validaVencedor()