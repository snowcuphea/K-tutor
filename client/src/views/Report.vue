<template>
  <v-container class="px-5 d-flex flex-column">
    <div class="d-flex flex-column my-3">
      <h3> {{ nickName }}'s Study Report </h3>

      <Experience :experience="-1" />

      <div v-if="contiDay > 5" class="d-flex">
        <v-icon small>mdi-flare</v-icon>
        <p class="px-1 mb-0" > Studied for
          <span style="font-weight: bolder"> {{ contiDay }}</span>
          days in a row! </p>
      </div>

      <div v-else class="d-flex align-center">
        <v-icon small>mdi-flare</v-icon>
        <p class="px-1 mb-0"> 
          Studied for <span style="font-weight: bolder"> 
            {{ contiDay }} </span><span v-if="contiDay == 1"> day.</span> <span v-else> days.</span>
        </p>
      </div>

      <div v-if="studyCnt" class="d-flex align-center">
        <v-icon small>mdi-flare</v-icon>
        <p class="px-1 mb-0"> 
         Studied <span style="font-weight: bolder"> {{ studyCnt }} </span> lesson cards.
        </p>
      </div>

      <div v-else class="d-flex align-center">
        <v-icon small>mdi-flare</v-icon>
        <p class="px-1 mb-0"> 
         Try taking a class for the first time!
        </p>
      </div>

      <!-- <p class="px-3" v-else> Studied for <span style="font-weight: bolder"> {{ contiDay }} </span><span v-if="contiDay == 1"> day.</span> <span v-else> days.</span></p>
      <p class="px-3" v-if="studyCnt"> Studied <span style="font-weight: bolder"> {{ studyCnt }} </span> lesson cards. </p>
      <p class="px-3" v-else> Try taking a class for the first time! </p> -->
    </div>

    <div>
      <h3>Recent Lesson Cards</h3>
      <ClassCards />
    </div>

    <div class="my-3 d-flex flex-column">
      <h3>Learning Progress</h3>
      <ClassProgress :showMore="showMore" />
      <v-btn class="mt-n5 align-self-end" @click="showMore = !showMore"
        v-if="!showMore && recent_lc_progress.length > 3"
        plain text retain-focus-on-click>more</v-btn>
      <v-btn class="mt-n5 align-self-end" @click="showMore = !showMore"
        v-else-if="showMore && recent_lc_progress.length > 3"
        plain text retain-focus-on-click>less</v-btn>
    </div>

    <div>
      <h3>All Culture Progress</h3>
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
    ...mapState(['nickName','contiDay','studyCnt','recent_lc_progress'])
  }
}
</script>

<style>

</style>