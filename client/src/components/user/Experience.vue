<template>
  <v-container>
    <div class="d-flex">
      <p>Lv.{{ userLevel }}</p>
      <v-spacer></v-spacer>
      <p>{{ userExperience }}/{{ userLevel*10 }}</p>
    </div>
    <v-progress-linear
      :value="progress">
    </v-progress-linear>
    <div>
      <p v-if="experience != -1" class="text-end">+{{ experience }}</p>
    </div>
  </v-container>
</template>

<script>
import { mapState } from 'vuex'

export default {
  props: [ 'experience' ],
  computed: {
    ...mapState(['userLevel', 'userExperience']),

    progress() {
      return this.userExperience/(this.userLevel * 10) * 100
    }
  }
}
</script>

<style>

</style>