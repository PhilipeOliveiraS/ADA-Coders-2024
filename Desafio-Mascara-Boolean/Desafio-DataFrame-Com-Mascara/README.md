# 📊 Projeto - Usando DataFrame e pd.concat no Pandas com máscara para filtrar dados

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![NumPy](https://img.shields.io/badge/NumPy-1.21-green)
![GitHub](https://img.shields.io/badge/GitHub-Repo-yellow)
![Contribua](https://img.shields.io/badge/Contribua-Welcome-brightgreen)


![Project Banner](https://source.unsplash.com/random/800x200?coding)


## 📚 Descrição

Este projeto realiza uma análise dos livros de J.R.R. Tolkien e Dan Brown. Ele lista todos os livros dos autores, adiciona novos livros ao inventário e filtra apenas os livros de J.R.R. Tolkien, exibindo o resultado.


### Explicação do Código

1. **Importando o pandas**:
    ```python
    import pandas as pd
    ```
    - `pandas` é uma biblioteca essencial para a manipulação de dados em Python.

2. **Criando um DataFrame inicial**:
    ```python
    data = {
        'autor': ['Dan Brown', 'Dan Brown', 'Dan Brown', 'J.R.R. Tolkien', 'J.R.R. Tolkien', 'J.R.R. Tolkien', 'J.R.R. Tolkien'],
        'titulo': ['O Código Da Vinci', 'Anjos e Demônios', 'Inferno', 'O Hobbit', 'O Senhor dos Anéis - A Sociedade do Anel', 'O Senhor dos Anéis - As Duas Torres', 'O Senhor dos Anéis - O Retorno do Rei'],
        'preco': [50.00, 45.00, 55.00, 150.00, 300.00, 300.00, 300.00]
    }

    df_livros = pd.DataFrame(data)
    ```
    - Criamos um dicionário `data` com os detalhes dos livros e o transformamos em um DataFrame `df_livros`.

3. **Exibindo o DataFrame inicial**:
    ```python
    print("DataFrame inicial:")
    print(df_livros)
    ```
    - Exibimos o DataFrame inicial contendo os livros de Dan Brown e J.R.R. Tolkien.

4. **Criando novos dados para adicionar**:
    ```python
    novos_livros = pd.DataFrame({
        'autor': ['J.R.R. Tolkien', 'J.R.R. Tolkien', 'J.R.R. Tolkien', 'J.R.R. Tolkien'],
        'titulo': ['O Silmarillion', 'Contos Inacabados', 'O Mundo de Tolkien', 'Os Filhos de Húrin'],
        'preco': [250.00, 200.00, 180.00, 220.00]
    })
    ```
    - Criamos um novo DataFrame `novos_livros` com os livros adicionais de J.R.R. Tolkien.

5. **Adicionando novos livros ao DataFrame existente usando `pd.concat`**:
    ```python
    df_livros = pd.concat([df_livros, novos_livros], ignore_index=True)
    ```
    - Utilizamos `pd.concat` para concatenar `df_livros` e `novos_livros`, criando um DataFrame atualizado.

6. **Exibindo o DataFrame completo**:
    ```python
    print("\nDataFrame completo após adicionar os demais livros de J.R.R. Tolkien:")
    print(df_livros)
    ```
    - Exibimos o DataFrame atualizado com todos os livros adicionados.

7. **Filtrando e exibindo apenas os livros de J.R.R. Tolkien**:
    ```python
    mascara_tolkien = df_livros['autor'] == 'J.R.R. Tolkien'

    print("\nDataFrame filtrado com apenas os livros de J.R.R. Tolkien:")
    df_tolkien = df_livros[mascara_tolkien]
    print(df_tolkien)
    ```
    - Criamos uma máscara `mascara_tolkien` para filtrar os livros de J.R.R. Tolkien e exibimos o DataFrame filtrado.

### README.md

```markdown

## Passos do Código

1. **Importação do pandas**:
    ```python
    import pandas as pd
    ```
    - A biblioteca `pandas` é utilizada para a manipulação de dados.

2. **Criação do DataFrame inicial**:
    ```python
    data = {
        'autor': ['Dan Brown', 'Dan Brown', 'Dan Brown', 'J.R.R. Tolkien', 'J.R.R. Tolkien', 'J.R.R. Tolkien', 'J.R.R. Tolkien'],
        'titulo': ['O Código Da Vinci', 'Anjos e Demônios', 'Inferno', 'O Hobbit', 'O Senhor dos Anéis - A Sociedade do Anel', 'O Senhor dos Anéis - As Duas Torres', 'O Senhor dos Anéis - O Retorno do Rei'],
        'preco': [50.00, 45.00, 55.00, 150.00, 300.00, 300.00, 300.00]
    }

    df_livros = pd.DataFrame(data)
    ```
    - Criamos um dicionário `data` com os detalhes dos livros e o transformamos em um DataFrame `df_livros`.

3. **Exibição do DataFrame inicial**:
    ```python
    print("DataFrame inicial:")
    print(df_livros)
    ```
    - Exibimos o DataFrame inicial contendo os livros de Dan Brown e J.R.R. Tolkien.

4. **Criação de novos dados para adicionar**:
    ```python
    novos_livros = pd.DataFrame({
        'autor': ['J.R.R. Tolkien', 'J.R.R. Tolkien', 'J.R.R. Tolkien', 'J.R.R. Tolkien'],
        'titulo': ['O Silmarillion', 'Contos Inacabados', 'O Mundo de Tolkien', 'Os Filhos de Húrin'],
        'preco': [250.00, 200.00, 180.00, 220.00]
    })
    ```
    - Criamos um novo DataFrame `novos_livros` com os livros adicionais de J.R.R. Tolkien.

5. **Adição de novos livros ao DataFrame existente usando `pd.concat`**:
    ```python
    df_livros = pd.concat([df_livros, novos_livros], ignore_index=True)
    ```
    - Utilizamos `pd.concat` para concatenar `df_livros` e `novos_livros`, criando um DataFrame atualizado.

6. **Exibição do DataFrame completo**:
    ```python
    print("\nDataFrame completo após adicionar os demais livros de J.R.R. Tolkien:")
    print(df_liv

ros)
    ```
    - Exibimos o DataFrame atualizado com todos os livros adicionados.

7. **Filtragem e exibição apenas dos livros de J.R.R. Tolkien**:
    ```python
    mascara_tolkien = df_livros['autor'] == 'J.R.R. Tolkien'

    print("\nDataFrame filtrado com apenas os livros de J.R.R. Tolkien:")
    df_tolkien = df_livros[mascara_tolkien]
    print(df_tolkien)
    ```
    - Criamos uma máscara `mascara_tolkien` para filtrar os livros de J.R.R. Tolkien e exibimos o DataFrame filtrado.
```

Agora o código está ajustado para evitar erros e a explicação fornece um guia claro sobre como ele funciona.