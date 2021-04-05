<template>
  <v-container class="classCards">
    <v-card v-for="(card,idx) in recent_learned_lc" :key="idx"
    class="mr-3 class-card" elevation="0" tile>
      <!-- <img :src="card.imgurl" alt="아직읎다" width="100px" height="80px"> -->
      <img :src="require(`@/assets/images/poster/poster1.jpg`)" alt="아직읎다" width="100px" height="80px">
      <p class="card-line"> {{ card.main_kw_kor }} </p>
      <p class="card-line"> {{ card.main_kw_eng }} neet to add</p>
    </v-card>
  </v-container>
</template>

<script>

import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState(['recent_learned_lc'])
  }
}
</script>

<style>

.classCards {
  display: flex;
  overflow-x: auto;
}

.classCards::-webkit-scrollbar {
  display: none;
}

.class-card {
  min-width : 100px !important;
  max-width : 100px !important;
  min-height: 130px !important;
  max-height: 130px !important;
}

.card-line {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  margin-bottom: 0 !important;
}

</style>