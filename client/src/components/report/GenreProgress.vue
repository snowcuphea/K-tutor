<template>
  <v-container class="d-flex justify-space-around">
    <div v-for="(prgs, idx) in progress" :key="idx">
      <v-progress-circular size="60" width="10" :value="percentage(prgs)">
        {{ percentage(prgs) }}
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
    ...mapState(['progress'])
  }
}
</script>

<style>

</style>