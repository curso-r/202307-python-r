# -*- coding: utf-8 -*-
"""Aula2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10NccfjFl5zHzgmrONqS6F6m5_GHxM1Ms

# Revisão
"""

x = 1

x+1

"""Temos algumas palavras importantes pra lembrar!

1. São as "novas" de Python que tem a ver com orientação a objetos...

Tudo no python é **objeto**, que é um sinônimo de **variável**, e isso quer dizer que o código vai se parecer com uma historinha sobre os objetos. Os objetos tomam algumas ações e essas ações são pré-determinadas numa lista e cada ação dessa lista se chama **método**
"""

variavel_texto = "Fernando"

variavel_texto.

"""Também existem **funções** no pyhton, a `help` é um exemplo. Um **método** é mais ou menos como uma função, mas é uma função que mora um objeto específico. Já uma função como a `help` não mora em lugar nenhum."""

help(variavel_texto.count)

variavel_texto.upper()

upper(variavel_texto)

type(variavel_texto)

variavel_nova = "Fernando2"

help(str.capitalize)

import pandas

dados = pandas.read_csv("https://raw.githubusercontent.com/curso-r/main-r4ds-1/master/dados/imdb.csv")

type(dados)

dados.sum()

lista = [5, 3, 4]

x = 1
y = 2
z = 3

lista_com_variaveis = [x, y, z]

lista_com_variaveis

lista_com_variaveis + lista

"""## Array do numpy"""

# Commented out IPython magic to ensure Python compatibility.
# %whos

import numpy

# Commented out IPython magic to ensure Python compatibility.
# %whos

array_numpy = numpy.array([1,2,3])

array_numpy_2 = numpy.array([5,3,4])

type(array_numpy)

lista

array_numpy

array_numpy_2

array_numpy + array_numpy_2

array_numpy/array_numpy_2

array_numpy**array_numpy_2

array_numpy-array_numpy_2

numpy.array(["a", 1])



"""# Tipos básicos

str (string)
int (inteiro)
num (numérico)
object (meio que o "coringa" do pandas mas na maior parte das vezes quer dizer stringr)

# Tipos básicos de array...

métodos de array numérico

# Tipos de misturas

dict, tupla, lista
"""

# Indo de lista pra array
array_numpy = numpy.array([1,2,3])

# Voltando de array pra lista
listona = list(array_numpy)

listona

vetor_de_tamanho_4 = numpy.array([3, 5, 7, 6])

vetor_de_tamanho_4 = numpy.array([3, 5, 7, 6])

vetor_de_tamanho_3 = numpy.array([1, 2, 3])


# isso dá erro:
vetor_de_tamanho_3 + vetor_de_tamanho_4

# enquanto no R, teríamos uma reciclagem

# vetor_de_tamanho_3 viraria [1, 2, 3, 1]

vetor_de_tamanho_4.mean()

vetor_de_tamanho_4.min()

vetor_de_tamanho_4.max()

vetor_de_tamanho_4.std()

vetor_de_tamanho_4.sort()

vetor_de_tamanho_4

numpy.log(vetor_de_tamanho_4)

numpy.mean(vetor_de_tamanho_4)

# Exercícios

# 1. Crie um array utilizando o pacote numpy que contenha a idade das pessoas
# que moram com você ou que você convive de maneira mais próxima

array_idade_das_pessoas = numpy.array([90, 123, 23])

# 2. Calcule a média de idade das pessoas que estão no vetor anterior

array_idade_das_pessoas.mean()

array_idade_das_pessoas.sum()/len(array_idade_das_pessoas)

# 3. Explore os métodos de um ndarray do numpy para calcular a variância desse vetor de idades

array_idade_das_pessoas.var()

numpy.array([1, "a"])

# str > float > int > bool

numpy.array([1, 2]).astype("bool")

array_de_numeros_em_texto = numpy.array(['1', '2'])

str(array_de_numeros_em_texto)

type(array_de_numeros_em_texto)

array_de_numeros_em_texto.dtype

