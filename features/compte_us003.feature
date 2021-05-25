# Created by Amine at 09-Mar-21
@sequential
Feature: US_003 Compte Epargne
  En tant que detenteur que client
  Je souhaite consulter mon compte  afin de connaitre mon epargne cummulé.

  Scenario Outline: calcul du nouveau solde d'epargne
    Given le compte epargne de num <numCompte> et de solde <solde> fructufié au taux <taux>
    When le client souhaite visualiser son nouveau solde après 1 an
    Then son nouveau solde <nouveau> sera automatiquement calculé
    Examples:
      |numCompte| solde | taux   |  nouveau  |
      | 325698  | 200   | 5      |   210     |
      | 123456  | 1000  | 10     |   1100    |