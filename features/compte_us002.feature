# Created by Amine at 09-Mar-21
@sequential
Feature: US_002 Débiter un compte
  En tant que detenteur d'un compte bancaire
  Je veux pouvoir débiter mon compte en retirant une somme d'argent prédéfinie.

  Scenario Outline: calcul du nouveau solde après retrait
    Given le compte <numCompte> avec le solde <solde>
    When le client retire la somme <montant>
    Then son nouveau solde <newSolde> après retrait sera automatiquement calculé
    Examples:
      |numCompte| solde | montant | newSolde  |
      | 325698  | 200   | 100     | 100       |
      | 123456  | 250   | 50      | 200       |

    Scenario Outline:  refus: le type du montant non valide
      Given le compte <numCompte> avec le solde <solde> de type text
      When le client retire la somme <montant>
      Then le système refuse la transaction avec le message de type "<errorName>"
      Examples:
        |numCompte| solde | montant | errorName |
        | 325698  | 500   | "120"  | TypeError |

    Scenario Outline:  refus: compte débiteur
      Given le compte <numCompte> avec le solde <solde>
      When le client retire la somme <montant>
      Then le système refuse la transaction avec le message "<errorName>"
      Examples:
        |numCompte| solde | montant | errorName |
        | 325698  | 500   | 1000  | Account balance is Null |