import requests

url= "https://67efe7452a80b06b8896368d.mockapi.io/pedido"# importando biblioteca da nossa API

data = {
    "nome":"macarrao", 
    "preco": 49.99,
    "quantidade": 2
}

response = requests.post(url, json=data)


print(response.status_code)
print(response.text)