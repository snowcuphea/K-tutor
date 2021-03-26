<template>
  <v-container class="head d-flex justify-center">
    <h1> {{ section }} </h1>
  </v-container>
</template>

<script>
import { mapState } from 'vuex'

export default {
  data: function() { 
    return {
      section : "Report"
    }
  },
  computed: {
    ...mapState([
      "currentPage"
      ]
    )
  },
  created() {
      this.section = this.currentPage
  },
    
  watch: {
    currentPage() {
      this.section = this.currentPage
    }
  }
}
</script>

<style>

.head {
  border-bottom: 1px solid;
}


</style>