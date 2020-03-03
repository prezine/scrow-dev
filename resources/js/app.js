require('./bootstrap');
import Vuelidate from 'vuelidate';
window.Vue = require('vue');

Vue.use(Vuelidate);

Vue.component('register-user', require('./components/auth/RegisterUser.vue').default);

new Vue({
    el: '#app',
});
