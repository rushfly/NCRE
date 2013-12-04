#coding=utf8
import os
from cntest.settings import MEDIA_ROOT


def handle_uploaded_file(f, path):
    with open(MEDIA_ROOT + path, 'wb+') as destination:  # 使用with不需要close文件
        for chunk in f.chunks():
            destination.write(chunk)
    return None


def media_exist(file_name):
    file_name = MEDIA_ROOT + file_name
    #    raise AssertionError
    if os.path.exists(file_name):
        return True
    else:
        return False


def delete_media(filename):
    """
    删除指定的media下文件，内部调用，无url接口，安全
    """
    filename = MEDIA_ROOT + filename
    #    raise AssertionError
    if os.path.exists(filename):
        try:
            os.remove(filename)
        except:
            pass
    return