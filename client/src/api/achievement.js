import { createInstance } from "./index.js"

const instance = createInstance()

function getAchieve( success, fail ) {

  instance.defaults.headers['Authorization'] = "jwt " + window.localStorage.getItem('jwt')

  instance
    .get("achievements")
    .then(success)
    .catch(fail)
}

// function getAchieve( success, fail ) {

//   instance.defaults.headers['Authorization'] = "jwt " + window.localStorage.getItem('jwt')

//   instance
//     .post("achievements")
//     .then(success)
//     .catch(fail)
// }




export { getAchieve }