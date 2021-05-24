from typing import List
from ..compte.Compte import Compte


class Client(object):

    def __init__(self, id: int, nom: str):
        self.id: int = id
        self.nom: str = nom
        self.email: str = None
        self.adresse: str = None
        self.telephone: int = None
        self.comptes: List[Compte] = []

    def __str__(self):
        return str((self.id, self.nom))

    def getId(self) -> int:
        return self.__getattribute__("id")

    def setId(self, value: int):
        self.__setattr__("id", value)

    def getNom(self) -> str:
        return self.__getattribute__("nom")

    def setNom(self, value: str):
        self.__setattr__("nom", value)

    def getEmail(self) -> str:
        return self.__getattribute__("email")

    def setEmail(self, value: str):
        self.__setattr__("email", value)

    def getAdresse(self) -> str:
        return self.__getattribute__("adresse")

    def setAdresse(self, value: str):
        self.__setattr__("adresse", value)

    def getTelephone(self) -> int:
        return self.__getattribute__("telephone")

    def setTelephone(self, value: int):
        self.__setattr__("telephone", value)

    def setCompte(self, comptes: List[Compte]):
        if isinstance(comptes, list):
            for compte in comptes:
                self.comptes.append(compte.numCompte)
        else:
            self.comptes.append(comptes.numCompte)

    def getCompte(self) -> List[Compte]:
        return self.comptes
