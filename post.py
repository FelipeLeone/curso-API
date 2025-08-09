import requests

url= "https://67efe7452a80b06b8896368d.mockapi.io/camisa"# importando biblioteca da nossa API

data = {
    "nome":"Leone", 
    "marca":"Nike",
    "preco": 49.99,
    "tamanho":"G",
}
#POST para inserir obj
response = requests.post(url, json=data)
if response.status_code ==201:
    new_post = response.json()
    print("novo post criado !")
    print(new_post)
else:
    print(f"Falha na requisição: {response.status_code}{response.text}")    