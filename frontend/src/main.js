// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import axios from "axios";
import VueAxios from 'vue-axios'
import VueCookies from "vue-cookies";

import App from './App'
import router from "./router";
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import echarts from 'echarts'

Vue.use(VueCookies);
Vue.use(VueAxios, axios);
Vue.use(ElementUI);

//解决跨域，部署时采用
axios.defaults.baseURL = 'http://112.124.56.37:8000/'

Vue.prototype.$echarts = echarts
Vue.config.productionTip = false;
Vue.prototype.$axios = axios;
Vue.prototype.$cookies = VueCookies;
/* eslint-disable no-new */


new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>'
})


