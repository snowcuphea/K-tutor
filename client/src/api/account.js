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

export { getToken, getInfo, signUp }