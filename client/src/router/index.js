import Vue from 'vue'
import VueRouter from 'vue-router'
import Class from '../views/Class.vue'
// import ClassMain from '../views/class/ClassMain.vue'
import Test from '../views/Test.vue'
import Achievement from '../views/Achievement.vue'
import MyPage from '../views/MyPage.vue'
import Report from '../views/Report.vue'
import Login from '../views/user/Login.vue'
import Signup from '../views/user/Signup.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/report',
    name: 'Report',
    component: Report,
  },
  {
    path: '/class',
    name: 'Class',
    component: Class,
    // children: [
    //   {
    //     path: '',
    //     redirect: 'classmain'
    //   },
    //   {
    //     path: 'classmain',
    //     name: 'ClassMain',
    //     component: ClassMain
    //   },

    // ],
  },

  {
    path: '/test',
    name: 'Test',
    component: Test
  },
  {
    path: '/achievement',
    name: 'Achievement',
    component: Achievement
  },
  {
    path: '/mypage',
    name: 'MyPage',
    component: MyPage
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router