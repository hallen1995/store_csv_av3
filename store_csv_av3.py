import pandas as pd

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
    'Store_Sales' : 'Vendas (dólar)'
})
print(13*" " + "Planilha de Controle de Fluxo")
print(tabelaFiltrado)


#Calculando o valor Máximo, Mínimo, Médio e Desvio padrão  
print('\n Calculando o valor máximo, mínimo, médio e desvio padrão:')

print('\n- Controle dos valores da coluna Estoque:')
dadosDisp = tabelaFiltrado['Estoque']
print("Valor máximo:", dadosDisp.values.max())
print("Valor mínimo:", dadosDisp.values.min())
print("Valor médio:", dadosDisp.values.mean())
print("Valor do desvio padrão:", dadosDisp.values.std())
print(50*"-")

print('\n- Controle dos valores da coluna Visitantes:')
dadosDisp = tabelaFiltrado['Visitantes']
print("Valor máximo:", dadosDisp.values.max())
print("Valor mínimo:", dadosDisp.values.min())
print("Valor médio:", dadosDisp.values.mean())
print("Valor do desvio padrão:", dadosDisp.values.std())
print(50*"-")

print('\n- Controle dos valores da coluna Vendas (dólar):')
dadosDisp = tabelaFiltrado['Vendas (dólar)']
print("Valor máximo:", dadosDisp.values.max())
print("Valor mínimo:", dadosDisp.values.min())
print("Valor médio:", dadosDisp.values.mean())
print("Valor do desvio padrão:", dadosDisp.values.std())
print(50*"-")

################################################################



