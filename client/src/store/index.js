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
    classList:[], //title을 선택하면 나오는 학습 리스트


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
    userExperience: 35,
    userGrade: [30,60,20,70,80,50,30,20,70,90],
    userLearnedKeword: [ //유저가 학습한 키워드랑 키워드에 대한 정보
      
      {learned_seq:1, cpct_seq:1, cs_seq:3, cs_title: '스위트홈', cs_type:'drama', cs_level:3},
      {learned_seq:2, cpct_seq:1,  cs_seq:4, cs_title: '미스터선샤인', cs_type:'drama', cs_level:2},
      {learned_seq:3, cpct_seq:2,  cs_seq:4, cs_title: '미스터선샤인', cs_type:'drama', cs_level:2},

      {learned_seq:5, cpct_seq:1,  cs_seq:6, cs_title: '승리호', cs_type:'movie', cs_level:1},
      {learned_seq:6, cpct_seq:2,  cs_seq:6, cs_title: '승리호', cs_type:'movie', cs_level:1},
      {learned_seq:7, cpct_seq:3,  cs_seq:6, cs_title: '승리호', cs_type:'movie', cs_level:1},

      {learned_seq:9, cpct_seq:1, cs_seq:11, cs_title: '방탄소년단', cs_type:'pop', cs_level:1},
      {learned_seq:10, cpct_seq:2, cs_seq:11, cs_title: '방탄소년단', cs_type:'pop', cs_level:1},
      {learned_seq:11, cpct_seq:3, cs_seq:11, cs_title: '방탄소년단', cs_type:'pop', cs_level:1},

    ],

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
      { title : '도깨비', line: '흩날리는 벚꽃 잎이', img : 'poster7' },
      { title : '방탄소년단', line: '울려 퍼질 이 거리를 우우 둘이 걸어요', img : 'poster11' },
      { title : '승리호', line: '바람 불면 울렁이는 기분 탓에 나도 모르게', img : 'poster1' },
      { title : '아이유', line: '바람ㄴ 불면 저편에서', img : 'poster7' },
      { title : '태양의 후예', line: '봄바람 휘날리며', img : 'poster11' },
      { title : '도깨비', line: '흩날리는 벚꽃 잎이', img : 'poster1' },
      { title : '방탄소년단', line: '울려 퍼질 이 거리를 우우 둘이 걸어요', img : 'poster1' },
      { title : '승리호', line: '바람 불면 울렁이는 기분 탓에 나도 모르게', img : 'poster1' },
      { title : '아이유', line: '바람ㄴ 불면 저편에서', img : 'poster1' },
    ],
    
    lessonInfo: {},

    studyCnt: 100,
    contiDay: 9,
  
    items: [
      {
        title: '빛나는 트로피',
        src: require('@/assets/img/score.png'),
        contents: 'test에서 만점을 5회 달성하셨습니다',
      },
      {
        title: '출석왕',
        src: require('@/assets/img/award.png'),
        contents: '30일 동안 매일 출석',
      },
      {
        title: '오늘만 사는 사람',
        src: require('@/assets/img/hardworker.png'),
        contents: '하루에 카드 30개 학습',
      },
      {
        title: '초보',
        src: require('@/assets/img/jun.png'),
        contents: '1개의 작품 학습 완료',
      },
      {
        title: '명예 한국인',
        src: require('@/assets/img/korean.png'),
        contents: '학습률 100% 달성',
      },
      {
        title: '팝스타',
        src: require('@/assets/img/kpop.png'),
        contents: 'K-POP 30개 이상 학습 완료',
      },
      {
        title: '만렙',
        src: require('@/assets/img/level.png'),
        contents: '레벨 10 달성',
      },
      {
        title: '마스터',
        src: require('@/assets/img/master.png'),
        contents: '한 장르의 학습률 100% 달성',
      },
      {
        title: '신생아',
        src: require('@/assets/img/sign.png'),
        contents: '계정 생성 완료',
      },
      {
        title: '100수생',
        src: require('@/assets/img/tester.png'),
        contents: 'test 100회 완료',
      },
      {
        title: '중수',
        src: require('@/assets/img/sen.png'),
        contents: '10개의 작품 학습 완료',
      },
      {
        title: '빛나는 트로피',
        src: require('@/assets/img/score.png'),
        contents: 'test에서 만점을 5회 달성하셨습니다',
      },
      {
        title: '출석왕',
        src: require('@/assets/img/award.png'),
        contents: '30일 동안 매일 출석',
      },
      {
        title: '오늘만 사는 사람',
        src: require('@/assets/img/hardworker.png'),
        contents: '하루에 카드 30개 학습',
      },
      {
        title: '초보',
        src: require('@/assets/img/jun.png'),
        contents: '1개의 작품 학습 완료',
      },
      {
        title: '명예 한국인',
        src: require('@/assets/img/korean.png'),
        contents: '학습률 100% 달성',
      },
      {
        title: '팝스타',
        src: require('@/assets/img/kpop.png'),
        contents: 'K-POP 30개 이상 학습 완료',
      },
      {
        title: '만렙',
        src: require('@/assets/img/level.png'),
        contents: '레벨 10 달성',
      },
      {
        title: '마스터',
        src: require('@/assets/img/master.png'),
        contents: '한 장르의 학습률 100% 달성',
      },
      {
        title: '뉴비',
        src: require('@/assets/img/sign.png'),
        contents: '계정 생성 완료',
      },
      {
        title: '100수생',
        src: require('@/assets/img/tester.png'),
        contents: 'test 100회 완료',
      },
      {
        title: '중수',
        src: require('@/assets/img/sen.png'),
        contents: '10개의 작품 학습 완료',
      },
    ],
  },
  
  getters: {
    getCurrentTypeTitleList: function (state) {
      let list = state.allTitleList.filter(
        (re) => re.cs_type === state.currentType
      )
      return list
    },

    getCurrentClassLearnedKeword: function (state) {
      let list = state.userLearnedKeword.filter(
        (re) => re.cs_seq === state.currentClass.cs_seq
      )
      return list
    },
  },

  mutations: {
    changeCurrentPage ( state , changeItem ) {
      state.currentPage = changeItem.navName
      state.currentPageValue = changeItem.navValue
    },
    changeExperience ( state, experience ) {
      state.userExperience += experience
      const temp = state.userExperience - (state.userLevel)*10
      if ( state.userExperience >= state.userLevel*10 ) {
        state.userExperience = state.userLevel*10
        setTimeout( function() {
          state.userLevel += 1
          state.userExperience = 0
        },1500)
        setTimeout( function () {
          state.userExperience += temp
        }, 1500)
      }
    },
    changeLastGrade ( state, grade ) {
      state.userGrade.shift();
      state.userGrade.push(grade)
    },
    changeCurrentClass ( state, item) {
      state.currentClass =item
    },
    getListCurrentClass (state, titleInfo) {
      //titleInfo.cs_seq로 axios 요청받아서 리스트 받아오기
      console.log("뮤테이션 getListCurrentClass실행:::", titleInfo)
      const tempClassList = [
        {cpct_seq:1, title:titleInfo.cs_title, img:'poster1', keyword:'싶어', keyword_en: 'to want' },
        {cpct_seq:2, title:titleInfo.cs_title, img:'poster2', keyword:'좋아', keyword_en: 'I like it'},
        {cpct_seq:3, title:titleInfo.cs_title, img:'poster3', keyword:'사랑해', keyword_en: 'I love you'},
      ]
      state.classList = tempClassList

    },
    getLessonInfo ( state ) {
      // axios 요청 보내서 state에 저장
      const lessonForm = {
        type: 'drama',
        title: '태양의 후예',
        img: 'poster1',
        keyword_kr: '싶어',
        keyword_en: 'to want',
        lines_kr: [
          "나랑 벚꽃축제 갈래?",  
          "너무 좋아, 나도 벚꽃 보러 가고 싶었어.", 
          "그러면 토요일 어때?"
        ],
        lines_en:  [
          "Wanna visit the cherry blossom festival with me?", 
          "Yes, I would love to go see cherry blossoms.",
          "Saturday sounds good?"
        ],
        example_kr: [
          "제주도 가고 싶다.",
          "예제2"
        ],
        example_en: [
          "Want to visit Jeju Island.",
          "example2"
        ]
      }
      state.lessonInfo = lessonForm
    }
  },

  actions: {
    changePage ({ commit }, changeItem ) {
      commit('changeCurrentPage', changeItem)
    },
    gainExperience ({ commit }, experience) {
      setTimeout( function() {
        commit('changeExperience', experience )
      }, 1500)
    },
    changeLastGrade ({ commit }, grade ) {
      commit('changeLastGrade', grade)
    },
    changeCurrentClass ({ commit }, item ) {
      commit('changeCurrentClass', item)
    },
    getListCurrentClass ({ commit }, titleInfo) {
      commit('getListCurrentClass', titleInfo)
    },
    getLessonInfo ({ commit }) {
      commit('getLessonInfo')
    }
  },

  modules: {
  },

  plugins: [createPersistedState()],

})
