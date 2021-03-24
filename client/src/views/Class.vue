<template>
  <v-container id="class">

    <v-row>

      <v-col class="d-flex justify-space-between">

        <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
        <h1>{{currentPage}}</h1>
        <v-app-bar-nav-icon @click.stop="drawer = !drawer" class="hide" />
      </v-col>

    </v-row>


    <v-row v-if="$store.state.currentType">
      <TitleList :genre="$store.state.currentType" />
    </v-row>
    <v-row v-else>
      <v-row v-if="currentClass">
      <p> 최근클래스정보 : {{currentClass}} </p>
      <ClassSheet :classInfo="currentClass" style="background-color:skyblue" />
    </v-row>


    <v-row v-else>
      <p>디폴트 클래스 정보 : {{defaultClass}} </p>
      <ClassSheet :classInfo="defaultClass"  style="background-color:beige" />
    </v-row>
    </v-row>


    <v-navigation-drawer v-model="drawer" absolute temporary>
      <v-list nav dense>
        <v-subheader>Select Theme</v-subheader>
        <v-list-item-group active-class="deep-purple--text text--accent-4" v-model="drawerGroup">

          <v-list-item @click="resetList">
            <v-list-item-title>리스트 초기화(테스트용)</v-list-item-title>
          </v-list-item>
          <v-list-item @click="makeList">
            <v-list-item-title>리스트 불러오기(테스트용)</v-list-item-title>
          </v-list-item>
          <v-list-item @click="goToDefault">
            <v-list-item-title>genre 초기화(테스트용)</v-list-item-title>
          </v-list-item>
          <v-list-item @click="resetSelectClass">
            <v-list-item-title>클래스선택 초기화(테스트용)</v-list-item-title>
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
  import ClassSheet from '@/components/class/ClassSheet.vue'

  import TitleList from '@/components/class/TitleList.vue'

  import {
    mapState
  } from 'vuex'


  export default {
    name: "Class",
    components: {
      TitleList,
      ClassSheet,
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
        "currentPage", "currentClass", "defaultClass"
      ])

    },
    methods: {
      goToMovieList() {
        this.$store.state.currentType = "movie"

      },
      goToDramaList() {
        this.$store.state.currentType = "drama"

      },
      goToPopList() {
        this.$store.state.currentType = "pop"

      },
      goToDefault() {
        this.$store.state.currentType = ""

      },
      resetList(){
        this.$store.state.allTitleList =  []
      },
      resetSelectClass(){
        this.$store.state.currentClass =  ''
        this.$store.state.currentType =  ''

      },
      makeList() {

        this.$store.state.allTitleList =  [

      {cs_seq:1, cs_title: '싸이코지만괜찮아', cs_type:'drama', cs_level:1},
      {cs_seq:2, cs_title: '사랑의불시착', cs_type:'drama', cs_level:1},
      {cs_seq:3, cs_title: '스위트홈', cs_type:'drama', cs_level:3},
      {cs_seq:4, cs_title: '미스터선샤인', cs_type:'drama', cs_level:2},
      {cs_seq:5, cs_title: '이태원클라쓰', cs_type:'drama', cs_level:2},

      {cs_seq:6, cs_title: '승리호', cs_type:'movie', cs_level:1},
      {cs_seq:7, cs_title: '부산행', cs_type:'movie', cs_level:2},
      {cs_seq:8, cs_title: '설국열차', cs_type:'movie', cs_level:2},
      {cs_seq:9, cs_title: '반도', cs_type:'movie', cs_level:3},
      {cs_seq:10, cs_title: '극한직업', cs_type:'movie', cs_level:1},

      {cs_seq:11, cs_title: '방탄소년단', cs_type:'pop', cs_level:1},
      {cs_seq:12, cs_title: '블랙핑크', cs_type:'pop', cs_level:1},
      {cs_seq:13, cs_title: '아이유', cs_type:'pop', cs_level:1},
      {cs_seq:14, cs_title: '소녀시대', cs_type:'pop', cs_level:2},
      {cs_seq:15, cs_title: '트와이스', cs_type:'pop', cs_level:2},
      {cs_seq:16, cs_title: '태연', cs_type:'pop', cs_level:2},
      {cs_seq:17, cs_title: '악동뮤지션', cs_type:'pop', cs_level:3},
      {cs_seq:18, cs_title: '갓세븐', cs_type:'pop', cs_level:3},
      {cs_seq:19, cs_title: '세븐틴', cs_type:'pop', cs_level:3},
      {cs_seq:20, cs_title: '엑소', cs_type:'pop', cs_level:1},
      {cs_seq:21, cs_title: '박효신', cs_type:'pop', cs_level:1},
      
      ]
       


      },

    }

  }
</script>

<style>

</style>