<template>
  <v-container>
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
  watch: {
    currentPage() {
      this.section = this.currentPage
    }
  }
}
</script>

<style>

</style>