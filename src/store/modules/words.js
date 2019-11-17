import wordServices from '../../services/wordServices'

const state = {
    words: [],              // list words
    word:{}                 // one word
};

const getters = {
    words: state => {
        return state.words
    }
};

const actions = {
    getWord({commit}, wordId) {
        wordServices.fetchWord(wordId)
            .then(word => {
                commit('setWord', word)
            })
    },
    getWords({commit}, lessonId) {
        wordServices.fetchWordInLesson(lessonId)
            .then(words => {
                commit('setWords', words)
            })
    },
    addWord({commit}, words) {
        wordServices.postWord(words)
            .then(() => {
                commit('addWord', words)
            })
    },
    deleteWord({commit}, wordId) {
        wordServices.deleteWord(wordId);
        commit('deleteWord', wordId)
    }
};

const mutations = {
    setWord(state, word){
        state.word = word
    },
    setWords(state, words) {
        state.words = words
    },
    addWord(state, word) {
        state.messages.push(word)
    },
    deleteWord(state, wordId) {
        state.words = state.words.filter(obj => obj.id !== wordId)
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}