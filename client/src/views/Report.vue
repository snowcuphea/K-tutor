<template>
  <v-container class="px-5 d-flex flex-column">
    <div class="d-flex flex-column">
      <h3> {{ userName }}'s Study Report </h3>
      <Experience :experience="-1" />
      <p class="px-3"> Studied for <span> {{ contiDay }} </span> days in a row! </p>
      <p class="px-3"> Studied <span> {{ studyCnt }} </span> lesson cards. </p>
    </div>

    <div>
      <h3>Recent Lesson Cards</h3>
      <ClassCards />
    </div>

    <div>
      <h3>Recent Class Progress</h3>
      <ClassProgress />
    </div>

    <div>
      <h3>All Genre Progress</h3>
      <GenreProgress />
    </div>

  </v-container>
</template>

<script>
import { mapState } from 'vuex' 

import Experience from "@/components/user/Experience.vue"
import ClassCards from "@/components/report/ClassCards.vue"
import ClassProgress from "@/components/report/ClassProgress.vue"
import GenreProgress from "@/components/report/GenreProgress.vue"


export default {
  components: {
    Experience,
    ClassCards,
    ClassProgress,
    GenreProgress
  },
  computed: {
    ...mapState(['userName', 'userLevel','contiDay','studyCnt'])
  }
}
</script>

<style>

</style>