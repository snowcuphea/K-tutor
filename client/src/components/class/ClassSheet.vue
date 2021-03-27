<template>
  <v-container id="classSheet">
    <v-row>
      <v-btn @click="startClass()"> 학습하기 </v-btn>
    </v-row>
    <v-row>
    <img :src="require(`@/assets/images/poster/poster${classInfo.cs_seq}.jpg`)" alt="title" class="imgSize">
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