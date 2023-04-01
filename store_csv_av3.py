    
import pandas as pd

tabela = pd.read_csv("C:/Users/usuario/Desktop/store_csv_av3/Stores.csv", sep=',')
# print(tabela)

tabela.columns.values
tabelacolumns = ['Store ID ', 'Store_Area', 'Items_Available', 'Daily_Customer_Count', 'Store_Sales']
tabelaFiltrado = tabela.filter(items=tabelacolumns)
tabelaFiltrado = tabelaFiltrado.rename(columns={
    'Store ID ' : 'ID',
    'Store_Area' : 'Itens',
    'Items_Available' : 'Disponíveis',
    'Daily_Customer_Count' : 'Visitantes',
    'Store_Sales' : 'Vendas (dólar)'
})
print(tabelaFiltrado)

#amanha retomada