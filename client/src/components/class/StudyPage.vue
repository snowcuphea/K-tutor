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

        <v-card tile height="13%" elevation="0"
         class="d-flex justify-center align-center" >
          <h2>Step {{ currentStep }}. {{ stepName[currentStep] }} </h2>

        </v-card>

        <v-card tile height="76%" elevation="0" class="px-5">

          <!-- step1 -->
          <v-card class="step1" v-if="currentStep == 1" tile height="100%" elevation="0">
            <v-card tile height="40%" elevation="0">
              <img :src="require(`@/assets/images/card/${lessonInfo.imgurl}`)"   
               alt="포스터 이미지" width="100%">
              <!-- <img :src="require(`@/assets/images/poster/poster1.jpg`)"
               alt="포스터 이미지" height="100%" width="100%"> -->
               <!-- <v-text>@/assets/images/card/{{lessonInfo.imgurl}}</v-text> -->
            </v-card>
            <v-card tile height="60%" elevation="0" class="d-flex flex-column pt-2 px-2">
              <v-btn class="mb-4" fab small dark color="teal accent-4" @click="speech"><v-icon>mdi-volume-high</v-icon></v-btn>
              <div v-for="(line, idx) in lessonInfo.lines_kr" :key="idx">
                <div v-if="idx%2 == 0" class="pb-2">
                  <p>{{ lessonInfo.lines_kr[idx] }} </p>
                  <p>{{ lessonInfo.lines_en[idx] }} </p>
                </div>
                <div v-else class="pb-2">
                  <p>{{ lessonInfo.lines_kr[idx] }} </p>
                  <p>{{ lessonInfo.lines_en[idx] }} </p>
                </div>
              </div>
              <div class="d-flex justify-end mt-n3 lesson-source">
                <span> Source : {{ lessonInfo.title }} </span>
              </div>
            </v-card>
          </v-card>

          <!-- step2 -->
          <v-card class="step2" v-else-if="currentStep == 2" tile height="100%" elevation="0">
            <v-card tile height="25%" elevation="0" class="d-flex flex-column">
              <div class="d-flex align-center justify-space-between">
                <h3>[ Key Sentence ]</h3>
                <v-btn fab small dark @click="speech_keysentence"><v-icon>mdi-volume-high</v-icon></v-btn>
              </div>
              <div class="pl-5 pt-2">
                <p> {{ lessonInfo.lines_kr[1] }} </p>
                <p> {{ lessonInfo.lines_en[1] }} </p>
              </div>
            </v-card>
            <v-card tile height="25%" elevation="0" class="pt-4">
              <div class="d-flex align-center justify-space-between">
                <h3>[ Key Word ]</h3>
                <!-- <v-btn plain icon class=""><v-icon>mdi-volume-high</v-icon></v-btn> -->
              </div>
              <div class="pl-5 pt-2">
                <p> {{ lessonInfo.keyword_kr }} </p>
                <p> {{ lessonInfo.keyword_en }} </p>
              </div>
            </v-card>
            <v-card tile height="50%" elevation="0">
              <div class="d-flex align-center justify-space-between">
                <h3>[ Example ]</h3>
                <v-btn fab small dark class="" @click="speech_example"><v-icon>mdi-volume-high</v-icon></v-btn>
              </div>
              <div class="pl-5 pt-2" v-for="(example, idx) in lessonInfo.example_kr" :key="idx">
                <p>{{ lessonInfo.example_kr[idx] }} </p>
                <p class="pt-3"> {{ lessonInfo.example_en[idx] }} </p>
              </div>
            </v-card>
          </v-card>

          <!-- step3 -->
          <v-card class="step3" v-else tile height="100%" elevation="0" color="black">
            <v-card tile height="70%" elevation="0">
              <div v-for="(line, idx) in lessonInfo.lines_kr" :key="idx">
                <div v-if="idx%2 == 0" class="pb-4">
                  <p class="pb-2">{{ lessonInfo.lines_kr[idx] }} </p>
                  <p>{{ lessonInfo.lines_en[idx] }} </p>
                </div>
                <div v-else class="pb-4">
                  <p class="pb-2">{{ myAnswer }} </p>
                  <p class="answer-correct mt-n2"
                   v-if="pass"> Correct, you may proceed. </p>
                  <p class="answer-wrong mt-n2"
                   v-else-if="pass == false && pass !== null"
                  >Incorrect, try again.</p>
                  <p>{{ lessonInfo.lines_en[idx] }} </p>
                </div>
              </div>
              <div class="d-flex justify-end mt-n3 lesson-source">
                <span> Source : {{ lessonInfo.title }} </span>
              </div>

              <div class="d-flex justify-space-between">
                <v-btn fab small dark class="ml-1" @click="speech_keysentence"><v-icon>mdi-volume-high</v-icon></v-btn>
                <v-btn plain icon @click="empty()"><v-icon>mdi-restart</v-icon></v-btn>
              </div>
            </v-card>
            <v-card tile height="30%" elevation="0">
              <v-btn v-for="(choice,idx) in choices" :key="idx" 
              @click="putAnswer(choice)" :disabled="checked.includes(choice)"
              class="mx-1 my-2"> {{ choice.slice(1) }} </v-btn>
            </v-card>
          </v-card>



        </v-card>

        <v-card tile height="11%" elevation="0"
         class="d-flex align-center px-5" >
          <v-btn text plain @click="currentStep -= 1" v-if="currentStep != 1">
            previous
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn text plain @click="nextStep" v-if="currentStep != 3">
            next
          </v-btn>
          <v-btn text plain @click="submitLesson" v-if="currentStep == 3" :disabled="!pass">
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
          v-if="this.currentClassIndex !== classList.length-1"
        >
          More
        </v-btn>
      </v-card>

    </v-dialog>



  </v-container>
