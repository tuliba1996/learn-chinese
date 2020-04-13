import Vue from 'vue'
import Vuex from 'vuex'
import messages from './modules/messages'
import words from './modules/words'
import lessons from "./modules/lessons";
import auth from "./modules/auth"
Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
    messages,
    words,
    lessons,
  }
})