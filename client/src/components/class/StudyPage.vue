<template>
  <v-container>
    <v-dialog
      v-model="openStudyPage"
      fullscreen
      hide-overlay
      transition="slide-x-reverse-transition"
      scrollable
    >
      <v-card height="100%" width="100%" tile>
        <v-btn
          icon
          class="close-dialog"
          @click="closeStudyPage"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>

        <v-card tile height="15%" elevation="0"
         class="d-flex justify-center align-center" >
          <h3>Step {{ currentStep }}. {{ stepName[currentStep] }} </h3>

        </v-card>

        <v-card tile height="72%" elevation="0" class="px-5">
          <div v-if="currentStep == 1">
            step1
          </div>

          <div v-else-if="currentStep == 2">
            step2
          
          </div>

          <div v-else>
            step3
          </div>


        </v-card>

        <v-card tile height="13%" elevation="0"
         class="d-flex justify-end align-center pr-5" >
          <v-btn text plain @click="currentStep -= 1" v-if="currentStep != 1">
            previous
          </v-btn>
          <v-btn text plain @click="currentStep += 1" v-if="currentStep != 3">
            next
          </v-btn>
          <v-btn text plain @click="submitLesson" v-if="currentStep == 3 ">
            Finish
          </v-btn>
        </v-card>

      </v-card>
    </v-dialog>

    <v-dialog
      v-model="resultDialog"
      persistent
    >
      <v-card class="d-flex flex-column pt-8" height="100%" width="100%" tile>
        <v-card tile class="d-flex flex-column justify-center align-center" elevation="0">
          <h3>Congratulations</h3>
          <h4>You've gained 3 points</h4>
        </v-card>
        <v-card tile elevation="0" class="px-8">
          <Experience :experience="exp"/>
        </v-card>
      </v-card>

      <v-card tile class="d-flex justify-center pb-8" elevation="0">
        <v-btn
          color=""
          text
          @click="endClass"
          class="d-flex justify-center"
        >
          Stop
        </v-btn>
        <v-btn
          color="primary"
          text
          @click="nextLesson"
          class="d-flex justify-center"
        >
          More
        </v-btn>
      </v-card>

    </v-dialog>



  </v-container>
</template>

<script>
import { mapState } from 'vuex'

import Experience from "@/components/user/Experience.vue"

export default {
  props: ["openStudyPage"],
  data() {
    return {
      currentStep: 1,
      stepName: [null, "Go Through", "Learn", "Practice"],
      resultDialog: false,
      exp: 0,
    }
  },
  components: {
    Experience
  },
  methods:{
    closeStudyPage() {
      this.$emit('closeStudyPage')
    },
    submitLesson() {
      this.resultDialog = !this.resultDialog
      this.exp = 3
      // this.$store.dispatch('gainExperience', this.exp)
    },
    nextLesson() {
      console.log("hi")
    },
    endClass() {
      this.currentStep = 1
      this.resultDialog = !this.resultDialog
      this.$emit('closeStudyPage')
    }
  },
  computed: {
    ...mapState([ "lessonInfo" ])
  },

}
</script>

<style>

</style>