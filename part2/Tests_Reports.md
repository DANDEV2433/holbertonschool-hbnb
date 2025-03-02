## Rapports de tests
### Tests Utilisateur
Test de création d'utilisateur
```python3
curl -X 'POST' \
  'http://127.0.0.1:5000/api/v1/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "first_name": "john",
  "last_name": "doe",
  "email": "doe@gmail.com"
}'
```
Réponse attendue
```python3
{
  "id": "f0323b2f-37b8-420d-9677-f9c8b528a7ca",
  "first_name": "john",
  "last_name": "doe",
  "email": "doe@gmail.com"
}

// 201 OK
```

Test Données invalides pour un utilisateur
```python3
curl -X 'POST' \
  'http://127.0.0.1:5000/api/v1/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "first_name": "",
  "last_name": "",
  "email": "invalid"
}'
```
Réponse attendue
```python3
{
  "id": "e6b6bf1b-f7e6-4c6f-88df-5d32156648c8",
  "first_name": "",
  "last_name": "",
  "email": "invalid"
}

// 201 OK
```

Test d'identifiants déjà utilisés lors de la création d'un utilisateur
```python3
curl -X 'POST' \
  'http://127.0.0.1:5000/api/v1/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "first_name": "john",
  "last_name": "doe",
  "email": "doe@gmail.com"
}'
```
Réponse attendue
```python3
{
  "error": "Email already registered"
}

// 400 Error
```

### Tests Récupération d'Utilisateur
```python3
curl -X 'GET' \
  'http://127.0.0.1:5000/api/v1/users/f0323b2f-37b8-420d-9677-f9c8b528a7ca' \
  -H 'accept: application/json'
```
Réponse attendue
```python3
{
  "id": "f0323b2f-37b8-420d-9677-f9c8b528a7ca",
  "first_name": "john",
  "last_name": "dooe",
  "email": "doe@gmail.com"
}

// 200 OK
```

Récupération avec un mauvais ID
```python3
curl -X 'GET' \
  'http://127.0.0.1:5000/api/v1/users/e2674q9j-51i9-d3a1-3168-u6t5o953n6lb' \
  -H 'accept: application/json'
```
Réponse attendue
```python3
{
  "error": "User not found"
}

// 404 ERROR
```

### Tests des équipements
Enregistrer un nouvel équipement
```python3
curl -X 'POST' \
  'http://127.0.0.1:5000/api/v1/amenities/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "micro-onde"
}'
```
Réponse obtenue
```python3
201

{
  "message": "La commodite a ete creee",
  "commodite": {
    "id": "c7c26eaa-f922-4c4b-a1b3-7ba9cc7d5775",
    "name": "micro-onde",
    "created_at": "2025-03-02T18:44:34.525817",
    "updated_at": "2025-03-02T18:44:34.525829"
  }
}
```
Récupérer une liste de tout les équipements
```python3
curl -X 'GET' \
  'http://127.0.0.1:5000/api/v1/amenities/' \
  -H 'accept: application/json'
```
Réponse obtenue
```python3
200

{
    "id": "c7c26eaa-f922-4c4b-a1b3-7ba9cc7d5775",
    "name": "micro-onde",
    "created_at": "2025-03-02T18:44:34.525817",
    "updated_at": "2025-03-02T18:44:34.525829"
  }
```
Récupérer les informations de tout les équipements par l'id
```python3
curl -X 'GET' \
  'http://127.0.0.1:5000/api/v1/amenities/c7c26eaa-f922-4c4b-a1b3-7ba9cc7d5775' \
  -H 'accept: application/json'
```
Réponse obtenue
```python3
200

{
  "id": "c7c26eaa-f922-4c4b-a1b3-7ba9cc7d5775",
  "name": "micro-onde",
  "created_at": "2025-03-02T18:44:34.525817",
  "updated_at": "2025-03-02T18:44:34.525829"
}
```
Mettre a jour les infos d'un équipement
```python3
curl -X 'PUT' \
  'http://127.0.0.1:5000/api/v1/amenities/c7c26eaa-f922-4c4b-a1b3-7ba9cc7d5775' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "lave-vaisselle"
}'
```
Réponse obtenue
```python3
error 500
TypeError: InMemoryRepository.update() missing 1 required positional argument: 'data'
```

### Tests Place
test créer un nouveau Lieu
```python3
curl -X 'POST' \
  'http://127.0.0.1:5000/api/v1/places/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "cozy place",
  "description": "A nice place to stay",
  "price": 100.0,
  "latitude": 37.7749,
  "longitude": -122.4194,
  "owner_id": "f0323b2f-37b8-420d-9677-f9c8b528a7ca",
  "owner": {
    "id": "f0323b2f-37b8-420d-9677-f9c8b528a7ca",
    "first_name": "john",
    "last_name": "doe",
    "email": "doe@gmail.com"
  },
  "amenities": [
    "wi-fi"
  ],
  "reviews": [
    {
      "id": "string",
      "text": "string",
      "rating": 0,
      "user_id": "string"
    }
  ]
}'
```
réponse attendue
```python3
TypeError: Place.__init__() got an unexpected keyword argument 'reviews'

/// 500 erreur interne au serveur
```

test pour lister tout les lieux d'un utilisateur
```python3
curl -X 'GET' \
  'http://127.0.0.1:5000/api/v1/places/' \
  -H 'accept: application/json'
```
réponse attendue
```python3
[]

// 200 Liste des lieux récupérée
```

test pour mettre à jour un lieu
```python3
curl -X 'PUT' \
  'http://127.0.0.1:5000/api/v1/places/e6b6bf1b-f7e6-4c6f-88df-5d32156648c8' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "cozy place",
  "description": "it'\''s cozy",
  "price": 100,
  "latitude": 37,
  "longitude": -122,
  "owner_id": "f0323b2f-37b8-420d-9677-f9c8b528a7ca",
  "owner": {
    "id": "f0323b2f-37b8-420d-9677-f9c8b528a7ca",
    "first_name": "john",
    "last_name": "doe",
    "email": "doe@gmail.com"
  },
  "amenities": [
    "wi-fi"
  ],
  "reviews": [
    {
      "id": "string",
      "text": "string",
      "rating": 0,
      "user_id": "string"
    }
  ]
}'
```
réponse attendue
```python3
TypeError: HBnBFacade.update_place() got an unexpected keyword argument 'title'

// 500 erreur interne au serveur
```

test pour retrouver un lieu par son ID
```python3
curl -X 'GET' \
  'http://127.0.0.1:5000/api/v1/places/e6b6bf1b-f7e6-4c6f-88df-5d32156648c8' \
  -H 'accept: application/json'
```
réponse attendue
```python3
AttributeError: 'HBnBFacade' object has no attribute 'get_place_by_id'

// 500 erreur interne au serveur
```
