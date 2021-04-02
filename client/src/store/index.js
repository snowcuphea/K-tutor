// import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"
import { getLessonList, getLessonInfo, sendLessonInfo, getQuizInfo } from "@/api/klass.js"
import { getExamProblems, getExamReport } from "@/api/exam.js"
import { getExp, getMyAcieve, addAchieve } from "@/api/account.js"

Vue.use(Vuex)



export default new Vuex.Store({
  state: {
    time: null,
    alert: {
      status: false,
      color: "primary",
      content: "",
    },

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
    currentClass: {name_kor: '사랑의불시착', type:'drama', level:1}, //최근 클래스 정보
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

    testChance: 2,
    quizChance: 3,

    studyCnt: 0,
    contiDay: 0,

    AchievementList:[],
  
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
      state.currentClass = {name_kor: '사랑의불시착', type:'drama', level:1}
      state.classList = []
      state.userGrade_score = []
      state.userGrade_date = []
      state.progress = []
      state.recent_lc_progress = []
      state.recent_learned_lc = []
      state.testChance = 2
      state.quizChance = 3
      state.AchievementList = []
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
        title: state.currentClass.name_kor,
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
      // state.time = new Date().getDay()
      state.time = new Date().getMinutes()

      state.currentClass = { type: report.recent_cs.type, name_kor: report.recent_cs.name_kor, name_eng:report.recent_cs.name_eng ,level: Number(report.recent_cs.level) }

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
          if ( progress.title === state.currentClass.name_kor ){
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
        title: state.currentClass.name_kor, done: 0, total: state.classList.length
      }

      state.recent_lc_progress.push(progressForm)
      console.log(state.recent_lc_progress)
    },
    SAVEACIEVEMENTLIST ( state, achievements ) {
      const achieve_list = []

      for (let achievement of achievements) {
        const achieve_arr = {
          id: achievement.id, title:achievement.title, content:achievement.content, src:require('@/assets/img/score.png'), total:30, done:3
        }
        achieve_list.push(achieve_arr)
      }
      state.AchievementList = achieve_list
    },

    SHOWALERT ( state, alertInfo ) {
      
      var timeout = 2000

      if ( alertInfo.color == "error" || alertInfo.color == "warning" ) {
        timeout = 3000
      }

      state.alert = alertInfo
      setTimeout(() => {
        state.alert.status = false
      }, timeout);

    },
    RESETCHANCE ( state ) {
      state.quizChance = 3
      state.testChance = 2
      console.log("reset 됐어")
    },
    CHANGECHANCE ( state, type) {
      if ( type == "test" ) {
        state.testChance -= 1
        console.log(state.testChance)
      } else {
        state.quizChance -= 1
        console.log(state.quizChance)
      }
    },
    COMPLETEACHIEVE ( state, achieveId ) {
      state.AchievementList[achieveId-1].status = 1
      console.log(state.AchievementList)
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
      console.log("selectedItem", selectedItem)
      let selectedClassInfo ={
        type : selectedItem.type,
        name_kor: selectedItem.name_kor,
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
        name: state.currentClass.name_kor
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
          commit( 'SAVEACIEVEMENTLIST', res.data )
        },
        (err) => {
          console.log(err.data)
        }
      )
      console.log(commit)
    },

    deleteUser( {commit} ) {
      commit('LOGOUT')
    },
    showAlert( {commit}, alertInfo ) {
      commit("SHOWALERT", alertInfo)
    },
    resetChance( { commit } ) {
      commit('RESETCHANCE')
    },
    changeChance( { commit }, type ) {
      commit('CHANGECHANCE', type)
    },
    completeAchieve({ commit }, achieveInfo ) {
      
      const achieveForm = {
        ...achieveInfo,
        "status": 1,
      }
      
      addAchieve(
        achieveForm,
        (res) => {
          console.log(res.data)
          commit( "COMPLETEACHIEVE", achieveInfo.id )
        },
        (err) => {
          console.log(err)
        }
      )
    }

  },

  modules: {
  },

  plugins: [createPersistedState()],

})
