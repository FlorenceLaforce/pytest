import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

UNITES = ("C", "F")

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Exercice")
        self.geometry("600x800")
        self.creer_widget()


    def creer_widget(self):

        self.frm_principale = tk.Frame(self)
        self.frm_principale.grid(column=0, row=0, sticky="nsew")

        self.lbl_frame = tk.LabelFrame(self.frm_principale, text = "Information")
        self.lbl_frame.grid(column=0, row=0, sticky="nsew")

        lbl_capteur = tk.Label(self.lbl_frame, text = "Capteur:")
        lbl_capteur.grid(column=0, row=0, sticky="w")

        lbl_valeur = tk.Label(self.lbl_frame, text = "Valeur:")
        lbl_valeur.grid(column=0, row=1, sticky="w")

        lbl_unite = tk.Label(self.lbl_frame, text = "Unité:")
        lbl_unite.grid(column=0, row=2, sticky="w")

        ent_capteur = tk.Entry(self.lbl_frame)
        ent_capteur.grid(column=1, row=0, sticky="w")

        ent_valeur = tk.Entry(self.lbl_frame)
        ent_valeur.grid(column=1, row=1, sticky="w")

        ent_unite = tk.Entry(self.lbl_frame)
        ent_unite.grid(column=1, row=2, sticky="w")

        bouton = ttk.Button(self.lbl_frame, text= "enregistrer")
        bouton.grid(column=1, row=3, sticky="w")

        self.columes = ["id", "capteur", "valeur", "unite"]
        self.tableau = ttk.Treeview(self.frm_principale, columns = self.columes, show="headings")
        self.tableau.heading("id", text="ID")
        self.tableau.heading("capteur", text="Capteur")
        self.tableau.heading("valeur", text="Valeur")
        self.tableau.heading("unite", text="Unite")

        self.tableau.column("id",width=60)
        self.tableau.column("capteur",width=90)
        self.tableau.column("valeur",width=90)
        self.tableau.column("unite",width=80)

        self.tableau.grid(row=1, column=0, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()
