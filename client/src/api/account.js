import { createInstance } from "./index.js"

const instance = createInstance()

function getToken(user, success, fail) {

  const account = {
    username: user.userEmail,
    password: user.userPassword
  }

  instance
    .post("account/api/token", account)
    .then(success)
    .catch(fail);
  
}

function getInfo( success, fail ) {

  instance.defaults.headers['Authorization'] = "jwt " + window.localStorage.getItem('jwt')

  instance
    .get("account/login")
    .then(success)
    .catch(fail)
}

function deleteUser( success, fail ) {

  instance.defaults.headers['Authorization'] = "jwt " + window.localStorage.getItem('jwt')

  instance
    .delete("account/modify_delete")
    .then(success)
    .catch(fail)
}

function signUp(user, success, fail ){
  const accountInfo = {
    username: user.userEmail,
    password: user.userPassword,
    nickname: user.userNickname
  }

  instance
    .post("account/signup", accountInfo)
    .then(success)
    .catch(fail);
}

function getExp( exp, success, fail ){
  
  instance.defaults.headers['Authorization'] = "jwt " + window.localStorage.getItem('jwt')

  const expInfo = {
    "exp": exp
  }

  instance
    .post("account/get_exp", expInfo)
    .then(success)
    .catch(fail)

}

function getMyAcieve( success, fail ){

  instance.defaults.headers['Authorization'] = "jwt " + window.localStorage.getItem('jwt')

  instance
    .get("account/achievements")
    .then(success)
    .catch(fail)

}

function addAchieve( achieved, success, fail ){

  instance.defaults.headers['Authorization'] = "jwt " + window.localStorage.getItem('jwt')

  instance
    .post("account/achievements", achieved)
    .then(success)
    .catch(fail)

}

function sendEmail( mail, success, fail) {

  instance.defaults.headers['Authorization'] = "jwt " + window.localStorage.getItem('jwt')

  instance
    .post("account/inquiry", mail)
    .then(success)
    .catch(fail)

}


export { getToken, getInfo, signUp, getExp, getMyAcieve, addAchieve, deleteUser, sendEmail }
