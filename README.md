# Interface

## Introduction

Bienvenue dans la documentation de l'interface de notre application de surveillance. Cette interface permet de visualiser et interagir avec les données collectées par l'Agent. Ce document fournit des informations complètes pour comprendre, installer et utiliser l'interface.

## Fonctionnalités

L'interface offre un ensemble complet de fonctionnalités pour faciliter la gestion et la visualisation des données de surveillance. Les principales fonctionnalités incluent :

- Navigation intuitive sur les tableaux de bord.
- Ajout dynamique de serveurs.
- Vue intégrée de la santé des serveurs surveillés.
- Graphiques historiques pour les métriques clés (CPU, RAM, etc.).

## Architecture

L'architecture de l'interface est conçue pour assurer une expérience utilisateur fluide. Elle interagit avec l'Agent via une API pour récupérer et afficher les données de surveillance. La structure modulaire permet une extensibilité facile pour l'ajout de nouvelles fonctionnalités et l'accés sur d'autre serveur.

## Installation

Pour installer l'interface sur votre ordinateur, suivez ces étapes :

1. Connectez-vous au docker de l'école Télécom Saint-Etienne : docker login devops.telecomste.fr:5050
2. Récupérez l'image du docker : docker pull devops.telecomste.fr:5050/printerfaceadmin/2023-24/group1/interface/mon_app:main
3. Lancez le conteneur de cette image : docker run -d devops.telecomste.fr:5050/printerfaceadmin/2023-24/group1/interface/mon_app:main 
4. Accédez au site WEB via l'adresse IP suivante : http://127.0.0.1:5000

## Utilisation

Une fois installée, l'interface peut être utilisée en suivant ces directives :

- Accédez à l'URL spécifique où l'interface est déployée.
- Utilisez les fonctionnalités intégrées pour explorer les différents tableaux de bord.
- Ajoutez des serveurs selon vos besoins.

L'ajout de serveur se fait via l'URL complet du serveur, sous la forme : "http://utilisateur.nom\_de\_domaine:PORT/"

## Configuration

La configuration de l'interface peut être ajustée en modifiant les paramètres appropriés. Ces paramètres peuvent inclure des éléments tels que les préférences d'affichage, etc. Consultez la documentation détaillée pour obtenir des instructions sur la configuration.

## Fonctionnalités manquantes

Les fonctionnalités permettant de récupérer les logs, le nombre d'erreur 404 et les 5 derniers messages d'erreur ne fonctionnent pas. 
Cependant, si vous vous rendez sur 127.0.0.1:5000/server/server_id/graph/dataLogs, vous pourrez voir les données qui sont supposées être juste pour la récupération des logs et du nombre d'erreur 404.

## Contribuer

Si vous souhaitez contribuer au développement de l'interface, suivez ces étapes :

1. Clonez le dépôt sur votre machine.
2. Explorez le code source et identifiez les zones où vous souhaitez contribuer.
3. Suivez les instructions spécifiques dans la section "Contribuer" du README de l'Agent pour soumettre des modifications.

## Licence

Ce projet est publié sous Apache License 2.0

---

