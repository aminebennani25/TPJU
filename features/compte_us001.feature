@sequential
Feature: US_001 Créditer un compte
  En tant que detenteur d'un compte bancaire
  Je veux pouvoir verser de l'argent afin de pouvoir créditer mon compte.

  Scenario Outline: calcul du nouveau solde
    Given un compte <numCompte> avec un solde <solde>
    When le client verse la somme <montant>
    Then le nouveau solde <newSolde> sera automatiquement calculé
    Examples:
      |numCompte| solde | montant | newSolde  |
      | 325698  | 100   | 1000    | 1100      |
      | 123456  | 100   | 2000    | 2100      |
