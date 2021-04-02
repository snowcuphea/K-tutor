import { createInstance } from "./index.js"

const instance = createInstance()

// 전체 수업(?) 받아오기
function getClassList( success, fail ) {

  instance
    .get("klass/cs/list")
    .then(success)
    .catch(fail)

}

// 학습카드 전체 받아오기
function getLessonList( klass, success, fail ) {

  instance.defaults.headers['Authorization'] = "jwt " + window.localStorage.getItem('jwt')

  const type = klass.type
  const name_kor = klass.name_kor

  instance
    .get(`klass/${type}/${name_kor}/list`)
    .then(success)
    .catch(fail)
}

// 학습카드 상세 정보 받아오기
function getLessonInfo( lessonId, success, fail ) {

  instance.defaults.headers['Authorization'] = "jwt " + window.localStorage.getItem('jwt')
   

  instance
    .get(`klass/lc/${lessonId}`)
    .then(success)
    .catch(fail)

}

// 학습카드 수강 완료 요청 
function sendLessonInfo( lessonInfo, success, fail ) {

  instance.defaults.headers['Authorization'] = "jwt " + window.localStorage.getItem('jwt')

  instance
   .post(`klass/lc/${lessonInfo.id}`, lessonInfo)
   .then(success)
   .catch(fail)
}

function getQuizInfo( info ,success, fail ) {

  instance.defaults.headers['Authorization'] = "jwt " + window.localStorage.getItem('jwt')

  instance
    .get(`klass/${info.type}/${info.name}/quiz`)
    .then(success)
    .catch(fail)
}


export { getClassList, getLessonList, getLessonInfo, sendLessonInfo, getQuizInfo }