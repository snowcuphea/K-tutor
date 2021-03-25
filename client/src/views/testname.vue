<template>
  <div>
    <v-app-bar>

    </v-app-bar>
    <v-col
      rows
      cols="4"
      v-for="(item, index) in items"
      :key = "index"
    >
      <v-img
        :src="item.src"
        height="100%"
        width="100%"
        padding="0"
        @click="imgClick"
      />

        <app-my-modal
          :item = "item"
          :visible.sync="visible">
        </app-my-modal>

  </div>
</template>

<script>
import Achivemodal from '../components/modal/Achivemodal'
export default {
  components: {
    myModal: Achivemodal
  },
  data: () => ({
    items: [
      {
        title: 'score',
        src: require('@/assets/img/score.png'),
        contents: '1',
      },
      {
        title: 'award',
        src: require('@/assets/img/award.png'),
        contents: '2',
      },
      {
        title: 'hardworker',
        src: require('@/assets/img/hardworker.png'),
        contents: '135',
      },
      {
        title: 'jun',
        src: require('@/assets/img/jun.png'),
        contents: '123124',
      },
      {
        title: 'korean',
        src: require('@/assets/img/korean.png'),
        contents: '1255215',
      },
      {
        title: 'kpop',
        src: require('@/assets/img/kpop.png'),
        contents: '1234',
      },
      {
        title: 'level',
        src: require('@/assets/img/level.png'),
        contents: '6',
      },
      {
        title: 'master',
        src: require('@/assets/img/master.png'),
        contents: '4',
      },
      {
        title: 'sign',
        src: require('@/assets/img/sign.png'),
        contents: '3',
      },
    ],
    visible: false,
  }),
  methods: {
    imgClick() {
      this.visible = !this.visible
    }
  }
}
</script>

<style>

#progress {
  width: 50%;
}

</style>