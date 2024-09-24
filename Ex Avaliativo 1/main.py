from database import Database
from writeAJson import writeAJson
from MotoristaDAO import MotoristaDAO
from cli import MotoristaCLI

db = Database(database="ExAvaliativo1", collection="Motoristas")
#db.resetDatabase()

motoristaModel = MotoristaDAO(database=db)


motoristaCLI = MotoristaCLI(motoristaModel)
motoristaCLI.run()