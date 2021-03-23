<template>
  <v-app>
    <Header v-if="isNotClass" />
    <!-- <h1>안냥</h1> -->

    <v-main>
      <router-view />
    </v-main>

    <Footer />
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

  data: () => ({
  }),

  computed : {
    isNotClass () {
      if (['Class'].includes(this.$route.name)) {
        return false
      } else {
        return true
      }
    },


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



</style>