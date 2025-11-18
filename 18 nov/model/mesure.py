"""
module contenant la classe Mesure
"""
class Mesure:
    def __init__(self, capteur, valeur, unite):
        self.capteur = capteur
        self.valeur = valeur
        self.unite = unite

    @property
    def capteur(self):
        return self.__capteur

    @capteur.setter
    def capteur(self, capteur):
        if not isinstance(capteur, str) or not capteur.strip():
            raise ValueError("capteur doit etre non vide")
        self.__capteur = capteur

    @property
    def valeur(self):
        return self.__valeur

    @valeur.setter
    def valeur(self, valeur):
        try:
            f = float(valeur)
        except Exception:
            raise ValueError(" La valeur mesuré doit être doit etre un nombre")
        self.__valeur = valeur

    @property
    def unite(self, v):
        if v not in ("C", "F"):
            raise ValueError("la valeur doit <UNK>tre un nombre")
        self.unite = v


