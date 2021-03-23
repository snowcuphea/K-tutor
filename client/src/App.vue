<template>
  <v-app>
    <Header />

    <v-main>
      <router-view />
    </v-main>

    <Footer />
  </v-app>
</template>

<script>
import "@/assets/css/mycss.css"

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
};
</script>

<style>

</style>