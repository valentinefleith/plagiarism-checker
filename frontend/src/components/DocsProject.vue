<template>
  <div class="container">
    <aside class="sidebar">
      <h2>Sommaire</h2>
      <ul>
        <li 
          v-for="(header, index) in headers" 
          :key="index" 
          :class="{ active: activeSection === header.id }"
        >
        <a :href="'#' + header.id" @click="setActiveSection(header.id)">
          {{ header.text }}
        </a>

        </li>
      </ul>
    </aside>

    <div class="nouvelle-page">
      <h1>Bienvenue sur la doc !</h1>
      <div class="markdown-content" v-html="markdownContent"></div>
    </div>
    <button v-show="showScrollTop" @click="scrollToTop" class="scroll-top">⬆️</button>
  </div>
  <div class="progress-bar" :style="{ width: scrollProgress + '%' }"></div>
</template>

<script>
import { ref, onMounted } from "vue";
import { marked } from "marked";

export default {
  name: "DocsProject",
  setup() {
    const markdownContent = ref("");
    const headers = ref([]);
    const activeSection = ref("");

    const slugify = (text) => {
      return text
        .toLowerCase()
        .replace(/[^\w\s-]/g, "") 
        .replace(/\s+/g, "-"); 
    };

    const loadMarkdown = async () => {
      try {
        const response = await fetch("/docs/guide_projet.md");
        if (!response.ok) throw new Error("Erreur lors du chargement du Markdown");

        let text = await response.text();
        markdownContent.value = marked.parse(text);

        const tempDiv = document.createElement("div");
        tempDiv.innerHTML = markdownContent.value;

        const extractedHeaders = [];
        tempDiv.querySelectorAll("h1, h2, h3").forEach((header) => {
          const id = slugify(header.innerText);
          header.id = id;
          extractedHeaders.push({ id, text: header.innerText });
        });

        markdownContent.value = tempDiv.innerHTML;
        headers.value = extractedHeaders;
      } catch (error) {
        console.error(error);
      }
    };

    const updateActiveSection = () => {
      const scrollPosition = window.scrollY + 100;
      let currentSection = "";
      headers.value.forEach((header) => {
        const element = document.getElementById(header.id);
        if (element && element.offsetTop <= scrollPosition) {
          currentSection = header.id;
        }
      });
      activeSection.value = currentSection;
    };

    const setActiveSection = (id) => {
      activeSection.value = id;
    };

    onMounted(() => {
      loadMarkdown();
      window.addEventListener("scroll", updateActiveSection);
    });

    const showScrollTop = ref(false);

    const checkScroll = () => {
      showScrollTop.value = window.scrollY > 300;
    };

    const scrollToTop = () => {
      window.scrollTo({ top: 0, behavior: "smooth" });
    };

    onMounted(() => {
      window.addEventListener("scroll", checkScroll);
    });

    const scrollProgress = ref(0);

    const updateScrollProgress = () => {
      const scrollTop = window.scrollY;
      const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
      scrollProgress.value = (scrollTop / scrollHeight) * 100;
    };

    onMounted(() => {
      window.addEventListener("scroll", updateScrollProgress);
    });

    return { markdownContent, headers, activeSection, setActiveSection, showScrollTop, scrollToTop, scrollProgress }
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@300;600&display=swap');

.container {
  display: flex;
  max-width: 1200px;
  margin: 50px auto;
  align-items: flex-start;
}

.sidebar {
  width: 270px;
  background: #f8f9fa;
  padding: 20px;
  border-radius: 12px;
  border: 2px solid #66a3ff;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 20px;
  height: fit-content;
}

.sidebar h2 {
  font-size: 20px;
  color: #0044cc;
  margin-bottom: 15px;
  text-align: center;
}

.sidebar ul {
  list-style-type: none;
  padding: 0;
}

.sidebar li {
  margin-bottom: 10px;
  transition: transform 0.2s ease-in-out;
}

.sidebar li:hover {
  transform: translateX(5px);
}

.sidebar li.active a {
  color: #ff4081;
  font-weight: bold;
  border-left: 3px solid #ff4081;
  padding-left: 10px;
}

.sidebar a {
  text-decoration: none;
  color: #007bff;
  font-size: 16px;
  font-weight: 600;
  display: block;
  padding: 5px 0;
  transition: color 0.3s ease-in-out;
}

.sidebar a:hover {
  color: #ff4081;
}

.nouvelle-page {
  flex: 1;
  padding: 30px;
  background: linear-gradient(135deg, #cce5ff, #99ccff);
  border-radius: 20px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
  color: #333;
  font-family: "Nunito", sans-serif;
  max-width: 900px;
  border: 4px solid #66a3ff;
  animation: fadeIn 0.8s ease-in-out;
}

.markdown-content {
  background-color: #ffffff;
  padding: 30px;
  border-radius: 15px;
  border: 2px solid #66a3ff;
  margin-top: 25px;
  max-width: 800px;
  width: 100%;
  text-align: left;
  color: #333;
  font-family: "Nunito", sans-serif;
  line-height: 1.8;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.markdown-content pre {
  background-color: #1e1e2f;
  color: #ffffff;
  padding: 12px;
  border-radius: 8px;
  overflow-x: auto;
  font-size: 15px;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.2);
}

.markdown-content code {
  font-family: "Courier New", monospace;
  background-color: #f5f5f5;
  padding: 3px 7px;
  border-radius: 5px;
  font-size: 16px;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.scroll-top {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background: #007bff;
  color: white;
  border: none;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  font-size: 24px;
  cursor: pointer;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  transition: opacity 0.3s ease-in-out;
}

.scroll-top:hover {
  background: #0056b3;
}

.progress-bar {
  position: fixed;
  top: 0;
  left: 0;
  height: 5px;
  background: #ff4081;
  transition: width 0.2s;
}

</style>