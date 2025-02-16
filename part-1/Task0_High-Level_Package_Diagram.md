![Capture d'écran 2025-02-16 105052](https://github.com/user-attachments/assets/82742c9c-8f44-4d09-a4b4-4e6ac54ed8d4)
```
Présentation Générale
Ce diagramme représente un système structuré en trois couches principales : la couche de présentation, la couche de logique métier et la couche de persistance. Chaque couche a un rôle bien défini et communique avec les autres couches via des interfaces spécifiées.

1. Couche de Présentation (PresentationLayer)
Description : C'est l'interface utilisateur du système. Elle expose des API (Interface de Programmation d'Application) que les utilisateurs finaux utilisent pour interagir avec le système.

Composants :

UserAPI : Interface pour les opérations utilisateur (par exemple, inscription, connexion).

PlaceAPI : Interface pour les opérations liées aux lieux (par exemple, création, mise à jour, suppression de lieux).

ReviewAPI : Interface pour les opérations liées aux avis (par exemple, ajout d'avis, consultation des avis).

AmenityAPI : Interface pour les opérations liées aux commodités (par exemple, ajout de commodités, consultation des commodités).

Relation : La couche de présentation communique avec la couche de logique métier via une interface de façade (FacadeInterface), qui masque la complexité des opérations internes.

2. Couche de Logique Métier (BusinessLogicLayer)
Description : C'est le cœur fonctionnel du système où se trouvent les règles métier et la logique de traitement.

Composants :

User : Entité représentant les utilisateurs.

Place : Entité représentant les lieux.

Review : Entité représentant les avis.

Amenity : Entité représentant les commodités.

UserService : Service gérant les opérations liées aux utilisateurs.

PlaceService : Service gérant les opérations liées aux lieux.

ReviewService : Service gérant les opérations liées aux avis.

AmenityService : Service gérant les opérations liées aux commodités.

Relation : La couche de logique métier communique avec la couche de persistance pour effectuer des opérations de base de données (Database Operations).

3. Couche de Persistance (PersistenceLayer)
Description : C'est la couche responsable de l'accès aux données et de leur stockage.

Composants :

DatabaseAccess : Interface pour accéder à la base de données.

Méthodes readData() et writeData() : Pour lire et écrire les données dans la base de données.

Relation : La couche de persistance fournit des opérations de base de données à la couche de logique métier.

Relations entre les Couches
Couche de Présentation à Couche de Logique Métier : Utilise une interface de façade pour simplifier les appels aux services de la logique métier.

Couche de Logique Métier à Couche de Persistance : Effectue des opérations de lecture et d'écriture dans la base de données via la couche de persistance.
```
