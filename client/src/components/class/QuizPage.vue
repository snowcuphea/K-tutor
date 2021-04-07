<template>
  <v-container>
    <v-dialog
      v-model="openQuizPage"
      fullscreen
      hide-overlay
      transition="slide-x-reverse-transition"
      scrollable
    >
      <v-card height="100%" width="100%" tile>
        <v-btn
          icon
          class="close-dialog"
          @click="closeQuizPage"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>

        <v-card tile height="13%" elevation="0"
         class="d-flex justify-center align-center" >
          <h2>[ {{ currentProblem + 1 }}/5  ]</h2>

        </v-card>

        <v-card tile height="76%" elevation="0" class="px-5">
          <v-card class="quiz" tile height="100%" elevation="0">
            <v-card tile elevation="0">
              <div class="px-2" v-for="(line, idx) in quizInfo.quizzes[currentProblem].lines_kr" :key="idx">
                <div v-if="idx%2 == 0" class="pb-4">
                  <p class="pb-2">{{ quizInfo.quizzes[currentProblem].lines_kr[idx] }} </p>
                  <p>{{ quizInfo.quizzes[currentProblem].lines_en[idx] }} </p>
                </div>
                <div v-else class="pb-4">
                  <p class="pb-2">{{ myAnswer }} </p>
                  <p class="answer-correct mt-n2"
                   v-if="pass"> Correct, you may proceed. </p>
                  <p class="answer-wrong mt-n2"
                   v-else-if="pass == false && pass !== null"
                  >Incorrect, try again.</p>
                  <p>{{ quizInfo.quizzes[currentProblem].lines_en[idx] }} </p>
                </div>
              </div>
              <div class="d-flex justify-end mt-n3 lesson-source">
                <span> Source : {{ quizInfo.title }} </span>
              </div>

              <div class="d-flex justify-space-between">
                <v-btn fab small dark color="teal accent-4" elevation="3" @click="speech"><v-icon>mdi-volume-high</v-icon></v-btn>
                <v-btn @click="empty()"><v-icon class="mr-1">mdi-restart</v-icon>reset</v-btn>
              </div>
            </v-card>
            <v-card tile elevation="0" class="mt-3">
              <v-btn v-for="(choice,idx) in choices" :key="idx" 
              @click="putAnswer(choice)" color="orange lighten-5" :disabled="checked.includes(choice)"
              class="mx-1 my-2"> {{ choice.slice(2) }} </v-btn>
            </v-card>
          </v-card>

        </v-card>

        <v-card tile height="11%" elevation="0"
         class="d-flex align-center px-5" >
          <v-spacer></v-spacer>
          <v-btn text plain @click="nextProblem" v-if="currentProblem != 4" :disabled="!pass">
            next
          </v-btn>
          <v-btn text plain @click="submitQuiz" v-if="currentProblem == 4" :disabled="!pass">
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
          <h4>You've gained 5 points</h4>
        </v-card>
        <v-card tile elevation="0" class="px-8">
          <Experience :experience="exp"/>
        </v-card>
      </v-card>

      <v-card tile class="d-flex justify-center pb-8" elevation="0">
        <v-btn
          color=""
          text
          @click="endQuiz"
          class="d-flex justify-center"
        >
          close
        </v-btn>
      </v-card>

    </v-dialog>



  </v-container>
</template>

<script>
import { mapState } from 'vuex'

import Experience from "@/components/user/Experience.vue"



export default {
  props: ["openQuizPage"],
  data() {
    return {
      currentProblem: 0,
      resultDialog: false,
      exp: 0,
      
      myAnswer: "",
      checked: [],
      order: 0,
      pass: null,

      selectedVoicer: 'Microsoft SunHi Online (Natural) - Korean (Korea)',
      voiceList:[],
      textToSpeech:window.speechSynthesis,
    }
  },
  components: {
    Experience
  },
  methods:{
    closeQuizPage() {
      this.defaultSetting()
      this.$emit('closeQuizPage')
    },
    nextProblem() {
      this.currentProblem += 1
      this.checked = []
      this.pass = null
      this.order = 0
      this.createEmptyList()
    },
    submitQuiz() {
      this.resultDialog = !this.resultDialog
      this.exp = 5
      this.$store.dispatch('gainExperience', this.exp)
      this.$store.dispatch( "changeChance", "quiz")
    },
    endQuiz() {
      this.defaultSetting()
      this.resultDialog = !this.resultDialog
      this.$emit('closeQuizPage')
    },
    defaultSetting() {
      this.currentProblem = 0
      this.exp = 0
      this.order = 0
      this.myAnswer = ''
      this.checked = []
      this.pass = null
    },
    empty() {
      this.order = 0
      this.checked = []
      this.pass = null
      this.createEmptyList()
    },
    putAnswer(choice) {
      const temp = this.myAnswer.split(" ")
      this.checked.push(choice)
      temp[this.order] = choice.slice(2)
      this.order += 1
      this.myAnswer = temp.join(' ')
      if (this.order == temp.length ) {
        if (this.isCorrect()) {
          this.pass = true
        } else {
          this.pass = false
        }
      }
    },
    isCorrect() {
      const answer = this.quizInfo.quizzes[this.currentProblem].lines_kr[1].split(' ')
      const myanswer = this.myAnswer.split(' ')
      for ( let idx = 0; idx < answer.length ; idx++) {
        var compare = answer[idx]
        var myCompare = myanswer[idx]
        if ( compare !== myCompare ) {
          return false
        }
      }
      return true
    },
    createEmptyList() {
      var target = this.quizInfo.quizzes[this.currentProblem].lines_kr[1].split(' ')
      var new_line = []
      target.forEach( function(part, index) {
        this[index] = '_____'
      }, new_line)
      this.myAnswer = new_line.join(' ')
    },
    speech(){
        const text = this.quizInfo.quizzes[this.currentProblem].lines_kr[1]
        let speaker=new SpeechSynthesisUtterance(text);
        const findedVoicer = this.voiceList.find((item)=>{
            return item.name == this.selectedVoicer
        }) 
        speaker.voice=findedVoicer;
        speaker.volume=0.5;
        this.textToSpeech.speak(speaker)
    },
    async getVoices(){
        let interval;
        return new Promise((resolve)=>{
            interval=setInterval(()=>{
                if(this.textToSpeech.getVoices().length){
                    resolve(this.textToSpeech.getVoices())
                    clearInterval(interval)
                }
            },100)
        })
    }
  },
  computed: {
    ...mapState([ "quizInfo" ]),
    choices() {
      var target = this.quizInfo.quizzes[this.currentProblem].lines_kr[1].split(' ')
      var newList = []
      for (var word in target) {
        if ( word < 10 ) {
          newList.push("0"+String(word)+target[word])
        } else {
          newList.push(String(word)+target[word])
        }
      }
      for (let i = newList.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [newList[i], newList[j]] = [newList[j], newList[i]];
      }
      return newList
    },
  },
  watch: {
    quizInfo() {
      this.createEmptyList()
    }
  },
  async created() {
    this.createEmptyList()
    const voicesList=await this.getVoices();
    this.voiceList = voicesList
  },

}
</script>

<style>

.quiz p {
  margin-bottom: 0 !important;
}

.lesson-source span {
  color: grey;
  font-size: 0.7em;
}

.answer-correct {
  color: green;
  font-size: 0.9em;
}

.answer-wrong {
  color: red;
  font-size: 0.9em;
}

</style>