import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import(/* webpackChunkName: "login" */ '@/views/LoginView'),
    meta: {
      isKeepAlive: false
    }
  },
  {
    path: '/index',
    name: 'index',
    component: () => import('@/views/IndexView'),
    meta: {
      isKeepAlive: true
    }
  }
]


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
