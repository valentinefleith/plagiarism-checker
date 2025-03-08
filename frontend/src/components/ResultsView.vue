<template>
    <div class="home">
      <h1>IA Detector</h1>
      <div v-if="resultats.length">
        <h2>Résultats de l'analyse</h2>
        <ul class="results-list">
        <li v-for="(result, index) in resultats" :key="index" class="result-item">
          <p>{{ result }}</p>
        </li>
      </ul>
      </div>
    </div>
  </template>

<script>
import { useRoute,  } from "vue-router";
import {  ref } from "vue";

export default {
  name: "ResultsView",
  setup() {
    const route = useRoute();

    // Initialisation des variables
    const resultats = ref(route.query.data || "Pas de donnees");
  

    // Vérification de la data reçue
    if (route.query.data) {
      try {
        resultats.value = JSON.parse(route.query.data);
        console.log("Résultats après parsing :", resultats.value);
      } catch (error) {
        console.error("Erreur lors du parsing des données JSON :", error);
        resultats.value = [];  // Remettre à un tableau vide en cas d'erreur
      }
    } else {
      console.warn("Aucune donnée de prédiction reçue !");
    }


    return { resultats };
  }
};

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
  
  ul {
  list-style-type: none;
  padding-left: 0; 
}

.result-item {
  background-color: #fafafa;
  border-radius: 10px;
  padding: 16px;
  margin-bottom: 15px;
  font-size: 16px;
  color: #333;
  border-left: 5px solid #007bff; 
  box-sizing: border-box;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.result-item:hover {
  background-color: #e8f4fd;
  transform: translateX(5px);
}

.result-item:last-child {
  margin-bottom: 0; 
}

  </style>