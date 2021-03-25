<template>
  <v-container class="classCards">
    <v-card v-for="(card,idx) in userLearned" :key="idx"
    class="mr-3 class-card" elevation="0" tile>
      <img :src="require(`@/assets/images/poster/${card.img}.jpg`)" alt="읎다" width="100px">
      <p class="card-line"> {{ card.line }} </p>
    </v-card>
  </v-container>
</template>

<script>


import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState(['userLearned'])
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
  min-height: 100px !important;
  max-height: 100px !important;
}

.card-line {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

</style>