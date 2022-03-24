from socket import timeout
from turtle import title
import requests
from bs4 import BeautifulSoup


# url base de onde será retirada as informações
url_base = "https://lista.mercadolivre.com.br/"
#!=========================================================================!

# input de qual produto será procurado na url_base
produto = input('Qual produto você deseja buscar?')

#!=========================================================================!

# resposta da pesquisa
response = requests.get(f"{url_base}{produto}")

#!=========================================================================!

# pegando o conteudo e passando o formato do site
site = BeautifulSoup(response.text, 'html.parser')

#!=========================================================================!

# Procurando a div específica do produto
produtosProcurados = site.findAll('div', attrs={
    "class": "andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default andes-card--animated"})
# print(produtoProcurado.prettify())
#!=========================================================================!

# Pegando o título do produto que está em title como um atributo da tag <a>

# titulo = produtoProcurado.find(
#     'a', attrs={'class': 'ui-search-result__content ui-search-link'})

# OU
# titulo = produtoProcurado.a['title']

#!=========================================================================!

# Pegando o link do produto que está em href como atribudo da tag <a>
# link = produtoProcurado.find(
#     'a', attrs={'class': 'ui-search-result__content ui-search-link'})

#!=========================================================================!

# OU
# link = produtoProcurado.a['href']

#!=========================================================================!

# Pegando o símbolo do valor {r$, usd...}
# simbolo = produtoProcurado.find('span', attrs={'class': 'price-tag-symbol'})
# print(simbolo.text)

#!=========================================================================!

# Pegando o primeiro valor inteiro do produto
# valorInt = produtoProcurado.find('span', attrs={'class': "price-tag-fraction"})
# print(valorInt.text)

#!=========================================================================!
# Pegando o valor decimal
# valorDec = produtoProcurado.find('span', attrs={'class': 'price-tag-cents'})
# print(valorDec.text)
#!=========================================================================!

# Printando todas as informações colhidas
# OBS: ['exemplo'] pega exatamente o atributo que está dentro da tag procurada
# print(f"Título: {titulo['title']}\nLink: {link['href']}\nValor:{simbolo.text} {valorInt.text},{valorDec.text}")


# AUTOMATIZANDO: COLHENDO AS INFOS DE TODOS OS PRODUTOS DA PÁGINA QUE ESTÁ CARREGADA

for produtoProcurado in produtosProcurados:
    titulo = produtoProcurado.find(
        'a', attrs={'class': 'ui-search-result__content ui-search-link'})
    link = produtoProcurado.find(
        'a', attrs={'class': 'ui-search-result__content ui-search-link'})
    simbolo = produtoProcurado.find(
        'span', attrs={'class': 'price-tag-symbol'})
    valorInt = produtoProcurado.find(
        'span', attrs={'class': "price-tag-fraction"})
    valorDec = produtoProcurado.find(
        'span', attrs={'class': 'price-tag-cents'})
        # TRATANDO ERRO COM O IF, POIS NEM TODOS OS PRODUTOS SÃO NUMEROS DECIMAIS
    if(valorDec):
        print(
            f"\nTítulo: {titulo['title']}\nLink: {link['href']}\nValor:{simbolo.text} {valorInt.text},{valorDec.text}\n")
    else:
        print(
            f"\nTítulo: {titulo['title']}\nLink: {link['href']}\nValor:{simbolo.text} {valorInt.text},00\n")
