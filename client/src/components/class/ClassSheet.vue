<template>
  <v-container id="classSheet">
    <v-row>
      <v-btn @click="startClass()"> 학습하기 </v-btn>
    </v-row>
    <v-row>
      <v-col>
      <img :src="require(`@/assets/images/poster/poster${classInfo.cs_seq}.jpg`)" alt="title" class="imgSize">
      </v-col>
    </v-row>

    <v-row>
      <h1>blahblah</h1>
      <h1>blahblah</h1>
      <h1>blahblah</h1>
      <h1>blahblah</h1>
      <h1>blahblah</h1>
      <h1>blahblah</h1>
      <h1>blahblah</h1>
      <h1>blahblah</h1>
      <h1>blahblah</h1>
      <h1>blahblah</h1>
      <h1>blahblah</h1>
      <h1>blahblah</h1>
      <h1>blahblah</h1>
      <h1>blahblah</h1>
      <h1>blahblah</h1>
    </v-row>

    <StudyPage :openStudyPage="openStudyPage" @closeStudyPage="endClass"/>
  </v-container>
</template>

<script>
import StudyPage from "@/components/class/StudyPage.vue"


  import {
    mapState
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
      }
    },
    computed: {
      ...mapState([
        "currentClass", "defaultClass"
      ])
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