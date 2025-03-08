<template>
  <div class="home">
    <h1>Plagiat Detector</h1>
    <p>Collez le texte que vous soupçonnez avoir été écrit par IA, ou joignez le fichier avec le drag and drop</p>
    <div class="textarea-container">    
         <textarea v-model="textInput" placeholder="Collez votre texte ici..."></textarea> <!-- on utilise v-model -->
        <button @click="envoyerTexte">Envoyer</button>
    </div>

   <!-- Ajout d'un bouton pour accéder à la doc -->
   <button class="doc-button" @click="goToDocs">📖 Voir la doc ✨</button>

   <!-- Affichage de la modale si isModalVisible est vrai -->
   <ModaleComponant 
      v-if="isModalVisible" 
      :data="resultats"
      :text="textInput"
      :isVisible="isModalVisible" 
      @close="isModalVisible = false" 
    />

    <DropZone @drop.prevent="drop" @change="selectedFile"/>
    <span class="file-info">Fichier : {{ dropzonefile.name }}</span>
    <div id="contributeurs"><h3>Contributeurs</h3>
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
// @ is an alias to /src
import DropZone from '@/components/DropZone.vue';
import ModaleComponant from '@/components/ModaleComponant.vue';
import {ref} from "vue";
import {useRouter} from "vue-router";

export default {
  name: 'HomeView',
  components: {
    DropZone,
    ModaleComponant
  },
  setup() {
    const router = useRouter();
    const resultats = ref({});
    const textInput = ref("");
    const isModalVisible = ref(false);
  

        // Fonction pour récupérer le texte 
        const envoyerTexte = async () => {
    if (!textInput.value.trim()) {
      console.log("Le texte est vide !");
      return;
    }
    const phrases = textInput.value.split("\n").filter(line => line.trim() !== "");

try {
  const responses = await Promise.all(
    phrases.map(async (phrase) => {
      const response = await fetch("http://127.0.0.1:8000/prediction/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ body: phrase }),
      });
      console.log(response)
      return response.json();
    })
  );

  console.log(responses);
  resultats.value = responses;
  console.log("Données envoyées à la modale :", resultats.value);
  isModalVisible.value = true;

} catch (error) {
  console.error("Erreur lors de l'envoi :", error);
}
};

  //cette fonction va lire le fichier et envoyer le contenu
  const lireFichierEnvoyer = async (fichier) => {
  if (!fichier) {
    console.log("Aucun fichier sélectionné.");
    return;
  }

  const reader = new FileReader();

  reader.onload = async function (e) {
    const fileContent = e.target.result;
    // Découper le contenu du fichier en lignes (comme pour envoyerTexte)
    const lignes = fileContent.split("\n").filter(line => line.trim() !== "");
    // console.log(lignes);
    try {
      const responses = await Promise.all(
        lignes.map(async (ligne) => {
          const data = { body: ligne }; // on prépare chaque ligne à envoyer
          const response = await fetch('http://127.0.0.1:8000/prediction/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),  
          });

          const result = await response.json();
          return {
            text: ligne,  
            prediction: result.prediction,  
            probability: result.probability, 
          };
        })
      );

      console.log('Réponses du serveur avec texte :', responses);
      resultats.value = responses;
      console.log("Résultats mis à jour :", resultats.value);
      isModalVisible.value = true;

    } catch (error) {
      console.error('Erreur lors de l\'envoi :', error);
    }
  };

  reader.onerror = function () {
    alert('Erreur lors de la lecture du fichier');
  };

  reader.readAsText(fichier);
};


// Fonction pour le drag and drop du fichier
let dropzonefile = ref("");
const drop = (e) => {
  e.preventDefault();
  const fichier = e.dataTransfer.files[0];
  // gestion il faut que le fichier soit .txt pour être lu correctement
  if (!fichier || fichier.type !== "text/plain") {
    alert("Veuillez sélectionner un fichier .txt");
    return;
  }
  dropzonefile.value = fichier;  //mettre à jour la variable pour l'afficher (Fichier :)
  lireFichierEnvoyer(fichier); // Appel de la fonction envoyerFichier
  
};

// Fonction lorsque l'utilisateur sélectionne un fichier via son OS
const selectedFile = () => {
  const fichier = document.querySelector('.dropzonefile').files[0];
  if (!fichier || fichier.type !== "text/plain") {
    alert("Veuillez sélectionner un fichier .txt");
    return;
  }
  dropzonefile.value = fichier;
  lireFichierEnvoyer(fichier);  
};


// y

const goToDocs = () => {
  router.push("/docs"); // Redirection vers la page de documentation
};

return { textInput, envoyerTexte, resultats, isModalVisible, dropzonefile, drop, selectedFile, goToDocs };
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

.doc-button {
  margin-top: 20px;
  background-color: #007BFF; 
  color: #ffffff;  
  font-size: 16px;
  font-weight: bold;
  padding: 10px 20px;
  border: 2px solid #0056b3; 
  border-radius: 15px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: background 0.3s ease, transform 0.2s ease;
}

.doc-button:hover {
  background-color: #3399FF; 
  border-color: #004085; 
  transform: scale(1.05);
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