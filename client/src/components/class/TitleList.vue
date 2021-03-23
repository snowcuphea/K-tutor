<template>
  <v-container>
    <p>장르 : {{genre}}</p>

  </v-container>
</template>

<script>
  export default {
    name: "TitleList",
    components: {

    },
    data: () => ({

    }),
    methods: {

    },
    props: {
      genre: [Object, String],
      
    },

    created() {


    }
  }
</script>

<style>

</style>