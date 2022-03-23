import requests

# OBTENDO INFORMAÇÕES SOBRE O SITE FAZENDO UM GET UTILIZANDO A LIB REQUESTS
response = requests.get("https://www.youtube.com/")
print(f'StatusCode: {response.status_code}')
print(f'Headers: {response.headers}')
print(f'Content: {response.content}')
