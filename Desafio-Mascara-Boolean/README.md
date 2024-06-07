# 📊 Projeto de Notas e Recuperação com máscara Booleana

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![NumPy](https://img.shields.io/badge/NumPy-1.21-green)
![GitHub](https://img.shields.io/badge/GitHub-Repo-yellow)
![Contribua](https://img.shields.io/badge/Contribua-Welcome-brightgreen)


![Project Banner](https://source.unsplash.com/random/800x200?coding)


## 📚 Descrição

Este projeto simula o recebimento de notas de 10 alunos, identifica aqueles que precisam de recuperação (nota abaixo de 5), simula o recebimento de notas de recuperação e, finalmente, determina quais alunos foram reprovados após a recuperação.

---

## 🛠️ Funcionalidades

- **Entrada de Notas:** Simula a entrada de notas para 10 alunos.
- **Identificação de Recuperação:** Usa uma máscara booleana para identificar alunos que precisam de recuperação.
- **Atualização de Notas:** Atualiza as notas dos alunos com base nas notas de recuperação simuladas.
- **Identificação de Reprovados:** Identifica alunos reprovados após a recuperação.
- **Exibição de Resultados:** Exibe informações sobre alunos em recuperação e reprovados.


---

## 📊 Detalhamento do Código

#### Importação da Biblioteca NumPy
```python
import numpy as np
```
- **Importação da Biblioteca NumPy:** NumPy é uma biblioteca fundamental para a computação científica em Python, permitindo a criação e manipulação de arrays e matrizes de forma eficiente.

#### Simulação de Entrada de Notas dos Alunos
```python
notas = [4.0, 6.5, 3.0, 8.0, 7.5, 2.0, 9.0, 5.5, 4.5, 1.0]
```
- **Lista de Notas:** Cria uma lista com as notas de 10 alunos. Essas notas são usadas para simular uma entrada de dados.

#### Conversão da Lista para um Array NumPy
```python
notas_array = np.array(notas)
```
- **Array NumPy:** Converte a lista de notas em um array NumPy para aproveitar as operações eficientes dessa biblioteca.

#### Criação de Máscara para Identificar Alunos em Recuperação
```python
mascara_recuperacao = notas_array < 5
```
- **Máscara Booleana:** Cria uma máscara booleana (array de True/False) que identifica quais alunos têm notas abaixo de 5 e, portanto, precisam de recuperação.

#### Exibição de Notificações para Alunos em Recuperação
```python
print("Notificações de recuperação:")
notas_recuperacao = np.zeros_like(notas_array)
```
- **Inicialização de Notas de Recuperação:** Cria um array de zeros do mesmo tamanho que `notas_array` para armazenar as notas de recuperação.

#### Simulação de Entrada de Notas de Recuperação
```python
notas_recuperacao_entrada = [5.0, 6.0, 4.5, 8.0, 7.5, 5.0, 9.0, 5.5, 6.0, 3.5]
```
- **Notas de Recuperação:** Lista com as notas de recuperação que serão atribuídas aos alunos.

#### Atualização de Notas com Base na Recuperação
```python
for i in range(len(notas)):
    if mascara_recuperacao[i]:
        print(f"Aluno {i+1} está em recuperação com a nota {notas_array[i]}.")
        nova_nota = notas_recuperacao_entrada[i]
        print(f"Nota de recuperação para Aluno {i+1}: {nova_nota}")
        notas_recuperacao[i] = nova_nota
    else:
        notas_recuperacao[i] = notas_array[i]
```
- **Iteração e Atualização:** Itera sobre as notas originais. Se a nota está abaixo de 5, atualiza com a nota de recuperação correspondente; caso contrário, mantém a nota original.

#### Atualização das Notas com as da Recuperação
```python
notas_array[mascara_recuperacao] = notas_recuperacao[mascara_recuperacao]
```
- **Substituição Condicional:** Usa a máscara booleana para substituir as notas originais pelas notas de recuperação onde necessário.

#### Verificação de Alunos Reprovados Após Recuperação
```python
mascara_reprovados = notas_array < 5
print("\nResultado final após recuperação:")
for i in range(len(notas_array)):
    if mascara_reprovados[i]:
        print(f"Aluno {i+1} foi reprovado com a nota {notas_array[i]}.")
    else:
        print(f"Aluno {i+1} foi aprovado com a nota {notas_array[i]}.")
```
- **Máscara de Reprovados:** Cria uma nova máscara booleana para identificar alunos que continuam com notas abaixo de 5 após a recuperação.
- **Exibição de Resultados:** Itera novamente para exibir o status final (aprovado/reprovado) de cada aluno.

#### Exibição das Notas Finais
```python
print("\nNotas finais dos alunos:")
print(notas_array)
```
- **Notas Finais:** Exibe as notas finais de todos os alunos após a recuperação.


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
Fundamentos do Python Usados
1. Listas e Arrays
Listas: Armazenam as notas dos alunos inicialmente.
Arrays NumPy: Convertem listas em arrays NumPy para manipulação eficiente.
2. Operações com Arrays NumPy
Máscara Booleana: Cria uma máscara que identifica alunos com notas abaixo de 5.
3. Estruturas de Controle de Fluxo
Loop For: Itera sobre as notas dos alunos e aplica a lógica de recuperação.
4. Condicionais
If-Else: Verifica se um aluno precisa de recuperação e, posteriormente, se foi aprovado ou reprovado após a recuperação.
5. Impressão e Formatação de Strings
Print e f-strings: Exibem informações no console de maneira clara e formatada.
6. Atualização Condicional de Arrays
Atualização com Máscara: Usa máscaras booleanas para substituir as notas originais pelas notas de recuperação onde necessário.

---

---


![GitHub Repo](https://gh-card.dev/repos/PH3-Digital/ADA-Coders-2024/Desafio-Mascara-Boolean.svg)

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=PH3-Digital&show_icons=true&theme=radical)

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=PH3-Digital&layout=compact&theme=radical)

---

## 📈 Estatísticas do Repositório

![GitHub repo size](https://img.shields.io/github/repo-size/PH3-Digital/ADA-Coders-2024/Desafio-Mascara-Boolean)
![GitHub contributors](https://img.shields.io/github/contributors/PH3-Digital/ADA-Coders-2024)
![GitHub stars](https://img.shields.io/github/stars/PH3-Digital/ADA-Coders-2024?style=social)
![GitHub forks](https://img.shields.io/github/forks/PH3-Digital/ADA-Coders-2024?style=social)

---