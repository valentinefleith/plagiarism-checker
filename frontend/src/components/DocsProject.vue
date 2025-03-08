<template>
  <div class="nouvelle-page">
    <h1>Bienvenue sur la doc 📖✨</h1>
    
    <!-- Conteneur du contenu Markdown -->
    <div class="markdown-content" v-html="markdownContent"></div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { marked } from "marked";

export default {
  name: "DocsProject",
  setup() {
    const markdownContent = ref("");

    // Fonction pour charger et convertir le Markdown
    const loadMarkdown = async () => {
      try {
        const response = await fetch("/docs/guide_projet.md");
        if (!response.ok) throw new Error("Erreur lors du chargement du Markdown");

        const text = await response.text();
        markdownContent.value = marked(text); // Convertir en HTML
      } catch (error) {
        console.error(error);
      }
    };

    onMounted(loadMarkdown); // Charger le Markdown au montage du composant

    return { markdownContent };
  }
};
</script>

<style scoped>
.nouvelle-page {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #ddeeff, #aaccff); /* Dégradé bleu pastel */
  border-radius: 15px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  color: #333;
  font-family: "Poppins", sans-serif;
  max-width: 900px;
  margin: 50px auto;
  border: 3px solid #77aaff;
}

.markdown-content {
  background-color: #ffffff;
  padding: 25px;
  border-radius: 10px;
  border: 2px solid #77aaff;
  margin-top: 20px;
  max-width: 800px;
  width: 100%;
  text-align: left;
  color: #333;
  font-family: "Poppins", sans-serif;
  line-height: 1.8;
}

.markdown-content h1 {
  font-size: 28px;
  color: #0056b3;
  border-bottom: 2px solid #77aaff;
  padding-bottom: 5px;
  margin-bottom: 15px;
}

.markdown-content h2 {
  font-size: 24px;
  color: #007bff;
  margin-top: 20px;
}

.markdown-content p {
  font-size: 16px;
  color: #444;
  line-height: 1.6;
  margin-bottom: 10px;
}

.markdown-content ul {
  list-style-type: disc;
  margin-left: 20px;
  padding-left: 20px;
}

.markdown-content ul li {
  margin-bottom: 8px;
}

.markdown-content a {
  color: #ff69b4;
  font-weight: bold;
  text-decoration: none;
  transition: color 0.3s ease-in-out;
}

.markdown-content a:hover {
  color: #ff85c2;
  text-decoration: underline;
}

/* Blocs de code */
.markdown-content pre {
  background-color: #282c34;
  color: #ffffff;
  padding: 10px;
  border-radius: 5px;
  overflow-x: auto;
}

.markdown-content code {
  font-family: "Courier New", monospace;
  background-color: #f8f9fa;
  padding: 2px 5px;
  border-radius: 5px;
}
</style>