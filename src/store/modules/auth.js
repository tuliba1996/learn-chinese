import authServices from '../../services/authServices'


const state = {
    token: '',
  show_error: false
};


const getters = {
  token: state => {
    return state.token
  }
};


const actions = {
  login({ commit }, payload) {
    authServices.login(payload)
    .then(data => {
      commit('setToken', data)
    })
    .catch(err =>{
      commit('showError', err)
    })
  },
};

const mutations = {
  setToken (state, data) {
    state.token = data.access;
    state.show_error = false;
  },
  showError(state, err) {
    state.show_error = true;
  }
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}