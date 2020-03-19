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

export const formErrorHandler = (response, storeInstance, fieldErrorsHolder) => {
  if (response.non_field_errors) {
    storeInstance.commit({type: 'warning', msg: response.non_field_errors})
  } else {
    fieldErrorsHolder = response;
  }
};
