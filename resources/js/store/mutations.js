export default {
  sendVerificationLink: (state, payload) => {
    state.resendVerificationLink.sent = payload;
  },
  setstatusMsg: (state, payload) => {
    state.statusMsg = payload;
  },
  createUser: (state, payload) => state.userCreated = payload
};
