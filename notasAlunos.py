import numpy as np

# Pedindo ao usuário para inserir 10 notas
notas = []
for i in range(10):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

# Convertendo a lista para um array numpy
notas_array = np.array(notas)

# Calculando a média
media = np.mean(notas_array)

# Calculando o desvio padrão
desvio_padrao = np.std(notas_array)

# Encontrando a nota máxima e mínima
nota_maxima = np.max(notas_array)
nota_minima = np.min(notas_array)

# Exibindo os resultados
print(f"Média das notas: {media}")
print(f"Desvio padrão das notas: {desvio_padrao}")
print(f"Nota máxima: {nota_maxima}")
print(f"Nota mínima: {nota_minima}")
