import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        # TODO
        try:
            threshold = float(self._view.guadagno_medio_minimo.value)
        except:
            self._view.show_alert("Inserisci un numero valido!")
            return

        self._model.costruisci_grafo(threshold)
        num_hub = self._model.get_num_nodes()
        num_tratte = self._model.get_num_edges()
        lista_tratte = self._model.get_all_edges()

        id_to_nome = {hub.id: hub.nome for hub in self._model._lista_hub}

        self._view.lista_visualizzazione.controls.clear()

        self._view.lista_visualizzazione.controls.append(
            ft.Text(f"Numero di Hub: {num_hub}")
        )
        self._view.lista_visualizzazione.controls.append(
            ft.Text(f"Numero di Tratte: {num_tratte}")
        )
        if not lista_tratte:
            self._view.lista_visualizzazione.controls.append(ft.Text("Nessuna tratta supera la soglia indicata."))
        else:
            for h1_id, h2_id, guadagno in lista_tratte:
                nome1 = id_to_nome.get(h1_id, str(h1_id))
                nome2 = id_to_nome.get(h2_id, str(h2_id))
                self._view.lista_visualizzazione.controls.append(
                    ft.Text(f"{nome1} - {nome2}: {guadagno:.2f} €")
                )

        self._view.update()
        #for h1, h2, w in lista_tratte:
            #self._view.lista_visualizzazione.controls.append(
                #ft.Text(f"{h1.nome} - {h2.nome}: {w:.2f} €"))
        #self._view.update()

