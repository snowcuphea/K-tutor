<template>
  <v-container class="px-5 d-flex flex-column">
    <div class="d-flex flex-column">
      <h3> Report Card </h3>
      <GradeChart />
      <p class="mt-2">Average of last {{ userGrade_score.length }} exams: {{ average }} </p>
    </div>

    <Experience :experience="-1" />

    <div class="d-flex justify-center">
      <v-btn class="mt-5" @click="startTest">시험보기</v-btn>
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
  methods: {
    ableTest() {
      if ( this.recent_learned_lc.length > 9 ) {
        return true
      } else {
        return false
      }
    },
    startTest() {
      if (this.ableTest() ){
        this.$store.dispatch( "getTestQuestions" )
        this.showDialog = !this.showDialog
      }
    }
  },
  computed: {
    ...mapState([ "userGrade_score", "recent_learned_lc"  ]),

    average() {
      var total = 0
      this.userGrade_score.forEach(element => {
        total += element
      });

      return total/this.userGrade_score.length
    }
  },
  created() {
    // 시험 내용 요청 보내서 store에 저장
    if (this.ableTest()) {
      this.$store.dispatch( "getTestQuestions" )
    }

  }


}
</script>

<style>

</style>