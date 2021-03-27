<template>
  <v-container>
    <v-dialog
      v-model="openStudyPage"
      fullscreen
      hide-overlay
      transition="slide-x-reverse-transition"
      scrollable
    >
      <v-card height="100%" width="100" tile>
        <v-btn
          icon
          class="close-dialog"
          @click="closeStudyPage"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>

        <v-card tile height="15%" elevation="0">
          step 정보
        </v-card>

        <v-card tile height="72%" elevation="0">
          학습 내용
        </v-card>

        <v-card tile height="13%" elevation="0">
          몇번째 페이지인지
        </v-card>

      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
export default {
  props: ["openStudyPage"],
  data() {
    return {

    }
  },
  methods:{
    closeStudyPage() {
      this.$emit('closeStudyPage')
    }
  }
}
</script>

<style>

</style>