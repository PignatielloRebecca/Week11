import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        self._model.buildGrafo()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"{self._model._grafo}"))
        self._view.update_page()

    def handleCompConnessa(self,e):
        text_id=self._view._txtIdOggetto.value # devo prende il valore dell'oggetto
        #converto in un intero, non ci devono essere eccezioni
        try:
            id=int(text_id)
            print(f"{id}")
            # se qui posso usare id per le operazioni seguenti
            #uso delle funzioni di Network sul grafo
            numNodi=self._model.calcolaConnessa(id)  # devo passare l'id, non un oggetto del nodo della ricerca della componente
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Dim componente connessa: {numNodi}"))
            self._view.update_page()

        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Inserisci un id numerico"))
            self._view.update_page()



# quando premo il pulsante componente connessa: devo determinare la componente connessa nel grafo: con vertice precedentemente
# selezionato e verificare se il nodo esiste

#--> prendere una casella di testo: TEXTIDIOGGETTO: chiama la funzione handleComponenteConnessa
# prima di cancellare il grafo sempre meglio analizzare quello che ce dentro

# i successori sono tutti i nodi raggiungibili da quell'elemento
# successori, predeccessori e grafo hanno dei significati diversi
