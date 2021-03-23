import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    currentPage: 'Report',
  },
  mutations: {
    changeCurrentPage ( state , pageName ) {
      state.currentPage = pageName
    }
  },
  actions: {
    changePage ({ commit }, pageName ) {
      commit('changeCurrentPage', pageName)
    }
  },
  modules: {
  }
})
