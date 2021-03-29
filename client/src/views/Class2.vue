<template>
  <div id="class">
    <v-app-bar-nav-icon class="nav-icon" @click="drawer = !drawer" />
    <v-container class="class-head d-flex justify-center">
      <h2> Class </h2>
    </v-container>

    <v-navigation-drawer v-model="drawer" absolute temporary style="z-index:99;">
      <v-list
        nav
        dense
      >
        <v-subheader>Select Theme</v-subheader>
        <v-list-item-group
          v-model="selectedIdx"
          active-class="deep-purple--text text--accent-4"
        >
          <v-list-item v-for="(type, idx) in typeData" :key="idx" @click="selectType(type)">
            <v-list-item-title>{{ type.type_title }}</v-list-item-title>
          </v-list-item>

        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <v-dialog v-model="dialog" fullscreen hide-overlay transition="fab-transition">
      <v-card>
        <v-toolbar flat>
          <v-btn icon @click="dialog = false">
            <v-icon>mdi-close</v-icon>
          </v-btn>
          <v-toolbar-title>{{ selectedType }} List</v-toolbar-title>
          <v-toolbar-items>
          </v-toolbar-items>
        </v-toolbar>
        <TitleList @closeDialog="dialog = false" />
      </v-card>
    </v-dialog>

    <v-container>
      
      <ClassSheet :classInfo="currentClass ? currentClass : defaultClass" />

    </v-container>

  </div>
</template>

<script>
import { mapState } from 'vuex'

import TitleList from '@/components/class/TitleList.vue'
import ClassSheet from '@/components/class/ClassSheet.vue'

export default {
  components: {
    TitleList,
    ClassSheet
  },
  data() { 
    return {
      drawer: false,
      dialog: false,
      selectedIdx: null,
      selectedType: null,
      typeData: [
        {
          type_seq: 1,
          cs_type: "movie",
          type_title: "K-Movie"
        },
        {
          type_seq: 2,
          cs_type: "drama",
          type_title: "K-Drama"
        },
        {
          type_seq: 3,
          cs_type: "pop",
          type_title: "K-Pop"
        },
      ],

    }
  },
  methods: {
    selectType( type ) {
      this.selectedType = type.type_title
      this.$store.state.currentType = type.cs_type
    }
  },
  watch: {
    selectedIdx() {
      this.drawer = !this.drawer
      this.dialog = !this.dialog
    }
  },
  computed: {
    ...mapState(["currentClass", "defaultClass"])
  }
}
</script>

<style>

.nav-icon {
  position: fixed;
  top: 0.8em;
  left: 1em;
  z-index: 50;
}

.class-head {
  position: sticky;
  background-color: white;
  top: 0;
  height: 60px;
  border-bottom: 1px solid;
  z-index: 49;
}

</style>