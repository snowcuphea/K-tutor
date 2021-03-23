import Vue from 'vue'
import VueRouter from 'vue-router'
import Class from '../views/Class.vue'
import Test from '../views/Test.vue'
import Achievement from '../views/Achievement.vue'
import MyPage from '../views/MyPage.vue'
import Report from '../views/Report.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/',
    redirect: '/report',
  },
  {
    path: '/report',
    name: 'Report',
    component: Report,
  },
  {
    path: '/class',
    name: 'Class',
    component: Class
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
