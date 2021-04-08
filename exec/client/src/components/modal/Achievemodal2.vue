<template>
  <div>
    <v-img
      id="img"
      width="100%"
      height="100%"
      :src="require(`@/assets/images/achievement/${modalItem.imgurl}`)"
      @click="modalClick"
      :class="isDone() ? '':'achievementNot'"
    />
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
      if (this.isDone() ) {
        this.$emit('update2',this.modalItem)
      }
    },
    isDone() {
      if (this.modalItem.status == 1) {
        return true
      } else {
        return false
      }
    }
  },
  created() {

  }


}
</script>

<style>




</style>