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


function updateUser( user, success, fail ) {

  instance.defaults.headers['Authorization'] = "jwt " + window.localStorage.getItem('jwt')

  const accountInfo = {
    nickname: user.userNickname,
    password: user.userPassword
  }

  instance
    .put("account/modify_delete", accountInfo)
    .then(success)
    .catch(fail)
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

  const achievedForm = {
    "AcId" : String(achieved)
  }

  instance
    .post("account/achievements", achievedForm)
    .then(success)
    .catch(fail)

}

function sendEmail( mail, success, fail) {

  const mailInfo = {
    "title": mail.title,
    "content": mail.content,
  }
  console.log(mailInfo)

  instance.defaults.headers['Authorization'] = "jwt " + window.localStorage.getItem('jwt')

  instance
    .post("account/inquiry", mailInfo)
    .then(success)
    .catch(fail)

}


export { getToken, getInfo, signUp, getExp, getMyAcieve, addAchieve, deleteUser, sendEmail, updateUser }
