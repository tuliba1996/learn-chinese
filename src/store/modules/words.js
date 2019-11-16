import wordServices from '../../services/wordServices'

const state = {
    words: []
};

const getters = {
    words: state => {
        return state.words
    }
};

const actions = {
    getWord({commit}) {
        wordServices.fetchWord()
            .then(word => {
                commit('setWords', word)
            })
    },
    getWords({commit}, lessonId) {
      console.log(`lessid`, lessonId);
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