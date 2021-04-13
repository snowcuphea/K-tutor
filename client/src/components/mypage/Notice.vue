<template>
  <v-dialog
    v-model="showNotice"
    fullscreen
  >
    <v-card class="notice" width="100%" height="100%" tile>

      <h2 class="head d-flex justify-center" style="padding: 12px; background-color: white;"> Notice </h2>
      <v-btn
        icon
        class="close-dialog"
        @click="hideDialog"
      >
        <v-icon>mdi-close</v-icon>
      </v-btn>


      <h1 class="px-3">Version</h1>
      <h3 class="px-6 pb-5"> Ver.{{ noticeItems_version }} - (04/08/2021 updated)  </h3>
      <h1 class="px-3">Greetings</h1>
      <h3 class="px-6 pb-5"> {{ noticeItems_kr }}  </h3>
      <h3 class="px-6 py-5"> {{ noticeItems_eng }}  </h3>

      <h1 class="px-3">Copyright</h1>
      <h2 class="px-5">Kpop from Melon</h2>
      <div v-for="(title, idx) in allTitleList" :key="idx">
        <h3 v-if="title.type == 'kpop'" class="px-6 pb-3">{{ title.name_kor }}/{{ title.name_eng }}</h3>
      </div>
      <h2 class="px-5">Kdrama/kmovie from Netflix</h2>
      <div v-for="(title, idx) in allTitleList" :key="idx">
        <h3 v-if="title.type !== 'kpop'" class="px-6 pb-3">{{ title.name_kor }}/{{ title.name_eng }}</h3>
      </div>
    </v-card>
    
  </v-dialog>
</template>

<script>
import { mapState } from 'vuex'


export default {
  props: ['showNotice'],
  data: () => ({
    noticeItems_version: "1.0.0",
    noticeItems_kr: "K-tutor(말뭉치)는 한국의, 말뭉치 데이터('malmoongchi')를 \
        활용하여 제작한 서비스입니다. 말뭉치는 언어 연구를 위하여 컴퓨터가 \
        텍스트를 가공, 처리, 분석할 수 있는 형태로 모아 놓은 자료의 집합, 말모둠, 글모둠을 뜻합니다.",
    noticeItems_eng: "K-tutor is a service made using Korean corpus data\
     (말뭉치, 'malmoongchi'). Malmoongchi(말뭉치) is a collection of data, \
     words, and writings that a computer can process, process, or analyze text for language research.",
  }),
  methods: {
    hideDialog () {
      this.$emit('hideTutorial')
    }
  },
  computed: {
    ...mapState(['allTitleList'])
  }
}
</script>

<style>

.notice {
  overflow-y: auto;
}

</style>