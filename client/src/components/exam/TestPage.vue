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
            <div v-for="(line, idx) in questions[targetQuestion].lines_kr" :key="idx">
              <div v-if="questions[targetQuestion].lines_kr.length == 3">
                <p v-if="idx%2 == 0"> A: {{ line }} </p>
                <p v-else> B: {{ myAnswer }} </p>
              </div>
              <div v-else>
                <p> A: {{ myAnswer }}</p>
              </div>
            </div>

            <div class="d-flex justify-end">
              <p> Source : {{questions[targetQuestion].source }} </p>
            </div>

            <div class="d-flex justify-space-between">
              <v-btn plain icon><v-icon>mdi-volume-high</v-icon></v-btn>
              <v-btn plain icon @click="empty(targetQuestion)"><v-icon>mdi-restart</v-icon></v-btn>
            </div>
          </v-card>

          <v-card tile height="45%" elevation="0"
          class="px-5 ">
            <v-btn v-for="(choice,idx) in choices" :key="idx" 
            @click="putAnswer(choice)" :disabled="checked.includes(choice)"
            class="ma-2"> {{ choice }} </v-btn>
          </v-card>

        </v-card>
        
        <v-card tile height="10%" elevation="0"
         class="d-flex justify-end align-center" >
          <v-btn text plain @click="previousQuestion" v-if="targetQuestion != 0">
            previous
          </v-btn>
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

        <v-card elevation="0" class="px-8">
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
          <Experience :experience="grade/10"/>
        </v-card>
        
        <v-spacer></v-spacer>

        <v-card class="mb-3 d-flex justify-center" elevation="0">
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

export default {
  props: ['showDialog'],
  components: {
    Experience
  },
  data() {
    return {
      targetQuestion : 0,
      showDialog2 : false,
      questions: [
        {source : "태양의 후예", 
        lines_kr : ["오늘 저녁에 뭐 먹었어?", "나는 오늘 저녁으로 고기를 먹었어.","오, 맛있었니?"],
        lines_en : ["What did you have for dinner?", "I had proteins for dinner.","Wow, how was it?"]},
        {source : "도깨비", 
        lines_kr : ["나랑 벚꽃축제 갈래?", "너무 좋아 나도 벚꽃 보러 가고 싶었어.","그러면 토요일 어때?"],
        lines_en : ["Do you want to go to the cherry blossom festival with me?", "Yes, I would love to go see cherry blossoms.","Saturday sounds good?"]},
        {source : "뉴스",
        lines_kr : ["이렇게 한줄로만 나오는 문제도 있다."],
        lines_en : ["There are questions that only have one sentence."]}
      ],
      answers: [ "나는 오늘 저녁으로 고기를 먹었어.", "너무 좋아, 나도 벚꽃 보러 가고 싶었어.","이렇게 한줄로만 나오는 문제도 있다."],
      myAnswers: new Array(3).fill([]),
      myAnswer: "",
      order: 0,
      checked: [],
      correct: new Array(3).fill(0),
      grade: 0

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
          if ( idx2 == answer.length - 1 ) {
            compare = compare.slice(0,-1)
          } 
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
      this.$store.dispatch('gainExperience', this.grade/10)
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
      temp[this.order] = choice
      this.order += 1
      this.myAnswer = temp.join(' ')
      if (this.order == temp.length -1 ) {
        this.myAnswers[this.targetQuestion] = this.myAnswer
      }
    },
    createEmptyList(idx) {
      const operators = ['.','!','?']
      var target = this.answers[idx].split(' ')
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
      this.myAnswers[idx] = new_line.join(' ')
    },
    defaultSetting() {
      for (let idx = 0 ; idx < this.answers.length; idx++) {
        this.createEmptyList(idx)
      }
      this.myAnswer = this.myAnswers[0]
      this.correct = new Array(3).fill(0)
      this.order = 0
      this.targetQuestion = 0
      this.grade = 0
    }
  },
  created() {
    this.defaultSetting()
  },
  computed: {
    choices() {
      const operators = ['.','!','?']
      var target = this.answers[this.targetQuestion].split(' ')
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

  }
}
</script>

<style>

</style>