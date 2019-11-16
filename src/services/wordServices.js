import api from '@/services/api'

export default {
  fetchWord(){
    return api.get(`word/`)
              .then(response => response.data)
  },
  fetchWordInLesson(lessonId) {
    return api.get(`lesson/${lessonId}/get_word`)
              .then(response => response.data)
  },
  postWord(payload) {
    return api.post(`word/`, payload)
              .then(response => response.data)
  },
  deleteWord(wordId) {
    return api.delete(`word/${wordId}`)
              .then(response => response.data)
  },
}