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

          <v-card tile height="70%" elevation="0"
          class="">
            {{ questions[targetQuestion].source }}
          </v-card>

          <v-card tile height="30%" elevation="0">
            {{ answers[targetQuestion] }}
          </v-card>

        </v-card>
        
        <v-card tile height="10%" elevation="0"
         class="d-flex justify-end align-center" >
          <v-btn text plain @click="previousQuestion" v-if="targetQuestion != 0">
            이전으로
          </v-btn>
          <v-btn text plain @click="nextQuestion" v-if="targetQuestion != questions.length - 1">
            다음으로
          </v-btn>
          <v-btn text plain @click="submitTest" v-if="targetQuestion == questions.length -1">
            제출하기
          </v-btn>
        </v-card>
      </v-card>

    </v-dialog>

    <v-dialog
      v-model="showDialog2"
      max-width="500px"
    >
      <v-card>
        <v-card-title>
          Dialog 2
        </v-card-title>
        <v-card-text>
        </v-card-text>
        <v-card-actions>
          <v-btn
            color="primary"
            text
            @click="endTest"
          >
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
        
  </v-container>
</template>

<script>
export default {
  props: ['showDialog'],
  data() {
    return {
      targetQuestion : 0,
      showDialog2 : false,
      questions: [
        {source : "태양의 후예", 
        lines_kr : ["오늘 저녁에 뭐 먹었어?", "나는 오늘 저녁으로 고기를 먹었어.","오, 맛있었니?"],
        lines_en : ["What did you have for dinner?", "I had proteins for dinner.","Wow, how was it?"]},
        {source : "도깨비", 
        lines_kr : ["나랑 벚꽃축제 갈래?", "좋아, 벚꽃 보러 가고 싶었어.","그러면 토요일 어때?"],
        lines_en : ["Do you want to go to the cherry blossom festival with me?", "Yes, I would love to go see cherry blossoms.","Saturday sounds good?"]},
      ],
      answers: new Array(2).fill(""),

    }
  },
  methods: {
    hideDialog() {
      this.$emit('hideDialog')
    },
    previousQuestion() {
      this.targetQuestion -= 1
      console.log(this.targetQuestion)
    },
    nextQuestion() {
      this.targetQuestion += 1
      console.log(this.targetQuestion)
    },
    endTest() {
      this.showDialog2 = false
      this.$emit('hideDialog')
    },
    submitTest() {
      this.showDialog2 = true
    }
  },
  created() {
    this.answers[0] = "hello1"
    this.answers[1] = "hello2"
  }
}
</script>

<style>

</style>