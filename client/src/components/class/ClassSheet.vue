<template>
  <v-container id="classSheet">
    <v-row>
      <v-col class="d-flex flex-column justify-center align-center">
        <h2> {{currentClass.name_kor}} </h2>
        <h2> {{currentClass.name_eng}} </h2>
      </v-col>
    </v-row>

    <v-row>
      <v-col>
        <img :src="require(`@/assets/images/poster/${currentClass.imgurl}`)" alt="title" class="imgSize">
        <!-- <img :src="require(`@/assets/images/poster/poster1.jpg`)" alt="title" class="imgSize"> -->
      </v-col>
    </v-row>

    <v-row no-gutters>
      <v-col class="my-1">
        <div class="d-flex justify-end">
          <span class="text--secondary">chances: </span>
          <div class="d-flex">
            <v-icon v-for="left in chanceUsed()" :key="left" small>mdi-heart</v-icon>
          </div>
          <div  class="d-flex">
            <v-icon v-for="used in quizChance" :key="used" color="red" small>mdi-heart</v-icon>
          </div>
        </div>
      </v-col>
    </v-row>

    <v-row no-gutters >
      <v-col cols="8" class="d-flex align-center" >
        <span v-if="currentClass.level == 0">Difficulty: Beginner</span>
        <span v-else-if="currentClass.level == 1">Difficulty: Intermediate</span>
        <span v-else-if="currentClass.level == 2">Difficulty: Advanced</span>
        <span v-else>Difficulty: Basic</span>
      </v-col>
      <v-col cols="4" class="d-flex justify-end">
        <v-btn class="main-bg-color-imp" dark rounded  @click="startQuiz()"> quiz </v-btn>
      </v-col>
    </v-row>

    

    <v-row>
      <v-col>
        <div class="d-flex">
          <p class="mb-1 mr-1">Learning Progress</p>
           <v-icon>
            mdi-progress-check
          </v-icon>
          <v-spacer></v-spacer>
          <p class="mb-0">{{getCurrentClassLearnedKeword.length}}/ {{classList.length}}</p>
        </div>
        <v-progress-linear :value="progress" height="10" color="teal accent-4" striped>
        </v-progress-linear>

      </v-col>
    
      
    </v-row>

    <v-row>
      <v-col>
        <v-card class="my-1 mx-2" v-for="(item,idx) in classList" :key="item.main_kw_word" @click="startClass(item, idx)">
          <v-card-text>
            <v-row>
              <v-col cols="1" xs="1" class="d-flex justify-center align-center">
                <span>{{idx+1}}</span>
              </v-col>
              <v-col cols="4" xs="4" style="" class="d-flex justify-center">
                <!-- <img :src="require(`@/assets/images/poster/poster1.jpg`)" alt="keyword" class="imgSize"> -->
                <img :src="require(`@/assets/images/card/${item.imgurl}`)" alt="keyword" class="imgSize">
              </v-col>
              <v-col cols="5" xs="6" class="d-flex align-center">
                <div class="d-flex flex-column ">
                  <h3 class="text--primary my-1"> {{item.main_kw_kor}}</h3>
                  <span class=""> {{ item.main_kw_eng }} </span>
                </div>
              </v-col>
              <v-col cols="2" xs="1" class="d-flex align-center justify-center">
                <!-- item.cs_seq가 getCurrentClassLearnedKeword의 cs_seq에 있는지 검사해서 완료여부도 넣어야됨 -->
                <!-- <v-icon v-if="checkCompleted(item.id)" color="green darken-2">mdi-checkbox-marked-circle</v-icon>  -->
                <v-icon v-if="checkCompleted(item.id)" color="teal accent-4">mdi-checkbox-marked-circle</v-icon> 
                <v-icon v-else color="blue-grey darken-2">mdi-checkbox-marked-circle-outline</v-icon> 
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <StudyPage :openStudyPage="openStudyPage" @closeStudyPage="endClass" v-if="!(Object.entries(lessonInfo).length === 0 && lessonInfo.constructor === Object)"/>
    <QuizPage :openQuizPage="openQuizPage" @closeQuizPage="endQuiz" v-if="!(Object.entries(quizInfo).length === 0 && quizInfo.constructor === Object)" />

  </v-container>
</template>

<script>
  import StudyPage from "@/components/class/StudyPage.vue"
  import QuizPage from "@/components/class/QuizPage.vue"

  import {
    mapState, mapGetters
  } from 'vuex'

  export default {
    name: "ClassSheet",
    components: {
      StudyPage,
      QuizPage
    },
    data: () => ({
      openStudyPage: false,
      openQuizPage: false,
    }),
    props: {
      classInfo: [Object, String],

    },
    methods: {
      chanceUsed() {
        return 3 - this.quizChance
      },
      startClass(item, idx) {
        // 서버에 요청을 보내서 해당 학습 내용을 받아온다
        // this.$store.dispatch('changeCurrentClass', item)
        this.$store.dispatch('getLessonInfoByItem',item.id )
        this.$store.dispatch('changeCurrentClassIndex', idx)
        this.openStudyPage = !this.openStudyPage
      },
      endClass() {
        this.openStudyPage = !this.openStudyPage
      },
      checkCompleted(id) {
        for (let single of this.getCurrentClassLearnedKeword) {
          if ( single.id == id ) {
            return true
          }
        }
        return false
      },
      ableQuiz() {
        if (this.getCurrentClassLearnedKeword.length > 4) {
          return true
        } else {
          return false
        }
      },
      startQuiz() {
        // 서버에 요청을 보내서 퀴즈 받아오기
        if ( this.ableQuiz() && this.quizChance != 0) {
          this.$store.dispatch('getQuizInfo')
          this.openQuizPage = !this.openQuizPage
        } else if ( this.quizChance == 0) {
          const alertInfo = {
            status: true,
            color: "warning",
            content: "Used all quiz coins for today."
          }
          this.$store.dispatch("showAlert", alertInfo)
        } else {
          const alertInfo = {
            status: true,
            color: "warning",
            content: "Take 5 lessons before taking a quiz."
          }
          this.$store.dispatch("showAlert", alertInfo)
        }
      },
      endQuiz() {
        this.openQuizPage = !this.openQuizPage
      }

    },
    computed: {
      ...mapState([
        "currentClass", "defaultClass", "classList", "quizChance", "lessonInfo", "quizInfo"
      ]),
      ...mapGetters([
        "getCurrentClassLearnedKeword",
      ]),
      
      progress() {
        return (this.getCurrentClassLearnedKeword.length) / (this.classList.length) * 100
      },
    },
    created() {
      if ( this.ableQuiz() ) {
        this.$store.dispatch('getQuizInfo')
      }

      this.$store.dispatch('getListCurrentClass',this.currentClass )

    }
  }
</script>

<style scoped>
  .imgSize {
    /* max-width: 15vh; */
    /* height: 50vh; */
    max-width: 100%;
  }
</style>