<template>
  <v-card height="100%" class="start-home d-flex justify-center align-center">

    <img src="@/assets/logo.png" height="100px" width="100px" alt="poster image">
  </v-card>

</template>

<script>
import { mapState } from 'vuex'

export default {
  data() {
    return {
      nowTime: new Date(),
    }
  },
  created() {
    // default page
    const defaultSetting = {
      navName: "Report",
      navValue: 2
    }
    // default setting
    this.$store.dispatch('changePage', defaultSetting)

    setTimeout(() => {
      if (this.isLogin){
        this.$router.push({path: '/report'})
      } else {
        this.$router.push({path: '/login'})
      }
    }, 1500);

  },
  computed: {
    ...mapState(['isLogin', 'time'])
  }
}
</script>

<style>

.start-home {
  background-color: #62D2A2 !important;

}

</style>