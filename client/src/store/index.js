// import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"
import { getLessonList, getLessonInfo, sendLessonInfo, getQuizInfo } from "@/api/klass.js"
import { getExamProblems, getExamReport } from "@/api/exam.js"
import { getExp, getMyAcieve } from "@/api/account.js"

Vue.use(Vuex)



export default new Vuex.Store({
  state: {
    isLogin: false,
    userEmail: null,
    nickName: null,
    userLevel: 1,
    userExperience: 0,
    required_exp: [0, 10, 20, 30, 50, 70,
      100, 150, 200, 250, 300,
      400, 500, 600, 750, 1000],


    currentPage: '', //밑 navbar에서 선택한 페이지
    currentPageValue: 2, //밑 navbar에서 선택한 index
    currentType: '', //선택한 타입(영화, 드라마, 가수) 
    currentClass: {name: '사랑의불시착', type:'drama', level:1}, //최근 클래스 정보
    defaultClass:'', 
    classList:[], //title을 선택하면 나오는 학습 리스트


    allTitleList: [], //{level:"0", name:"소녀시대", type:"kpop"} 형태
    //type은 kpop, drama, movie 세 가지 
    
    userGrade_date : [],
    userGrade_score : [],

    progress: [],

    recent_lc_progress: [],
    recent_learned_lc: [],

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
    LOGOUT ( state ){
      localStorage.removeItem("jwt")
      state.isLogin = false
      state.userEmail= null,
      state.nickName= null,
      state.contiDay = 0,
      state.studyCnt = 0,
      state.userLevel= 1,
      state.userExperience= 0,
      state.currentPage = ''
      state.currentPageValue = 2
      state.currentType = ''
      // 나중에 최근 학습내역으로 해야하나
      state.currentClass = {name: '사랑의불시착', type:'drama', level:1}
      state.classList = []
      state.userGrade_score = []
      state.userGrade_date = []
      state.progress = []
      state.recent_lc_progress = []
      state.recent_learned_lc = []
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
      const temp = state.userExperience - state.required_exp[state.userLevel]
      if ( state.userExperience >= state.required_exp[state.userLevel] ) {
        state.userExperience = state.required_exp[state.userLevel]
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
    GETQUIZINFO ( state, problems ) {

      const quizForm = {
        title : problems[0].cs,
        quizzes: []
      }
      
      for (let problem of problems) {
        const problemForm = {
          lines_kr : [problem.problem.before_kor, problem.problem.main_kor, problem.problem.after_kor ],
          lines_en : [problem.problem.before_eng, problem.problem.main_eng, problem.problem.after_eng ],
        }
        quizForm.quizzes.push(problemForm)
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
    GETTESTGRADES ( state, grades ) {

      state.userGrade_score = []
      state.userGrade_date = []

      for ( let grade of grades) {
        state.userGrade_score.push(grade.score)
        state.userGrade_date.push(grade.exam_date)
      }

    },
    GETREPORTINFO ( state, report ) {

      console.log(report)
      state.currentClass = { type: report.recent_cs.type, name: report.recent_cs.name, level: Number(report.recent_cs.level) }
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

      if ( report.recent_learned_lc.length > 10) {
        var amount = 10
      } else {
        amount = report.recent_learned_lc.length
      }

      for (let idx = 0; idx < amount; idx++) {
        const lessonCardForm = {
          id: report.recent_learned_lc[idx].id,
          imgurl: report.recent_learned_lc[idx].imgurl,
          main_kw_kor: report.recent_learned_lc[idx].main_kw_kor,
          main_kw_eng: report.recent_learned_lc[idx].main_kw_eng,
        }
        state.recent_learned_lc.push(lessonCardForm)
      }

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
      
      console.log(state.classList[idx])

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
        
        state.recent_learned_lc.pop()
        
        const lessonCardForm = {
          id: state.classList[idx].id ,
          imgurl: null,
          main_kw_kor: state.classList[idx].main_kw_kor,
          main_kw_eng: state.classList[idx].main_kw_eng,
        }

        state.recent_learned_lc.unshift(lessonCardForm)

        state.classList[idx]["already_learned"] = true
      }
    },
    ADDTOPROGRESSLIST ( state ) {
      const progressForm = {
        title: state.currentClass.name, done: 0, total: state.classList.length
      }

      state.recent_lc_progress.push(progressForm)
      console.log(state.recent_lc_progress)
    },
    SAVEACIEVEMENTLIST ( state, achievements ) {
      const achieve_arr = []

      // console.log(achievements)
      for (let achievement in achievements) {
        this.achieve_arr.push({title:achievement.title, content:achievement.content, url:achievement.imgurl})

      }
      console.log(achieve_arr)
      // for (let achievement of achievements) {
      //   const achievementForm = {
      //     title: achievement
      //   }
          // achievementsrc: require('@/assets/img/score.png'),
          // contents: 'test에서 만점을 5회 달성하셨습니다',
          // max_num: 5,
          // num: 3
        // }
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

      getExp(
        experience,
        (res) => {
          console.log(res.data)
        },
        (err) => {
          console.log(err)
        }
      )

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
    getQuizInfo ({ commit, state }) {

      const form = {
        type: state.currentClass.type,
        name: state.currentClass.name
      }

      getQuizInfo(
        form,
        (res) => {
          commit('GETQUIZINFO', res.data )
        },
        (err) => {
          console.log(err)
        }
      )

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
          commit( 'GETTESTGRADES', res.data )
        },
        (err) => {
          console.log("최근 성적 10개 받아오기", err)
        }
      )

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
    changeCurrentClassIndex ( { commit }, idx ) {
      commit( 'CHANGECURRENTCLASSINDEX', idx)
    },
    addtoProgressList( { commit } ) {
      commit( 'ADDTOPROGRESSLIST' )
    },
    getAchievementList( {commit } ) {

      getMyAcieve(
        (res) => {
          console.log(res.data)
          // commit( 'SAVEACIEVEMENTLIST', res.data )
        },
        (err) => {
          console.log(err.data)
        }
      )
      console.log(commit)
    },

    deleteUser( {commit} ) {
      commit('LOGOUT')
    }




  },

  modules: {
  },

  plugins: [createPersistedState()],

})
