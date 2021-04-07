<template>
  <v-container>

    <div class="modal-overlay"
      v-if="visible"
      @click="closeModal"
      >
      <v-card width="90%" height="70%" class="pa-3 modal-window" >
        <v-btn
          icon
          class="close-dialog"
          @click="closeModal"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>
        <v-img 
          :src="require(`@/assets/images/achievement/${item.imgurl}`)"
          height="50%"
          width="60%"
          class="mx-auto"
        />
        <v-card-title class="modal_title">
          {{ item.great_kor }}
        </v-card-title>
        <v-card-subtitle>
          {{ item.great_eng }}
        </v-card-subtitle>

        <v-card-text class="modal_contents">
          {{ item.great_dsc | dsc() }} <br>
          <a :href="item.great_dsc | toLink() ">Learn more via Wikipedia</a>
        </v-card-text>
      </v-card>
    </div>

    <v-subheader style="padding:0;">
      <v-container class="progress_top">

        <v-row style="margin-bottom: 0;">
          <v-col
            cols="8"
            class="d-flex flex-column"
          >
            <h4>Achievement Status</h4>

            <v-progress-linear
              color="light-blue"
              height="15"
              :value="(getCurrentAchieved.length/9)*100"
              striped
            >
              <h6>{{ getCurrentAchieved.length }}/9</h6> 
                
            </v-progress-linear>

          </v-col>
          <v-col
            cols="4"
          >
            <div class="d-flex justify-end" style="padding-right: 10%;">
              <v-btn
                icon
                plain
                :color="viewlist===false ? 'secondary' : 'primary'"
              >
                <v-icon @click="viewList">mdi-view-list</v-icon>
              </v-btn>
              <v-btn
                icon
                plain
                :color="viewcalendar===false ? 'secondary' : 'primary'"
              >
                <v-icon @click="viewCalendar">mdi-grid</v-icon>
              </v-btn>
              
            
            </div>

          </v-col>
        </v-row>
      </v-container>
    </v-subheader>
    <div style="padding-top: 3%;">

      <div class="wrap d-flex flex-column" v-if="viewlist">

        <div
          v-for = "(item, idx) in $store.state.AchievementList"
          :key = "idx"
        >

          <appMyModal :modalItem="item" @update2="modal" />

        </div>

      </div>
      <div v-if="viewcalendar">
        
        <v-row
          class="d-flex wrap"

        >
          <v-col
            cols="4"
            v-for = "(item,idx) in $store.state.AchievementList"
            :key = "idx"
          >
            <appMyModal2 :modalItem="item" @update2="modal" />

          </v-col>
        </v-row>
<a href=""></a>
      </div>
    </div>
    
  </v-container>
</template>

<script>
import Achievemodal from '../components/modal/Achievemodal'
import Achievemodal2 from '../components/modal/Achievemodal2'

import { mapGetters, mapState } from 'vuex'

import Vue from 'vue'

Vue.filter('dsc', function(value) {
  const newDsc = value.split("https")
  
  return newDsc[0] 
})
Vue.filter('toLink', function(value) {
  const newDsc = value.split("https")

  return "https" + newDsc[1] 
})



export default {
  name: "Achievement",
  components: {
    appMyModal: Achievemodal,
    appMyModal2: Achievemodal2
  },
  data: () => ({
    nowTime: new Date(),
    visible: false,
    viewlist: true,
    viewcalendar: false,
  }),
  methods: {
    modal (modalItem) {
      this.item = modalItem,
      this.visible = !this.visible
    },
    closeModal () {
      this.visible = !this.visible
    },
    viewList () {
      if (this.viewlist == false) {
        this.viewlist = !this.viewlist
        this.viewcalendar = !this.viewcalendar
      }
    },
    viewCalendar () {
      if (this.viewcalendar == false) {
        this.viewcalendar = !this.viewcalendar
        this.viewlist = !this.viewlist
      }
    },
  },
  created() {
    this.$store.dispatch('getAchievementList')

    // console.log(this.time, this.nowTime.getDate())
    if ( this.nowTime.getDate() !== this.time ) {
      console.log(this.time, this.nowTime.getDate())
      this.$store.dispatch( 'resetChance', this.nowTime.getDate() )
    } 

  },
  computed: {
    ...mapGetters(["getCurrentAchieved"]),
    ...mapState(["time", "myCompleteAchievement"])
  }
}
</script>

<style>

.progress_top {
  position: fixed;
  z-index: 5;
  background-color: white;
  margin-right: 62;
}

.app_bar {
  text-align: center;
}

#achieve_body {
  overflow-y: auto;
  height: 500px;
}

#achieve_body::-webkit-scrollbar {
  display: none;
}

.modal-overlay {
  display: flex;
  align-items: center;
  justify-content: center;
  position: fixed;
  z-index: 6;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
}

.modal-window {
  overflow-y: auto;
}

.modal_img {
  height: 50%;
  width: 50%;
}

.modal_title {
  /* text-align: center; */
}

.modal_contents {
  /* text-align: center; */
}

.main_img {
  max-height: 400px;
}

</style>