from behave import given, when, then, step
from hamcrest import assert_that, equal_to
from src.classes.compte.Epargne import Epargne


class StepUS003CompteEpargne:

    @given('le compte epargne de num {numCompte} et de solde {solde} fructufié au taux {taux}')
    def __init__(self, numCompte, solde, taux):
        self.epargne = Epargne(numCompte=eval(
            numCompte), solde=eval(solde), taux=eval(taux))

    @when('le client souhaite visualiser son nouveau solde après 1 an')
    def step_inter(self):
        pass

    @then('son nouveau solde {nouveau} sera automatiquement calculé')
    def step_new_epargne(self, nouveau):
        assert_that(self.epargne.getNewSolde(), equal_to(eval(nouveau)))
