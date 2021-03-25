import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"


Vue.use(Vuex)



export default new Vuex.Store({
  state: {
    currentPage: '', //밑 navbar에서 선택한 페이지
    currentPageValue: 2, //밑 navbar에서 선택한 index
    currentType: '', //선택한 타입(영화, 드라마, 가수) 
    currentClass:'', //최근 클래스 정보
    defaultClass:{cs_seq:1, cs_title: '싸이코지만괜찮아', cs_type:'drama', cs_level:1}, 

    allTitleList: [
      {cs_seq:1, cs_title: '싸이코지만괜찮아', cs_type:'drama', cs_level:1},
      {cs_seq:2, cs_title: '사랑의불시착', cs_type:'drama', cs_level:1},
      {cs_seq:3, cs_title: '스위트홈', cs_type:'drama', cs_level:3},
      {cs_seq:4, cs_title: '미스터선샤인', cs_type:'drama', cs_level:2},
      {cs_seq:5, cs_title: '이태원클라쓰', cs_type:'drama', cs_level:2},

      {cs_seq:6, cs_title: '승리호', cs_type:'movie', cs_level:1},
      {cs_seq:7, cs_title: '부산행', cs_type:'movie', cs_level:2},
      {cs_seq:8, cs_title: '설국열차', cs_type:'movie', cs_level:2},
      {cs_seq:9, cs_title: '반도', cs_type:'movie', cs_level:3},
      {cs_seq:10, cs_title: '극한직업', cs_type:'movie', cs_level:1},

      {cs_seq:11, cs_title: '방탄소년단', cs_type:'pop', cs_level:1},
      {cs_seq:12, cs_title: '블랙핑크', cs_type:'pop', cs_level:1},
      {cs_seq:13, cs_title: '아이유', cs_type:'pop', cs_level:1},
      {cs_seq:14, cs_title: '소녀시대', cs_type:'pop', cs_level:2},
      {cs_seq:15, cs_title: '트와이스', cs_type:'pop', cs_level:2},
      {cs_seq:16, cs_title: '태연', cs_type:'pop', cs_level:2},
      {cs_seq:17, cs_title: '악동뮤지션', cs_type:'pop', cs_level:3},
      {cs_seq:18, cs_title: '갓세븐', cs_type:'pop', cs_level:3},
      {cs_seq:19, cs_title: '세븐틴', cs_type:'pop', cs_level:3},
      {cs_seq:20, cs_title: '엑소', cs_type:'pop', cs_level:1},
      {cs_seq:21, cs_title: '박효신', cs_type:'pop', cs_level:1},

    ],
    
    userName: 'DanceMachine',
    userLevel: 4,
    userExperience: 39,
    userGrade: [30,60,20,70,80,50,30,20,70,90],

    userProgress: {
      genres: [
        { type : 'kmovie', total : 58, done : 45 },
        { type: 'kdrama', total : 80, done : 57 },
        { type : 'kpop', total : 94, done : 89 }
      ],
      class: [
        { title: '태양의 후예', total : 100, done : 35},
        { title: '도깨비', total : 100, done : 87},
        { title: '승리호', total : 43, done : 23},
        { title: '사이코지만 괜찮아', total : 100, done : 64},
        { title: '기생충', total : 100, done : 64},
        { title: '박효신', total : 87, done : 64},
        { title: '방탄소년단', total : 70, done : 64},
      ]
    },

    userLearned: [
      { title : '태양의 후예', line: '봄바람 휘날리며', img : 'poster1' },
      { title : '도깨비', line: '흩날리는 벚꽃 잎이', img : 'poster1' },
      { title : '방탄소년단', line: '울려 퍼질 이 거리를 우우 둘이 걸어요', img : 'poster1' },
      { title : '승리호', line: '바람 불면 울렁이는 기분 탓에 나도 모르게', img : 'poster1' },
      { title : '아이유', line: '바람ㄴ 불면 저편에서', img : 'poster1' },
      { title : '태양의 후예', line: '봄바람 휘날리며', img : 'poster1' },
      { title : '도깨비', line: '흩날리는 벚꽃 잎이', img : 'poster1' },
      { title : '방탄소년단', line: '울려 퍼질 이 거리를 우우 둘이 걸어요', img : 'poster1' },
      { title : '승리호', line: '바람 불면 울렁이는 기분 탓에 나도 모르게', img : 'poster1' },
      { title : '아이유', line: '바람ㄴ 불면 저편에서', img : 'poster1' },
    ],

    studyCnt: 100,
    contiDay: 9,
    



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
