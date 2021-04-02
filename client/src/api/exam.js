import { createInstance } from "./index.js"

const instance = createInstance()


function getExamProblems( success, fail ) {

  instance.defaults.headers['Authorization'] = "jwt " + window.localStorage.getItem('jwt')

  instance
    .get("exam/take")
    .then(success)
    .catch(fail)

}

function sendExamResult( result, success, fail ) {

  instance.defaults.headers['Authorization'] = "jwt " + window.localStorage.getItem('jwt')

  const body = { "score" : result }

  instance
    .post("exam/take", body)
    .then(success)
    .catch(fail)

}

function getExamReport( success, fail ) {

  instance.defaults.headers['Authorization'] = "jwt " + window.localStorage.getItem('jwt')

  instance
    .get("exam/report")
    .then(success)
    .catch(fail)

}


export { getExamProblems, sendExamResult, getExamReport }