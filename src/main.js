import Vue from 'vue'
import App from '@/App.vue'

import store from '@/store/'
import router from '@/router'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.config.productionTip = false;

// Vue.use(VueRouter)
Vue.use(ElementUI);

const vue = new Vue({
  router,
  store,
  render: h => h(App)
});

vue.$mount('#app');
