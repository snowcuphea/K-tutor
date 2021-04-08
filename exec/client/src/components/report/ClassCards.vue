<template>
  <v-container class="classCards">
    <v-card v-for="(card,idx) in recent_learned_lc" :key="idx"
    class="mr-3 class-card" elevation="0" tile>
      <img :src="require(`@/assets/images/card/${card.imgurl}`)" alt="poster image" height="43%">
      <p class="card-line"> {{ card.main_kw_kor }} </p>
      <p class="card-line"> {{ card.main_kw_eng }} </p>
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