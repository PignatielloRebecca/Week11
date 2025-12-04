from model.model import Model

model=Model()

# dovrei aver gia letto gli oggetti
print(model._objects_dict[1234])
model.buildGrafo()
print(model._grafo)
