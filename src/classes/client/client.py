

class Client(object):

    def __init__(self, id, nom):
        self.id = id
        self.nom = nom
        self.email = None
        self.adresse = None
        self.telephone = None
        self.comptes = []

    def getId(self):
        return self.__getattribute__("id")

    def setId(self, value):
        self.__setattr__("id", value)

    def getNom(self):
        return self.__getattribute__("nom")

    def setNom(self, value):
        self.__setattr__("nom", value)

    def getEmail(self):
        return self.__getattribute__("email")

    def setEmail(self, value):
        self.__setattr__("email", value)

    def getAdresse(self):
        return self.__getattribute__("adresse")

    def setAdresse(self, value):
        self.__setattr__("adresse", value)

    def getTelephone(self):
        return self.__getattribute__("telephone")

    def setTelephone(self, value):
        self.__setattr__("telephone", value)

    def setComptes(self, listComptes):
        self.comptes.extend(listComptes)

    def getComptes(self):
        return self.comptes
