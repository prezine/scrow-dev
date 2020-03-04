import axios from 'axios';

export default {
  resendVerificationLink: ({commit}) => {
    axios.post('/api/users/resend-verification-link').then(resp => {
      commit('sendVerificationLink', true);
      commit('setstatusMsg', {msg: resp.data.response, type: 'success'});
    }).catch(err => {
      commit('sendVerificationLink', false);
      commit('setstatusMsg', {msg: err.response.data.response, type: 'error'});
    });
  }
};
