import pandas as pd

# Criando um DataFrame inicial com os livros de Dan Brown e J.R.R. Tolkien
dictionary = {
    'Autores': ['Dan Brown', 'Dan Brown', 'Dan Brown', 'J.R.R. Tolkien', 'J.R.R. Tolkien', 'J.R.R. Tolkien', 'J.R.R. Tolkien'],
    'Títulos': ['O Código Da Vinci', 'Anjos e Demônios', 'Inferno', 'O Hobbit', 'O Senhor dos Anéis - A Sociedade do Anel', 'O Senhor dos Anéis - As Duas Torres', 'O Senhor dos Anéis - O Retorno do Rei'],
    'Preços' : [50.00, 45.00, 55.00, 150.00, 300.00, 300.00, 300.00]
}
## DataFrame
df_livros = pd.DataFrame(dictionary)

# Exibindo o DataFrame inicial
print("DataFrame inicial:")
print(df_livros)

# Adicionando os demais livros de J.R.R. Tolkien usando append
# Criando novos dados para adicionar
novos_livros = pd.DataFrame({
    'Autores': ['J.R.R. Tolkien', 'J.R.R. Tolkien', 'J.R.R. Tolkien', 'J.R.R. Tolkien'],
    'Títulos': ['O Silmarillion', 'Contos Inacabados', 'O Mundo de Tolkien', 'Os Filhos de Húrin'],
    'Preços': [250.00, 200.00, 180.00, 220.00]
})

# Adicionando os novos livros ao DataFrame existente usando pd.concat
df_livros = pd.concat([df_livros, novos_livros], ignore_index=True)

# Exibindo o DataFrame completo após adicionar os livros
print("\nDataFrame completo após adicionar os demais livros de J.R.R. Tolkien:")
print(df_livros)

# Criando uma máscara para filtrar os livros de J.R.R. Tolkien
mascara_tolkien = df_livros['Autores'] == 'J.R.R. Tolkien'

# Exibindo o DataFrame filtrado com apenas os livros de J.R.R. Tolkien
print("\nDataFrame filtrado com apenas os livros de J.R.R. Tolkien:")
df_tolkien = df_livros[mascara_tolkien]
print(df_tolkien)
