<template>
  <v-container id="class">

    <v-row >

    <v-col class="d-flex justify-space-between">

      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <h1>{{currentPage}}</h1>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" class="hide" />
    </v-col>

    </v-row>

    <!-- <v-row>
      <p>선택된 라우터 : {{$route.path}}</p>
    <router-view style="background-color:pink;" />
    </v-row> -->

    <v-row v-if="$store.state.currentType != null" >
      <TitleList :genre="$store.state.currentType"  />
    </v-row>
    <v-row v-else>
      <router-view style="background-color:pink;" />
    </v-row>


    <v-navigation-drawer v-model="drawer" absolute temporary>
      <v-list nav dense>
        <v-subheader>Select Theme</v-subheader>
        <v-list-item-group active-class="deep-purple--text text--accent-4" v-model="drawerGroup">

          <v-list-item @click="goToDefault">
            <v-list-item-title>genre 초기화(테스트용)</v-list-item-title>
          </v-list-item>

          <v-list-item @click="goToMovieList">
            <v-list-item-title>K-movie</v-list-item-title>
          </v-list-item>

          <v-list-item @click="goToDramaList">
            <v-list-item-title>K-drama</v-list-item-title>
          </v-list-item>

          <v-list-item @click="goToPopList">
            <v-list-item-title>K-pop</v-list-item-title>
          </v-list-item>


        </v-list-item-group>
      </v-list>


    </v-navigation-drawer>





  </v-container>
</template>

<script>

import TitleList from '../components/class/TitleList.vue'

  import {
    mapState
  } from 'vuex'


  export default {
    name: "Class",
    components: {
      TitleList,
    },
    data: () => ({

      drawer: false,
      drawerGroup: null,
      

    }),
    watch: {
      drawerGroup() {
        this.drawer = false
      },
    },

    created: function () {

    },
    computed: {
      ...mapState([
        "currentPage"
      ])

    },
    methods: {
      goToMovieList(){
        this.$store.state.currentType = "movie"
        
      },
      goToDramaList(){
        this.$store.state.currentType = "drama"
        
      },
      goToPopList(){
        this.$store.state.currentType = "pop"
        
      },
      goToDefault(){
        this.$store.state.currentType = ""
        
      },

    },

  }
</script>

<style>

</style>