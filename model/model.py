from database.DAO import DAO
import networkx as nx
from model.connessione import Connessione

class Model:
    def __init__(self):
        self._objects_list=[] # ci ricordiamo che è una lista
        # creo un dizionario di objects
        self._getObjects()
        self._objects_dict={} # costruisco la id map di object
        for o in self._objects_list:
            self._objects_dict[o.object_id] = o  # vado ad infilare l'oggetto
        # non orientato, semplice ma pesato -->Graph()
        self._grafo=nx.Graph()

    def _getObjects(self):
        self._objects_list=DAO.readObjects() # leggo dal DAO

    def buildGrafo(self):
        # nodi, sto aggiungendo i nodi
        # questa funzione aggiunge la lista
        self._grafo.add_nodes_from(self._objects_list)

        # archi
        """
        # modo1, molto lungo da leggere 
        for u in self._objects_list:
            for v in self._objects_list:
                DAO.readEdges(u,v)  # da scrivere 
        
        """

        #MODO 2 (usare una query sola per estrarre le connessioni)
        # oggetti che hanno un oggetto d'arte di partenza e uno di arrivo
        # aggiungo un arco fra questi ue elementi
        # funzione che mi dica se esiste una connesione fra due nodi
        # leggo le connessioni dal DAO

        connessioni=DAO.readConnesioni(self._objects_dict) # leggo dal DAO, prendo una lista di connesioni
        for c in connessioni:
            self._grafo.add_edge(c.o1,c.o2, peso=c.peso)

    def calcolaConnessa(self, id_nodo):
        # cosa fanno i successore, restituisce un iteratore dei successori del nodo radice
        nodo_sorgente=self._objects_dict[id_nodo]

        # USANDO I SUCCESSORI
        successori=nx.dfs_successors(self._grafo, nodo_sorgente) # funzione che riceve il grafo e il nodo
        print(f"Succesori: {len(successori)}")
        #for nodo in successori:
            #esplora tutti i successori del nodo in questione
            # parto da un nodo e segui archi per trovare i successori (si puo fare anche con i predecessori)

            #print(nodo)
        # USANDO I PREDECCESSORI (MA DEVO POI INCREMENETARE DI 1)
        predecessori=nx.dfs_predecessors(self._grafo, nodo_sorgente)
        print(f"predecessori: {len(predecessori)}")  # non viene lo stesso risultato
        # mi posso far restituire l'albero

        # OTTENGO L'ALBERO DI FISITA
        albero=nx.dfs_tree(self._grafo, nodo_sorgente)
        print(f"albero: {albero}")  # l'albero completo, include un nodo im più
        return len(albero.nodes)  # numero di nodi, lunghezza e la restituisco













