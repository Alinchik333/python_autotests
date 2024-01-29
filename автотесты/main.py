import requests
TOKEN="011230c700f85c1b35c40677db903a0e"
URL = 'https://api.pokemonbattle.me:9104'
HEADERS = {
    "Content-Type": "application/json",
    "trainer_token": TOKEN
}
body ={
    "name": "KZKZ",
    "photo": "https://dolnikov.ru/pokemons/albums/171.png"
}

response=requests.post(url=f'{URL}/pokemons', json = body, headers=HEADERS, timeout=5)
print(response.text)
ID=response.json()["id"]

body={
    "pokemon_id": ID,
    "name": "Денис Барбарис крутой",
    "photo": "https://dolnikov.ru/pokemons/albums/172.png"
}
response=requests.put(url=f'{URL}/pokemons', json = body, headers=HEADERS, timeout=5)
print(response.text)

body={
    "pokemon_id": ID
}
response=requests.post(url=f'{URL}/trainers/add_pokeball', json = body, headers=HEADERS, timeout=5)
print(response.text)
