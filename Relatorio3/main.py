from database import Database
from Pokedex import *
from Relatorio3.helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")

#db.resetDatabase()

#pokemon = db.collection.find_one({"name":"Pikachu"})
#writeAJson(pokemon, "pokemon")

#tipos = ["Grass", "Poison"]
#pokemons = pokemons = db.collection.find({ "type": {"$in": tipos}, "next_evolution": {"$exists": True} })
#writeAJson(pokemons, "pokemons")

pokedex = Pokedex(db)

tipos = ["Fire", "Ice"]
pokedex.listaTipo(tipos)

fraquezas = ["Flying"]
pokedex.procuraFraquezas(fraquezas)

pokedex.naoEvoluem()

pokedex.semOvos()

pokedex.spawnChance(0.3, 0.6)