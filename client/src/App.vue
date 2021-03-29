<template>
  <v-app>
    <Header class="header" v-if="isNotClass"/>

    <v-main class="main">
      <router-view />
    </v-main>

    <Footer v-if="isNotMain"/>


  </v-app>
</template>

<script>
  import Header from "@/components/common/Header.vue"
  import Footer from "@/components/common/Footer.vue"


  export default {
    name: 'App',

    components: {
      Header,
      Footer
    },

    data: function () {
      return {

      }
    },

    computed: {
      isNotClass() {
        if (['Class', 'TitleList', 'ClassMain','Login','Home'].includes(this.$route.name)) {
          return false
        } else {
          return true
        }
      },

      isNotMain() {
        if (['Login','Home'].includes(this.$route.name)) {
          return false
        } else {
          return true
        }
      }

      // isNotClass () {
      //   if (this.$route.name === 'Class') {
      //     return false
      //   } else {
      //     return true
      //   }
      // },

    },
    methods: {

    },
    created() {
    }
  };
</script>

<style>
  @import "./assets/css/mycss.css";

  @font-face {
    font-family: 'RIDIBatang';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_twelve@1.0/RIDIBatang.woff') format('woff');
    font-weight: normal;
    font-style: normal;
  }

  @font-face {
    font-family: 'SeoulHangangM';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_two@1.0/SeoulHangangM.woff') format('woff');
    font-weight: normal;
    font-style: normal;
  }

  * {
    font-family: "RIDIBatang", sans-serif;
  }

  .header{
    min-height:60px;
    max-height:60px;
  }

  .main{
    height: 10px;
    overflow-y: auto;
  }

  .main::-webkit-scrollbar {
    display: none;
  }

</style>