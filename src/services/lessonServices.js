import api from '@/services/api'

export default {
  fetchLesson() {
    return api.get(`lesson/`)
              .then(response => response.data)
  },
  postLesson(payload) {
    return api.post(`lesson/`, payload)
              .then(response => response.data)
  },
  deleteLesson(lessonId) {
    return api.delete(`lesson/${lessonId}`)
              .then(response => response.data)
  }
}