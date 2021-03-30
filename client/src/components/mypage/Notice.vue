<template>
  <div>
    <v-dialog
      v-model="showNotice"
      fullscreen
    >
      <v-card width="100%" height="100%" tile>

        <h2 class="head d-flex justify-center" style="padding: 12px; background-color: white;"> Notice </h2>
        <v-btn
          icon
          class="close-dialog"
          @click="hideDialog"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>


        <h1>안녕하세요</h1>
        <h3 v-for="(noticeItem,idx) in noticeItems" :key="idx">
          {{ noticeItem }}
        </h3>

      </v-card>
      
    </v-dialog>
  </div>

</template>

<script>
export default {
  props: ['showNotice'],
  data: () => ({
    noticeItems: ['K-tutor입니다', '만나서 반갑습니다.', '공지사항은 아직 없습니다', '나중에 생기면 올릴게요','수고하세요' ]
  }),
  methods: {
    hideDialog () {
      this.$emit('hideTutorial')
    }
  }
}
</script>

<style>

</style>