<template>
  <v-container id="classSheet">
    <v-row>
      <!-- <p>클래스시트 : {{classInfo}}</p> -->
    </v-row>
    <v-row>
      <v-col>
      <img :src="require(`@/assets/images/poster/poster${classInfo.cs_seq}.jpg`)" alt="title" class="imgSize">
      </v-col>
    </v-row>

    <v-row>
      <v-col>
        <v-card class="my-1 mx-2" v-for="item in getCurrentTypeTitleList" :key="item.cs_seq"
        @click="selectClass(item)">
          <v-card-text>
            <v-row>
              <v-col cols="5" xs="6" style="" class="d-flex justify-center">
                <img :src="require(`@/assets/images/poster/poster${item.cs_seq}.jpg`)" alt="title" class="imgSize">
              </v-col>
              <v-col cols="7" xs="6" class="d-flex align-center">
                <h3 class="text--primary">{{item.cs_title}}</h3>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>

      </v-col>

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