import requests

id = 15

url = f"https://67efe7452a80b06b8896368d.mockapi.io/camisa/{id}"


data = {
    "nome":"Leone", 
    "marca":"Lacoste",
    "preco": 69.99,
    "tamanho":"M",
}
#put Atualiza completamente o objeto
response = requests.put(url, json=data) 


if response.status_code == 200:
    atualizado = response.json()
    print(f"usuario com id {id}foi atualizado com sucesso") 
    print(atualizado)
    
    
else:
    print(f"Falha na requisição: {response.status_code}{response.text}") 






