import { createStore } from 'vuex'

export default createStore({
  state: {
    account: {
      token: 0,
      username: 'san',
      user_id: 1115,
      role:'teacher'
    },
    menuInfo: {
      title: '主页',
      path: '/index'
    }
  },
  mutations: {
    setToken(state, payload) {
      state.account.token = payload.token
      state.account.username = payload.username
      state.account.user_id = payload.user_id
      state.account.role = payload.role
    },
    setMenuActive(state, payload) {
      state.menuInfo.title = payload.title
      state.menuInfo.path = payload.path
    }
  },
  actions: {
  
  },
  modules: {
  
  }
})
