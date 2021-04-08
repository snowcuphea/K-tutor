function newbie( isLogin, completedAchieve) {

  if ( isLogin && !completedAchieve.includes(1)) {
    return true
  } else {
    return false
  }
}

function climber( completedAchieve ) {

  if ( !completedAchieve.includes(2)) {
    return true
  } else {
    return false
  }

}

function flexx( completedAchieve ) {
  
  if ( !completedAchieve.includes(3) ) {
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

function intermediate( completedAchieve ) {

  if ( !completedAchieve.includes(6)) {
    return true
  } else {
    return false
  }

}

function hardWorker( completedAchieve ) {

  if ( !completedAchieve.includes(7) ) {
    return true
  } else {
    return false
  }

}

function getBreak( completedAchieve ) {

  if ( !completedAchieve.includes(8) ) {
    return true
  } else {
    return false
  }

}

function becomingPro( grade, completedAchieve ) {

  if ( grade ==  100 && !completedAchieve.includes(9)) {
    return true
  } else {
    return false
  }

}




export { newbie, climber, flexx, slump, easyPeasy, intermediate, hardWorker, getBreak, becomingPro }