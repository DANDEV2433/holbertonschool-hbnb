# Documentation Technique du Projet HBnB

## Introduction

Ce document technique décrit l'architecture et le fonctionnement du projet HBnB. Il inclut une vue d'ensemble de l'architecture du projet, une explication détaillée de la couche logique métier et les interactions entre les composants via des diagrammes de séquence des appels API. L'objectif est de fournir une référence claire et structurée pour le développement et la mise en œuvre du projet.

## Architecture de Haut Niveau

Le projet HBnB est organisé en trois couches principales :

- **Presentation Layer (Couche de Présentation)** : Elle fournit les interfaces utilisateur et expose les API.
- **Business Logic Layer (Couche Logique Métier)** : Elle contient les entités principales et la logique métier associée.
- **Persistence Layer (Couche de Persistance)** : Elle gère l'accès et la manipulation des données dans la base de données.

### Diagramme de l'Architecture de Haut Niveau

```mermaid
classDiagram
class PresentationLayer {
<<Interface>>
+UserAPI
+PlaceAPI
+ReviewAPI
+AmenityAPI
}
class BusinessLogicLayer {
+User
+Place
+Review
+Amenity
+UserService
+PlaceService
+ReviewService
+AmenityService
}
class PersistenceLayer {
-DatabaseAccess
-readData()
-writeData()
}
PresentationLayer --> BusinessLogicLayer : FacadeInterface
BusinessLogicLayer --> PersistenceLayer : Database Operations
```

## Couche Logique Métier

La couche logique métier contient les principales entités utilisées dans le projet HBnB : `User`, `Place`, `Review`, et `Amenity`. Chaque entité a des attributs et méthodes spécifiques qui assurent la gestion des opérations métier.

### Diagramme de Classes de la Couche Logique Métier

```mermaid
classDiagram
direction TB
    class User {
        -uuid : str
        +firstname : str
        +lastname : str
        +email : str
        -admin : bool
        -password : str
        +date_of_creation : int
        +date_of_update : int
        register()
        login()
        logout()
        delete()
        get_date_of_creation()
        get_date_of_update()
    }
    class Review {
        -uuid : str
        +user : str
        +place : str
        +rating : int
        +comment : str
        +date_of_review : int
        +date_of_update : int
        write_review()
        delete()
        edit()
        get_reviews_by_place()
        get_reviews_by_user()
        get_date_of_review()
        get_date_of_creation()
    }
    class Place {
        - uuid : str
        +title : str
        +latitude : str
        +longitude : str
        +price : int
        +owner : str
        +description : str
        +average_rating : int
        +aminities : str
        +date_of_creation : int
        +date_of_update : int
        create_place()
        update_place()
        delete_place()
        get_available_dates()
        calculate_price()
        claculate_average_rating()
        get_amenities()
        add_amenity()
        remove_amenity()
        get_date_of_creation()
        get_date_of_update()
    }
    class Amenity {
        -uuid : str
        +name : str
        +description : str
        +date_of_creation : int
        +date_of_update : int
        create_amenity()
        update_amenity()
        delete_amenity()
        get_all_amenity()
        get_date_of_creation()
        get_date_of_update()
    }
    User --> Review
    Review --|> Place
    Review --|> User
    User --> Place
    Amenity *-- Place
```

## Flux d'Interaction des API

### Enregistrement d'un Utilisateur

```mermaid
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

### Création d'un Lieu

```mermaid
sequenceDiagram
    participant User
    participant API
    participant AuthService
    participant PlaceService
    participant Database
    User->>API: login(username, password)
    API->>AuthService: validateCredentials(username, password)
    AuthService-->>API: token/JWT
    API-->>User: token/JWT
    User->>API: createPlace(token, title, latitude, longitude, price, owner, description, amenities)
    API->>AuthService: validateToken(token)
    alt Token valid
        AuthService-->>API: success
        API->>PlaceService: validatePlaceData(title, latitude, longitude, price, owner, description, amenities)
        alt Place data valid
            PlaceService-->>API: success
            API->>PlaceService: createPlace(title, latitude, longitude, price, owner, description, amenities)
            PlaceService->>Database: insertPlaceData
            Database-->>PlaceService: uuid
            PlaceService-->>API: success, uuid
            API-->>User: success, uuid
        else Place data invalid
            PlaceService-->>API: failure, validation_errors
            API-->>User: failure, validation_errors
        end
    else Token invalid
        AuthService-->>API: failure, token_errors
        API-->>User: failure, token_errors
    end
```

### Soumission d'un Avis

```mermaid
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

## Conclusion

Ce document présente une vue complète de l'architecture du projet HBnB, détaillant la structure en couches, la logique métier et les interactions API essentielles. Il servira de guide de référence pour les développeurs travaillant sur l'implémentation du projet.

