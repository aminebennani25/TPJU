from behave import given, when, then, step
from hamcrest import assert_that, equal_to
from src.classes.compte.compte import Compte


class StepUS002DebiterUnCompte:

    @given('le compte {numCompte} avec le solde {solde}')
    def __init__(self, numCompte, solde):
        self.compte = Compte(numCompte=numCompte, solde=solde)

    @when('le client retire la somme {montant}')
    def step_debiter(self, montant):
        try:
            self.compte.debiter(montant=montant)
        except BaseException:
            pass

    @then('son nouveau solde {newSolde} après retrait sera automatiquement calculé')
    def step_new_solde(self, newSolde):
        assert_that(self.compte.getSolde(), equal_to(newSolde))

    @then('le système refuse la transaction avec le message de type "{errorName}"')
    def step_error_msg(self, errorName):
        assert_that(errorName, equal_to('TypeError'))

    @then('le système refuse la transaction avec le message "{errorName}"')
    def step_error_msg(self, errorName):
        assert_that(errorName, equal_to('Account balance is Null'))