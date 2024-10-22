class JogoDatabase:
    def __init__(self, database):
        self.db = database

    def create_jogador(self, name):
        query = "CREATE (:Jogador {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def create_partida(self, numero):
        query = "CREATE (:Partida {numero: $numero})"
        parameters = {"numero": numero}
        self.db.execute_query(query, parameters)

    def create_jogo(self, name, numero):
        query = "MATCH (p:Partida {numero: $numero}), (j:Jogador {name: $name}) CREATE (j)<-[:JOGA]-(p)"
        parameters = {"name": name, "numero": numero}
        self.db.execute_query(query, parameters)

    def get_partidas(self):
        query = "MATCH (p:Partida) RETURN p.numero AS numero"
        results = self.db.execute_query(query)
        return [result["numero"] for result in results]

    def get_jogadores(self):
        query = "MATCH (j:Jogador) RETURN j.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_jogos(self):
        query = "MATCH (j:Jogador)<-[:JOGA]-(p:Partida) RETURN j.name AS name, p.numero AS numero"
        results = self.db.execute_query(query)
        return [(result["name"], result["numero"]) for result in results]

    def update_jogador(self, old_name, new_name):
        query = "MATCH (j:Jogador {name: $old_name}) SET j.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def insert_jogador_partida(self, name, numero):
        query = "MATCH (j:Jogador {name: $name}) MATCH (p:Partida {numero: $numero}) CREATE (j)-[:JOGA]->(p)"
        parameters = {"name": name, "numero": numero}
        self.db.execute_query(query, parameters)


    def delete_partida(self,numero):
        query = "MATCH (p:Partida {numero: $numero}) DETACH DELETE p"
        parameters = {"numero": numero}
        self.db.execute_query(query, parameters)

    def delete_jogador(self, name):
        query = "MATCH (j:Jogador {name: $name}) DETACH DELETE a"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def delete_jogo(self, name):
        query = "MATCH (j:Jogador {name: $name})<-[:JOGA]-(p:Partida) DETACH DELETE j"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)