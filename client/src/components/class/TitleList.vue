<template>
  <v-container>
    <v-row class="d-flex justify-center my-2">
    <h3> K-{{genre}} List</h3>
    </v-row>
    <v-row class="d-flex flex-column">
      <v-col>
        <v-card class="my-1 mx-2" v-for="item in getCurrentTypeTitleList" :key="item.cs_seq"
        @click="selectClass(item)">
          <v-card-text>
            <v-row>
              <v-col cols="4" xs="6" style="" class="d-flex justify-center">
                <img :src="require(`@/assets/images/poster/poster${item.cs_seq}.jpg`)" alt="title" class="imgSize">
              </v-col>
              <v-col cols="8" xs="6" class="d-flex align-center">
                <h3 class="text--primary">{{item.cs_title}}</h3>
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
      selectClass(item){
        console.log(item)
        this.$store.state.currentClass = item
        console.log("go To selected Class!!!!!!!:::::", item.cs_title)
        this.$router.push({
          name: 'Class'
        })


      }


    },
    props: {
      genre: [Object, String],

    },

    created() {
      console.log("")


    },
    computed: {
      ...mapState(["dramaList", "movieList", "popList"]),
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