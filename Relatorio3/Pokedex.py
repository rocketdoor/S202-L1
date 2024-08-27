#from database import Database
from Relatorio3.helper.writeAJson import writeAJson

class Pokedex:
    def __init__(self, database):
        self.database = database

    def listaTipo(self, types: list):
        pokemons = self.database.collection.find({"type": {"$in": types}})
        writeAJson(pokemons, "pokemons_por_tipo")

    def procuraFraquezas(self, weaknesses: list):
        pokemons = self.database.collection.find({"weaknesses": {"$in": weaknesses}})
        writeAJson(pokemons, "pokemons_por_fraqueza")

    def naoEvoluem(self):
        pokemons = self.database.collection.find({"next_evolution": {"$exists": False}, "prev_evolution": {"$exists": False}})
        writeAJson(pokemons, "pokemons_sem_evolucoes")

    def semOvos(self):
        pokemons = self.database.collection.find({"egg": "Not in Eggs"})
        writeAJson(pokemons, "pokemons_sem_ovos")

    def spawnChance(self, menor, maior):
        pokemons = self.database.collection.find({"spawn_chance": {"$gt": menor, "$lt": maior}})
        writeAJson(pokemons, "pokemons_entre_spawnChance")