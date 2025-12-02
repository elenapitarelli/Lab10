from dataclasses import dataclass

@dataclass
class Tratta:
    def __init__(self, hub1, hub2, numero_spedizioni, valore_medio):
        self.hub1 = hub1
        self.hub2 = hub2
        self.numero_spedizioni = numero_spedizioni
        self.valore_medio_tratta = valore_medio