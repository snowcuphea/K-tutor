<template>
  <v-container>
    <div class="d-flex">
      <p class="mb-0">Lv.{{ userLevel }}</p>
      <v-spacer></v-spacer>
      <p class="mb-0" v-if="userLevel < 15">{{ userExperience }}/{{ required_exp[this.userLevel] }}</p>
      <p class="mb-0" v-else>MAX</p>
    </div>
    <v-progress-linear
      :value="progress" height="10" color="teal accent-4" striped>
    </v-progress-linear>
    <div v-if="userLevel != 15">
      <p v-if="experience != -1" class="text-end">+{{ experience }} exp</p>
    </div>
  </v-container>
</template>

<script>
import { mapState } from 'vuex'

import { intermediate } from '@/store/achievement.js'


export default {
  props: [ 'experience' ],
  computed: {
    ...mapState(['userLevel', 'userExperience','required_exp', 'myCompleteAchievement']),

    progress() {
      if (this.userLevel == 15) {
        return 100
      } else {
        return this.userExperience/this.required_exp[this.userLevel] * 100
      }
    }
  },
  watch: {
    userLevel() {
      if ( intermediate( this.myCompleteAchievement ) ) {
        this.$store.dispatch('completeAchieve', 6)
      }
    }
  }
}
</script>

<style>

</style>