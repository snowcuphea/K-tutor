<template>
  <v-container>
    <v-btn @click="showDialog = !showDialog">시험보기</v-btn>

    <TestPage :showDialog="showDialog" @hideDialog="showDialog = !showDialog"/>
    
  </v-container>
</template>

<script>
import TestPage from "@/components/exam/TestPage.vue"

export default {
  components: {
    TestPage,
  },
  data() {
    return {
      showDialog: false,
    }
  }

}
</script>

<style>

</style>