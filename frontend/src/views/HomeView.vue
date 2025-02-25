<template>
  <div class="home">
    <h1>DragDrop</h1>
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
  height : 100vh;
  display:flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #f1f1f1 ;
}

h1 {
  font-size: 40px;
  margin-bottom: 32px;
}
.file-info {
  margin-top: 32px;
}
</style>
