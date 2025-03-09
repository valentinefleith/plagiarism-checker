<template>
  <div v-if="isVisible" class="modal">
    <div class="modal-content">
      <!-- la croix -->
      <span class="close" @click="closeModal">&times;</span>
      <h2>Résultats de l'analyse</h2>
      <p>Probabilité de plagiat : {{ computeMean }}%</p>
      <button @click="redirectToPage">Voir les détails des résultats</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "ModaleComponant",
  props: {
    data: Object,        // Données envoyées au composant
    text: String,
    isVisible: Boolean,  // Contrôle de la visibilité de la modale
  },
  computed: {
    computeMean() {
      let total = 0;
      for (let i = 0; i < this.data.length; i++) {
        total += this.data[i].probability;
      }
      let avg = total / this.data.length
      return Math.round(avg * 100) / 100
    }
  },
  methods: {
    closeModal() {
      this.$emit("close");  // Émet l'événement "close" pour masquer la modale
    },
    redirectToPage() {
      console.log("Données envoyées : ", this.data);
        this.$router.push({
          path: "/results",
          query: {
            data: JSON.stringify(this.data),  // Convertir en JSON seulement si `data` est valide
            
          }
        }).then(() => {
          this.$router.replace({ path: '/results' }); // On remplace l'URL sans query params
        });
    }
  }
}
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
  height: 150px;
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

button {
  position: relative;
  right: 50;
  transform: (42px, 18px);
  bottom: -31px;
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
