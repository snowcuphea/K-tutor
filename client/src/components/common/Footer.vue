<template>
  <v-bottom-navigation class="foot-nav" :value="value">
    <v-btn v-for="(nav,idx) in navs" :key="idx" color="" class="mt-2" width="20%" plain @click="goTo(nav, idx)">
      <span>{{ nav.name }}</span>
      <v-icon>{{ nav.icon }}</v-icon>
    </v-btn>
  </v-bottom-navigation>
</template>

<script>

import { mapState } from 'vuex'


export default {
  data: function() {
    return {
      value: this.$store.state.currentPageValue,
      current: this.$store.state.currentPage,
      navs: [
        {name : "Class", icon: "mdi-notebook-multiple", path: "Class"},
        {name : "Test", icon: "mdi-book-edit", path: "Test"},
        {name : "Report", icon: "mdi-file-chart", path: "Report"},
        {name : "Achieve", icon: "mdi-trophy", path: "Achievement"},
        {name : "MyPage", icon: "mdi-account", path: "MyPage"},
      ]
    }
  },
  methods: {
    goTo(nav, idx) {
      if ( this.current !== nav.name ) {
        this.current = nav.name
        this.value = idx
        this.$router.push({ name: nav.path })
      
        const changeItem = {
          navName : nav.name,
          navValue : idx
        }
        this.$store.dispatch('changePage', changeItem)
        console.log(this.current, this.value)

      }

    }
  },
  computed: {
    ...mapState([
      "currentPageValue"
      ]
    )
  },


}
</script>

<style>

.foot-nav {
  border-top: 1px solid;
  height: 4.5em !important;
  z-index: 96;
}

</style>