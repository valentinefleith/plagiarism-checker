<template>
  <div class="home">
    <h1>Détecteur de plagiat par IA</h1>
    <div v-if="resultats.length" class="results-container">
      <h2>Estimation du pourcentage {{ computeMean }}%</h2>
      <ul class="results-list">
        <li v-for="(result, index) in resultats" :key="index" class="result-card">
          <div class="result-content">
            <p class="result-text">{{ result.text }}</p>
            <span class="percentage-badge" :class="getPercentageClass(result.probability)">
              {{ result.probability }}%
            </span>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { useRoute } from "vue-router";
import { ref } from "vue";

export default {
  name: "ResultsView",
  computed: {
    computeMean() {
      let total = 0;
      for (let i = 0; i < this.resultats.length; i++) {
        total += this.resultats[i].probability;
      }
      let avg = total / this.resultats.length;
      return Math.round(avg * 100) / 100
    }
  },
  setup() {
    const route = useRoute();

    
    const resultats = ref(route.query.data ? JSON.parse(route.query.data) : []);

    const getPercentageClass = (probability) => {
      if (probability >= 75) return "fort";
      if (probability >= 50) return "moyen";
      return "bas";
    };

    return { resultats, getPercentageClass };
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
  background-color: #f9fafb;
  padding: 20px;
}

h1 {
  font-size: 40px;
  margin-bottom: 20px;
  color: #333;
}

.results-container {
  width: 80%;
  max-width: 600px;
  background: #fff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.results-list {
  list-style: none;
  padding: 0;
}

.result-card {
  background: #ffffff;
  padding: 15px;
  margin: 10px 0;
  border-radius: 8px;
  box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.result-card:hover {
  transform: translateY(-3px);
}

.result-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.result-text {
  flex: 1;
  font-size: 16px;
  color: #555;
}

.percentage-badge {
  padding: 8px 14px;
  border-radius: 20px;
  font-size: 14px;
  font-weight: bold;
  color: white;
  text-align: center;
  min-width: 60px;
}

.fort {
  background-color: #dc3545;
}

.moyen {
  background-color: #ffc107;
}

.bas {
  background-color: #28a745;
}
</style>
