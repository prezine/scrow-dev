export default {
  isVerificationLinkSent: state => {
    return state.resendVerificationLink.sent;
  },
  statusMsg: state => {
    return state.statusMsg;
  },
  userCreated: state => state.userCreated
};
