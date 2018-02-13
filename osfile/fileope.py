#-------------------------------------------------------------------------------
# Name:        fileope.py
# Purpose:     ファイル操作用モジュール
#
# Author:      shikano.takeki
#
# Created:     22/12/2017
# Copyright:   (c) shikano.takeki 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
import os
import shutil
import gzip
import tarfile
import zipfile

def get_file_names(dir_path: str):
    """指定したディレクトリ直下のファイル名一覧を取得する関数.

    Args:
        param1 dir_path: ファイル名一覧を取得するディレクトリパス.

    Returns:
        ファイル名の一覧を格納したリスト.
    """
    file_names = list()
    if not dir_path[-1] in "/":
        dir_path += "/"
    for file in os.listdir(dir_path):
        if os.path.isfile(r"{0}{1}".format(dir_path, file)):
            file_names.append(file)

    return file_names

def get_dir_names(dir_path: str):
    """指定したディレクトリ直下のディレクトリ名一覧を取得する関数.

    Args:
        param1 dir_path: ディレクトリ名一覧を取得するディレクトリパス。

    Returns:
        ディレクトリ名の一覧を格納したリスト.
    """
    dir_names = list()
    if not dir_path[-1] in "/":
        dir_path += "/"
    for dir in os.listdir(r"{}".format(dir_path)):
        if os.path.isdir(r"{0}{1}".format(dir_path, dir)):
            dir_names.append(dir)

    return dir_names

def dir_exists(path: str):
    """wrapper of os.path.isdir().

    Args:
        param1 path: directory path.

    Returns:
        if directory exists, return True, or False.
    """
    return os.path.isdir(r"{}".format(path))

def make_dirs(path: str):
    """wrapper of os.makedirs().

    Args:
        param1 path: directory path.

    Returns:
        Not returns value.
    """
    os.makedirs(r"{}".format(path))

def rm_filedir(path: str):
    """wrappaer of os.remove()

    Args:
        path: target file to remove
    """
    os.remove(r'{}'.format(path))

def remove_dir(path: str):
    """wrapper of os.rmdir()

    Args:
        param1 path: directory path.

    Returns:
        Not Returns value.
    """
    os.rmdir(r"{}".format(path))

def remove_dirs(path: str):
    """wrapper of os.removedirs()

    Args:
        param1 path: directory path.

    Returns:
        Not Returns value.
    """
    os.removedirs(r"{}".format(path))

def f_remove_dirs(path: str, ignore_errors=False):
    """wrapper of shutil.rmtree()

    Args:
        param1 path: directory path.

    Returns:
        Not Returns value.
    """
    shutil.rmtree(r"{}".format(path), ignore_errors=ignore_errors)

def compress_gz(path: str):
    """existed file compress to gzip and remove one.

    Args:
        param1 path: target file to compress.
    """
    with open(r'{}'.format(path), 'rb') as f_read:
        with gzip.open(r'{}.gz'.format(path), 'wb') as f_out:
            shutil.copyfileobj(f_read, f_out)

def create_tararchive(path: str, mode=None):
    """create a tar archive from an existed file/dir.

    Args:
        param1 path: the target file/dir
        param2 mode: compression mode. default is gz.
            other mode ... bz2 xz

    Raises:
        TarError
    """
    if mode is None:
        mode = 'gz'
    prefix_mode = "w:"
    mode = prefix_mode + mode

    archive_name = path + '.tar.gz'
    try:
        archive = tarfile.open(r"{}".format(archive_name), mode=mode)
        archive.add(archive_name)
    except tarfile.TarError:
        raise
    else:
        archive.close()

def zip_data(file_path: str, archive_name=None):
    """
    ファイル及びフォルダごとZIP化関数
    :param file_path: the target file to archive.
    :param archive_name: archive name saved(not path)
    :param save_dir: the directory to save an archive.
    :return:

    Raises:
        FileNotFoundError: raises if file does not exist.
    """
    # head... base directory.
    # tail... file name or directory name.
    head, tail = os.path.split(file_path)
    basedir_idx = len(head)
    if archive_name is None:
        zip_path = file_path + ".zip"
    else:
        zip_path = head + archive_name + ".zip"

    with zipfile.ZipFile(file=zip_path, mode='w') as zipobj:
        if os.path.isfile(file_path):
            fname = os.path.split(file_path)[1]
            zipobj.write(file_path, arcname=fname)
            print(">> archived...   {}".format(fname))
            return
        for dir, sub_dir, file_names in os.walk(file_path):
            dir_name = os.path.split(dir)[1]
            print(">> archived...   {}".format(dir))
            zipobj.write(dir, arcname=dir[basedir_idx:])
            for file_name in file_names:
                print(">> archived...   {}".format(os.path.join(dir, file_name)))
                zipobj.write(os.path.join(dir, file_name),
                             arcname=os.path.join(dir[basedir_idx:], file_name))


class FileOpeException(Exception):
    pass


