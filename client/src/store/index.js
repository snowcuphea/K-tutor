import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"

import { getLessonList, getLessonInfo, sendLessonInfo, getQuizInfo } from "@/api/klass.js"
import { getExamProblems, getExamReport } from "@/api/exam.js"
import { getExp, getMyAcieve, addAchieve } from "@/api/account.js"

import { climber, flexx } from "@/store/achievement.js"

Vue.use(Vuex)



export default new Vuex.Store({
  state: {
    isLogin: false,
    time: null,
    userEmail: null,
    nickName: null,
    userLevel: 1,
    userExperience: 0,
    required_exp: [
      0, 10, 20, 30, 50, 70,
      100, 150, 200, 250, 300,
      400, 500, 750, 1000 
    ],
    
    userGrade_date : [], 
    userGrade_score : [],
    allProgress: [],        // 전체 type에 대한 진행도
    recent_lc_progress: [], // 최근 학습한 진행도
    recent_learned_lc: [],  // 최근 학습한 학습카드


    alert: {
      status: false,
      color: "primary",
      content: "",
    },


    currentPage: '', //밑 navbar에서 선택한 페이지
    currentPageValue: 2, //밑 navbar에서 선택한 index
    currentType: '', //선택한 타입(영화, 드라마, 가수) 
    currentClass: {},


    allTitleList: [], //{level:"0", name:"소녀시대", type:"kpop"} 형태
    //type은 kpop, drama, movie 세 가지 
    classList:[], //title을 선택하면 나오는 학습 리스트

    currentClassIndex: 0,
    lessonInfo: {},
    dbLessonInfo: {},

    quizInfo: {},
    testQuestions: [],

    testChance: 2,
    quizChance: 3,

    studyCnt: 0,
    contiDay: 0,

    AchievementList: [],
    myCompleteAchievement: [],
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
    getCurrentAchieved: function (state) {
      let list = state.AchievementList.filter(
        (re) => re["status"] == 1
      )
      return list
    }
  },

  mutations: {
    LOGOUT ( state ){
      localStorage.removeItem("jwt")
      state.isLogin = false
      state.userEmail= null
      state.nickName= null
      state.contiDay = 0
      state.studyCnt = 0
      state.userLevel= 1
      state.userExperience= 0
      state.currentPage = ''
      state.currentPageValue = 2
      state.currentType = ''
      state.lessonInfo = {}
      state.dbLessonInfo = {}
      state.currentClass = ''
      state.classList = []
      state.userGrade_score = []
      state.userGrade_date = []
      state.allProgress = []
      state.recent_lc_progress = []
      state.recent_learned_lc = []
      state.testChance = 2
      state.quizChance = 3
      state.AchievementList = []
      state.myCompleteAchievement = []
      state.quizInfo = {}
      state.testQuestions = []
    },

    GETCLASSLIST(state, titlelist){
      console.log(titlelist)
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
      // state.quizInfo = {}
      // state.testQuestions = []
    },
    CHANGECURRENTCLASS ( state, item) {
      // console.log("현재", item)
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
      const lessonForm = {
        id: item.id,
        type: state.currentClass.type,
        title: state.currentClass.name_kor,
        title_eng: state.currentClass.name_eng,
        imgurl: item.imgurl,
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

      state.recent_lc_progress = []
      state.recent_learned_lc = []

      state.currentClass = { 
        type: report.recent_cs.type,
        imgurl: report.recent_cs.imgurl,
        name_kor: report.recent_cs.name_kor, 
        name_eng: report.recent_cs.name_eng ,
        level: report.recent_cs.level 

      }

      const progressForm = [
        {type: "drama", done: report.progress.drama[0] , total: report.progress.drama[1] },
        {type: "kpop", done: report.progress.kpop[0] , total: report.progress.kpop[1] },
        {type: "movie", done: report.progress.movie[0] , total: report.progress.movie[1] }
      ]
      state.allProgress = progressForm
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
      
      // console.log(state.classList[idx])


      if ( state.classList[idx]["already_learned"] == false) {
        
        state.classList[idx]["already_learned"] = true

        for ( let progress of state.recent_lc_progress){
          if ( progress.title === state.currentClass.name_kor ){
            progress.done += 1
          }
        }
        
        for ( let one of state.allProgress ) {
          if ( one.type == state.currentClass.type) {
            one.done += 1
          }
        }
        
        if ( state.recent_learned_lc.length > 9) {
          state.recent_learned_lc.pop()
        }

        state.recent_learned_lc.unshift(state.classList[idx])

        // console.log(state.recent_learned_lc)

      }
    },
    ADDTOPROGRESSLIST ( state ) {
      const progressForm = {
        title: state.currentClass.name_kor, done: 0, total: state.classList.length
      }

      state.recent_lc_progress.push(progressForm)
      // console.log(state.recent_lc_progress)
    },
    SAVEACIEVEMENTLIST ( state, achievements ) {
      // console.log(achievements)
      const achieve_list = []
      const tempComplete = []
      for (let achievement of achievements) {
        const achieve_arr = {
          achievement_id: achievement.achievement_id, 
          title: achievement.title, 
          content: achievement.content, 
          imgurl: achievement.imgurl, 
          done: achievement.done,
          total: achievement.total, 
          status: achievement.status,
          great_kor: achievement.great_kor,
          great_eng: achievement.great_eng,
          great_dsc: achievement.great_dsc,
        }
        achieve_list.push(achieve_arr)
        
        if (achievement.status == 1) {
          tempComplete.push(achievement.achievement_id)
        }
      }
      state.AchievementList = achieve_list
      state.myCompleteAchievement = tempComplete
      // console.log("store", state.AchievementList)
      // console.log("store", state.myCompleteAchievement)
    },

    SHOWALERT ( state, alertInfo ) {
      
      var timeout = 5000

      // if ( alertInfo.color == "error" || alertInfo.color == "warning" ) {
      //   timeout = 3000
      // }

      state.alert = alertInfo
      setTimeout(() => {
        state.alert.status = false
      }, timeout);

    },
    RESETCHANCE ( state, nowTime ) {
      state.quizChance = 3
      state.testChance = 2
      state.time = nowTime
      state.isSameDay = false
      console.log("reset 됐어")
      // console.log(state.time, state.quizChance, state.testChance)
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
      state.myCompleteAchievement.push(achieveId)
    },
    SETTIME ( state ) {
      state.time = new Date().getDate()
    },
    UPDATEUSERINFO ( state, userInfo ) {
      state.nickName = userInfo
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
    gainExperience ({ commit,state }, experience) {

      if (state.userLevel < 15) {
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
      }

    },
    changeCurrentClass ({ commit }, item ) {
      commit('CHANGECURRENTCLASS', item)
    },
    getListCurrentClass ({ commit }, selectedItem) {
      // console.log("selectedItem", selectedItem)
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
          console.log("여기", err)
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
          // console.log(res.data)
          commit( 'SAVEACIEVEMENTLIST', res.data )
        },
        (err) => {
          console.log(err.data)
        }
      )
    },
    deleteUser( {commit} ) {
      commit('LOGOUT')
    },
    showAlert( {commit}, alertInfo ) {
      commit("SHOWALERT", alertInfo)
    },
    resetChance( { commit, state, dispatch }, nowTime ) {
      commit('RESETCHANCE', nowTime)
      if ( climber( state.myCompleteAchievement ) ) {
        dispatch('completeAchieve', 2)
      }
    },
    changeChance( { commit }, type ) {
      commit('CHANGECHANCE', type)
    },
    completeAchieve({ dispatch, commit ,state }, id ) {
      
      if ( state.AchievementList[id-1].status == 0) {
        
        addAchieve(
          id,
          (res) => {
            if (res.data == "Achieved") { 
              commit( "COMPLETEACHIEVE", id )
              const alertInfo = {
                status: true,
                color: "success",
                content: `Achievement "${state.AchievementList[id-1].title}" completed.`
              }
              dispatch('showAlert', alertInfo)
              if ( flexx( state.myCompleteAchievement ) ) {
                dispatch('completeAchieve', 3)
              }
            } else {
              console.log(state.AchievementList[id-1].title ,res.data)
            }
          },
          (err) => {
            console.log(err)
          }
        )
      }
    },
    setTime( { commit }) {
      commit('SETTIME')
    },
    updateUserInfo ( { commit }, userInfo ) {
      commit ( 'UPDATEUSERINFO', userInfo )

    }
  },

  modules: {
  },

  plugins: [createPersistedState()],

})