</template>

<script>
import { mapState,mapGetters } from 'vuex'

import Experience from "@/components/user/Experience.vue"



export default {
  props: ["openStudyPage"],
  data() {
    return {
      currentStep: 1,
      stepName: [null, "Go Through", "Learn", "Practice"],
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
    closeStudyPage() {
      this.defaultSetting()
      this.$emit('closeStudyPage')
    },
    submitLesson() {
      if (this.getCurrentClassLearnedKeword.length == 0) {
        this.$store.dispatch('addtoProgressList')
      }
      this.resultDialog = !this.resultDialog
      this.exp = 3
      for ( let learned of this.getCurrentClassLearnedKeword ){
        if (this.lessonInfo.id == learned.id) {
          this.exp = 0
        }

      }
      if ( this.exp !== 0) {
        this.$store.dispatch('gainExperience', this.exp)
        this.$store.dispatch('sendCompleteLesson', this.currentClassIndex)
      }
    },
    nextStep() {
      this.currentStep += 1
      this.createEmptyList()
    },
    nextLesson() {
      this.defaultSetting()
      this.resultDialog = !this.resultDialog
      this.$store.dispatch('changeCurrentClassIndex', this.currentClassIndex+1)
      this.$store.dispatch('getLessonInfoByItem', this.classList[this.currentClassIndex].id )
    },
    endClass() {
      this.defaultSetting()
      this.resultDialog = !this.resultDialog
      this.$emit('closeStudyPage')
    },
    defaultSetting() {
      this.currentStep = 1
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
      temp[this.order] = choice.slice(1)
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
      const answer = this.lessonInfo.lines_kr[1].split(' ')
      const myanswer = this.myAnswer.split(' ')
      // const operators = ['.','!','?']
      for ( let idx = 0; idx < answer.length ; idx++) {
        var compare = answer[idx]
        var myCompare = myanswer[idx]
        // if ( idx == answer.length -1 ) {
        //   for (var operator of operators) {
        //     if (compare.slice(-1) === operator) {
        //       compare = compare.slice(0,-1)
        //     }
        //   }
        // }
        if ( compare !== myCompare ) {
          console.log(compare, myCompare)
          return false
        }
      }
      return true
    },
    createEmptyList() {
      // const operators = ['.','!','?']
      var target = this.lessonInfo.lines_kr[1].split(' ')
      var new_line = []
      // var last_word = ''
      target.forEach( function(part, index) {
        this[index] = '_____'
      }, new_line)
      // for (var operator of operators) {
      //   if (target[target.length - 1 ].slice(-1) === operator) {
      //     last_word = operator
      //   }
      // }
      // new_line.push(last_word)
      this.myAnswer = new_line.join(' ')
    },
    speech(){
          const text = []
          var cnt = 0
          while (cnt < 3) {
            text.push(this.lessonInfo.lines_kr[cnt])
            cnt += 1
          }
          let speaker=new SpeechSynthesisUtterance(text);
          const findedVoicer = this.voiceList.find((item)=>{
              return item.name == this.selectedVoicer
          }) 
          // console.log(findedVoicer)
          // console.log(speaker)

          speaker.voice=findedVoicer;
          speaker.volume=0.5;
          this.textToSpeech.speak(speaker)
      },
      speech_keysentence(){
        const text = this.lessonInfo.lines_kr[1]
        let speaker=new SpeechSynthesisUtterance(text);
          const findedVoicer = this.voiceList.find((item)=>{
              return item.name == this.selectedVoicer
          }) 
          // console.log(findedVoicer)
          // console.log(speaker)

          speaker.voice=findedVoicer;
          speaker.volume=0.5;
          this.textToSpeech.speak(speaker)
      },
      speech_example(){
        const text = []
        var cnt = 0
        while (cnt < 1) {
          text.push(this.lessonInfo.example_kr[cnt])
          cnt += 1
        }
        let speaker=new SpeechSynthesisUtterance(text);
          const findedVoicer = this.voiceList.find((item)=>{
              return item.name == this.selectedVoicer
          }) 
          // console.log(findedVoicer)
          // console.log(speaker)

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
    ...mapState([ "lessonInfo", "currentClassIndex", "classList"]),
    ...mapGetters(["getCurrentClassLearnedKeword"]),
    choices() {
      var target = this.lessonInfo.lines_kr[1].split(' ')
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
  watch: {
    openStudyPage() {
      this.createEmptyList()
    }
  },
  async created() {
    this.createEmptyList()
    const voicesList=await this.getVoices();
    this.voiceList = voicesList
  }

}
</script>

<style>

.step1 p {
  margin-bottom: 0 !important;
}

.step2 p {
  margin-bottom: 0 !important;
}

.step3 p {
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