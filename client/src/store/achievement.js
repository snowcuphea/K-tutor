function newbie( isLogin, completedAchieve) {

  if ( isLogin && !completedAchieve.includes(1)) {
    return true
  } else {
    return false
  }
}

// function climber( ) {

// }

function flexx( completedAchieve ) {

  if ( completedAchieve.length == 8 && !completedAchieve.includes(3) ) {
    return true
  } else {
    return false
  }

}

function slump( grade, completedAchieve ) {

    if ( grade < 50 && !completedAchieve.includes(4)) {
      return true
    } else {
      return false
    }

}

function easyPeasy( grade, completedAchieve ) {

  if ( grade == 100 && !completedAchieve.includes(5)) {
    return true
  } else {
    return false
  }

}

function intermediate( level, completedAchieve ) {

  if ( level == 5 && !completedAchieve.includes(6)) {
    return true
  } else {
    return false
  }

}

// function hardWorker(  , completedAchieve ) {


// }

// function getBreak(  , completedAchieve ) {


// }

// function becomingPro(  , completedAchieve) {


// }





export { newbie, flexx, slump, easyPeasy, intermediate }