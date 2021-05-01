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

//部署时增加，解决跨域问题
axios.defaults.baseURL = "http://112.124.56.37:8000/"

Vue.use(VueCookies);
Vue.use(VueAxios, axios);
Vue.use(ElementUI);
axios.defaults.baseURL = "http://172.17.0.3:8000/"
Vue.config.productionTip = false;
Vue.prototype.$axios = axios;
Vue.prototype.$cookies = VueCookies;
Vue.prototype.$echarts = echarts

new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>'
})


