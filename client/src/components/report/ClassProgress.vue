<template>
  <v-container>
    <div v-for="(cls, idx) in orderedList()" :key="idx"
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
    },

    orderedList() {

      const newList = []

      for ( var cls of this.userProgress.class ){
        const form = {
          title: cls.title, 
          total: cls.total, 
          done: cls.done, 
          percentage: this.percentage(cls)
        }
        newList.push(form)
      }
      
      newList.sort((a,b) => {
        return - (a.percentage - b.percentage)
      })


      return newList

    }

  },
  computed: {
    ...mapState(['userProgress'])
  }
}
</script>

<style>

</style>