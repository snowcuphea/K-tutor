import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"


Vue.use(Vuex)



export default new Vuex.Store({
  state: {
    currentPage: '',
    currentPageValue: 2,
    currentType: '',

    allTitleList: [
      {name: '싸이코지만괜찮아', cs_type:'drama'},
      {name: '사랑의불시착', cs_type:'drama'},
      {name: '스위트홈', cs_type:'drama'},
      {name: '미스터선샤인', cs_type:'drama'},
      {name: '이태원클라쓰', cs_type:'drama'},

      {name: '승리호', cs_type:'movie'},
      {name: '부산행', cs_type:'movie'},
      {name: '설국열차', cs_type:'movie'},
      {name: '반도', cs_type:'movie'},
      {name: '극한직업', cs_type:'movie'},

      {name: '방탄소년단', cs_type:'pop'},
      {name: '블랙핑크', cs_type:'pop'},
      {name: '아이유', cs_type:'pop'},
      {name: '소녀시대', cs_type:'pop'},
      {name: '트와이스', cs_type:'pop'},
      {name: '태연', cs_type:'pop'},
      {name: '악동뮤지션', cs_type:'pop'},
      {name: '갓세븐', cs_type:'pop'},
      {name: '세븐틴', cs_type:'pop'},
      {name: '엑소', cs_type:'pop'},
      {name: '박효신', cs_type:'pop'},

    ],
    
    userLevel: 4,
    userExperience: 39,
    



  },
  getters: {
    getCurrentTypeTitleList: function (state) {
      let list = state.allTitleList.filter(
        (re) => re.cs_type === state.currentType
      )
      return list

    }

  },
  mutations: {
    changeCurrentPage ( state , changeItem ) {
      state.currentPage = changeItem.navName
      state.currentPageValue = changeItem.navValue
    },
    changeExperience ( state, experience ) {
      state.userExperience += (experience)
      const temp = state.userExperience - (state.userLevel)*10
      if ( state.userExperience >= state.userLevel*10 ) {
        state.userExperience = state.userLevel*10
        setTimeout( function() {
          state.userLevel += 1
          state.userExperience = 0
        },500)
        setTimeout( function () {
          state.userExperience += temp
        }, 500)
      }
    }
  },
  actions: {
    changePage ({ commit }, changeItem ) {
      commit('changeCurrentPage', changeItem)
    },
    gainExperience ({ commit }, experience) {
      setTimeout( function() {
        commit('changeExperience', experience )
      }, 1000)
    }
  },
  modules: {
  },

  plugins: [createPersistedState()],

})
