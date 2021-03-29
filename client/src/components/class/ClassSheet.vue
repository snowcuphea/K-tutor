<template>
  <v-container id="classSheet">
    <v-row>
      <v-col class="d-flex justify-center">
        <h2> {{currentClass.cs_title}} </h2>
        <!-- <span> 여기에 나중에 영어이름도 넣기 </span> -->
        
      </v-col>
    </v-row>

    <v-row>
      <v-col>
        <!-- <img :src="require(`@/assets/images/poster/poster${classInfo.cs_seq}.jpg`)" alt="title" class="imgSize"> -->
        <img :src="require(`@/assets/images/poster/poster1.jpg`)" alt="title" class="imgSize">
      </v-col>
    </v-row>

    <v-row >
      <v-col >
        <span v-if="currentClass.cs_level == '0'">Difficulty: Beginner</span>
        <span v-else-if="currentClass.cs_level == '1'">Difficulty: Intermediate</span>
        <span v-else-if="currentClass.cs_level == '2'">Difficulty: Advanced</span>
        <span v-else>Difficulty: Basic</span>
      </v-col>
    </v-row>

    <v-row>
      <v-col>
        <div class="d-flex">
          <p class="mb-1">Learning Progress</p>
          <v-spacer></v-spacer>
          <p class="mb-0">{{getCurrentClassLearnedKeword.length}}/ {{classList.length}}</p>
        </div>
        <v-progress-linear :value="progress" height="10">
        </v-progress-linear>

      </v-col>
    </v-row>

    <v-row>
      <v-btn @click="startQuiz()"> quiz </v-btn>
    </v-row>

    <v-row>
      <v-col>
        <v-card class="my-1 mx-2" v-for="(item,idx) in classList" :key="item.keyword" @click="startClass()">
          <v-card-text>
            <v-row>
              <v-col cols="1" xs="1" class="d-flex justify-center align-center">
                <span>{{idx+1}}</span>
              </v-col>
              <v-col cols="3" xs="4" style="" class="d-flex justify-center">
                <img :src="require(`@/assets/images/poster/${item.img}.jpg`)" alt="keyword" class="imgSize">
              </v-col>
              <v-col cols="7" xs="6" class="d-flex align-center">
                <div class="d-flex flex-column">
                  <h3 class="text--primary my-1"> {{item.keyword}}</h3>
                  <span class="my-1"> {{item.keyword_en}} -{{item.title}}中-</span>
                </div>
              </v-col>
              <v-col cols="1" xs="1" class="d-flex align-center">
                <!-- item.cs_seq가 getCurrentClassLearnedKeword의 cs_seq에 있는지 검사해서 완료여부도 넣어야됨 -->
                <span v-if="checkCompleted(item)">O</span> 
                <span v-else>X</span> 
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <StudyPage :openStudyPage="openStudyPage" @closeStudyPage="endClass" />
    <QuizPage :openQuizPage="openQuizPage" @closeQuizPage="endQuiz" />

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
      startClass() {
        // 서버에 요청을 보내서 해당 학습 내용을 받아온다
        this.$store.dispatch('getLessonInfo')
        this.openStudyPage = !this.openStudyPage
      },
      endClass() {
        this.openStudyPage = !this.openStudyPage
      },
      checkCompleted(item) {
        // if item.cs_seq in getCurrentClassLearnedKeword.cs_
        console.log(item)
        return true
      },
      startQuiz() {
        // 서버에 요청을 보내서 퀴즈 받아오기
        this.$store.dispatch('getQuizInfo')
        this.openQuizPage =!this.openQuizPage
      },
      endQuiz() {
        this.openQuizPage = !this.openQuizPage
      }

    },
    computed: {
      ...mapState([
        "currentClass", "defaultClass", "classList",
      ]),
      ...mapGetters([
        "getCurrentClassLearnedKeword",
      ]),
      
      progress() {
        return (this.getCurrentClassLearnedKeword.length) / (this.classList.length) * 100
      },
    },
  }
</script>

<style scoped>
  .imgSize {
    /* max-width: 15vh; */
    /* height: 50vh; */
    width: 100%;
  }
</style>