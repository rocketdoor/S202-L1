from database import Database

db = Database("bolt://44.200.120.207", "neo4j", "hook-grams-runout")

query = "MATCH (t:Teacher) WHERE t.name = 'Renzo' RETURN [t.cpf, t.ano_nasc]"
parameters = {"name": 'Renzo'}
print(db.execute_query(query, parameters))

query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name, t.cpf"
parameters = {}
print(db.execute_query(query, parameters))

query = "MATCH (c:City) RETURN c.name"
parameters = {}
print(db.execute_query(query, parameters))

query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name, s.address, s.number"
parameters = {}
print(db.execute_query(query, parameters))

query = "MATCH (t:Teacher) RETURN min(t.ano_nasc) as mais_velho, max(t.ano_nasc) as mais_novo"
parameters = {}
print(db.execute_query(query, parameters))

query = "MATCH (c:City) RETURN avg(c.population)"
parameters = {}
print(db.execute_query(query, parameters))

query = "MATCH (c:City) WHERE c.cep = '37540-000' RETURN replace(c.name, 'a', 'A')"
parameters = {}
print(db.execute_query(query, parameters))

query = "MATCH (t:Teacher) RETURN substring(t.name, 2, 1)"
parameters = {}
print(db.execute_query(query, parameters))

