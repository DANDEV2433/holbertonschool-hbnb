## Sequence diagram for API calls

### 1.User Registration Diagram
![Capture d'écran diagram task 1User Registration Diagram](https://s10.aconvert.com/convert/p3r68-cdx67/a1wz1-22g5i.png)
```
sequenceDiagram
    participant Utilisateur
    participant API
    participant ServiceUtilisateur
    participant BaseDeDonnées

    Utilisateur->>API: Demande d'enregistrement (nom, email, mdp)
    API->>ServiceUtilisateur: Vérifier et créer l'utilisateur
    ServiceUtilisateur->>BaseDeDonnées: Vérifier si l'email existe
    BaseDeDonnées-->>ServiceUtilisateur: Email disponible
    ServiceUtilisateur->>BaseDeDonnées: Enregistrer l'utilisateur
    BaseDeDonnées-->>ServiceUtilisateur: Confirmation d'enregistrement
    ServiceUtilisateur-->>API: Succès (ID utilisateur)
    API-->>Utilisateur: Confirmation d'inscription
```

### Description Détailée du Diagramme
Le processus d’enregistrement d’un utilisateur suit une séquence bien définie pour assurer la validation et la création sécurisée d’un compte. 
Tout commence lorsque l’utilisateur envoie une requête d’inscription à l’API, en fournissant ses informations personnelles telles que son nom, son adresse email et son mot de passe. 
L’API transmet ensuite cette requête au service de gestion des utilisateurs, qui est chargé d’effectuer les vérifications nécessaires avant de procéder à la création du compte.

Tout d’abord, le service utilisateur interroge la base de données afin de vérifier si l’adresse email fournie existe déjà. 
Si l’email est déjà utilisé, une réponse d’erreur est renvoyée à l’API, qui informe l’utilisateur que l’inscription ne peut pas aboutir. 
En revanche, si l’email est disponible, le service utilisateur procède à l’enregistrement du nouvel utilisateur en cryptant son mot de passe pour des raisons de sécurité, puis en sauvegardant les informations dans la base de données.
Une fois l’inscription réussie, la base de données envoie une confirmation au service utilisateur, qui retourne à son tour une réponse contenant l’identifiant unique du nouvel utilisateur.
L’API envoie alors un message de confirmation à l’utilisateur pour lui indiquer que son compte a bien été créé.


### 2.Place Creation Diagram
![Capture d'écran 2025-02-16 181134](https://github.com/user-attachments/assets/452854b6-19e5-4f52-b42a-248e5730df2c)
![Capture d'écran 2025-02-16 181207](https://github.com/user-attachments/assets/c9fc5dcb-0857-4fb9-a585-a03720b6c1c3)

### Description Détailée du Diagramme
Processus de Connexion

User envoie une requête de connexion à l'API avec les informations d'identification (username et password).

API transfère ces informations à AuthService pour validation.

AuthService vérifie les informations d'identification :

Si elles sont valides, AuthService génère un token JWT et le renvoie à l'API.

Si elles ne sont pas valides, AuthService renvoie une réponse d'échec.

API transmet le token JWT au User en cas de succès, ou un message d'erreur en cas d'échec.

Création de Place avec Authentification JWT

User envoie une requête à l'API pour créer une place, en incluant le token JWT dans les en-têtes de la requête et les détails de la place (title, latitude, longitude, price, owner, description, amenities).

API extrait le token JWT et le transmet à AuthService pour validation.

AuthService vérifie le token JWT :

Si le token est valide, AuthService renvoie une réponse de succès à l'API.

Si le token est invalide, AuthService renvoie une réponse d'échec.

API vérifie la réponse de validation du token :

Si le token est valide, l'API procède à la validation des données de la place.

Si le token est invalide, l'API renvoie une réponse d'échec au User avec les erreurs liées au token.

Validation des Données de la Place

Si le token JWT est valide, l'API envoie les données de la place à PlaceService pour validation.

PlaceService vérifie les données de la place :

Si les données sont valides, PlaceService renvoie une réponse de succès à l'API.

Si les données sont invalides, PlaceService renvoie une réponse d'échec avec les erreurs de validation.

Insertion des Données de la Place

Si les données de la place sont valides, l'API envoie une demande à PlaceService pour créer la place avec les détails fournis.

PlaceService insère les données de la place dans la Database.

La Database confirme la création de la place et renvoie un identifiant unique (uuid) à PlaceService.

PlaceService renvoie une réponse de succès à l'API avec l'uuid de la place créée.

API transmet la réponse de succès au User avec l'uuid.

### 3.Review Submission Diagram
![Screenshot 2025-02-16 110756](https://github.com/user-attachments/assets/18856d1d-f3c0-46b8-aa3d-e4298930ff5c)
```
sequenceDiagram
    participant User
    participant Frontend
    participant ReviewService
    participant Database

    User->>Frontend: Submit Review (rating, comment, place_id)
    Frontend->>ReviewService: API Request (POST /reviews)
    ReviewService->>Database: Validate place_id and user_id
    Database-->>ReviewService: Validation Success
    ReviewService->>Database: Insert Review (rating, comment, place_id, user_id)
    Database-->>ReviewService: Review Stored
    ReviewService->>Frontend: Response (201 Created, Review ID)
    Frontend-->>User: Review Submitted Successfully
```
### Description Détailée du Diagramme
L'utilisateur saisit un avis sur un lieu via l’interface utilisateur.
L’application (Frontend) reçoit la demande et la prépare pour l’envoi au serveur via l’API.
Le frontend envoie une requête HTTP POST à l’API du ReviewService avec les données de l’avis.
Le Frontend agit comme un intermédiaire entre l’utilisateur et le backend.
Il envoie une requête au ReviewService pour traiter la soumission de l’avis.
Avant d'insérer l'avis, le ReviewService doit vérifier que l'ID du lieu (place_id) existe bien dans la base, et que l'ID de l’utilisateur (user_id) est valide.
Ensuite, la base de données confirme au ReviewService que le lieu existe (place_id valide), et que l'utilisateur existe (user_id valide).
Après validation, le ReviewService insère l'avis avec la note (rating), le commentaire (comment), l'ID du lieu (place_id) et l'ID de l'utilisateur (user_id).
La base de données confirme au ReviewService que l’avis a bien été enregistré.
Le ReviewService envoie une réponse HTTP 201 Created au Frontend.
Le Frontend informe l’utilisateur que l’avis a bien été soumis.


### 4.Fetching a List of Places
![Screenshot Fetching a List of Places](https://s10.aconvert.com/convert/p3r68-cdx67/axot0-c9d4s.png)
```
sequenceDiagram
    participant Utilisateur
    participant API
    participant LogiqueMétier
    participant BaseDeDonnées
    Utilisateur->>API: GET /places?ville=Bordeaux&prix_max=100
    API->>LogiqueMétier: Appliquer les filtres et valider la requête
    LogiqueMétier->>BaseDeDonnées: Rechercher les lieux correspondants
    BaseDeDonnées-->>LogiqueMétier: Retourner la liste des lieux
    alt Aucun lieu trouvé
        LogiqueMétier-->>API: Retourner liste vide
        API-->>Utilisateur: 200 OK ([])
    else
        LogiqueMétier-->>API: Formatter les résultats
        API-->>Utilisateur: 200 OK (Liste des lieux)
    end
```
### Description Détailée du Diagramme
Fetching a List of Places

Le diagramme de séquence Fetching a List of Places décrit le processus par lequel un utilisateur envoie une requête pour obtenir une liste de lieux selon certains critères par exemple la ville le prix... 
L’API reçoit la requête et la transmet à la couche de logique métier, qui applique les filtres et interroge la base de données.
Si des lieux correspondent, ils sont retournés à l’utilisateur sous forme de liste.
Sinon, une réponse vide est envoyée.

