<template>
  <v-container class="d-flex justify-space-around">
    <div v-for="(prgs, idx) in allProgress" :key="idx">
      <v-progress-circular size="60" width="10" :value="percentage(prgs)" color="teal accent-4">
        <span style="color:black;"> {{ percentage(prgs) }} </span>
      </v-progress-circular>
      <p class="text-center pt-1">{{ prgs.type }}</p>
    </div>
  </v-container>
</template>

<script>
import { mapState } from 'vuex'

export default {

  methods: {
    percentage(prgs) {

      return (prgs.done / prgs.total * 100).toFixed(0) + '%'
    }
  },
  computed: {
    ...mapState(['allProgress'])
  }
}
</script>

<style>

</style>