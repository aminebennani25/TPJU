from src.classes.compte.Courant import Courant
from src.classes.compte.Epargne import Epargne
from src.classes.client.Client import Client

if __name__ == "__main__":
    cl = Client(id=1, nom="Amine")

    c = Courant(numCompte=12, solde=100)
    cl.setCompte(c)

    c.debiter(20)
    c.crediter(500)

    e = Epargne(numCompte=13, solde=1000, taux=7)
    cl.setCompte(e)
    e.GetNewSolde()

    comptes = cl.getCompte()
    print("Compte du client: ", cl.getNom())
    print("mes comptes: ", comptes)

    print("Compte Courant: n°{} - solde: {}".format(c.getNumCompte(), c.getSolde()))
    print("Compte Epargne n°{} - solde: {}".format(e.getNumCompte(), e.getSolde()))
