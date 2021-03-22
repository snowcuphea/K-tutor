<template>
  <v-app>
    <div class="wrap">
      <router-view />
    </div>
    <v-bottom-navigation
      color="primary"
    >
      <v-btn :to="{name: 'Class'}">
        <span>Class</span>
        <v-icon>mdi-history</v-icon>
      </v-btn>

      <v-btn :to="{name: 'Test'}">
        <span>Test</span>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn :to="{name: 'Report'}">
        <span>Report</span>
        <v-icon>mdi-map-marker</v-icon>
      </v-btn>

      <v-btn :to="{name: 'Achievement'}">
        <span>Achieve</span>
        <v-icon>mdi-map-marker</v-icon>
      </v-btn>

      <v-btn :to="{name: 'MyPage'}">
        <span>My Page</span>
        <v-icon>mdi-map-marker</v-icon>
      </v-btn>
    </v-bottom-navigation>
  </v-app>
</template>

<script>
import "@/assets/css/mycss.css"

export default {
  name: 'App',

  components: {
    
  },

  data: () => ({
  }),
};
</script>

<style>

v-app {
  height: 100%;
}

.wrap {
  height: 90%
}

</style>