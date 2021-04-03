<template>
  <div>
    <!-- <v-list> -->
      <v-row style="margin-bottom: 0.5%; margin-top: 0.5%;">
        <v-col cols="4">
          <v-img
            width="100%"
            height="100%"
            :src="modalItem.imgurl"
            @click="modalClick"
            :class="isDone() ? '':'achievementNot'"
          />
        </v-col>
        <v-col cols="8" class="d-flex flex-column">
          <h3>
            {{ modalItem.title }}

          </h3>
          <v-spacer></v-spacer>
          <h5 style="margin:0;">
            {{ modalItem.content }}

          </h5>
          <v-spacer></v-spacer>
          <v-progress-linear
            style="width: 90%"
            color="light-blue"
            height="13"
            :value="modalItem.done*100/modalItem.total"
            striped
          >
            <h6>
              {{ modalItem.done }} / {{ modalItem.total }}

            </h6>
          </v-progress-linear>

        </v-col>

      </v-row>

    <!-- </v-list> -->
  </div>
  
</template>


<script>
export default {
  props: {
    visible: {
      type: Boolean,
      require: true,
      default: false
    },
    modalItem: {
      type: Object,
      require: false,
    },
  },
  methods: {
    modalClick() {
      this.$emit('update2',this.modalItem)
    },
    isDone() {
      if (this.modalItem.status == 1) {
        return true
      } else {
        return false
      }
    }
  },
}
</script>

<style>

.title_contents {
  /* flex-direction: column; */
}

</style>