"""Pandas x Numpy

Numpy é uma biblioteca/pacote/library que serve pra você fazer contas com vetores, métodos matemáticos

o Pandas é uma biblioteca de manipulação de dados, então ela define o DataFrame e um milhão de métodos pra mexer com dataframe, tipo filtrar, criar coluna, sumarizar, pivotar etc. o Pandas depende do numpy

o statsModels é a biblioteca de estatística do Python

## Introdução ao Pandas
"""

# Commented out IPython magic to ensure Python compatibility.
# %whos

import pandas as pd

# Commented out IPython magic to ensure Python compatibility.
# %whos

imdb = pd.read_csv("https://raw.githubusercontent.com/curso-r/main-r4ds-1/master/dados/imdb.csv")

# Commented out IPython magic to ensure Python compatibility.
# %whos

type(imdb)

numpy.array([1, 2, 0])/0

imdb

imdb.describe()

imdb.info()

"""# Principais verbos de manipualação de dados no Pandas

- Ordenar linhas (sort_values)
- Selecionar linhas/colunas
    - Selecionar colunas = "filter" do Python x "select" do R
    - Selecionar linhas = "query" do Python x "filter" do R
- Criar colunas
- Sumarizar (com ou sem grupos)
- Pivotar
"""

# no dplyr R a gente faz arrange(imdb, ano)

# no Python Pandas:

dados.sort_values(["ano", "titulo"], ascending = [False, True])

colunas_para_ordenar = ["receita"]

dados_ordenados = dados.sort_values(colunas_para_ordenar, ascending = True)
# não tem modificação IN PLACE acontecendo

dados_ordenados

dados

"""# Selecionando colunas

"""

imdb_apenas_ano_receita = imdb.filter(['ano', 'receita'])

imdb_apenas_ano_receita

colunas_para_selecionar = ['ano', 'receita', 'orcamento']

apenas_ano_receita_orcamento = imdb.filter(colunas_para_selecionar).sort_values('receita')

ordenado_receita_selecao = (imdb.
                        filter(colunas_para_selecionar).
                        sort_values("receita")
)
# isso aqui é o que a gente chama de method chaining.
# CUIDADO!!!! PRECISA COMEÇAR COM PARÊNTESES

ordenado_receita_selecao = imdb.
filter(colunas_para_selecionar).
sort_values("receita")
# NÃO FUNCIONA!!

ordenado_receita_selecao = (imdb
.filter(colunas_para_selecionar)
.sort_values("receita"))
# funciona

imdb.loc[:, ["ano", "receita"]]

imdb.loc[:, colunas_para_selecionar]

imdb.filter(colunas_para_selecionar)

(imdb.
 query("ano <= 1945").
 filter(["ano", "titulo"]))

# select(filter(dados, ano <= 1945), ano, titulo)
# dados |> filter(ano <= 1934) é o mesmo que filter(dados, ano <= 1945)

# operadores lógicos

# & significa E (podemos usar and em vários casos)
# | significa OU (podemos usar or em vários casos)
# == significa comparação
# != significa diferença

# >
# <

# in (contenção)??? %in%
# PRÓXIMA AULA!!!

# podemos usar and ao invés de &
imdb.query("ano <= 1945 or orcamento > receita")

# pode o and e o or

# o fato disso: imdb.ano <= 1945 resultar em True/False

# garante que

imdb.query("ano <= 1945")

filmes_que_deram_lucro = imdb.query("receita > orcamento")

# isso aqui dá True/False....
filmes_que_deram_lucro.receita.isna()

# Será que posso colocar no "query"???

imdb.query("receita.isnan()")
# não podemos...

# o que será que o comando abaixo faz com os NaN???
filmes_que_deram_lucro = imdb.query("receita > orcamento")

# Podemos testar ordenando:
filmes_que_deram_lucro.sort_values("receita")

# Os NaN foram embora!

imdb.query("receita/orcamento > 1")

imdb.query("ano <= 1980").plot("receita", "orcamento", kind = "scatter")