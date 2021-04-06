<template>
  <v-container >
    <v-dialog
      v-model="showDialog"
      fullscreen
      hide-overlay
      transition="slide-x-reverse-transition"
      scrollable
    >
      <v-card height="100%" width="100%" tile>
        <v-btn
          icon
          class="close-dialog"
          @click="hideDialog"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>

        <v-card tile height="15%" elevation="0"
         class="d-flex justify-center align-center" >
          <h3>[ {{ targetQuestion+1 }}/{{ questions.length }} ]</h3>

        </v-card>

        <v-card tile height="75%" elevation="0">
          <v-card tile height="55%" elevation="0"
          class="px-5">
            <p>Listen carefully and select the correct words in order.</p>
            <div class="px-2" v-for="(line, idx) in questions[targetQuestion].lines_kr" :key="idx">
              <div v-if="questions[targetQuestion].lines_kr.length == 3">
                <p v-if="idx%2 == 0">{{ line }} </p>
                <p v-else>{{ myAnswer }} </p>
              </div>
              <div v-else>
                <p>{{ myAnswer }}</p>
              </div>
            </div>

            <div class="d-flex justify-end mt-n3 test-page">
              <span> Source : {{questions[targetQuestion].source }} </span>
            </div>

            <div class="d-flex justify-space-between mt-2">
              <v-btn fab small dark color="teal accent-4" elevation="3" @click="speech"><v-icon>mdi-volume-high</v-icon></v-btn>
              <v-btn @click="empty(targetQuestion)"><v-icon class="mr-1">mdi-restart</v-icon>reset</v-btn>
            </div>
          </v-card>

          <v-card tile height="45%" elevation="0"
          class="px-5 ">
            <v-btn v-for="(choice,idx) in choices" :key="idx" 
            @click="putAnswer(choice)" :disabled="checked.includes(choice)"
            class="ma-2"> {{ choice.slice(1) }} </v-btn>
          </v-card>

        </v-card>
        
        <v-card tile height="10%" elevation="0"
         class="d-flex align-center px-5" >
          <v-btn text plain @click="previousQuestion" v-if="targetQuestion != 0">
            previous
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn text plain @click="nextQuestion" v-if="targetQuestion != questions.length - 1">
            next
          </v-btn>
          <v-btn text plain @click="submitTest" v-if="targetQuestion == questions.length -1">
            submit
          </v-btn>
        </v-card>
      </v-card>

    </v-dialog>

    <v-dialog
      v-model="showDialog2"
      fullscreen
      hide-overlay
      transition="slide-x-reverse-transition"
      scrollable
    >
      <v-card class="d-flex flex-column" height="100%" width="100%" tile>
        <v-btn
          icon
          class="close-dialog"
          @click="hideDialog"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>
        <v-card tile height="15%" class="d-flex justify-center align-center" elevation="0">
          <h3>Test Report</h3>
        </v-card>

        <v-card tile elevation="0" class="px-8">
          <Experience :experience="grade/10"/>
          <div>
            <h4>Test Result :   {{ grade }}/{{ answers.length * 10 }}</h4>
          </div>

          <div class="mt-5">
            <h4 v-if="myCorrect().length != 0">Correct Answers</h4>
            <div v-for="(correct,idx) in myCorrect()" :key="'correct'+idx"
            class="px-3">
              <p>{{ correct.problemId }}. {{ correct.correctAnswer }} </p>
            </div>
            <h4 v-if="myWrong().length != 0">Incorrect Answers</h4>
            <div v-for="(wrong,idx) in myWrong()" :key="'wrong'+idx"
            class="px-3">
              <p>{{ wrong.problemId }}. {{ wrong.correctAnswer }} </p>
              <p>My Answer : {{ wrong.myAnswer }} </p>
            </div>
          </div>
        </v-card>
        
        <v-spacer></v-spacer>

        <v-card tile class="mb-3 d-flex justify-center" elevation="0">
          <v-btn
            color="primary"
            text
            @click="endTest"
            class="d-flex justify-center"
          >
            end test
          </v-btn>
        </v-card>
      </v-card>
    </v-dialog>
        
  </v-container>
</template>

<script>
import Experience from "@/components/user/Experience.vue"
import { mapState } from "vuex"
import { sendExamResult } from "@/api/exam.js"

import { slump, easyPeasy, becomingPro } from '@/store/achievement.js'


