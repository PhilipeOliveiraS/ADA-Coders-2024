# 📊 Projeto - Usando DataFrame e pd.concat no Pandas com máscara para filtragem de dados

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![NumPy](https://img.shields.io/badge/NumPy-1.21-green)
![GitHub](https://img.shields.io/badge/GitHub-Repo-yellow)
![Contribua](https://img.shields.io/badge/Contribua-Welcome-brightgreen)


![Project Banner](https://source.unsplash.com/random/800x200?coding)


## 📚 Descrição

Este projeto realiza uma análise dos livros dos autores J.R.R. Tolkien e Dan Brown. Ele lista todos os livros dos autores, adiciona novos livros ao inventário e filtra apenas os livros de J.R.R. Tolkien, exibindo o resultado.

## ⚙ Funcionalidades

- Listagem inicial dos livros de Dan Brown e J.R.R. Tolkien.
- Adição de novos livros de J.R.R. Tolkien ao inventário.
- Filtragem e exibição dos livros de J.R.R. Tolkien.

## 🔍 Explicação do Código

### 1. Importando o pandas

```python
import pandas as pd
```

- A biblioteca `pandas` é utilizada para a manipulação de dados em Python, permitindo a criação e manipulação de DataFrames.

### 2. Criando um DataFrame inicial

```python
dictionary = {
    'Autores': ['Dan Brown', 'Dan Brown', 'Dan Brown', 'J.R.R. Tolkien', 'J.R.R. Tolkien', 'J.R.R. Tolkien', 'J.R.R. Tolkien'],
    'Títulos': ['O Código Da Vinci', 'Anjos e Demônios', 'Inferno', 'O Hobbit', 'O Senhor dos Anéis - A Sociedade do Anel', 'O Senhor dos Anéis - As Duas Torres', 'O Senhor dos Anéis - O Retorno do Rei'],
    'Preços' : [50.00, 45.00, 55.00, 150.00, 300.00, 300.00, 300.00]
}
df_livros = pd.DataFrame(dictionary)
```

- Criamos um dicionário `dictionary` contendo os detalhes dos livros e o transformamos em um DataFrame `df_livros`.

### 3. Exibindo o DataFrame inicial

```python
print("DataFrame inicial:")
print(df_livros)
```

- Exibimos o DataFrame inicial contendo os livros de Dan Brown e J.R.R. Tolkien.

### 4. Adicionando novos livros ao DataFrame existente

#### a. Criando novos dados

```python
novos_livros = pd.DataFrame({
    'Autores': ['J.R.R. Tolkien', 'J.R.R. Tolkien', 'J.R.R. Tolkien', 'J.R.R. Tolkien'],
    'Títulos': ['O Silmarillion', 'Contos Inacabados', 'O Mundo de Tolkien', 'Os Filhos de Húrin'],
    'Preços': [250.00, 200.00, 180.00, 220.00]
})
```

- Criamos um novo DataFrame `novos_livros` com os livros adicionais de J.R.R. Tolkien.

#### b. Adicionando os novos livros ao DataFrame existente

```python
df_livros = pd.concat([df_livros, novos_livros], ignore_index=True)
```

- Utilizamos `pd.concat` para concatenar `df_livros` e `novos_livros`, criando um DataFrame atualizado.

### 5. Exibindo o DataFrame completo

```python
print("\nDataFrame completo após adicionar os demais livros de J.R.R. Tolkien:")
print(df_livros)
```

- Exibimos o DataFrame atualizado com todos os livros adicionados.

### 6. Filtrando e exibindo apenas os livros de J.R.R. Tolkien

#### a. Criando uma máscara

```python
mascara_tolkien = df_livros['Autores'] == 'J.R.R. Tolkien'
```

- Criamos uma máscara `mascara_tolkien` para filtrar os livros de J.R.R. Tolkien.

#### b. Aplicando a máscara e exibindo o DataFrame filtrado

```python
print("\nDataFrame filtrado com apenas os livros de J.R.R. Tolkien:")
df_tolkien = df_livros[mascara_tolkien]
print(df_tolkien)
```

- Aplicamos a máscara para filtrar e exibimos o DataFrame contendo apenas os livros de J.R.R. Tolkien.

---

## Resultados

### DataFrame Inicial
```plaintext
          Autores                                  Títulos  Preços
0       Dan Brown                          O Código Da Vinci    50.0
1       Dan Brown                           Anjos e Demônios    45.0
2       Dan Brown                                   Inferno    55.0
3  J.R.R. Tolkien                                  O Hobbit   150.0
4  J.R.R. Tolkien  O Senhor dos Anéis - A Sociedade do Anel   300.0
5  J.R.R. Tolkien             O Senhor dos Anéis - As Duas Torres   300.0
6  J.R.R. Tolkien         O Senhor dos Anéis - O Retorno do Rei   300.0
```

### DataFrame Completo Após Adição
```plaintext
          Autores                          Títulos  Preços
0       Dan Brown                O Código Da Vinci    50.0
1       Dan Brown                 Anjos e Demônios    45.0
2       Dan Brown                         Inferno    55.0
3  J.R.R. Tolkien                        O Hobbit   150.0
4  J.R.R. Tolkien  O Senhor dos Anéis - A Sociedade do Anel   300.0
5  J.R.R. Tolkien             O Senhor dos Anéis - As Duas Torres   300.0
6  J.R.R. Tolkien         O Senhor dos Anéis - O Retorno do Rei   300.0
7  J.R.R. Tolkien                  O Silmarillion   250.0
8  J.R.R. Tolkien                Contos Inacabados   200.0
9  J.R.R. Tolkien                 O Mundo de Tolkien   180.0
10 J.R.R. Tolkien                  Os Filhos de Húrin   220.0
```

### DataFrame Filtrado com Apenas Livros de J.R.R. Tolkien
```plaintext
          Autores                          Títulos  Preços
3  J.R.R. Tolkien                        O Hobbit   150.0
4  J.R.R. Tolkien  O Senhor dos Anéis - A Sociedade do Anel   300.0
5  J.R.R. Tolkien             O Senhor dos Anéis - As Duas Torres   300.0
6  J.R.R. Tolkien         O Senhor dos Anéis - O Retorno do Rei   300.0
7  J.R.R. Tolkien                  O Silmarillion   250.0
8  J.R.R. Tolkien                Contos Inacabados   200.0
9  J.R.R. Tolkien                 O Mundo de Tolkien   180.0
10 J.R.R. Tolkien                  Os Filhos de Húrin   220.0
```
---

## 🔗 Fundamentos do Python Aprendidos
- Biblioteca pandas: Uso para manipulação e análise de dados.
- Dicionários: Estrutura de dados para armazenar pares chave-valor.
- DataFrames: Estrutura de dados bidimensional em pandas.
- Função print: Exibição de dados no console.
- Função pd.concat: Para concatenar DataFrames.
- Máscaras Booleanas: Para filtrar dados em DataFrames.

---
## 🎉 Conclusão
Este código ilustra o uso de várias funcionalidades da biblioteca pandas para manipulação de dados tabulares em Python. Com ele, aprendemos a:

- Criar DataFrames
- Adicionar novos dados
- Concatenar DataFrames
- Criar máscaras booleanas para filtrar dados
- Exibir resultados

---


![GitHub Repo](https://gh-card.dev/repos/PhilipeOliveiraS/ADA-Coders-2024.svg)

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=PhilipeOliveiraS&show_icons=true&theme=radical)

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=PhilipeOliveiraS&layout=compact&theme=radical)

---

## 📈 Estatísticas do Repositório

![GitHub repo size](https://img.shields.io/github/repo-size/PhilipeOliveiraS/ADA-Coders-2024)
![GitHub contributors](https://img.shields.io/github/contributors/PhilipeOliveiraS/ADA-Coders-2024)
![GitHub stars](https://img.shields.io/github/stars/PhilipeOliveiraS/ADA-Coders-2024?style=social)
![GitHub forks](https://img.shields.io/github/forks/PhilipeOliveiraS/ADA-Coders-2024?style=social)

---
---

Este projeto é mantido por [PhilipeOliveiraS](https://github.com/PhilipeOliveiraS). Contribuições são bem-vindas!

---
