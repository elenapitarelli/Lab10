from database.DB_connect import DBConnect
from model.hub import Hub
from model.spedizione import Spedizione
from model.tratta import Tratta

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """

    def __init__(self):
        pass

    @staticmethod
    def readHub():
        connessione = DBConnect.get_connection()
        result = []
        cursor = connessione.cursor(dictionary=True)
        query = "SELECT * FROM hub"
        cursor.execute(query)
        for row in cursor:
            hub = Hub(row["id"], row["codice"], row["nome"], row["citta"], row["stato"], row["latitudine"], row["longitudine"])
            result.append(hub)
        cursor.close()
        connessione.close()
        return result

    def tratte_filtrate(self,threshold):
        connessione = DBConnect.get_connection()
        result = []
        cursor = connessione.cursor(dictionary=True)
        query = ("""SELECT 
            LEAST(s.id_hub_origine, s.id_hub_destinazione) AS hub1,
            GREATEST(s.id_hub_origine, s.id_hub_destinazione) AS hub2,
            COUNT(*) AS numero_spedizioni,
            AVG(s.valore_merce) AS valore_medio_tratta
        FROM spedizione s
        GROUP BY hub1, hub2
        HAVING AVG(s.valore_merce) >= %s
    """)
        cursor.execute(query,(threshold,))
        for row in cursor:
            tratta = Tratta(row["hub1"], row["hub2"], row["numero_spedizioni"], row["valore_medio_tratta"])
            result.append(tratta)
        cursor.close()
        connessione.close()
        return result

    def readSpedizioni(self):
        connessione = DBConnect.get_connection()
        result = []
        cursor = connessione.cursor(dictionary=True)
        query = "SELECT * FROM spedizioni"
        cursor.execute(query)
        for row in cursor:
            spedizione = Spedizione(row["id"], row["id_compagnia"], row["numero_tracking"], row["id_hub_origine"],
                                    row["id_hub_destinazione"], row["data_ritiro_programmata"], row["distanza"], row["data_consegna"])
            result.append(spedizione)
        cursor.close()
        connessione.close()
        return result



