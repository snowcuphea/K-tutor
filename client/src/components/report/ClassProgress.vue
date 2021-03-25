<template>
  <v-container>
    <div v-for="(cls, idx) in userProgress.class" :key="idx"
    class="d-flex">
      <v-row>
        <v-col cols="4">
          <p> {{ cls.title }} </p>
        </v-col>

        <v-col>
          <p class="mb-0 text-end"> {{ cls.done }}/{{ cls.total }} </p>
          <v-progress-linear :value="percentage(cls)"></v-progress-linear>
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script>
import { mapState } from 'vuex'

export default {

  methods: {
    percentage(cls) {

      return (cls.done / cls.total * 100).toFixed(0)
    }
  },
  computed: {
    ...mapState(['userProgress'])
  }
}
</script>

<style>

</style>