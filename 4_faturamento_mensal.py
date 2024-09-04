def calcular_percentual_faturamento(faturamento):

    if not faturamento:
        return "O dicionário de faturamento está vazio."

    faturamento_total = sum(valor for valor in faturamento.values() if valor > 0)

    if faturamento_total == 0:
        return "Não há valores de faturamento válidos."

    percentuais = {}
    for estado, valor in faturamento.items():
        if valor > 0:
            percentual = (valor / faturamento_total) * 100
            percentuais[estado] = percentual

    return percentuais

# Exemplo de uso:
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 1,
    "Outros": 19849.53
}

resultados = calcular_percentual_faturamento(faturamento)
if isinstance(resultados, dict):
    for estado, percentual in resultados.items():
        print(f"{estado}: {percentual:.2f}%")
else:
    print(resultados)
