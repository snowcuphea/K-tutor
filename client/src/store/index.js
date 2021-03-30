// import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"
import {getLessonList } from "@/api/klass.js"


Vue.use(Vuex)



export default new Vuex.Store({
  state: {
    loginUserInfo:'',

    currentPage: '', //밑 navbar에서 선택한 페이지
    currentPageValue: 2, //밑 navbar에서 선택한 index
    currentType: '', //선택한 타입(영화, 드라마, 가수) 
    currentClass:'', //최근 클래스 정보
    defaultClass:{cs_seq:1, cs_title: '싸이코지만괜찮아', cs_type:'drama', cs_level:1}, 
    classList:[], //title을 선택하면 나오는 학습 리스트


    allTitleList: [], //{level:"0", name:"소녀시대", type:"kpop"} 형태
    //type은 kpop, drama, movie 세 가지 
    
    userName: 'DanceMachine',
    userLevel: 4,
    userExperience: 35,
    userGrade: {
      dates : [
        "2021-03-31 23:32:32","2021-03-31 23:32:32","2021-03-31 23:32:32",
        "2021-03-31 23:32:32","2021-03-31 23:32:32","2021-03-31 23:32:32",
        "2021-03-31 23:32:32","2021-03-31 23:32:32","2021-03-31 23:32:32",
        "2021-03-31 23:32:32"
      ],
      grades : [
        20,30,50,70,30,50,70,80,90,50
      ]
    },
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
    quizInfo: {},
    testQuestions: [],
    studyCnt: 100,
    contiDay: 9,
  
    items: [
      {
        title: '빛나는 트로피',
        src: require('@/assets/img/score.png'),
        contents: 'test에서 만점을 5회 달성하셨습니다',
        max_num: 5,
        num: 3
      },
      {
        title: '출석왕',
        src: require('@/assets/img/award.png'),
        contents: '30일 동안 매일 출석',
        max_num: 30,
        num: 5
      },
      {
        title: '오늘만 사는 사람',
        src: require('@/assets/img/hardworker.png'),
        contents: '하루에 카드 30개 학습',
        max_num: 30,
        num: 10
      },
      {
        title: '초보',
        src: require('@/assets/img/jun.png'),
        contents: '1개의 작품 학습 완료',
        max_num: 1,
        num: 0
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
        (re) => re.type === state.currentType
      )
      return list
    },

    getCurrentClassLearnedKeword: function (state) {
      let list = state.userLearnedKeword.filter(
        (re) => re.type === state.currentClass.cs_seq
      )
      return list
    },
  },

  mutations: {
    // setToken: function () {
    //   const token = localStorage.getItem('jwt')

    //   const config = {
    //     headers: {
    //       Authorization: `JWT ${token}`
    //     }
    //   }
    //   return config
    // },

    // LOGIN (state, userData) {
    //   localStorage.setItem('jwt', userData.token)
    //   state.loginUserInfo = userData

    // },
    LOGOUT ( state ){
      state.loginUserInfo = ''
      state.currentPage = ''
      state.currentPageValue = 2
      state.currentType = ''
      state.currentClass =''
      state.classList = []
      state.userName = ''
      state.userLevel = 1
      state.userExperience = 0
      state.userGrade = []
      state.userLearnedKeword = []
    },
    GETCLASSLIST(state, titlelist){
      state.allTitleList = titlelist
    },
  
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
    GETLISTCURRENTCLASS (state, resclassList) {
      //titleInfo.cs_seq로 axios 요청받아서 리스트 받아오기
      console.log("뮤테이션 getListCurrentClass실행:::", resclassList)
      const tempClassList = [
        {cpct_seq:1, title:state.currentClass.name, img:'poster1', keyword:'싶어', keyword_en: 'to want' },
        {cpct_seq:2, title:state.currentClass.name, img:'poster2', keyword:'좋아', keyword_en: 'I like it'},
        {cpct_seq:3, title:state.currentClass.name, img:'poster3', keyword:'사랑해', keyword_en: 'I love you'},
      ]
      state.classList = tempClassList
      // state.classList = resclassList

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
    },
    getQuizInfo ( state ) {
      const quizForm = {
        type: 'drama',
        title : '태양의 후예',
        quizzes: [
          {
            lines_kr : ["오늘 저녁에 뭐 먹었어?", "나는 오늘 저녁으로 고기를 먹었어.","오, 맛있었니?"],
            lines_en : ["What did you have for dinner?", "I had proteins for dinner.","Wow, how was it?"]
          },
          {
            lines_kr : ["나랑 벚꽃축제 갈래?", "너무 좋아, 나도 벚꽃 보러 가고 싶었어.","그러면 토요일 어때?"],
            lines_en : ["Wanna visit the cherry blossom festival with me?", "Yes, I would love to go see cherry blossoms.","Saturday sounds good?"]
          },
          {
            lines_kr : ["오늘 저녁에 뭐 먹었어?", "나는 오늘 저녁으로 고기를 먹었어.","오, 맛있었니?"],
            lines_en : ["What did you have for dinner?", "I had proteins for dinner.","Wow, how was it?"]
          },
          {
            lines_kr : ["나랑 벚꽃축제 갈래?", "너무 좋아, 나도 벚꽃 보러 가고 싶었어.","그러면 토요일 어때?"],
            lines_en : ["Wanna visit the cherry blossom festival with me?", "Yes, I would love to go see cherry blossoms.","Saturday sounds good?"]
          },
          {
            lines_kr : ["나랑 벚꽃축제 갈래?", "너무 좋아, 나도 벚꽃 보러 가고 싶었어.","그러면 토요일 어때?"],
            lines_en : ["Wanna visit the cherry blossom festival with me?", "Yes, I would love to go see cherry blossoms.","Saturday sounds good?"]
          },
        ]
      }
      state.quizInfo = quizForm
    },
    GETTESTQUESTIONS ( state ) {
      const testForm = [
        {source : "태양의 후예", type: "drama",
        lines_kr : ["오늘 저녁에 뭐 먹었어?", "나는 오늘 저녁으로 고기를 먹었어.","오, 맛있었니?"],
        lines_en : ["What did you have for dinner?", "I had proteins for dinner.","Wow, how was it?"]},
        {source : "도깨비", type: "movie",
        lines_kr : ["나랑 벚꽃축제 갈래?", "너무 좋아, 나도 벚꽃 보러 가고 싶었어.","그러면 토요일 어때?"],
        lines_en : ["Wanna visit the cherry blossom festival with me?", "Yes, I would love to go see cherry blossoms.","Saturday sounds good?"]},
        {source : "에일리 - 어느 날 우연히", type: "pop",  
        lines_kr : ["만약에 너에게 전활 걸면", "쓰다만 메시지를 보내면","무작정 찾아가서 널 본다면"],
        lines_en : ["Wanna visit the cherry blossom festival with me?", "Yes, I would love to go see cherry blossoms.","Saturday sounds good?"]},
        {source : "대화체", type: "chat",
        lines_kr : ["이렇게 한줄로만 나오는 문제도 있다."],
        lines_en : ["There are questions that only have one sentence."]}
      ]

      state.testQuestions = testForm
    },
    GETTESTGRADES ( state ) {
      const gradeForm = {
        date : [
          "31","1","2","3","4","4","4","5","5","6"
        ],
        scores : [
          20,30,50,70,30,50,70,80,90,50
        ]
      }

      state.userGrade = gradeForm
    }
  },

  actions: {
    // Login({ commit }, user){
    //   axios.post(`${SERVER_URL}/ktutor/login/`, user)
    //   .then(res => {
    //     commit("LOGIN", res.data)
    //   })
    //   .catch(err => {
    //     console.log("로그인 에러", err)
    //   })

    // },
    logout ( {commit} ){
      commit('LOGOUT')
    },
    getClassList({ commit }, titlelist ){ //로긴하고나서 타이틀제목가져옴
      commit('GETCLASSLIST', titlelist)
    },

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
    getListCurrentClass ({ commit }, selectedItem) {
      let selectedClassInfo ={
        type : selectedItem.type,
        title: selectedItem.name,
      }
      getLessonList(
        selectedClassInfo
        ,
        (res) => {
          console.log("getLessonList 액션즈 실행", res.data)
          commit('GETLISTCURRENTCLASS',res.data )
        },
        (err) => {
          console.log("getLessonList 액션즈 실패", err)
          console.log("집어넣은 selectedClassInfo,",selectedClassInfo )
        }
      )
      
    },
    getLessonInfo ({ commit }) {
      commit('getLessonInfo')
    },
    getQuizInfo ({ commit }) {
      commit('getQuizInfo')
    },
    getTestQuestions ({ commit } ) {
      commit('GETTESTQUESTIONS')
    },
    getTestGrades ({ commit }) {
      commit( 'GETTESTGRADES' )
    }

  },

  modules: {
  },

  plugins: [createPersistedState()],

})
