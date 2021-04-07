<template>
  <div>

    <v-dialog
      v-model="showTutorial"
      fullscreen
    >
      <v-card>
        <!-- <h2 class="head d-flex justify-center" style="padding: 12px; background-color: white;"> Tutorial </h2> -->
        <v-btn
          icon
          class="close-dialog"
          @click="hideDialog"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>

        
        <v-carousel :show-arrows="false" hide-delimiters height="100%">
          <v-carousel-item
            v-for="(it,i) in tutorialItems"
            :key="i"
            :src="it"
            class="tutorial_img"
          >
            <!-- <v-img :src="it" class="tutorial_img"></v-img> -->
          </v-carousel-item>
        </v-carousel>
      </v-card>

    </v-dialog>
  </div>

  

</template>

<script>
export default {
  props: ['showTutorial'],
  data: () => ({
    tutorialItems: [require('@/assets/img/mypage/1.png'), require('@/assets/img/mypage/2.png'), require('@/assets/img/mypage/3.png'), require('@/assets/img/mypage/4.png'), require('@/assets/img/mypage/5.png'), require('@/assets/img/mypage/6.png')]   
  }),
  methods: {
    hideDialog () {
      this.$emit('hideTutorial')
    }
  }
}
</script>

<style>

.tutorial_img {
  height: 100%;
  width: 100%;
}

</style>