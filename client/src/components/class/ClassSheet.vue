<template>
  <v-container id="classSheet">
    <v-row>
      <v-col>
        <span> {{currentClass.cs_title}} </span>
        <!-- <span> {{getCurrentClassLearnedKeword}} </span> -->
      </v-col>
    </v-row>

    <v-row>
      <v-col>
        <img :src="require(`@/assets/images/poster/poster${classInfo.cs_seq}.jpg`)" alt="title" class="imgSize">
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
                <span v-if="item.cs_seq">O</span> 
                <span v-else>X</span> 
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <v-row>
      <v-btn @click="startClass()"> 학습하기 </v-btn>
    </v-row>

    <StudyPage :openStudyPage="openStudyPage" @closeStudyPage="endClass" />
  </v-container>
</template>

<script>
  import StudyPage from "@/components/class/StudyPage.vue"


  import {
    mapState, mapGetters
  } from 'vuex'

  export default {
    name: "ClassSheet",
    components: {
      StudyPage
    },
    data: () => ({
      openStudyPage: false,

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