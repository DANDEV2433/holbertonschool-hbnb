## Sequence diagram for API calls

### 1.User Registration Diagram


### 2.Place Creation Diagram
![Capture d'écran 2025-02-16 181134](https://github.com/user-attachments/assets/452854b6-19e5-4f52-b42a-248e5730df2c)
![Capture d'écran 2025-02-16 181207](https://github.com/user-attachments/assets/c9fc5dcb-0857-4fb9-a585-a03720b6c1c3)
```
Description Détailée du Diagramme
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

```
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
### 4.Fetching a List of Places
