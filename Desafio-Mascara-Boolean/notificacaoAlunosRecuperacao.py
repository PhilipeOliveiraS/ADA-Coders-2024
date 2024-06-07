import numpy as np

# Simulando entrada de notas dos alunos
notas = [4.0, 6.5, 3.0, 8.0, 7.5, 2.0, 9.0, 5.5, 4.5, 1.0]

# Convertendo a lista para um array numpy
notas_array = np.array(notas)

# Criando a máscara para identificar alunos que precisam de recuperação (notas abaixo de 5)
mascara_recuperacao = notas_array < 5

# Exibindo notificações para alunos em recuperação
print("Notificações de recuperação:")
notas_recuperacao = np.zeros_like(notas_array)  # Array para armazenar notas de recuperação

# Simulando entrada de notas de recuperação
notas_recuperacao_entrada = [5.0, 6.0, 4.5, 8.0, 7.5, 5.0, 9.0, 5.5, 6.0, 3.5]

for i in range(len(notas)):
    if mascara_recuperacao[i]:
        print(f"Aluno {i+1} está em recuperação com a nota {notas_array[i]}.")
        nova_nota = notas_recuperacao_entrada[i]
        print(f"Nota de recuperação para Aluno {i+1}: {nova_nota}")
        notas_recuperacao[i] = nova_nota
    else:
        notas_recuperacao[i] = notas_array[i]

# Atualizando as notas com as da recuperação
notas_array[mascara_recuperacao] = notas_recuperacao[mascara_recuperacao]

# Verificando alunos reprovados após recuperação
mascara_reprovados = notas_array < 5
print("\nResultado final após recuperação:")
for i in range(len(notas_array)):
    if mascara_reprovados[i]:
        print(f"Aluno {i+1} foi reprovado com a nota {notas_array[i]}.")
    else:
        print(f"Aluno {i+1} foi aprovado com a nota {notas_array[i]}.")

# Exibindo o resultado final de todos os alunos
print("\nNotas finais dos alunos:")
print(notas_array)
