<template>
  <v-container>
    <div class="modal-overlay"
      v-if="visible"
      @click="closeModal"
      >
      <div class="modal-window">

        <v-img 
          :src="item.src"
          height="50%"
          width="50%"
          padding="0"
          class="modal_img"
        />
        <v-card-text class="modal_title">
          {{ item.title }}
        </v-card-text>

        <v-card-text class="modal_contents">
          {{ item.contents }}
        </v-card-text>
      </div>

    </div>
    <div class="main_progressbar" style="width:95%;">

      <v-row>
        <v-col
          cols="8"
          class="d-flex flex-column"
        >
          <h6>업적 달성률</h6>

          <v-progress-linear
            color="light-blue"
            height="10"
            value="30"
            striped
          >

          </v-progress-linear>

        </v-col>
        <v-col
          cols="4"
        >
          <div class="d-flex justify-end">
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
              <v-icon @click="viewCalendar">mdi-calendar-range</v-icon>
            </v-btn>

          </div>

        </v-col>
      </v-row>
    </div>
    <div>

      <div class="wrap d-flex flex-column" v-if="viewlist">

        <div
          v-for = "(item, idx) in $store.state.items"
          :key = "idx"
        >

          <appMyModal :modalItem="item" @update="modal" />


          <v-divider></v-divider>

        </div>

      </div>
      <div v-if="viewcalendar">
        
        <v-row
          class="d-flex wrap"

        >
          <v-col
            cols="4"
            v-for = "(item,idx) in $store.state.items"
            :key = "idx"
          >
            <appMyModal2 :modalItem="item" @update2="modal" />

          </v-col>
        </v-row>

      </div>
    </div>
    
  </v-container>
</template>

<script>
import Achievemodal from '../components/modal/Achievemodal'
import Achievemodal2 from '../components/modal/Achievemodal2'

export default {
  name: "Achievement",
  components: {
    appMyModal: Achievemodal,
    appMyModal2: Achievemodal2
  },
  data: () => ({
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
      console.log(this.viewlist)
      console.log(this.viewcalendar)

    },
    viewCalendar () {
      if (this.viewcalendar == false) {
        this.viewcalendar = !this.viewcalendar
        this.viewlist = !this.viewlist
      }
      console.log(this.viewlist)
      console.log(this.viewcalendar)

    }
  },
  created() {
    this.$store.dispatch('getAchievementList')
  }
}
</script>

<style>

.main_progressbar {
  position: fixed;
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
  z-index: 1;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
}

.modal-window {
  padding: 10px 20px;
  background: #fff;
  border-radius: 4px;
  overflow: hidden;
  min-width: 500px;
}

.modal_img {
  height: 50%;
  width: 50%;
  margin-left: 25%;
}

.modal_title {
  text-align: center;
}

.modal_contents {
  text-align: center;
}

.main_img {
  max-height: 400px;
}

</style>