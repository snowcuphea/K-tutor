<template>
  <v-container id="classSheet">
    <v-row>
    <!-- <p>클래스시트 : {{classInfo}}</p> -->
    </v-row>
    <v-row>
    <img :src="require(`@/assets/images/poster/poster${classInfo.cs_seq}.jpg`)" alt="title" class="imgSize">
    </v-row>

    <v-row>
      
    </v-row>


  </v-container>
</template>

<script>
  import {
    mapState
  } from 'vuex'

  export default {
    name: "ClassSheet",
    components: {

    },
    data: () => ({

    }),
    props: {
      classInfo: [Object, String],

    },



    computed: {
      ...mapState([
        "currentClass", "defaultClass"
      ])

    },
  }
</script>

<style scoped>
.imgSize {
    /* max-width: 15vh; */
    /* height: 50vh; */
    width: 100%;
  }

</style>