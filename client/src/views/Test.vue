<template>
  <v-container class="px-5 d-flex flex-column">
    <div class="d-flex flex-column">
      <h3> Report Card </h3>
      <GradeChart />
      <p>Average of last 10 exams: {{ average }} </p>
    </div>

    <Experience :experience="-1" />

    <div class="d-flex justify-center">
      <v-btn @click="showDialog = !showDialog">시험보기</v-btn>
    </div>

    <TestPage :showDialog="showDialog" @hideDialog="showDialog = !showDialog"/>
    
  </v-container>
</template>

<script>
import { mapState } from 'vuex'

import Experience from "@/components/user/Experience.vue"
import GradeChart from "@/components/exam/GradeChart.vue"
import TestPage from "@/components/exam/TestPage.vue"

export default {
  components: {
    Experience,
    GradeChart,
    TestPage,
  },
  data() {
    return {
      showDialog: false,
    }
  },
  computed: {
    ...mapState([ "userGrade" ]),

    average() {
      var total = 0
      this.userGrade.forEach(element => {
        total += element
      });

      return total/10
    }

  },


}
</script>

<style>

</style>