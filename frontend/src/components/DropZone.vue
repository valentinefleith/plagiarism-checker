<template>
<div 
@dragenter.prevent="toggleActive" 
@dragleave.prevent="toggleActive" 
@dragover.prevent
@drop.prevent="toggleActive"
:class="{'active-dropzone' : active}"
class="dropzone">
    <span>Drag and Drop un fichier</span>
    <span>OU</span>
    <label for="dropzonefile">Sélectionnez un fichier</label>
    <input type="file" id="dropzonefile" class="dropzonefile">
</div>
</template>

<script>
import {ref} from "vue";

export default {
  name: 'DropZone',
  setup() {
    const active = ref(false)

    //quand la constante est appelé on passe de true à false
    const toggleActive = () => {
      active.value = !active.value;
    }

    return {active, toggleActive}
  }
};

</script>
<style scoped lang="scss">
.dropzone {
  width: 400px;
  height:200px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  row-gap: 16px;
  border: 2px dashed #724ae8;
  background-color: #fff;
  transition: .3s ease all;



  label {
    padding:8px 12px;
    color: #fff;
    background-color: #724ae8;
    transition: 0.3s ease all;
    cursor: pointer;
  }


  label:hover {
    background-color: #4d22cb;
    transition: background 0.3s ease;
 
  }


  input {
    display: none;
  }
}
  .active-dropzone {
    color: #fff;
    border-color: #fff;
    background-color: #724ae8;

    label {
      
      background-color: #fff;
      color: #724ae8;
      
    }
  }

</style>
