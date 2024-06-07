# 📊 Projeto de Notas dos Alunos

![Python](https://img.shields.io/badge/Python-3.x-blue)
![NumPy](https://img.shields.io/badge/NumPy-1.21-green)
![GitHub](https://img.shields.io/badge/GitHub-Repo-yellow)
![Contribua](https://img.shields.io/badge/Contribua-Welcome-brightgreen)
![License](https://img.shields.io/github/license/PH3-Digital/ADA-Coders-2024)

![Project Banner](https://source.unsplash.com/random/800x200?coding)


## Descrição

Este projeto coleta notas de alunos, transforma esses dados em um array NumPy e realiza operações matemáticas como cálculo de média, desvio padrão, nota máxima e mínima. Ideal para iniciantes que desejam aprender Python e a biblioteca NumPy.

---

## 🛠️ Funcionalidades

- **Coleta de Dados:** Solicita ao usuário para inserir 10 notas de alunos.
- **Transformação de Dados:** Converte a lista de notas em um array NumPy.
- **Cálculo de Estatísticas:** Calcula a média, desvio padrão, nota máxima e mínima.
- **Exibição de Resultados:** Exibe os resultados de forma clara e objetiva.

---

## 📊 Detalhamento do Código

```python
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
```

### Explicação do Código

1. **Importação do NumPy:**
   ```python
   import numpy as np
   ```
   - O NumPy é uma biblioteca poderosa para computação numérica em Python, permitindo manipulação eficiente de arrays.

2. **Coletando as notas:**
   ```python
   notas = []
   for i in range(10):
       nota = float(input(f"Digite a nota {i+1}: "))
       notas.append(nota)
   ```
   - Cria uma lista vazia `notas` e usa um loop para solicitar 10 notas do usuário, convertendo cada entrada para `float` e adicionando à lista.

3. **Convertendo a lista em um array NumPy:**
   ```python
   notas_array = np.array(notas)
   ```
   - Transforma a lista de notas em um array NumPy para permitir operações matemáticas eficientes.

4. **Calculando a média:**
   ```python
   media = np.mean(notas_array)
   ```
   - Usa a função `mean` do NumPy para calcular a média dos valores no array.

5. **Calculando o desvio padrão:**
   ```python
   desvio_padrao = np.std(notas_array)
   ```
   - Usa a função `std` do NumPy para calcular o desvio padrão, que mede a dispersão das notas em relação à média.

6. **Encontrando a nota máxima e mínima:**
   ```python
   nota_maxima = np.max(notas_array)
   nota_minima = np.min(notas_array)
   ```
   - Usa as funções `max` e `min` do NumPy para encontrar os valores máximo e mínimo no array de notas.

7. **Exibindo os resultados:**
   ```python
   print(f"Média das notas: {media}")
   print(f"Desvio padrão das notas: {desvio_padrao}")
   print(f"Nota máxima: {nota_maxima}")
   print(f"Nota mínima: {nota_minima}")
   ```
   - Exibe a média, o desvio padrão, a nota máxima e a nota mínima calculados.

---
## 🚀 Como Usar

1. **Clone o Repositório:**
   ```sh
   git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
   cd NOME_DO_REPOSITORIO
   ```

2. **Instale as Dependências:**
   - Certifique-se de ter o Python e o NumPy instalados:
     ```sh
     pip install numpy
     ```

3. **Execute o Script:**
   ```sh
   python script_notas.py
   ```

4. **Insira as Notas:**
   - Siga as instruções no terminal para inserir as 10 notas.

---

## 📈 Estatísticas do Repositório

![GitHub repo size](https://img.shields.io/github/repo-size/PH3-Digital/ADA-Coders-2024)
![GitHub contributors](https://img.shields.io/github/contributors/PH3-Digital/ADA-Coders-2024)
![GitHub stars](https://img.shields.io/github/stars/PH3-Digital/ADA-Coders-2024?style=social)
![GitHub forks](https://img.shields.io/github/forks/PH3-Digital/ADA-Coders-2024?style=social)

---

## 🌟 Contribuindo

1. **Fork este repositório**
2. **Crie uma branch para sua feature**
   ```sh
   git checkout -b minha-nova-feature
   ```
3. **Faça commit das suas mudanças**
   ```sh
   git commit -am 'Adiciona nova feature'
   ```
4. **Envie para a branch**
   ```sh
   git push origin minha-nova-feature
   ```
5. **Abra um Pull Request**

---

### 📊 Fundamentos do Python Usados
Variáveis e Tipos de Dados:

Usamos variáveis para armazenar as notas, a média, o desvio padrão, etc.
Conversão de tipos (por exemplo, input para float).
Estruturas de Controle:

Uso de loops for para coletar as notas dos alunos.
Listas e Arrays:

Uso de listas para coletar dados e arrays NumPy para cálculos eficientes.
Funções e Métodos:

Uso de funções do NumPy (mean, std, max, min) para realizar operações matemáticas.
Entrada e Saída:

Uso da função input para coletar dados do usuário e print para exibir os resultados.
Essa estrutura ajuda a compreender tanto os fundamentos do Python quanto o uso eficiente do NumPy para manipulação e análise de dados numéricos.

---

---


![GitHub Repo](https://gh-card.dev/repos/PH3-Digital/ADA-Coders-2024.svg)

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=PH3-Digital&show_icons=true&theme=radical)

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=PH3-Digital&layout=compact&theme=radical)

![visitor badge](https://github-visitors-badge.glitch.me/badge?page_id=PH3-Digital/ADA-Coders-2024&left_color=green)
