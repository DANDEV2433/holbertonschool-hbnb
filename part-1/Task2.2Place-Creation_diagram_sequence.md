## Sequence diagram for API calls

### 1.User Registration Diagram


### 2.Place Creation Diagram
![Capture d'écran 2025-02-16 181134](https://github.com/user-attachments/assets/452854b6-19e5-4f52-b42a-248e5730df2c)
![Capture d'écran 2025-02-16 181207](https://github.com/user-attachments/assets/c9fc5dcb-0857-4fb9-a585-a03720b6c1c3)
```
![Capture d'écran 2025-02-16 182806](https://github.com/user-attachments/assets/5cd03109-048f-4b99-82ec-9ef754ee6ed8)

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
