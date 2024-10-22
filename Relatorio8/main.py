from database import Database
from JogoDatabase import JogoDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.87.1.210:7687", "neo4j", "beats-company-mop")
db.drop_all()


# Criando uma instância da classe JogoDatabase para interagir com o banco de dados
jogo_db = JogoDatabase(db)

# Criando alguns Jogadores
jogo_db.create_jogador("Roberto")
jogo_db.create_jogador("Guilherme")
jogo_db.create_jogador("Matheus")

# Criando alguns Partidas
jogo_db.create_partida("1")
jogo_db.create_partida("2")
jogo_db.create_partida("3")

# Criando jogos e suas relações com os jogadores
jogo_db.create_jogo("Roberto", "1")
jogo_db.create_jogo("Roberto", "3")
jogo_db.create_jogo("Guilherme", "2")
jogo_db.create_jogo("Matheus", "3")

# Atualizando o nome de um Jogador
jogo_db.update_jogador("Guilherme", "Gabriel")

#Inserindo um Jogador na Partida
jogo_db.insert_jogador_partida("Matheus", "1")


# Deletando um Jogador, uma Partida e a Participacao de alguem no Jogo
#jogo_db.delete_jogador("Roberto")
#jogo_db.delete_partida("2")
#jogo_db.delete_jogo("Matheus")

# Imprimindo todas as informações do banco de dados
print("Jogadores:")
print(jogo_db.get_jogadores())
print("Partidas:")
print(jogo_db.get_partidas())
print("Jogos:")
print(jogo_db.get_jogos())

# Fechando a conexão com o banco de dados
db.close()
