# Selenium

Basicamente é utilizado para testar aplicações web de forma automatizadas, e/ou para automatizar processos.
De certa forma 'controla' o navegador.

## Para usá-lo:

#### Instalação:

- Instale inicialmente `pip install selenium`
- Verifique a versão do seu navegador
- Necessário instalar um driver do seu navegador (google, opera, firefox...) link: https://chromedriver.chromium.org/downloads
- Importe o driver para uma pasta de fácil procura.
- importe o webdriver `from selenium import webdriver`
- atribua a uma variável o driver do seu navegador. Exemplo: `navegador = webdriver.SeuNavegador(caminho da pasta onde foi salvo o webdriver/nomedodriver.exe)`
- Agora, seja feliz codando.
