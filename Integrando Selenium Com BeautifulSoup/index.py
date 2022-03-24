import time
from urllib import request

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# Options ferramenta para definir opções ao navegador
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#!=========================================================================!


#!=========================================================================!

# Adicionado opções de abertura do navegador
options = Options()
# options.add_argument("--headless") # Faz toda a rotina programada sem mostrar o navegador
# Tamanho da janela que vai abrir do navegador
options.add_argument("window-size=400,800")

#!=========================================================================!

# Iniciando a automatização
browser = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
browser.get("https://www.airbnb.com.br/")
#!=========================================================================!

time.sleep(2)
# clicando no botão para pesquisar locais
button = browser.find_element(By.TAG_NAME, 'button')
button.click()

#!=========================================================================!

# Procurando, escrevendo e dando enter no local no input
input_place = browser.find_element(By.NAME, 'query')
input_place.send_keys('rio de janeiro')
time.sleep(1)
input_place.submit()

#!=========================================================================!
# Clicando na opção de casas, quartos...
time.sleep(1)
# selecionando através do seletor css, abaixo do botão tem uma img, e isso guia o selenium para saber qual botao certo 'clicar'
btn_choose = browser.find_element(By.CSS_SELECTOR, 'button > img')
btn_choose.click()
time.sleep(1)

#!=========================================================================!
# clicando no botao pular
btn_jump = browser.find_element(By.CLASS_NAME, '_fpnigw0')
btn_jump.click()
time.sleep(1)

#!=========================================================================!
# Pulando novamente
btn_jump = browser.find_element(By.CLASS_NAME, '_fpnigw0')
btn_jump.click()
time.sleep(6)
#!=========================================================================!
# Convertendo a última pagina para B.Soup
# OBS: browser.page_source pega todo o html da pagina carregada pelo selenium

page_content = browser.page_source

site = BeautifulSoup(page_content, 'html.parser')

print(site.prettify())
