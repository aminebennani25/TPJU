from behave import given, when, then, step
from hamcrest import assert_that, equal_to
from src.classes.compte.Courant import Courant


class StepUS001CrediterUnCompte:

    @given('un compte {numCompte} avec un solde {solde}')
    def __init__(self, numCompte, solde):
        self.compte = Courant(numCompte=eval(numCompte), solde=eval(solde))

    @when('le client verse la somme {montant}')
    def step_crediter(self, montant):
        try:
            self.compte.crediter(montant=eval(montant))
        except BaseException:
            pass

    @then('le nouveau solde {newSolde} sera automatiquement calculé')
    def step_new_solde(self, newSolde):
        assert_that(self.compte.getSolde(), equal_to(eval(newSolde)))
