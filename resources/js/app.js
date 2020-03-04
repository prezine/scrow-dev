require('./bootstrap');
import Vuelidate from 'vuelidate';

window.Vue = require('vue');
import {store} from './store/store';

Vue.use(Vuelidate);

Vue.component('register-user', require('./components/auth/RegisterUser.vue').default);
Vue.component('resend-verification-link', require('./components/auth/ResendVerificationLink.vue').default);
Vue.component('status-msg', require('./components/utils/StatusMsg.vue').default);

new Vue({
  el: '#app',
  store
});
