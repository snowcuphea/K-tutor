<template>
  <v-container id="class">
   
      <div class="d-flex justify-space-between">

      <v-app-bar-nav-icon @click.stop="drawer = !drawer"/>
      <h1>{{currentPage}}</h1>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" class="hide"/>
      </div>


    <v-navigation-drawer v-model="drawer" absolute temporary>
      <v-list nav dense>
        <v-list-item-group v-model="group" active-class="deep-purple--text text--accent-4">
          <v-list-item>
            <v-list-item-title>Foo</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>Bar</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>Fizz</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>Buzz</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

  </v-container>
</template>

<script>
  import {
    mapState
  } from 'vuex'


  export default {
    name: "Class",
    component: {},
    data: () => ({

       drawer: false,
      group: null,

    }),
    watch: {
      group () {
        this.drawer = false
      },
    },

    created: function () {

    },
    computed: {
      ...mapState([
        "currentPage"
      ])

    },
    methods: {

    },

  }
</script>

<style>

</style>