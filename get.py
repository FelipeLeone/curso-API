import requests

url= "https://67efe7452a80b06b8896368d.mockapi.io/pedido"# importando biblioteca
#url= "https://67efe7452a80b06b8896368d.mockapi.io/camisa/3"# importando biblioteca
#GET para visualizar objeto
response = requests.get(url)

if response.status_code == 200:
    post = response.json()
    for post in post[:10]:
        print(post)
else:
    print(f"Falha na requisição: {response.status_code}")
    print(response.text)