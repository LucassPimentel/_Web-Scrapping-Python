import time
from selenium import webdriver



driver = webdriver.Chrome('C:\chromedriver')

driver.get('https://www.google.com/')

time.sleep(5) # 'Congela' o código 

search_box = driver.find_element_by_name('q') # pesquisa pelo nome do elemento

search_box.send_keys('hello world') # escreve algo, no caso escreve no input pesquisar do google

search_box.submit() # basicamente aperta o enter

time.sleep(5) 

driver.quit()
