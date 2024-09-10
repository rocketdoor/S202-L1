from database import Database
from writeAJson import writeAJson
from bookModel import BookModel
from cli import BookCLI

db = Database(database="relatorio_05", collection="livros")
personModel = BookModel(database=db)


personCLI = BookCLI(personModel)
personCLI.run()