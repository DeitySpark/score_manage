import { createStore } from 'vuex'

export default createStore({
  state: {
    user: {
      token: 0,
      username: '未登录',
      role:'Student'
    },
    
  },
  mutations: {
    setToken(state, payload) {
      state.user.token = payload.token
      state.user.username = payload.username
      state.user.role = payload.role
    }
  },
  actions: {
  
  },
  modules: {
  
  }
})
