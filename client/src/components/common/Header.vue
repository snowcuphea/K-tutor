<template>
  <div class="head d-flex flex-column justify-center">
    <h2> {{ section }} </h2>
  </div>
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
  text-align: center;
}


</style>