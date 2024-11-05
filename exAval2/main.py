from database import Database
from teacher_crud import TeacherCRUD

db = Database("bolt://44.200.120.207", "neo4j", "hook-grams-runout")
db.drop_all()

teachercrud = TeacherCRUD(db)

teacher = teachercrud.create('Chris Lima', 1956, '189.052.396-66')

teacher_read = teachercrud.read('Chris Lima')

print(teacher_read)

newCpf = "162.052.777-77"

teacher = teachercrud.update('Chris Lima', newCpf)

teacher_read = teachercrud.read('Chris Lima')

print(teacher_read)

