<template>
  <v-container class="d-flex justify-space-around">
    <div v-for="(genre, idx) in userProgress.genres" :key="idx">
      <v-progress-circular size="60" width="10" :value="percentage(genre)">
        {{ percentage(genre) }}
      </v-progress-circular>
      <p class="text-center pt-1">{{ genre.type }}</p>
    </div>
  </v-container>
</template>

<script>
import { mapState } from 'vuex'

export default {

  methods: {
    percentage(genre) {

      return (genre.done / genre.total * 100).toFixed(0) + '%'
    }
  },
  computed: {
    ...mapState(['userProgress'])
  }
}
</script>

<style>

</style>