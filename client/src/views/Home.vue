<template>
  <v-card height="100%" class="start-home d-flex justify-center align-center">

    <img src="@/assets/logo.svg" height="100px" width="100px" alt="">
  </v-card>

</template>

<script>
export default {
  created() {
    // default page
    const defaultSetting = {
      navName: "Report",
      navValue: 2
    }
    // default setting
    this.$store.dispatch('changePage', defaultSetting)


    setTimeout(() => {
      this.$router.push({path: '/report'})
    }, 1500);
  }
}
</script>

<style>

.start-home {
  background-color: rgb(47, 184, 47) !important;

}

</style>