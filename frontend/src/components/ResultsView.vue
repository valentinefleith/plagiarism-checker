<template>
    <div class="home">
      <h1>IA Detector</h1>
      <p>Collez le texte que vous soupçonnez avoir été écrit par IA, ou joignez le fichier avec le drag and drop</p>
      
      <div v-if="results.length">
        <h2>Résultats de l'analyse</h2>
        <ul>
          <li v-for="(result, index) in results" :key="index">
        
            <p>{{ result }}</p>
          </li>
        </ul>
      </div>
  
      <div id="contributeurs">
        <h3>Contributeurs</h3>
        <ul>
          <li>
            <a href="https://github.com/Batouuuuu" target="_blank">
              <img src="https://github.com/Batouuuuu.png" alt="Utilisateur 2" class="avatar">
            </a>
          </li>
          <li>
            <a href="https://github.com/valentinefleith" target="_blank">
              <img src="https://github.com/valentinefleith.png" alt="Utilisateur 2" class="avatar">
            </a>
          </li>
          <li>
            <a href="https://github.com/deboraptor" target="_blank">
              <img src="https://github.com/deboraptor.png" alt="Utilisateur 2" class="avatar">
            </a>
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  import { useRoute } from 'vue-router'; 

  export default {
    name: 'ResultsView',
    setup() {
      const route = useRoute();
      const results = route.params.results || []; 
  
      return { results };
    }
  }
  </script>
  
  <style lang="scss" scoped>
  .home {
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #f1f1f1;
  }
  
  h1 {
    font-size: 40px;
    margin-bottom: 32px;
  }
  
  .file-info {
    margin-top: 32px;
  }
  
  .textarea-container {
    position: relative;
    width: 100%;
    max-width: 400px;
    display: flex;
    margin-top: 20px;
    margin-bottom: 20px;
  }
  
  textarea {
    width: 100%;
    height: 150px;
    padding: 10px;
    font-size: 12px;
    border: 1px solid #ccc;
    border-radius: 5px;
    resize: none;
    padding-bottom: 40px; 
  }
  
  button {
    position: absolute;
    right: 10px;
    bottom: 10px;
    padding: 8px 15px;
    font-size: 14px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background 0.3s ease;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  
  #contributeurs {
    text-align: center;
    position: absolute;
    bottom: 10px;
  }
  
  #contributeurs h3 {
    margin-bottom: 15px;
  }
  
  #contributeurs ul {
    list-style: none;
    padding: 0;
    display: flex;
    justify-content: center;
    gap: 20px;
  }
  
  #contributeurs li {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  #contributeurs a {
    text-decoration: none;
    color: black;
    font-weight: bold;
    font-size: 14px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  #contributeurs .avatar {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    border: 2px solid #333;
    transition: transform 0.3s ease;
  }
  
  #contributeurs .avatar:hover {
    transform: scale(1.1);
  }
  
  </style>