<template>
  <v-bottom-navigation class="foot-nav" :value="value">
    <v-btn  v-for="(nav,idx) in navs" :key="idx" color="" class="mt-2" plain @click="goTo(nav, idx)">
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
        {name : "Class", icon: "mdi-heart", path: "Class"},
        {name : "Test", icon: "mdi-heart", path: "Test"},
        {name : "Report", icon: "mdi-heart", path: "Report"},
        {name : "Achieve", icon: "mdi-heart", path: "Achievement"},
        {name : "MyPage", icon: "mdi-heart", path: "MyPage"},
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
}

</style>