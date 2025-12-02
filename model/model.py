from networkx.classes import number_of_edges

from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()
        self.DAO = DAO()
        self._lista_hub =  []
        self._tratte_filtrate = []

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """

        self.G.clear()

        self._lista_hub = self.DAO.readHub()
        self.G.add_nodes_from(self._lista_hub) #aggiungo nodi
        self._tratte_filtrate = self.DAO.tratte_filtrate(threshold)

        for tratta in self._tratte_filtrate:
            self.G.add_edge(tratta.hub1, tratta.hub2, weight= tratta.valore_medio_tratta) #arco non orientato con peso




    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        num_edges = self.G.number_of_edges()
        return num_edges


    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        num_nodi = self.G.number_of_nodes()
        return num_nodi

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """

        edges = []
        for nodo1, nodo2, valore in self.G.edges(data=True):
            edges.append((nodo1, nodo2, valore['weight']))
        return edges


