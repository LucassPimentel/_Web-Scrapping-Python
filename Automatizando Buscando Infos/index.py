from operator import index
import requests
from attr import attrs
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

response = requests.get("https://www.metropoles.com/distrito-federal")

#!=========================================================================!

# pega todo o conteúdo da pagina
content = response.content
#!=========================================================================!

# primeiro parametro para o BeautifulSoup é o conteúdo HTML
# segundo é o formato que o site está
site = BeautifulSoup(content, 'html.parser')

#!=========================================================================!

# Procura uma tag html
# primeiro parametro é a tag html que voce está procurando
# segundo parametro é o atribuito que ajudará a encontrar essa tag html
# attrs = atributos
# Obtive o html de toda a noticia
# OBS: .findAll - Procura todas as tags htmls que possuem determinado atributo
# OBS: Retorna um array
news = site.findAll('article', attrs={'class': 'm-feed m-feed-news-list'})

# Percorrendo o array que o findAll gerou e imprimindo cada titulo e cada resumo de noticia
for new in news:
    title = new.find('h6', attrs={'class': 'm-title'})
    resume = new.find('p', attrs={'class': 'm-resume'})
    if(title and resume):
        # adicionado os dados colhidos dentro de um array
        lista_noticias.append([title.text, resume.text])
        # print(f"Título: {title.text}\nResumo: {resume.text}")
    else:
        print('Ocorreu um erro, a notícia não possui título ou resumo.')


# Passando os dados como dataframe, para depois ser implementado no excel, por exemplo
# primeiro parametros os dados
# segundo parametro as colunas
# nesse caso a primeira coluna são os títulos das noticias
newsDtFrame = pd.DataFrame(lista_noticias, columns={'Título', 'Resumo'})
print(newsDtFrame)

# Salvando no formato que preferir, no caso estou salvando em excel
# baixar a lib openpyxl para poder salvar em excel
# primeiro parametro é o nome do arquivo
# segundo parametros é desativar o index (numeros que ficam ao lado das informações no terminal)
newsDtFrame.to_excel(
    'news.xlsx', index=False)
