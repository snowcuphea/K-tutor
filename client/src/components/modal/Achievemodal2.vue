<template>
  <div>

    <v-img
        width="100%"
        height="100%"
        :src="modalItem.src"
        @click="modalClick"
    >
        
    </v-img>


  </div>
</template>

<script>
export default {
  props: {
    modalItem: {
      type: Object,
      require: false,
    },
  },
  methods: {
    modalClick() {
      this.$emit('update2',this.modalItem)
    },
  }

}
</script>

<style>

</style>