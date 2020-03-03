window._ = require('lodash');

window.axios = require('axios');

window.axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

window.axios.defaults.xsrfCookieName = 'csrftoken';
window.axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
