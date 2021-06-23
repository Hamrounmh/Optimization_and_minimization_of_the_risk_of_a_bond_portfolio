# Minimisation-de-la-Conditional-Value-at-risk
This project involves the implementation of several financial models in Python in order to optimize and minimize the risk of an asset portfolio. by following the Markowitz model and optimizing Value at Risk and CVaR.

# Objectif : 

- 1 .Notre objectif consiste à implémenter la méthode treillis sur python. Cette méthode permet de calculer les prix des options CALL et PUT européennes et américaines selon le prix de l’actif à t=0, la période (en semaines), le taux annuel convertis, le strike K, et les taux d’augmentation où diminution d'un actif (Up et Down).
Ensuite tester la méthode sur différentes instances en faisant varier les paramètres n (le nombre de périodes), r (le taux), D et U. On essayera de considérer aussi des instances assez larges
- 2 . Optimisation du portfeuille et minimisation de la Cvar.

# Resultats : 
-1 . J'ai réalisé une méthode en python permettant de calculer les prix des options. J’ai réalisé ensuite une interface graphique qui adapte ma méthode python, et qui a pour but de faciliter la saisie et l’affichage du prix de l’option. Cette interface affiche également l’arborescence des variations des prix pour toutes les périodes t.
Ensuite, j’ai étudié le comportement des option européenne et américaine en variant les données. J’ai modélisé ces variations en graphes pour faciliter la compréhension du comportement des options.

2. Optimiser le risque d’un portefeuille repose sur la résolution des modèles de minimisation de risque, notamment sur les modèles de minimisation de la CVaR. Pour la résolution, j’ai utilisé l’outil Cplex de IBM que j’ai trouvé disponible sur internet pour les étudiants avec un nombre de contraintes illimitées.
Pour cette 2e partie, j’ai construit un portefeuille avec des actifs réels qui sont : S&P qui est un indice boursier basé sur plusieurs entreprises, Gov Bond qui sont des emprunts d’état, et Small cap qui est une société dans le domaine de la bourse.
Je vais commencer par construire un portefeuille Markowitz. Ce portefeuille doit me garantir en rendement R. J'ai comme données la matrice de covariance et les espérances de rendements des 3 actifs. Ce portefeuille va m’aider à bien comprendre les liens et les différences entre un portefeuille avec une variance minimale et un portefeuille avec un risque minimal.
Je vais ensuite, trouver un portefeuille avec un rendement égale à celui de Markowitz et calculer le VaR et la CVaR de ce portefeuille en utilisant les méthodes du cours que j'ai programmé en python. Ensuite, on va passer au modèle de minimisation de la CVaR en générant des simulations sur les prix des actifs. Puis à la comparaison des 2 portefeuilles avant et après la minimisation.
Enfin, on passera au modèle de maximisation du rendement du portefeuille en respectant un certain seuil de risque.
Avant d’entamer la résolution des modèles, je vais expliquer mes méthodes python que j'ai implémenté pour calculer la VaR et la CVaR d’un portefeuille sans minimisation, simuler les scénarios des actifs, et les différents tests effectués avec ses simulations.

# Technologies : 
- Python 
- Cplex Optimize
