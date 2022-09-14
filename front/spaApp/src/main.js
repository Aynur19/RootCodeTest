import 'vuetify/dist/vuetify.min.css'
import Vue from "vue";
import Vuetify from 'vuetify';
import App from "./App.vue";

Vue.config.productionTip = false;

Vue.use(Vuetify)

new Vue({
  el: '#app',
  vuetify: new Vuetify(),
  render: h => h(App)
})
