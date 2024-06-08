import matplotlib.pyplot as plt

# Dados fictícios de vendas
meses = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
vendas_este_ano = [200, 220, 250, 270, 300, 310, 320, 330, 340, 350, 360, 370]
vendas_ano_passado = [180, 200, 230, 250, 280, 290, 300, 310, 320, 330, 340, 350]

# Criando o gráfico de linha
plt.plot(meses, vendas_este_ano, label='Este Ano', marker='o')
plt.plot(meses, vendas_ano_passado, label='Ano Passado', marker='o')

# Adicionando título e rótulos aos eixos
plt.title('Comparação das Vendas Mensais')
plt.xlabel('Meses')
plt.ylabel('Valor das Vendas')

# Adicionando uma legenda
plt.legend()

# Salvando o gráfico como imagem
plt.savefig('vendas_comparacao.png')

# Mostrando o gráfico
plt.show()

