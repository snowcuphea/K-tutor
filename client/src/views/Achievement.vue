<template>
  <div>
    <v-container class="progress_top">
    </v-container>

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
      <v-subheader style="padding:0;">
        <v-container class="progress_top">

          <v-row style="margin-bottom: 0;">
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
                  <v-icon @click="viewCalendar">mdi-calendar-range</v-icon>
                </v-btn>
                
              
              </div>

            </v-col>
          </v-row>
        </v-container>
        <!-- <v-row>
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
        </v-row> -->
        <!-- <div class="main_progressbar" style="width:90%;">

        </div> -->
      </v-subheader>
      <div style="padding-top: 3%;">

        <div class="wrap d-flex flex-column" v-if="viewlist">

          <div
            v-for = "(item, idx) in $store.state.AchievementList"
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
              v-for = "(item,idx) in $store.state.AchievementList"
              :key = "idx"
            >
              <appMyModal2 :modalItem="item" @update2="modal" />

            </v-col>
          </v-row>

        </div>
      </div>
      
    </v-container>
  </div>
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