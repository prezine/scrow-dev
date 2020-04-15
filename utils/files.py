import calendar
import os
import time

from config.app_config import (
    PROFILE_UPLOAD_PATH,
    BUSINESS_AVATAR_UPLOAD_PATH,
    DOCUMENT_UPLOAD_PATH,
    PRODUCT_IMAGE_UPLOAD_PATH
)


class FileUpload:
    @staticmethod
    def __file_upload(instance, filename, path):
        ts = calendar.timegm(time.gmtime())
        ext = filename.split('.')[-1]
        if instance.id:
            filename = '%s/%s.%s' % (instance.id, ts, ext)
        else:
            filename = '%s.%s' % (ts, ext)
        return os.path.join(path, filename)

    def profile_image_upload_path(self, instance, filename):
        return self.__file_upload(instance, filename, PROFILE_UPLOAD_PATH)

    def business_avatar_upload_path(self, instance, filename):
        return self.__file_upload(instance, filename, BUSINESS_AVATAR_UPLOAD_PATH)

    def product_image_upload_path(self, instance, filename):
        return self.__file_upload(instance, filename, PRODUCT_IMAGE_UPLOAD_PATH)

    def document_upload_path(self, instance, filename):
        return self.__file_upload(instance, filename, DOCUMENT_UPLOAD_PATH)


file_upload_path = FileUpload()
