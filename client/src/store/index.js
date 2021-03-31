// import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"
import { getLessonList, getLessonInfo, sendLessonInfo } from "@/api/klass.js"
import { getExamProblems, getExamReport } from "@/api/exam.js"

Vue.use(Vuex)



export default new Vuex.Store({
  state: {
    isLogin: false,
    userEmail: null,
    nickName: null,
    userLevel: 1,
    userExperience: 0,

    currentPage: '', //밑 navbar에서 선택한 페이지
    currentPageValue: 2, //밑 navbar에서 선택한 index
    currentType: '', //선택한 타입(영화, 드라마, 가수) 
    currentClass:{name: '사랑의불시착', type:'drama', level:1}, //최근 클래스 정보
    defaultClass:'', 
    classList:[], //title을 선택하면 나오는 학습 리스트


    allTitleList: [], //{level:"0", name:"소녀시대", type:"kpop"} 형태
    //type은 kpop, drama, movie 세 가지 
    
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

    progress: [],

    recent_lc_progress: [],

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
    
    currentClassIndex: 0,
    lessonInfo: {},
    dbLessonInfo: {},
    quizInfo: {},
    testQuestions: [],
    studyCnt: 0,
    contiDay: 0,
  
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
      let list = state.classList.filter(
        (re) => re["already_learned"] == true
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
      localStorage.removeItem("jwt")
      state.isLogin = false
      state.userEmail= null,
      state.nickName= null,
      state.userLevel= 1,
      state.userExperience= 0,
      state.currentPage = ''
      state.currentPageValue = 2
      state.currentType = ''
      // 나중에 최근 학습내역으로 해야하나
      state.currentClass = {name: '사랑의불시착', type:'drama', level:1}
      state.classList = []
      state.userGrade = []
      state.userLearnedKeword = []
      state.progress = []
      state.recent_lc_progress = []
  

    },
    GETCLASSLIST(state, titlelist){
      state.allTitleList = titlelist
    },
  
    CHANGECURRENTPAGE ( state , changeItem ) {
      state.currentPage = changeItem.navName
      state.currentPageValue = changeItem.navValue
    },
    CHANGEEXPERIENCE ( state, experience ) {
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
    CHANGECURRENTCLASS ( state, item) {
      state.currentClass = item
      // console.log("뮤ㄴ=텡이션 현재커렌트클래스",state.currentClass )
    },
    GETLISTCURRENTCLASS (state, resclassList) {
      //titleInfo.cs_seq로 axios 요청받아서 리스트 받아오기
      // console.log("뮤테이션 getListCurrentClass실행:::", resclassList)
      state.classList = resclassList
      // console.log("현재 클래스 리스트는?", state.classList)

    },
    GETLESSONINFO ( state, item ) {
      // console.log("받아온 레슨인포", item)
      // console.log("받아오고 현재 currnetClass", state.currentClass)
      // axios 요청 보내서 state에 저장

      const lessonForm = {
        id: item.id,
        type: state.currentClass.type,
        title: state.currentClass.name,
        img: 'poster1',
        keyword_kr: item.main_kw_kor,
        keyword_en: item.main_kw_eng,
        lines_kr: [
          item.before_kor,  
          item.cpct_kor, 
          item.after_kor
        ],
        lines_en:  [
          item.before_eng,  
          item.cpct_eng, 
          item.after_eng
        ],
        example_kr: [
          item.example_kor,
        ],
        example_en: [
          item.example_eng
        ]
      }
      state.lessonInfo = lessonForm
      state.dbLessonInfo = item
      // console.log("레슨인포수정해떵0", state.lessonInfo)
    },
    GETQUIZINFO ( state ) {
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
    GETTESTQUESTIONS ( state , questions ) {
      let test = []
      for (let question of questions) {
        let lines = []
        if ( question.problem.before) {
          lines = [question.problem.before, question.problem.main, question.problem.after]
        } else {
          lines = [question.problem.main]
        }

        const testForm = {
          source : question.cs,
          lines_kr : lines,
        }
        test.push(testForm)
      }

      state.testQuestions = test
    },
    GETTESTGRADES ( state ) {
      const gradeForm = {
        dates : [
          "2021-03-31 23:32:32","2021-03-31 23:32:32","2021-03-31 23:32:32",
          "2021-03-31 23:32:32","2021-03-31 23:32:32","2021-03-31 23:32:32",
          "2021-03-31 23:32:32","2021-03-31 23:32:32","2021-03-31 23:32:32",
          "2021-03-31 23:32:32"
        ],
        grades : [
          20,30,50,70,30,50,70,80,90,50
        ]
      }
      
      state.userGrade = gradeForm
    },
    GETREPORTINFO ( state, report ) {
      const progressForm = [
        {type: "drama", done: report.progress.drama[0] , total: report.progress.drama[1] },
        {type: "kpop", done: report.progress.kpop[0] , total: report.progress.kpop[1] },
        {type: "movie", done: report.progress.movie[0] , total: report.progress.movie[1] }
      ]
      state.progress = progressForm
      state.isLogin = true
      state.nickName = report.user.nickname
      state.userLevel = report.user.level
      state.userExperience = report.user.exp
      state.studyCnt = report.learned_lc_cnt
      state.contiDay = report.user.consecutive_access

      
      console.log(report.recent_learned_lc)

      for (let progress in report.recent_lc_progress) {
        const lcProgressForm = {
          title: progress, done: report.recent_lc_progress[progress][0], total: report.recent_lc_progress[progress][1]
        }
        state.recent_lc_progress.push(lcProgressForm)
      }


    },
    ADDUSEREMAIL ( state, userEmail ) {
      state.userEmail = userEmail
    },
    CHANGECURRENTCLASSINDEX ( state, idx ) {
      state.currentClassIndex = idx
    },
    SENDCOMPLETELESSON ( state, idx ) {

      if ( state.classList[idx]["already_learned"] == false) {

        for ( let progress of state.recent_lc_progress){
          if ( progress.title === state.currentClass.name ){
            progress.done += 1
          }
        }
        
        for ( let one of state.progress ) {
          if ( one.type == state.currentClass.type) {
            one.done += 1
          }
        }

        state.classList[idx]["already_learned"] = true
      }
    },
    ADDTOPROGRESSLIST ( state ) {
      const progressForm = {
        title: state.currentClass.name, done: 0, total: state.classList.length
      }

      state.recent_lc_progress.push(progressForm)
      console.log(state.recent_lc_progress)
    }

  },

  actions: {
    logout ( {commit} ){
      commit('LOGOUT')
    },
    getClassList({ commit }, titlelist ){ //로긴하고나서 타이틀제목가져옴
      commit('GETCLASSLIST', titlelist)
    },

    changePage ({ commit }, changeItem ) {
      commit('CHANGECURRENTPAGE', changeItem)
    },
    gainExperience ({ commit }, experience) {
      setTimeout( function() {
        commit('CHANGEEXPERIENCE', experience )
      }, 1500)
    },
    changeCurrentClass ({ commit }, item ) {
      commit('CHANGECURRENTCLASS', item)
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
          // console.log("getLessonList 액션즈 실행", res.data)
          commit('GETLISTCURRENTCLASS',res.data )
          commit('CHANGECURRENTCLASS',selectedItem )
        },
        (err) => {
          console.log("getLessonList 액션즈 실패", err)
          console.log("집어넣은 selectedClassInfo,",selectedClassInfo )
        }
      )
      
    },
    getLessonInfoByItem ({ commit }, itemId) {
      getLessonInfo(
        itemId,
        (res) => {
          // console.log("getLessonInfoByItem뮤테이션",res.data)
          commit('GETLESSONINFO', res.data)

        },
        (err) => {
          console.log("asdfsadfsdad,ItemId", itemId)
          console.log("getLessonInfoByItem뮤테이션에러", err)

        }
      )
      // // 임시로 요청 실패해도 커밋 보내지게
      // commit('GETLESSONINFO', itemId)
      
    },
    getQuizInfo ({ commit }) {
      commit('GETQUIZINFO')
    },
    getTestQuestions ( { commit } ) {
      getExamProblems(
        (res) => {
          commit('GETTESTQUESTIONS', res.data)
        },
        (err) => {
          console.log("시험문제 10개 받아오기", err)
        }
      )
    },
    getTestGrades ({ commit }) {

      getExamReport(
        (res) => {
          console.log(res)
        },
        (err) => {
          console.log("최근 성적 10개 받아오기", err)
        }
      )

      commit( 'GETTESTGRADES' )
    },
    getReportInfo( { commit }, reportData ) {
      commit( 'GETREPORTINFO', reportData )
    },
    addUserEmail( { commit }, userEmail ) {
      commit ( 'ADDUSEREMAIL', userEmail )
    },
    sendCompleteLesson( { commit, state }, idx ) {

      const lessonInfo = {
        ...state.dbLessonInfo,
        "already_learned": true,
      }

      sendLessonInfo(
        lessonInfo,
        (res) => {
          console.log(res.data)
        },
        (err) => {
          console.log(err)
        }
      )

      commit( "SENDCOMPLETELESSON", idx )
    },
    changeCurrentClassIndex ( { commit }, idx) {
      commit( 'CHANGECURRENTCLASSINDEX', idx)
    },
    addtoProgressList( { commit }) {
      commit( 'ADDTOPROGRESSLIST' )
    }


  },

  modules: {
  },

  plugins: [createPersistedState()],

})
