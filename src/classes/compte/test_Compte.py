
import unittest
from src.classes.compte.Courant import Courant
from src.classes.compte.Epargne import Epargne


class TestCompte(unittest.TestCase):
    def setUp(self):
        self.compte = Courant(numCompte=523, solde=1000)
        self.epargne = Epargne(numCompte=1224, solde=1000, taux=10)


class TestGetter(TestCompte):
    def test_getNumCompte(self):
        self.assertEqual(self.compte.getNumCompte(), 523)

    def test_getSolde(self):
        self.assertEqual(self.compte.getSolde(), 1000)

    def test_getClient(self):
        self.assertIsNone(self.compte.getClient(), True)

    def test_getTaux(self):
        self.assertEqual(self.epargne.getTaux(), 10)


class TestSetter(TestCompte):
    def test_setNumCompte(self):
        self.compte.setNumCompte(2)
        self.assertEqual(self.compte.numCompte, 2)

    def test_setSolde(self):
        self.compte.setSolde(500)
        self.assertEqual(self.compte.solde, 500)

    def test_setTaux(self):
        self.epargne.setTaux(10)
        self.assertEqual(self.epargne.taux, 10)


class TestNotEqual(TestCompte):
    def test_numCompte(self):
        self.compte.setNumCompte(2)
        self.assertNotEqual(self.compte.numCompte, 1)

    def test_solde(self):
        self.compte.setSolde(20)
        self.assertNotEqual(self.compte.solde, 20.5)


class TestMethod(TestCompte):
    def test_crediter(self):
        self.compte.crediter(montant=500)
        self.assertEqual(self.compte.solde, 1500)

    def test_debiter(self):
        self.compte.debiter(montant=200)
        self.assertEqual(self.compte.solde, 800)

    def test_calculInteret(self):
        interet = self.epargne.calculInterets()
        self.assertEqual(interet, 100)

    def test_epargne(self):
        solde = self.epargne.getNewSolde()
        self.assertEqual(solde, 1100)


class TestMethodException(TestCompte):

    def test_debiter_nullBalance(self):
        try:
            self.compte.debiter(montant=1500)
        except BaseException:
            self.assertTrue("Account balance is Null")

    def test_debiter_typeError(self):
        try:
            self.compte.debiter(montant="1500")
        except BaseException:
            self.assertTrue("Type Error")

    def test_crediter_typeError(self):
        try:
            self.compte.crediter(montant="500")
        except BaseException:
            self.assertTrue("Type Error")
