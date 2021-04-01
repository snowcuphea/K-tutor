<template>
  <div>
    <!-- <v-list> -->
      <v-row style="margin-bottom: 0.5%; margin-top: 0.5%;">
        <v-col cols="4">
          <v-img
            width="100%"
            height="100%"
            :src="modalItem.src"
            @click="modalClick"
          />
        </v-col>
        <v-col cols="8" class="py-0 pr-0">
          <v-row class="d-flex flex-column align-items-center">
            <v-col>
              <h3>
                {{ modalItem.title }}

              </h3>

            </v-col>
            <v-col>
              <h5 style="margin:0;">
                {{ modalItem.contents }}

              </h5>

            </v-col>
            <v-col>
              <v-progress-linear
                style="width: 90%"
                color="light-blue"
                height="13"
                :value="modalItem.num*100/modalItem.max_num"
                striped
              >
                <h6>
                  {{ modalItem.num }} / {{ modalItem.max_num }}

                </h6>
              </v-progress-linear>

            </v-col>

          </v-row>

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
  },
}
</script>

<style>

.title_contents {
  /* flex-direction: column; */
}

</style>