<template>
  <div>
    <v-list-item
      @click="detailClick"
    >
      {{ pageDetailItem.title }}
    </v-list-item>

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
    pageDetailItem: {
      type: Object,
      require: false,
    },
  },
  methods: {
    detailClick() {
      this.$emit('pageUpdate',this.pageDetailItem)
    },
  },
}
</script>

<style>

</style>