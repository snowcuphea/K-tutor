<template>
  <v-container class="px-5 d-flex flex-column">

    <div class="d-flex flex-column">
      <div class="d-flex">
        <h3> Report Card </h3>
        <v-spacer></v-spacer>
        
        <div>
          <v-icon v-for="left in chanceUsed()" :key="left">mdi-heart</v-icon>
        </div>
        <div>
          <v-icon v-for="used in testChance" :key="used" color="red">mdi-heart</v-icon>
        </div>
      </div>
      <GradeChart />
      <p class="mt-2" v-if="average">Average of last {{ userGrade_score.length }} exams: {{ average }} </p>
      <p class="mt-2" v-else>Take a test to get information.</p>
    </div>

    <Experience :experience="-1" />

    <div class="d-flex justify-center">
      <v-btn elevation="2" class="main-bg-color-imp mt-5 text-subtitle-1" large dark @click="startTest">Take a Test</v-btn>
    </div>
    <TestPage :showDialog="showDialog" @hideDialog="showDialog = !showDialog" v-if="showDialog"/>
    
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
      nowTime: new Date(),
      showDialog: false,
    }
  },
  methods: {
    chanceUsed() {
      return 2-this.testChance
    },
    ableTest() {
      if ( this.recent_learned_lc.length > 9 ) {
        return true
      } else {
        return false
      }
    },
    startTest() {
      if (this.ableTest() && this.testChance != 0 ){
        this.$store.dispatch( "getTestQuestions" )
        this.showDialog = !this.showDialog
      } else if ( this.testChance == 0 ) {
        const alertInfo = {
          status: true,
          color: "warning",
          content: "Used all test coins for today."
        }
        this.$store.dispatch("showAlert", alertInfo)
      } else {
        const alertInfo = {
          status: true,
          color: "warning",
          content: "Take 10 lessons before taking a test."
        }
        this.$store.dispatch("showAlert", alertInfo)
      }
    },

  },
  computed: {
    ...mapState([ "userGrade_score", "recent_learned_lc", "testChance", "time" ]),

    average() {
      var total = 0
      this.userGrade_score.forEach(element => {
        total += element
      });

      if (this.userGrade_score.length) {
        var avg = total/this.userGrade_score.length
      } else {
        avg = 0
      }
      

      return avg
    }
  },
  created() {
    // 시험 내용 요청 보내서 store에 저장
    if (this.ableTest()) {
      this.$store.dispatch( "getTestQuestions" )
    }
    // console.log(this.time, this.nowTime.getDate())
    if ( this.nowTime.getDate() !== this.time ) {
      console.log(this.time, this.nowTime.getDate())
      this.$store.dispatch( 'resetChance', this.nowTime.getDate() )
    }
    
    this.$store.dispatch( 'getTestGrades' )
  }


}
</script>

<style>

</style>