<template>
  <v-container>
    <p>장르 : {{genre}}</p>

    <v-row class="d-flex flex-column">
      <v-col>
        <v-card max-width="400" class="my-1 mx-2" v-for="item in getCurrentTypeTitleList" :key="item.name">
          <v-card-text>
            <img>
            <p class="text--primary">
              {{item.name}}
            </p>
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

    },
    props: {
      genre: [Object, String],

    },

    created() {


    },
    computed: {
      ...mapState(["dramaList", "movieList", "popList"]),
      ...mapGetters(["getCurrentTypeTitleList"]),
    },
  }
</script>

<style>

</style>