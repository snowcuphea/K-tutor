<template>
  <v-bottom-navigation class="foot-nav" :value="value">
    <v-btn  v-for="(nav,idx) in navs" :key="idx" color="" class="mt-2" plain @click="goTo(nav, idx)">
      <span>{{ nav.name }}</span>
      <v-icon>{{ nav.icon }}</v-icon>
    </v-btn>


    <!-- <v-btn :to="{name: 'Class'}" value="Class">
      <span>Class</span>
      <v-icon>mdi-history</v-icon>
    </v-btn>

    <v-btn :to="{name: 'Test'}" value="Test">
      <span>Test</span>
      <v-icon>mdi-heart</v-icon>
    </v-btn>

    <v-btn :to="{name: 'Report'}" value="Report">
      <span>Report</span>
      <v-icon>mdi-map-marker</v-icon>
    </v-btn>

    <v-btn :to="{name: 'Achievement'}" value="Achievement">
      <span>Achieve</span>
      <v-icon>mdi-map-marker</v-icon>
    </v-btn>

    <v-btn :to="{name: 'MyPage'}" value="MyPage">
      <span>My Page</span>
      <v-icon>mdi-map-marker</v-icon>
    </v-btn> -->
  </v-bottom-navigation>
</template>

<script>
export default {
  data: function() {
    return {
      value: 2,
      current: "Report",
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
        this.$store.dispatch('changePage', nav.name)
        
        console.log(this.current, this.value)
      }

    }
  }
}
</script>

<style>

.foot-nav {
  border-top: 1px solid;
}

</style>