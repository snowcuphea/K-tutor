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
  const title = klass.title

  instance
    .get(`klass/${type}/${title}/list`)
    .then(success)
    .catch(fail)
}

// 학습카드 상세 정보 받아오기
function getLessonInfo( lessonId, success, fail ) {

  instance.defaults.headers['Authorization'] = "jwt " + window.localStorage.getItem('jwt')

  instance
    .get(`lc/${lessonId}`)
    .then(success)
    .catch(fail)

}

function sendLessonInfo( lessonId, success, fail ) {

  instance.defaults.headers['Authorization'] = "jwt " + window.localStorage.getItem('jwt')

  instance
   .post(`lc/${lessonId}`, lessonId)
   .then(success)
   .catch(fail)
}


export { getClassList, getLessonList, getLessonInfo, sendLessonInfo }