<template>
  <v-container class="px-5 d-flex flex-column">
    <div class="d-flex flex-column">
      <h3> {{ nickName }}'s Study Report </h3>
      <Experience :experience="-1" />
      <p class="px-3"> Studied for <span> {{ contiDay }} </span> days in a row! </p>
      <p class="px-3"> Studied <span> {{ studyCnt }} </span> lesson cards. </p>
    </div>

    <div>
      <h3>Recent Lesson Cards</h3>
      <ClassCards />
    </div>

    <div class="my-3 d-flex flex-column">
      <h3>Recent Learning Progress</h3>
      <ClassProgress :showMore="showMore" />
      <v-btn class="mt-n5 align-self-end" @click="showMore = !showMore"
        v-if="!showMore"
        plain text retain-focus-on-click>more</v-btn>
      <v-btn class="mt-n5 align-self-end" @click="showMore = !showMore"
        v-else
        plain text retain-focus-on-click>less</v-btn>
    </div>

    <div>
      <h3>All Theme Progress</h3>
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
  data() {
    return {
      showMore: false,
    }
  },
  components: {
    Experience,
    ClassCards,
    ClassProgress,
    GenreProgress
  },
  computed: {
    ...mapState(['nickName','contiDay','studyCnt'])
  }
}
</script>

<style>

</style>