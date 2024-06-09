

# 🔍 Análise de Correlação de Dados com Pairplot usando Seaborn


[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.11.2-orange.svg)](https://seaborn.pydata.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.3.3-yellow.svg)](https://pandas.pydata.org/)
![Data Analysis](https://img.shields.io/badge/Data%20Analysis-Titanic-green)
![Contribua](https://img.shields.io/badge/Contribua-Welcome-brightgreen)

![Project Banner](https://source.unsplash.com/random/800x200?coding)

## 📊 Descrição
Este projeto exemplifica o uso de **Python** e **Seaborn** para análise de correlação de dados utilizando o dataset `titanic` disponível no `seaborn`. Através do uso de pairplots, podemos visualizar as relações entre diferentes variáveis do dataset.
Utiliza Python juntamente com as bibliotecas Pandas e Seaborn para explorar, analisar e visualizar dados do famoso conjunto de dados do Titanic.
O objetivo deste projeto é fornecer uma análise visual dos dados do Titanic, focando nas relações entre diferentes variáveis como classe, cidade de embarque, e taxa de sobrevivência. Utilizamos Seaborn para criar gráficos de pares que ajudam a identificar correlações e distribuições de forma intuitiva e visual.

## 🛠️ Funcionalidades

- **Carregamento de Dados**: Carrega dados diretamente dentro do ambiente Python usando Seaborn.
- **Exploração de Dados**: Explora diferentes variáveis como `embark_town`, `class`, e `survived`.
- **Visualizações Estatísticas**: Utiliza gráficos de pares para visualizar as relações e distribuições das variáveis.


## 🚀 Explicação do Código


### Carregamento dos Dados
```python
import seaborn as sns
import pandas as pd

# Carregando o dataset 'titanic' do seaborn
titanic = sns.load_dataset('titanic')
```
Carregamos o dataset `titanic` que vem pré-carregado no `seaborn`.

### Exibição dos Primeiros Dados
```python
# Exibindo as primeiras linhas do dataset
print(titanic.head())
```
Utilizamos `head()` para visualizar as primeiras linhas do dataset.

### Análise de Dados Nulos
```python
# Analisando os dados faltantes
print(titanic.isnull().sum())
```
Verificamos a presença de valores nulos no dataset.

### Descrição Estatística
```python
# Descrição estatística dos dados
print(titanic.describe())
```
Obtemos uma descrição estatística básica das variáveis numéricas no dataset.

### Criação do Pairplot
```python
import seaborn as sns

# Criando o pairplot do dataset Titanic
sns.pairplot(titanic, hue='class')
```
Criamos um pairplot para visualizar as relações entre as variáveis numéricas, colorindo os pontos de acordo com a classe dos passageiros.


## 🧱 Fundamentos do Python
### Bibliotecas
- **Pandas**: Biblioteca poderosa para manipulação de dados em Python.
- **Seaborn**: Biblioteca de visualização de dados que fornece uma interface de alto nível para desenhar gráficos estatísticos atraentes e informativos.

### Funções e Métodos
- **`pd.read_csv()`**: Lê um arquivo CSV e o carrega em um DataFrame.
- **`DataFrame.head()`**: Exibe as primeiras linhas do DataFrame.
- **`DataFrame.isnull().sum()`**: Verifica a presença de valores nulos no DataFrame.
- **`DataFrame.describe()`**: Gera estatísticas descritivas do DataFrame.
- **`sns.pairplot()`**: Cria uma matriz de gráficos de dispersão de pares de variáveis no DataFrame.

## Visualização do Gráfico
![Pairplot do Titanic](pairplot_titanic.png)

---


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-green)](https://github.com/PH3-Digital/ADA-Coders-2024/tree/main/Desafio-CorrelacaoDados-Pairplot-Seaborn)



### Detalhamento dos Fundamentos do Python

- **Importações**: `import` é usado para adicionar módulos externos ao nosso script.
- **Pandas**: Utilizado para manipulação e análise de dados. A função `pd.read_csv()` é comumente usada para carregar dados de arquivos CSV, mas aqui utilizamos `sns.load_dataset()` para carregar dados diretamente via Seaborn.
- **Seaborn**: Uma biblioteca de visualização de dados baseada em Matplotlib que proporciona uma interface de alto nível para desenhar gráficos estatísticos atrativos.
- **DataFrames**: Estruturas de dados bidimensionais onde os dados são alinhados de forma tabular em linhas e colunas, facilitando a manipulação.
- **Métodos `.value_counts()`**: Retorna uma série contendo contagens de valores únicos, útil para obter uma contagem de frequência de informações categóricas.
- **`sns.pairplot()`**: Um método de Seaborn que cria gráficos entre pares de colunas num DataFrame para explorar as relações entre elas.

## Contribua!

Sinta-se livre para `fork` este repositório e contribuir com melhorias. Todas as sugestões e contribuições são bem-vindas!

[![Contribuir](https://yourbuttonimageurl.png)](https://github.com/PH3-Digital/ADA-Coders-2024/tree/main/Desafio-CorrelacaoDados-Pairplot-Seaborn)

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes.
```

Este `README.md` incorpora badges informativos, uma descrição clara do projeto, funcionalidades, visualizações gráficas, e uma explicação detalhada do código e dos fundamentos de Python usados.