export default {
  props: ['showDialog'],
  components: {
    Experience
  },
  data() {
    return {
      N: this.$store.state.testQuestions.length,
      targetQuestion : 0,
      showDialog2 : false,
      questions: this.$store.state.testQuestions,
      answers: [],
      myAnswers: new Array(this.N).fill([]),
      myAnswer: "",
      order: 0,
      checked: [],
      correct: new Array(this.N).fill(0),
      grade: 0,

      selectedVoicer: 'Microsoft SunHi Online (Natural) - Korean (Korea)',
      voiceList:[],
      textToSpeech:window.speechSynthesis,

    }
  },
  methods: {
    hideDialog() {
      this.defaultSetting()
      this.showDialog2 = false
      this.$emit('hideDialog')
    },
    previousQuestion() {
      this.targetQuestion -= 1
      this.order = 0
      this.checked = []
      this.myAnswer = this.myAnswers[this.targetQuestion]
      if (this.myAnswers[this.targetQuestion][0] != '_') {
        for (var choice of this.choices) {
          this.checked.push(choice)
        }
      }
    },
    nextQuestion() {
      this.targetQuestion += 1
      this.order = 0
      this.checked = []
      this.myAnswer = this.myAnswers[this.targetQuestion]
      if (this.myAnswers[this.targetQuestion][0] != '_') {
        for (var choice of this.choices) {
          this.checked.push(choice)
        }
      }
    },
    empty(idx) {
      this.order = 0
      this.checked = []
      this.createEmptyList(idx)
      this.myAnswer = this.myAnswers[idx]
    },
    endTest() {
      this.defaultSetting()
      this.showDialog2 = false
      this.$emit('hideDialog')
    },
    submitTest() {
      this.order = 0
      this.targetQuestion = 0
      for ( let idx = 0 ; idx < this.answers.length; idx++ ) {
        var flag = 1
        const answer = this.answers[idx].split(' ')
        const myanswer = this.myAnswers[idx].split(' ')

        for ( let idx2 = 0 ; idx2 < answer.length; idx2++ ) {
          var compare = answer[idx2]
          var myCompare = myanswer[idx2]
          if ( compare !== myCompare ) {
            flag = 0
            break
          }
        }

        if ( flag == 1) {
          this.correct[idx] = 1 
          this.grade += 10
        }
      }
      this.showDialog2 = true
      sendExamResult(
        this.grade,
        (res) => {
          console.log("시험성적 보내기", res.data)
          this.$store.dispatch( "getTestGrades" )
        },
        (err) => {
          console.log(err)
        }
      )

      if ( slump( this.grade, this.myCompleteAchievement ) ) {
        this.$store.dispatch('completeAchieve', 4)
      }
      if ( easyPeasy( this.grade, this.myCompleteAchievement ) ) {
        this.$store.dispatch('completeAchieve', 5)
      }
      if ( becomingPro( this.grade, this.myCompleteAchievement ) ) {
        this.$store.dispatch('completeAchieve', 9)
      }

      this.$store.dispatch('gainExperience', this.grade/10)
      this.$store.dispatch( "changeChance", "test")
    },
    myCorrect() {
      const correctList = []
      for ( let idx = 0 ; idx < this.answers.length; idx++ ) {
        if (this.correct[idx] == 1 ) {
          const form = {
            problemId: idx +1, correctAnswer: this.answers[idx], myAnswer: this.myAnswers[idx]
          }
          correctList.push(form)
        }
      }
      return correctList
    },
    myWrong() {
      const wrongList = []
      for ( let idx = 0 ; idx < this.answers.length; idx++ ) {
        if (this.correct[idx] == 0 ) {
          var myAnswer = this.myAnswers[idx]
          if ( myAnswer[0] == '_') {
            myAnswer = "No Answer Given"
          }
          const form = {
            problemId: idx +1, correctAnswer: this.answers[idx], myAnswer: myAnswer
          }
          wrongList.push(form)
        }
      }
      return wrongList
    },
    putAnswer(choice) {
      const temp = this.myAnswer.split(" ")
      this.checked.push(choice)
      temp[this.order] = choice.slice(1)
      this.order += 1
      this.myAnswer = temp.join(' ')
      if (this.order == temp.length ) {
        this.myAnswers[this.targetQuestion] = this.myAnswer
      }
    },
    createEmptyList(idx) {
      var target = this.answers[idx].split(' ')
      var new_line = []
      target.forEach( function(part, index) {
        this[index] = '_____'
      }, new_line)
      this.myAnswers[idx] = new_line.join(' ')
    },
    defaultSetting() {
      for (let idx = 0 ; idx < this.answers.length; idx++) {
        this.createEmptyList(idx)
      }
      this.myAnswer = this.myAnswers[0]
      this.correct = new Array(this.N).fill(0)
      this.order = 0
      this.targetQuestion = 0
      this.grade = 0
      this.checked = []
    },
    speech() {
        const text = []
        if (this.questions[this.targetQuestion].lines_kr.length == 3) {
          text.push(this.questions[this.targetQuestion].lines_kr[1])
        }
        else {
          text.push(this.questions[this.targetQuestion].lines_kr[0])
        }
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
  async created() {

    for (let answer of this.testQuestions) {
      if ( answer.lines_kr.length == 3 ) {
        this.answers.push(answer.lines_kr[1])
      } else {
        this.answers.push(answer.lines_kr[0])
      }
    }

    this.defaultSetting()

    const voicesList=await this.getVoices();
    this.voiceList = voicesList

  },
  computed: {
    ...mapState([ "testQuestions", "myCompleteAchievement" ]),
    choices() {
      var target = this.answers[this.targetQuestion].split(' ')
      var newList = []
      for (var word in target) {
        newList.push(String(word)+target[word])
      }
      for (let i = newList.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [newList[i], newList[j]] = [newList[j], newList[i]];
      }
      return newList
    },

  },
}
</script>

<style>

.test-page span {
  color: grey;
  font-size: 0.7em;
}

</style>