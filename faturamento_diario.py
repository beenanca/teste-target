# Função para encontrar o menor e o maior valor de faturamento
def maior_menor(vet):
    menor = min(vet)
    maior = max(vet)
    return menor, maior

# Função para calcular a média mensal ignorando dias sem faturamento
def media_mensal(vet):
    soma = sum(vet)
    media = soma / len(vet)
    return media

# Função para contar o número de dias com faturamento acima da média mensal
def numero_de_dias_acima_da_media(media, vet):
    num = sum(1 for valor in vet if valor > media)
    return num

# Vetor de valores de faturamento
valores = [22174.1664, 24537.6698, 26139.6134, 0.0, 0.0, 26742.6612, 0.0, 42889.2258, 
           46251.174, 11191.4722, 0.0, 0.0, 3847.4823, 373.7838, 2659.7563, 48924.2448, 
           18419.2614, 0.0, 0.0, 35240.1826, 43829.1667, 18235.6852, 4355.0662, 
           13327.1025, 0.0, 0.0, 25681.8318, 1718.1221, 13220.495, 8414.61]

# Filtra os valores sem zero para cálculo de média
v_sem_0 = [valor for valor in valores if valor > 0]

# Calcula o menor e maior valor de faturamento
menor, maior = maior_menor(v_sem_0)
print(f"Menor valor de faturamento ocorrido em um dia do mês: {menor:.2f}")
print(f"Maior valor de faturamento ocorrido em um dia do mês: {maior:.2f}")

# Calcula a média mensal dos dias com faturamento
media = media_mensal(v_sem_0)
print(f"Média mensal: {media:.2f}")

# Conta o número de dias acima da média mensal
num_dias_acima = numero_de_dias_acima_da_media(media, v_sem_0)
print(f"Número de dias com faturamento acima da média: {num_dias_acima}")
