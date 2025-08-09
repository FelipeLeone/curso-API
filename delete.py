import requests

id = 22

#url= "https://67efe7452a80b06b8896368d.mockapi.io/pedido"# importando biblioteca
url= f"https://67efe7452a80b06b8896368d.mockapi.io/camisa/{id}"# importando biblioteca
#Delete p remover obj
response = requests.delete(url)

if response.status_code == 200:
    print(f"usuario com id {id}foi executado com sucesso") 
    
    
else:
    print(f"Falha na requisição: {response.status_code}{response.text}") 





