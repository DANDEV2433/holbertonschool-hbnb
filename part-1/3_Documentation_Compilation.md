# **HBnB Technical Documentation**

## **1. Introduction**

### **Purpose of the Document**

This document provides a comprehensive technical overview of the HBnB project, detailing its architecture, business logic, and API interactions. It serves as a reference for developers and stakeholders to understand the system design and facilitate its implementation.

### **Scope**

The HBnB project is a platform where users can register, log in, create places, write reviews, and search for accommodations based on filters. This document covers:

- The **high-level architecture** of the application.
- The **detailed class diagram** for the Business Logic Layer.
- The **sequence diagrams** illustrating key API interactions.

---

## **2. High-Level Architecture**

### **Layered Architecture Overview**

The system follows a three-layer architecture:

1. **Presentation Layer** (Frontend): Handles user interactions and API requests.
2. **Business Logic Layer** (Backend Services): Processes data and enforces business rules.
3. **Persistence Layer** (Database): Stores and retrieves application data.

### **High-Level Package Diagram**

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

**Explanation:**

- The **Presentation Layer** interacts with users through APIs.
- The **Business Logic Layer** processes and validates data before interacting with the database.
- The **Persistence Layer** manages data storage and retrieval operations.

---

## **3. Business Logic Layer**

### **Class Diagram for Core Entities**

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

**Explanation:**

- **User** class manages authentication and profile details.
- **Review** class links a user to a place with ratings and comments.
- **Place** represents an accommodation, containing details and amenities.
- **Amenity** defines additional features available at a place.

---

## **4. API Interaction Flow**

### **User Registration Sequence**

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

### **User Login and Place Creation**

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

### **Review Submission**

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

---

## **5. Conclusion**

This document outlines the key architectural components, business logic, and API workflows of the HBnB platform. It serves as a foundational reference for the development team to ensure a well-structured and efficient implementation.

