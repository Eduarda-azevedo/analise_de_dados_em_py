# encoding: utf-8

import pandas as pd
import matplotlib.pyplot as plt

#Aluguel
A = pd.read_excel('discorama dados/Aluguel_editado.xlsx')
Aluguel = A.to_dict()
#pagamento
P = pd.read_excel('discorama dados/Pagamento_editado.xlsx')
Pagamento = P.to_dict()
#cliente
C = pd.read_excel('discorama dados/Cliente.xlsx')
Cliente = C.to_dict()
#inventário
I = pd.read_excel('discorama dados/Inventario_editado.xlsx')
Inventario = I.to_dict()
#filme
F = pd.read_excel('discorama dados/Filme.xlsx')
Filme = F.to_dict()

# Criar um dataframe com os dados
df_aluguel = pd.DataFrame(Aluguel)
df_pagamento = pd.DataFrame(Pagamento)
df_cliente = pd.DataFrame(Cliente)
df_inventario = pd.DataFrame(Inventario)
df_filme = pd.DataFrame(Filme)

# Calcular o total de filmes alugados
total_filmes_alugados = df_aluguel['Aluguel ID'].sum()

# Calcular o número de filmes alugados por gênero
aluguel_por_genero = df_aluguel.groupby('Genero')['True'].sum()
aluguel_por_genero1 = pd.pivot_table(df_aluguel, index='Genero', columns='Loja', values='True', aggfunc=sum)

# Calcular o número de filmes no inventario por gênero
inventario_por_genero = pd.pivot_table(df_inventario, index='Genero', columns='Loja', values='True', aggfunc=sum)

# Calcular os mau pagadores 
mau_pagadores = df_pagamento.groupby('Cliente')['juros'].sum()

#aluguel por mês em cada loja em 2005
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
df_aluguel['mês do aluguel'] = pd.Categorical(df_aluguel['mês do aluguel'], categories=meses, ordered=True)
df_aluguel= df_aluguel.sort_values('mês do aluguel')
aluguel_por_mes = pd.pivot_table(df_aluguel, index='mês do aluguel', columns='Loja', values='True', aggfunc=sum)

#ranking do 10 filmes mais alugados em cada loja
    #loja 1
filme_por_loja1 = df_aluguel.groupby('Filme')['Loja 1'].sum()
loja1 = filme_por_loja1.sort_values(ascending=False)
loja1 = loja1[:10]
print(f"Top 10 filmes Loja 1:\n {loja1}")
    #loja 2
filme_por_loja1 = df_aluguel.groupby('Filme')['Loja 2'].sum()
loja2 = filme_por_loja1.sort_values(ascending=False)
loja2 = loja2[:10]
print(f"Top 10 filmes Loja 2:\n {loja2}")

#Os 50 filmes mais caros de repor
filme_caro = df_filme.groupby('Titulo')['CR'].sum()
filme_caro = filme_caro.sort_values(ascending=False)
filme_caro = filme_caro[:50]
print(f"Os 50 filmes mais caros: \n{filme_caro}")

#dos top 50 caros que não valem a pena investir
filme_caro = filme_caro.reset_index()
loja1 = loja1.reset_index()
loja2 = loja2.reset_index()
filmecarolista = []
for z in range(50):
    filmecarolista.append(filme_caro['Titulo'][z])

print("Dos 50 filmes mais caros não investir em:")    
for j in range (50):
    if filmecarolista[j] in loja1 or filmecarolista[j] in loja2:
        pass
    else:
        print(filmecarolista[j])

    

# Exibir os resultados

print(f"Total de filmes: {len(df_inventario['Inventario ID'])}")
print(f"Total de filmes já alugados: {len(df_aluguel['Aluguel ID'])}")
loja = 1
for z in (df_inventario['Loja'].value_counts()):
    print (f"Total de filmes na loja {loja}: {z}")
    loja+=1

print("\nNúmero de filmes alugados por gênero, por ordem dos mais alugados:")
print(aluguel_por_genero.sort_values(ascending=False))

print("\nNúmero de clientes mau pagadores, por ordem dos devedores:")
print(mau_pagadores.sort_values(ascending=False))

# Plotar gráficos
aluguel_por_genero1.plot(kind='bar')
plt.title('Número de Filmes Alugados por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Número de Filmes Alugados')

aluguel_por_mes.plot(kind='bar')
plt.title('Número de Filmes Alugados por mês em 2005')
plt.xlabel('Mês')
plt.ylabel('Número de Filmes Alugados')

inventario_por_genero.plot(kind='bar')
plt.title('Número de Filmes no inventário por Gênero e Loja')
plt.xlabel('Gênero')
plt.ylabel('Número de Filmes')
plt.show()   