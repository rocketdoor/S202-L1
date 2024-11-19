from database import Database
from idolDatabase import IdolDatabase

db = Database("bolt://3.239.218.253", "neo4j", "misalignment-bands-war")
db.drop_all()

idb = IdolDatabase(db)

idb.create_idol("Wonyoung", 20, "South Korea", "Jang Wonyoung", "jwy1")
idb.create_group("IVE", 2021, "ssg3")
idb.create_company("Starship", "000.000.000-00")
idb.create_show("Music Bank", "Saturday", "to01")

idb.insert_idol_group("jwy1", "ssg3")
idb.insert_group_company("ssg3", "000.000.000-00")
idb.insert_group_show("ssg3", "to01")
idb.insert_idol_show("jwy1", "to01")


idol = idb.get_idol("jwy1")
print(idol)

group = idb.get_group("ssg3")
print(group)

company = idb.get_company("000.000.000-00")
print(company)

show = idb.get_show("to01")
print(show)


idb.update_idol("jwy1", "ayj1", "Yujin", "21", "South Korea", "Ahn Yujin")
print(idb.get_idol("ayj1"))

idb.update_group("ssg3", "wog1", "IZ*ONE", 2018)
print(idb.get_group("wog1"))

idb.update_company("000.000.000-00", "000.111.000-11", "WakeOne")
print(idb.get_company("000.111.000-11"))

idb.update_show("to01", "il01", "Inkigayo", "Sunday")
print(idb.get_show("il01"))


idb.delete_idol("ayj1")
idb.delete_group("wog1")
idb.delete_company("000.111.000-11")
idb.delete_show("il01")