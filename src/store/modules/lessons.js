import lessonServices from '../../services/lessonServices'

const state = {
  lessons: []
};

const getters = {
  lessons: state => {
    return state.lessons
  }
};

const actions = {
  getLessons({ commit }) {
    lessonServices.fetchLesson()
    .then(lessons => {
      commit('setLessons', lessons)
    })
  },
  addLesson({ commit }, lessons) {
    lessonServices.postLesson(lessons)
    .then(() => {
      commit('addLesson', lessons)
    })
  },
  deleteLesson( { commit }, lessonId) {
    lessonServices.deleteLesson(lessonId);
    commit('deleteLesson', lessonId)
  }
};

const mutations = {
  setLessons (state, lessons) {
    state.lessons = lessons
  },
  addLesson(state, lesson) {
    state.messages.push(lesson)
  },
  deleteLesson(state, lessonId) {
    state.lessons = state.lessons.filter(obj => obj.id !== lessonId)
  }
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}