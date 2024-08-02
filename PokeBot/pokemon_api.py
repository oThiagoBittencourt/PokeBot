import requests

class PokeAPI:
    def __init__(self):
        self.pokeAPI_url = "https://pokeapi.co/api/v2/"

    def search_pokemon(self, name:str):
        response = requests.get(self.pokeAPI_url + f"pokemon/{name}")

        if (response.status_code != 200):
            return
        return response.json()