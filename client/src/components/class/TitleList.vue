<template>
  <v-container>
    <v-row class="d-flex justify-center mb-2">
      <h2 v-if="currentType=='kpop'"> K-Pop List</h2>
      <h2 v-else> K-{{currentType}} List</h2>
    </v-row>
    <v-row class="d-flex flex-column">
      <v-col>
        <v-card class="my-1 py-5 " v-for="item in getCurrentTypeTitleList" :key="item.name" @click="selectClass(item)">
          <v-card-text>
            <v-row no-gutters>
              <v-col cols="4"  style="" class="d-flex justify-center">
                <!-- <img :src="require(`@/assets/images/poster/poster${item.cs_seq}.jpg`)" alt="title" class="imgSize"> -->
              </v-col>
              <v-col cols="5" class="d-flex align-center">
                <h3 class="text--primary">{{item.name}}</h3>
              </v-col>
              <v-col cols="3" class="d-flex align-center justify-end">
                <span v-if="item.level == '0'">Beginner</span>
                <span v-else-if="item.level == '1'">Intermediate</span>
                <span v-else-if="item.level == '2'">Advanced</span>
                <span v-else>Difficulty: Basic</span>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

  </v-container>
</template>

<script>
  import {
    mapGetters,
    mapState,
  } from "vuex";

  export default {
    name: "TitleList",
    components: {

    },
    data: () => ({

    }),
    methods: {
      selectClass(item) {
        console.log(item)
        this.$store.dispatch('changeCurrentClass', item)
        // this.$store.state.currentClass = item
        this.$emit("closeDialog")
        console.log("selected Class!!!!!!!:::::", item.name)
        this.$store.dispatch("getListCurrentClass", item) //선택한 타이틀의 학습리스트 가져온다.

      }


    },
    // props: {
    //   genre: [Object, String],

    // },

    created() {

    },
    computed: {
      ...mapState(["currentType"]),
      ...mapGetters(["getCurrentTypeTitleList"]),
    },
  }
</script>

<style scoped>
  .imgSize {
    /* max-width: 15vh; */
    height: 10vh;
  }
</style>