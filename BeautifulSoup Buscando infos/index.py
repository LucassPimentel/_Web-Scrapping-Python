import requests
from attr import attrs
from bs4 import BeautifulSoup

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
finder = site.find('article', attrs={'class': 'm-feed m-feed-news-list'})

#!=========================================================================!

# Printa o resultado da pesquisa de forma mais organizada
# print(finder.prettify())

#!=========================================================================!

# obtive somente o titulo da noticia, procurando dentro de uma procura
title = finder.find('h6', attrs={'class': 'm-title'})
# Printa somente o título da notífica
# print(f"Título: {title.text}")
# OBs: O .text pega somente o texto que está escrito dentro da tag pertencente.

#!=========================================================================!
# Obtive o resumo da notícia
resume = finder.find('p', attrs={'class': 'm-resume'})
# print(f"Resumo: {resume.text}")
# OBs: O .text pega somente o texto que está escrito dentro da tag pertencente.

#!=========================================================================!
# Printando o titulo e o resumo da notícia selecionada
print(f"Título: {title.text}\nResumo: {resume.text} ")
# OBs: O .text pega somente o texto que está escrito dentro da tag pertencente.
