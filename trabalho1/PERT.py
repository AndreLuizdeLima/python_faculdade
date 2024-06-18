def calcular_duracao_esperada_e_variancia(atividades):
    resultados = {}
    
    for atividade, tempos in atividades.items():
        O, M, P = tempos
        duracao_esperada = (O + 4 * M + P) / 6
        variancia = ((P - O) / 6) ** 2
        resultados[atividade] = {
            'Duração Esperada': duracao_esperada,
            'Variância': variancia
        }
    
    return resultados


atividades = {
    'Atividade A': (10, 15, 25),
    'Atividade B': (5, 7, 13),
    'Atividade C': (7, 16, 23),
    'Atividade D': (32, 41, 52),
    'Atividade E': (40, 52, 67)
  
}

resultados = calcular_duracao_esperada_e_variancia(atividades)

for atividade, valores in resultados.items():
    print(f"{atividade}: Duração Esperada = {valores['Duração Esperada']}, Variância = {valores['Variância']}")
