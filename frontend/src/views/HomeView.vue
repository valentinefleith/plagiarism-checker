<template>
  <div class="home">
    <h1>IA Detector</h1>
    <p>Collez le texte que vous soupçonnez avoir été écrit par IA, ou joignez le fichier avec le drag and drop</p>
    <div class="textarea-container">
        <textarea id="textInput" placeholder="Collez votre texte ici..."></textarea>
        <button onclick="envoyerTexte()">Envoyer</button>
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
    let dropzonefile = ref("")

    const drop = (e) => {
      dropzonefile.value = e.dataTransfer.files[0]

    }

    const selectedFile = () => {
      dropzonefile.value = document.querySelector('.dropzonefile').files[0]
    }
    return {dropzonefile, drop, selectedFile};
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