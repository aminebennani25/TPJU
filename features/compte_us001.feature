@sequential
Feature: US_001 Créditer un compte
  En tant que detenteur d'un compte bancaire
  Je veux pouvoir créditer mon compte en versant une somme d'argent prédéfinie.

  Scenario Outline: calcul du nouveau solde
    Given un compte <numCompte> avec un solde <solde>
    When le client verse la somme <montant>
    Then le nouveau solde <newSolde> sera automatiquement calculé
    Examples:
      |numCompte| solde | montant | newSolde  |
      | 325698  | 100   | 1000    | 1100      |
      | 123456  | 150   | 1000    | 1150      |

    Scenario Outline:  refus: type du montant non valide
      Given un compte <numCompte> avec un solde <solde> de type text
      When le client verse la somme <montant>
      Then le système refuse la transaction avec le "<errorName>"
      Examples:
        |numCompte| solde | montant | errorName |
        | 325698  | 100   | "1000"  | TypeError |

