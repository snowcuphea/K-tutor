<template>
  <div id="class">
    <v-app-bar-nav-icon class="nav-icon" @click="drawer = !drawer" />
    <div class="class-head d-flex flex-column justify-center">
      <h2> Class </h2>
    </div>

    <v-navigation-drawer v-model="drawer" stateless absolute overlay-opacity="0" temporary style="z-index:66; position: fixed;">
      <v-btn
        icon
        class="close-drawer"
        @click="drawer = !drawer"
      >
        <v-icon>mdi-arrow-collapse-left</v-icon>
      </v-btn>
      <v-list
        nav
        dense
      >
        <v-subheader class="my-3">Select Theme</v-subheader>
        <v-list-item-group
          v-model="selectedIdx"
          active-class="deep-purple--text text--accent-4"
        >
          <v-list-item v-for="(typeItem, idx) in typeData" :key="idx" @click="selectType(typeItem)">
            <!-- <v-list-item-title>{{ typeItem.name }}</v-list-item-title> -->
            <h3>{{ typeItem.name }}</h3>
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
          <v-toolbar-items>
          </v-toolbar-items>
        </v-toolbar>
        <TitleList @closeDialog="dialog = false" />
      </v-card>
    </v-dialog>

    <v-container class="class-container">
      
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
      nowTime: new Date(),
      drawer: false,
      dialog: false,
      selectedIdx: null,
      selectedType: null,
      typeData: [
        {
          type_seq: 1,
          type: "movie",
          name: "K-Movie"
        },
        {
          type_seq: 2,
          type: "drama",
          name: "K-Drama"
        },
        {
          type_seq: 3,
          type: "kpop",
          name: "K-Pop"
        },
      ],

    }
  },
  methods: {
    selectType( typeItem ) {
      this.selectedType = typeItem.name
      this.$store.state.currentType = typeItem.type
    }
  },
  watch: {
    selectedIdx() {
      this.drawer = !this.drawer
      this.dialog = !this.dialog
    }
  },
  computed: {
    ...mapState(["currentClass", "defaultClass", "allTitleList", "time"])
  },
  created() {
    // console.log("클래스에서 this.currentClass", this.currentClass)

    // console.log(this.time, this.nowTime.getDate())
    if ( this.nowTime.getDate() !== this.time ) {
      // console.log(this.time, this.nowTime.getDate())
      this.$store.dispatch( 'resetChance', this.nowTime.getDate() )
    } 

  },
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
  text-align: center;
}


.close-drawer {
  position: fixed;
  top: 1.5em;
  right: 0.5em;
  z-index: 99;
}

</style>