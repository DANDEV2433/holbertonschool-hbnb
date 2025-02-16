## Seqquence diagram for API calls

### User Registration Diagram


### Place Creation Diagram
![Capture d'écran 2025-02-16 101206](https://github.com/user-attachments/assets/4df1625b-6925-4125-85f3-a984649a286f)
![Capture d'écran 2025-02-16 101133](https://github.com/user-attachments/assets/a8790df8-af64-466c-a20b-78ef0acec736)
```
sequenceDiagram
    participant User
    participant API
    participant PlaceService
    participant Database

    User->>API: createPlace(title, latitude, longitude, price, owner, description, amenities)
    API->>PlaceService: validatePlaceData(title, latitude, longitude, price, owner, description, amenities)
    PlaceService-->>API: ValidateResult(succes/failure)
    alt Validation succes
        API->>PlaceService: createPlace(title, latitude, longitude, price, owner, description, amenities)
        PlaceService->>Datebase: InsertPlaceData(title, latitude, longitude, price, owner, description, amenities)
        Database-->>PlaceService: ConfirmPlaceCreated(uuid)
        PlaceService-->>API: PlaceCreationResponse(succes, uuid)
        API-->>User: Response (succes, uuid)
    else Validation failure
        API-->>User: (failure, validation_errors)
    end
```
### Review Submission Diagram
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
### Fetching a List of Places
