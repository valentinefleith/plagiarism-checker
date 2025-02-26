<template>
  <div class="home">
    <h1>IA Detector</h1>
    <p>Collez le texte que vous soupçonnez avoir été écrit par IA, ou joignez le fichier avec le drag and drop</p>
    <div class="textarea-container">
         <textarea v-model="textInput" placeholder="Collez votre texte ici..."></textarea> <!-- on utilise v-model -->
        <button @click="envoyerTexte">Envoyer</button>
    </div>

    <DropZone @drop.prevent="drop" @change="selectedFile"/>
    <span class="file-info">Fichier : {{ dropzonefile.name }}</span>
  </div>
</template>

<script>
// @ is an alias to /src
import DropZone from '@/components/DropZone.vue';
import {ref} from "vue"

export default {
  name: 'HomeView',
  components: {
    DropZone
  },
  setup() {

    const textInput = ref("")
        // Fonction pour récupérer le texte 
        const envoyerTexte = async () => {
    if (!textInput.value.trim()) {
      console.log("Le texte est vide !");
      return;
    }
    try {
      const response = await fetch("https://jsonplaceholder.typicode.com/posts", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ texte: textInput.value }),
      });

      const data = await response.json();
      console.log("Réponse du serveur :", data);
    } catch (error) {
      console.error("Erreur lors de l'envoi :", error);
    }
  };


  const envoyerFichier = async (fichier) => {
  if (!fichier) {
    console.log("Aucun fichier sélectionné.");
    return;
  }

  const formData = new FormData();
  formData.append("fichier", fichier);

  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/posts", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    console.log("Réponse du serveur :", data);
    alert(`Le fichier a été envoyé avec succès ! ID du fichier : ${data.id}`);
  } catch (error) {
    console.error("Erreur lors de l'envoi :", error);
  }
};


  //fonction pour le drag and drop du fichier
    let dropzonefile = ref("")
    const drop = async (e) => {
  e.preventDefault();
  const fichier = e.dataTransfer.files[0];
  await envoyerFichier(fichier); // appel de la fonction envoyerFichier
};

    

    //fonction lorsque l'utilisateur selectionne un fichier via son os
    const selectedFile = () => {
  const fichier = document.querySelector('.dropzonefile').files[0];
  envoyerFichier(fichier);
};

    return {textInput ,envoyerTexte, dropzonefile, drop, selectedFile};
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
</style>