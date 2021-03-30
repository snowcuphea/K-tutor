import { createInstance } from "./index.js"

const instance = createInstance()


function getExamProblems( success, fail ) {

  instance
    .get("/exam")
    .then(success)
    .catch(fail)

}

function sendExamResult( result, success, fail ) {

  instance.defaults.headers['Authorization'] = "jwt " + window.localStorage.getItem('jwt')

  instance
    .post("/exam", result)
    .then(success)
    .catch(fail)

}

function getExamReport( success, fail ) {

  instance.defaults.headers['Authorization'] = "jwt " + window.localStorage.getItem('jwt')

  instance
    .get("/exam/report")
    .then(success)
    .catch(fail)

}


export { getExamProblems, sendExamResult, getExamReport }