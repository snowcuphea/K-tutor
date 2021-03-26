<template>
  <v-container>
    <v-row v-if="currentClass">
      <p> 최근클래스정보 : {{currentClass}} </p>
      <ClassSheet :classInfo="currentClass" style="background-color:skyblue" />
    </v-row>


    <v-row v-else>
      <p>디폴트 클래스 정보 : {{defaultClass}} </p>
      <ClassSheet :classInfo="defaultClass"  style="background-color:beige" />
    </v-row>
  </v-container>
</template>

<script>
  import ClassSheet from '@/components/class/ClassSheet.vue'

  import {
    mapState
  } from 'vuex'

  export default {
    name: "ClassMain",
    components: {
      ClassSheet,
    },
    data: () => ({

    }),



    computed: {
      ...mapState([
        "currentClass", "defaultClass"
      ])

    },
  }
</script>

<style>

</style>