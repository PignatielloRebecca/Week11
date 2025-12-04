from database.DAO import DAO

results=DAO.readObjects()
print(results[6])
print(len(results))
# potenzialmente avremmo 85581 nodi