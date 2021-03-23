import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"


Vue.use(Vuex)



export default new Vuex.Store({
  state: {
    currentPage: '',
    currentPageValue: 2,
    currentGenre: '',

  },
  mutations: {
    changeCurrentPage ( state , changeItem ) {
      state.currentPage = changeItem.navName
      state.currentPageValue = changeItem.navValue
    }
  },
  actions: {
    changePage ({ commit }, changeItem ) {
      commit('changeCurrentPage', changeItem)
    }
  },
  modules: {
  },

  plugins: [createPersistedState()],

})
