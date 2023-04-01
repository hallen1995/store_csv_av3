import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.read_csv("C:/Users/usuario/Desktop/store_csv_av3/Stores.csv", sep=',')
# print(tabela)
#Mostrar tabela CSV completa
tabela.columns.values
tabelacolumns = ['Store ID ', 'Store_Area', 'Items_Available', 'Daily_Customer_Count', 'Store_Sales']
tabelaFiltrado = tabela.filter(items=tabelacolumns)
tabelaFiltrado = tabelaFiltrado.rename(columns={
    'Store ID ' : 'ID',
    'Store_Area' : 'Itens',
    'Items_Available' : 'Estoque',
    'Daily_Customer_Count' : 'Visitantes',
    'Store_Sales' : 'Vendas'
})
tabelaFiltrado.sort_values('Estoque')

print(9*" " + "Planilha de Controle de Fluxo")
print(tabelaFiltrado)


#Calculando o valor Máximo, Mínimo, Médio e Desvio padrão  
print('\n Calculando o valor máximo, mínimo, médio e desvio padrão:')
print('\n- Controle dos valores da coluna Estoque:')
dadosDisp = tabelaFiltrado['Estoque']

maxEstoque = dadosDisp.values.max()
print('Valor máximo:', maxEstoque)

minEstoque = dadosDisp.values.min()
print('Valor mínimo:', minEstoque)

meanEstoque = dadosDisp.values.mean()
print('Valor média:', meanEstoque)

stdEstoque = dadosDisp.values.std()
print('Valor desvio padrão:', stdEstoque)
print(50*"-")
# --------------------------------------------------
print('\n- Controle dos valores da coluna Visitantes:')
dadosDisp = tabelaFiltrado['Visitantes']
maxVisitas = dadosDisp.values.max()
print('Valor máximo:', maxVisitas)

minVisitas = dadosDisp.values.min()
print('Valor mínimo:', minVisitas)

meanVisitas = dadosDisp.values.mean()
print('Valor média:', meanVisitas)

stdVisitas = dadosDisp.values.std()
print('Valor desvio padrão:', stdVisitas)
print(50*"-")
# --------------------------------------------------
print('\n- Controle dos valores da coluna Vendas (dólar):')
dadosDisp = tabelaFiltrado['Vendas']
maxVendas = dadosDisp.values.max()
print('Valor máximo:', maxVendas)

minVendas = dadosDisp.values.min()
print('Valor mínimo:', minVendas)

meanVendas = dadosDisp.values.mean()
print('Valor média:', meanVendas)

stdVendas = dadosDisp.values.std()
print('Valor desvio padrão:', stdVendas)
print(50*"-")

# --------------------------------------------------
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

dadosEstoque = ['Máximo', 'Mínimo', 'Média', 'Desvio']
counts = (maxEstoque, minEstoque, meanEstoque, stdEstoque)

bar_labels = ['Max', 'Min', 'Med', 'Desv']
bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

ax.bar(dadosEstoque, counts, label=bar_labels, color=bar_colors)
ax.set_ylabel('Valor Alcançado')
ax.set_title('Controle do Estoque em: \n Qtd. Máxima, Qtd. Mínima, Média e Desvio Padrão')
ax.legend(title='Dados')

plt.show()

# --------------------------------------------------

fig, ax = plt.subplots()

dadosVisitas = ['Máximo', 'Mínimo', 'Média', 'Desvio']
counts = (maxVisitas, minVisitas, meanVisitas, stdVisitas)

bar_labels = ['Max', 'Min', 'Med', 'Desv']
bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

ax.bar(dadosVisitas, counts, label=bar_labels, color=bar_colors)
ax.set_ylabel('Valor Alcançado')
ax.set_title('Controle de Visitas em: \n Qtd. Máxima, Qtd. Mínima, Média e Desvio Padrão')
ax.legend(title='Dados')

plt.show()

# ------------------------------------------------------------------

fig, ax = plt.subplots()

dadosVendas = ['Máximo', 'Mínimo', 'Média', 'Desvio']
counts = (maxVendas, minVendas, meanVendas, stdVendas)

bar_labels = ['Max', 'Min', 'Med', 'Desv']
bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

ax.bar(dadosVendas, counts, label=bar_labels, color=bar_colors)
ax.set_ylabel('Valor Alcançado')
ax.set_title('Controle de Vendas (dólar) em: \n Qtd. Máxima, Qtd. Mínima, Média e Desvio Padrão')
ax.legend(title='Dados')

plt.show()

