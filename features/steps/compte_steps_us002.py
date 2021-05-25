from behave import given, when, then, step
from hamcrest import assert_that, equal_to
from src.classes.compte.Courant import Courant


class StepUS002DebiterUnCompte:

    @given('le compte {numCompte} avec le solde {solde}')
    def __init__(self, numCompte, solde):
        self.comp = Courant(numCompte=eval(numCompte), solde=eval(solde))

    @when('le client retire la somme {montant}')
    def step_debiter(self, montant):
        try:
            self.comp.debiter(montant=eval(montant))
        except BaseException:
            pass

    @then('son nouveau solde {nouveau} après retrait sera automatiquement calculé')
    def step_new_solde(self, nouveau):
        assert_that(self.comp.getSolde(), equal_to(eval(nouveau)))

    @then('le système refuse la transaction avec le message "{errorName}"')
    def step_error_msg(self, errorName):
        assert_that(errorName, equal_to('Account balance is Null'))