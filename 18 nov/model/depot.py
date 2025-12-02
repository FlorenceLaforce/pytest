"""
Couche d'accès à la base de données
"""

import sqlite3
from mesure import Mesure

class DepotMesure:
    def __init__(self, fichier_db = "mesure.db"):
        self.fichier_db = fichier_db
        self.creer_table()

    def creer_table(self):
        conn = sqlite3.connect(self.fichier_db)
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS mesures(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                capteur TEXT  not null,
                valeur REAL not null,
                unite TEXT not null,
            )
            """
        )
        conn.commit()
        conn.close()

    def ajouter(self, mesure):

        if not isinstance(mesure, Mesure):
            raise TypeError("la valeur doit <UNK>tre un nombre")
        conn = sqlite3.connect(self.fichier_db)
        cur = conn.cursor()
        cur.execute(
            "insert into mesures(capteur, valeur, unite) values (?, ?, ?)",
            (mesure.capteur, mesure.valeur, mesure.unite),
        )
        conn.commit()
        conn.close()

    def data(self):
        conn = sqlite3.connect(self.fichier_db)
        cur = conn.cursor()
