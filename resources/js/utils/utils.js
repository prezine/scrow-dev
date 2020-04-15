export const fileHandler = (file, extensions = [], maxFileSize) => {
  return new Promise((resolve, reject) => {
    if (!extensions.includes(file.type)) {
      reject('Unsupported file type!');
    }
    if (file.size > maxFileSize) {
      reject('File size ' + (file.size / 1024).toFixed(2) + 'KB is too big.');
    }
    resolve(true);
  });
};

export const formErrorHandler = (response, instance) => {
  if (response.non_field_errors) {
    instance.$store.commit('setstatusMsg', {type: 'warning', msg: response.non_field_errors[0]});
  } else {
    instance.formErrors = response;
  }
};

export const non400ErrorMsg = (instance) => {
  instance.$store.commit('setstatusMsg', {
    type: 'warning',
    msg: 'Request could not be completed. Please reload and try again.'
  });
};
