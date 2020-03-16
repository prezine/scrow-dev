require('./bootstrap');
import Vuelidate from 'vuelidate';
import Datetime from 'vue-datetime'
import Vue2Filters from 'vue2-filters'
import 'vue-datetime/dist/vue-datetime.css'

window.Vue = require('vue');
import {store} from './store/store';


Vue.use(Datetime);
Vue.use(Vue2Filters);
Vue.use(Vuelidate);

Vue.component('register-user', require('./components/auth/RegisterUser.vue').default);
Vue.component('register-business', require('./components/auth/RegisterBusiness.vue').default);
Vue.component('resend-verification-link', require('./components/auth/ResendVerificationLink.vue').default);
Vue.component('verify-business-details', require('./components/business/VerifyDetails.vue').default);

Vue.component('status-msg', require('./components/utils/StatusMsg.vue').default);

Vue.component('settings-tab', require('./components/settings/SettingsTab.vue').default);

Vue.component('profile-completion-bar', require('./components/users/ProfileCompletion.vue').default);

new Vue({
  el: '#app',
  store
});
