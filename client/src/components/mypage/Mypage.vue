<template>
  <div>
    <v-expand-transition @click="detailClick">
        <div v-show="show">
        <v-divider></v-divider>

        {{ pageModalItem.contents }}                  

        </div>
    </v-expand-transition>
    
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
    pageModalItem: {
      type: Object,
      require: false,
    },
  },
  methods: {
    detailClick() {
      this.$emit('pageUpdate',this.pageModalItem)
    },
  },
}
</script>

<style>

</style>