from abc import ABCMeta, abstractmethod


class Compte(object, metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, numCompte: int, solde: int):
        self.numCompte = numCompte
        self.solde = solde
        self.client = None

    def __str__(self):
        return str(self.numCompte)

    def getNumCompte(self) -> int:
        return self.__getattribute__("numCompte")

    def setNumCompte(self, value: int):
        self.__setattr__("numCompte", value)

    def getSolde(self) -> int:
        return self.__getattribute__("solde")

    def setSolde(self, value: int) -> int:
        self.__setattr__("solde", value)

    def setClient(self, client):
        self.client = client

    def getClient(self):
        return self.client

    @abstractmethod
    def debiter(self, montant: int):
        pass

    @abstractmethod
    def crediter(self, montant: int):
        pass

