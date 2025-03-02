## Rapports de tests
### Tests Utilisateur
Test de création d'utilisateur
```
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
```
{
  "id": "f0323b2f-37b8-420d-9677-f9c8b528a7ca",
  "first_name": "john",
  "last_name": "doe",
  "email": "doe@gmail.com"
}

// 201 OK
```

Test Données invalides pour un utilisateur
```
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
```
{
  "id": "e6b6bf1b-f7e6-4c6f-88df-5d32156648c8",
  "first_name": "",
  "last_name": "",
  "email": "invalid"
}

// 201 OK
```

Test d'identifiants déjà utilisés lors de la création d'un utilisateur
```
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
```
{
  "error": "Email already registered"
}

// 400 Error
```

### Tests Récupération d'Utilisateur
```
curl -X 'GET' \
  'http://127.0.0.1:5000/api/v1/users/f0323b2f-37b8-420d-9677-f9c8b528a7ca' \
  -H 'accept: application/json'
```
Réponse attendue
```
{
  "id": "f0323b2f-37b8-420d-9677-f9c8b528a7ca",
  "first_name": "john",
  "last_name": "dooe",
  "email": "doe@gmail.com"
}

// 200 OK
```

Récupération avec un mauvais ID
```
curl -X 'GET' \
  'http://127.0.0.1:5000/api/v1/users/e2674q9j-51i9-d3a1-3168-u6t5o953n6lb' \
  -H 'accept: application/json'
```
Réponse attendue
```
{
  "error": "User not found"
}

// 404 ERROR
```
