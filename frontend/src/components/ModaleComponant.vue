<template>
  <div v-if="isVisible" class="modal">
    <div class="modal-content">
      <!-- la croix -->
      <span class="close" @click="closeModal">&times;</span>
      <h2>Résultats de l'analyse</h2>
      <p>Prediction : {{ data.prediction }}</p>
      <p>Probability : {{ data.probability }}%</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "ModaleComponant",
  props: {
    data: Object,        // Données envoyées au composant
    isVisible: Boolean,  // Contrôle de la visibilité de la modale
  },
  methods: {
    closeModal() {
      this.$emit("close");  // Émet l'événement "close" pour masquer la modale
    },
  },
};
</script>

<style scoped>
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); 
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000; 
}

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 5px;
  width: 500px;
  height: 200px;
  text-align: center;
  position: relative; 
}

.close {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 24px;
  cursor: pointer;
  color: #333;
}

.close:hover {
  color: red; 
}
</style>
