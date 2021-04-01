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

        <v-card tile height="15%" elevation="0"
         class="d-flex justify-center align-center" >
          <h2>[ {{ currentProblem + 1 }}/5  ]</h2>

        </v-card>

        <v-card tile height="72%" elevation="0" class="px-5">
          <v-card class="quiz" tile height="100%" elevation="0" color="black">
            <v-card tile height="70%" elevation="0">
              <div v-for="(line, idx) in quizInfo.quizzes[currentProblem].lines_kr" :key="idx">
                <div v-if="idx%2 == 0" class="pb-4">
                  <p class="pb-2"><span v-if="quizInfo.type !== 'pop'">A: </span>{{ quizInfo.quizzes[currentProblem].lines_kr[idx] }} </p>
                  <p><span v-if="quizInfo.type !== 'pop'">A: </span>{{ quizInfo.quizzes[currentProblem].lines_en[idx] }} </p>
                </div>
                <div v-else class="pb-4">
                  <p class="pb-2"><span v-if="quizInfo.type !== 'pop'">B: </span>{{ myAnswer }} </p>
                  <p class="answer-correct mt-n2"
                   v-if="isCorrect()"> Correct, you may proceed. </p>
                  <p class="answer-wrong mt-n2"
                   v-else-if="isCorrect() == false && pass !== null"
                  >Incorrect, try again.</p>
                  <p><span v-if="quizInfo.type !== 'pop'">B: </span>{{ quizInfo.quizzes[currentProblem].lines_en[idx] }} </p>
                </div>
              </div>
              <div class="d-flex justify-end mt-n3 lesson-source">
                <span> Source : {{ quizInfo.title }} </span>
              </div>

              <div class="d-flex justify-space-between">
                <v-btn plain icon @click="speech"><v-icon>mdi-volume-high</v-icon></v-btn>
                <v-btn plain icon @click="empty()"><v-icon>mdi-restart</v-icon></v-btn>
              </div>
            </v-card>
            <v-card tile height="30%" elevation="0">
              <v-btn v-for="(choice,idx) in choices" :key="idx" 
              @click="putAnswer(choice)" :disabled="checked.includes(choice)"
              class="mx-1 my-2"> {{ choice }} </v-btn>
            </v-card>
          </v-card>

        </v-card>

        <v-card tile height="13%" elevation="0"
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

      // myText: quizInfo.quizzes[this.currentProblem].lines_kr[1].split(' '),
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
    },
    endClass() {
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
      temp[this.order] = choice
      this.order += 1
      this.myAnswer = temp.join(' ')
      if (this.order == temp.length -1 ) {
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
        if ( idx == answer.length -1 ) {
          compare = compare.slice(0, -1)
        }
        if ( compare !== myCompare ) {
          return false
        }
      }
      return true
    },
    createEmptyList() {
      const operators = ['.','!','?']
      var target = this.quizInfo.quizzes[this.currentProblem].lines_kr[1].split(' ')
      var new_line = []
      var last_word = ''
      target.forEach( function(part, index) {
        this[index] = '_____'
      }, new_line)
      for (var operator of operators) {
        if (target[target.length - 1 ].slice(-1) === operator) {
          last_word = operator
        }
      }
      new_line.push(last_word)
      this.myAnswer = new_line.join(' ')
    },
    speech(){
        const text = this.quizInfo.quizzes[this.currentProblem].lines_kr[1]
        let speaker=new SpeechSynthesisUtterance(text);
        const findedVoicer = this.voiceList.find((item)=>{
            return item.name == this.selectedVoicer
        }) 
        console.log(findedVoicer)
        console.log(speaker)

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
      const operators = ['.','!','?']
      var target = this.quizInfo.quizzes[this.currentProblem].lines_kr[1].split(' ')
      for (let i = target.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        for (const operator of operators) {
          if ( target[i].slice(-1) === operator){
            target[i] = target[i].slice(0,-1)
          }
          if ( target[j].slice(-1) === operator){
            target[j] = target[i].slice(0,-1)
          }
        }
        [target[i], target[j]] = [target[j], target[i]];
      }
      return target
    },
  },
  watch: {
    openStudyPage() {
      this.createEmptyList()
    }
  },
  //   async created () {
  //   const voicesList=await this.getVoices();
  //   this.voiceList = voicesList
  // },
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