import unittest
from .Client import Client
from ..compte.Courant import Courant


class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client(id=1, nom="toto")
        self.compte = Courant(numCompte=12, solde=1000)


class TestGetter(TestClient):
    def test_getId(self):
        self.assertEqual(self.client.getId(), 1)

    def test_getNom(self):
        self.assertEqual(self.client.getNom(), "toto")

    def test_getEmail(self):
        self.assertIsNone(self.client.getEmail(), True)

    def test_getAdresse(self):
        self.assertIsNone(self.client.getAdresse(), True)

    def test_getTelephone(self):
        self.assertIsNone(self.client.getTelephone(), True)

    def test_getCompte(self):
        self.assertEqual(len(self.client.getCompte()), 0)


class TestSetter(TestClient):
    def test_setId(self):
        self.client.setId(2)
        self.assertEqual(self.client.id, 2)

    def test_setNom(self):
        self.client.setNom("tata")
        self.assertEqual(self.client.nom, "tata")

    def test_setEmail(self):
        self.client.setEmail("toto@gmail.com")
        self.assertEqual(self.client.email, "toto@gmail.com")

    def test_setAdresse(self):
        self.client.setAdresse("17 rue toto")
        self.assertEqual(self.client.adresse, "17 rue toto")

    def test_setTelephone(self):
        self.client.setTelephone("0606060606")
        self.assertEqual(self.client.telephone, "0606060606")

    def test_setCompte(self):
        self.client.setCompte(self.compte)
        self.assertEqual(self.client.comptes, [12])


class TestNotEqual(TestClient):
    def test_id(self):
        self.client.setId(2)
        self.assertNotEqual(self.client.id, 1)

    def test_nom(self):
        self.client.setNom("tata")
        self.assertNotEqual(self.client.nom, "tato")

    def test_email(self):
        self.client.setEmail("toto@gmail.com")
        self.assertNotEqual(self.client.email, "tot@gmail.com")

    def test_adresse(self):
        self.client.setAdresse("17 rue toto")
        self.assertNotEqual(self.client.adresse, "17 rue tot")

    def test_telephone(self):
        self.client.setTelephone("0606060606")
        self.assertNotEqual(self.client.telephone, "0606060607")
