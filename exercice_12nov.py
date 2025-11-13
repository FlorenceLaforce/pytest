import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Exercice 12 Nov")
        self.geometry("800x600")

        #self.type_statut = tk.StringVar(value="Achat")
        self.creer_widget()



    def creer_widget(self):

        #frame
        self.frame = tk.Frame(self)
        self.frame.grid(column=0, row=0)

        self.lbl_frame = tk.LabelFrame(self.frame, text="Fiche Article")
        self.lbl_frame.grid(column=0, row=0, padx=10, pady=10)

        self.lbl_frame2 = tk.LabelFrame(self.lbl_frame, text="Outils de gestion")
        self.lbl_frame2.grid(column=0, row=5, columnspan=2, sticky="nsew", padx=10, pady=10)

        #label
        statut = tk.Label(self.lbl_frame, text="Statut")
        statut.grid(column=0, row=0, sticky="w", padx=10, pady=10)

        ISBN = tk.Label(self.lbl_frame, text="ISBN")
        ISBN.grid(column=0, row=1, sticky="w", padx=10, pady=10)

        Titre = tk.Label(self.lbl_frame, text="Titre")
        Titre.grid(column=0, row=2, sticky="w")

        Auteur = tk.Label(self.lbl_frame, text="Auteur")
        Auteur.grid(column=0, row=3, sticky="w")

        self.quantite_stock = tk.Label(self.lbl_frame, text="Quantité Achat")
        self.quantite_stock.grid(column=0, row=4, sticky="w")

        self.quantite_stock1 = tk.Label(self.lbl_frame, text="Quantité vendu")
        self.quantite_stock1.grid(column=0, row=4, sticky="w")

        #entry

        options = ["Achat", "Vente"]
        self.ent_statut = ttk.Combobox(self.lbl_frame, values=options, state="readonly", width=11)
        self.ent_statut.grid(column=1, row=0, sticky="e", padx=10, pady=10)
        self.ent_statut.set("Achat")

        ent_ISBN = tk.Entry(self.lbl_frame, width=14)
        ent_ISBN.grid(column=1, row=1, sticky="e", padx=10, pady=10)

        ent_Titre = tk.Entry(self.lbl_frame, width=14)
        ent_Titre.grid(column=1, row=2, sticky="e", padx=10, pady=10)

        ent_Auteur = tk.Entry(self.lbl_frame, width=14)
        ent_Auteur.grid(column=1, row=3, sticky="e",padx=10, pady=10)

        self.ent_quantite_stock = tk.Entry(self.lbl_frame, width=14)
        self.ent_quantite_stock.grid(column=1, row=4, sticky="e",padx=10, pady=10)

        self.ent_quantite_stock1 = tk.Entry(self.lbl_frame, width=14)
        self.ent_quantite_stock1.grid(column=1, row=4, sticky="e",padx=10, pady=10)

        #boutons

        ajouter = ttk.Button(self.lbl_frame2, text="Ajouter")
        ajouter.grid(column=0, row=0, sticky="nsew")

        supprimer = ttk.Button(self.lbl_frame2, text="Supprimer")
        supprimer.grid(column=0, row=1, sticky="nsew")

        modifier = ttk.Button(self.lbl_frame2, text="Modifier")
        modifier.grid(column=1, row=0, sticky="nsew")

        quitter = ttk.Button(self.lbl_frame2, text="Quitter")
        quitter.grid(column=1, row=1, sticky="nsew")

        #tableau

        self.columns = ("id", "isbn", "title", "author", "quantite")
        self.tableau = ttk.Treeview(self.frame, columns=self.columns, show="headings")
        self.tableau.heading("id", text="ID")
        self.tableau.heading("isbn", text="ISBN")
        self.tableau.heading("title", text="Titre")
        self.tableau.heading("author", text="Auteur")
        self.tableau.heading("quantite", text="Quantité")

        self.tableau.column("id", width=60)
        self.tableau.column("isbn", width=80)
        self.tableau.column("title",  width=110)
        self.tableau.column("author",  width=110)
        self.tableau.column("quantite", width=80)

        self.tableau.grid(column=1, row=0, sticky="w")

        self.ent_statut.bind("<<ComboboxSelected>>", self.changer_statut)

    def changer_statut(self, event=None):
        self.update_champs()


    def update_champs(self):
        if self.ent_statut.get() == "Achat":
            self.quantite_stock.grid()
            self.ent_quantite_stock.grid()
            self.quantite_stock1.grid_remove()
            self.ent_quantite_stock1.grid_remove()
        else:
            self.quantite_stock.grid_remove()
            self.ent_quantite_stock.grid_remove()
            self.quantite_stock1.grid()
            self.ent_quantite_stock1.grid()








if __name__ == "__main__":
    app = App()
    app.mainloop()





