<template>
  <v-container>
    <div class="d-flex">
      <p class="mb-0">Lv.{{ userLevel }}</p>
      <v-spacer></v-spacer>
      <p class="mb-0">{{ userExperience }}/{{ required_exp[this.userLevel] }}</p>
    </div>
    <v-progress-linear
      :value="progress" height="10" color="teal accent-4" striped>
    </v-progress-linear>
    <div>
      <p v-if="experience != -1" class="text-end">+{{ experience }} exp</p>
    </div>
  </v-container>
</template>

<script>
import { mapState } from 'vuex'

export default {
  props: [ 'experience' ],
  computed: {
    ...mapState(['userLevel', 'userExperience','required_exp']),

    progress() {
      return this.userExperience/this.required_exp[this.userLevel] * 100
    }
  }
}
</script>

<style>

</style>