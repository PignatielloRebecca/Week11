from database.DB_connect import DBConnect
from model.object import Object
from model.connessione import Connessione


class DAO():
    def __init__(self):
            pass
    @staticmethod
    def readObjects():
        conn=DBConnect.get_connection() # restituisce oggetto connesione
        result=[]
        cursor=conn.cursor(dictionary=True)# chiedo alla connessione un cursore
        query="SELECT * FROM objects" # tira fuori tutte le informazioni
        cursor.execute(query)
        # preparo a scandire i risultati
        for row in cursor:
            #result.append(Object(row["object_id"], row["object_name"])) # mi creo un oggetto
            result.append(Object(**row))  # fa l'unpacking del dizionario: estrarre le informazioni della forma: chiave--> valore

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def readConnesioni(objects_dict): # riceve la idMap degli Object
        conn = DBConnect.get_connection()  # restituisce oggetto connesione
        result = []
        cursor = conn.cursor(dictionary=True)  # chiedo alla connessione un cursore
        query = """select eo1.object_id AS o1, eo2.object_id AS o2, COUNT(*) as peso
                from exhibition_objects eo1, exhibition_objects eo2
                where eo1.exhibition_id=eo2.exhibition_id
                and eo1.object_id< eo2.object_id
                group by eo1.object_id, eo2.object_id"""  # tira fuori tutte le informazioni

        cursor.execute(query)
        # preparo a scandire i risultati
        # volgio fare degli oggetti di tipo connesione
        # passo l'oggetto dizionario per creare un ogetto
        for row in cursor:
            o1=objects_dict[row["o1"]]  # ma io nel model ho objects Dict
            o2=objects_dict[row["o2"]]
            peso=row["peso"]
            result.append(Connessione(o1,o2,peso))  # Costuisce una Connesione



        cursor.close()
        conn.close()
        return result #  lista di ogetti di tipo Connesione

# nella query raggruppo per coppie di object id.
# query non parametrizzata
# ottendo delle coppie di id degli oggetti