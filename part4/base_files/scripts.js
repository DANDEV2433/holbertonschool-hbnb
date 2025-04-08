/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/
// attend que toute la page HTML soit complètement chargée avant d’exécuter
document.addEventListener('DOMContentLoaded', () => {
    // Simule un utilisateur connecté 
    const isLoggedIn = true;
    if (isLoggedIn) {
      // on rend visible le bouton avec l’ID
      document.getElementById('add-review-button').style.display = 'block';
    }
});

 document.addEventListener('DOMContentLoaded', () => {
    // récupère le formulaire de login grâce à son ID
    const loginForm = document.getElementById('login-form');

    if (loginForm) {
      // On ajoute un écouteur d’événement qui s’active quand l’utilisateur soumet le formulaire
      loginForm.addEventListener('submit', async (event) => {
      // ça empêche le comportement par défaut de rechergement de la page
      event.preventDefault();
      // Récupère la valeur que l'utilisateur a saisie dans les champs email et password
      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;
      console.log("Email:", email);
      console.log("Password:", password);
      // Appelle la fonction loginUser pour tenter la connexion
      await loginUser(email, password);
      });
    }
  // Fonction qui envoie les identifiants à l'API et gère la réponse
  async function loginUser(email, password) {
    try {
        // Envoie une requête POST à l'API pour tenter de se connecter
         const response = await fetch('http://localhost:5500/part4/base_files/login.html', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({ email, password })
      });
        // Vérifie si la réponse est correcte
        if (!response.ok) throw new Error(data.message);
          // convertit la réponse en JSON
          const data = await response.json();
          // Affiche une alerte si la connexion échoue
          console.log("Login successful:");
          console.log("Add Token:", data.token);
          // stocke le token dans un cookie
          document.cookie = `token=${data.token}; path=/`;
          // Redirige l'utilisateur vers la page principale après la connexion
          window.location.href = 'index.html';

        if (response.ok) {
          const data = await response.json();
          document.cookie = `token=${data.access_token}; path=/`;
          window.location.href = 'index.html';
      } else {
        alert('Login failed: ' + response.statusText)
      }
    }catch (error) {
        // Affiche une alerte si la connexion échoue
        alert('Login failed: ' + error.message);
    }
  }})
