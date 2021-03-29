<template>
  <div>
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

    <v-container class="wrap d-flex flex-wrap main_img" id="achieve_body">
      <v-col
        rows
        cols="4"
        v-for = "(item, idx) in $store.state.items"
        :key = "idx"
      >
      
        <appMyModal :modalItem="item" @update="modal" />

      </v-col>
    </v-container>
    <div>
      <v-container>
        <v-flex>업적 달성률</v-flex>
      </v-container>
      <v-container>
        <v-row style="margin-left: 5px">
          <v-progress-linear
            style="width: 60%"
            color="light-blue"
            height="10"
            value="30"
            striped
          ></v-progress-linear>
          
          <v-flex text-right style="margin-right: 10px">
            <div>9 / 30</div>

          </v-flex>
        </v-row>
      </v-container>

    </div>

    
    <!-- <v-card-actions>
      <v-spacer></v-spacer>

      <v-btn
        icon
        @click="show = !show"
      >
        <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
      </v-btn>
    </v-card-actions>
    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>

        <v-container class="d-flex flex-wrap">
          <v-col
            rows
            cols="4"
            v-for = "(item, idx) in $store.state.items"
            :key = "idx"

          >
            <appMyModal :modalItem="item" @update="modal" />

          </v-col>
        </v-container>
      </div>
    </v-expand-transition> -->
    
  </div>
</template>

<script>
import Achievemodal from '../components/modal/Achievemodal'

export default {
  name: "Achievement",
  components: {
    appMyModal: Achievemodal
  },
  data: () => ({
    visible: false,
  }),
  methods: {
    modal (modalItem) {
      this.item = modalItem,
      this.visible = !this.visible
    },
    closeModal () {
      this.visible = !this.visible
    }
  }
}
</script>

<style>

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