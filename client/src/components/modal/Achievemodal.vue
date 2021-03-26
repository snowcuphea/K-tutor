<template>
  <div>
    <v-img
      width="100%"
      height="100%"
      :src="modalItem.src"
      @click="modalClick"
    />
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
      this.$emit('update',this.modalItem)
    },
  },
}
</script>

<style>

</style>