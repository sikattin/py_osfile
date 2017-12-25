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

def get_file_names(self, dir_path: str):
    """指定したディレクトリ直下のファイル名一覧を取得する関数.

    Args:
        param1 dir_path: ファイル名一覧を取得するディレクトリパス.

    Returns:
        ファイル名の一覧を格納したリスト.
    """
    file_names = list()
    for file in os.listdir(dir_path):
        if os.path.isfile(dir_path + file):
            file_names.append(file)

    return file_names

def get_dir_names(self, dir_path: str):
    """指定したディレクトリ直下のディレクトリ名一覧を取得する関数.

    Args:
        param1 dir_path: ディレクトリ名一覧を取得するディレクトリパス。

    Returns:
        ディレクトリ名の一覧を格納したリスト.
    """
    dir_names = list()
    for dir in os.listdir(dir_path):
        if os.path.isdir(dir_path + dir):
            dir_names.append(dir)

    return dir_names

def dir_exists(self, path: str):
    """wrapper of os.path.isdir().

    Args:
        param1 path: directory path.

    Returns:
        if directory exists, return True, or False.
    """
    return os.path.isdir(path)

def make_dirs(self, path: str):
    """wrapper of os.makedirs().

    Args:
        param1 path: directory path.

    Returns:
        Not returns value.
    """
    os.makedirs(path)

def remove_dir(self, path: str):
    """wrapper of os.rmdir()

    Args:
        param1 path: directory path.

    Returns:
        Not Returns value.
    """
    os.rmdir(path)

def remove_dirs(self, path: str):
    """wrapper of os.removedirs()

    Args:
        param1 path: directory path.

    Returns:
        Not Returns value.
    """
    os.removedirs(path)

def f_remove_dirs(self, path: str, ignore_errors=False):
    """wrapper of shutil.rmtree()

    Args:
        param1 path: directory path.

    Returns:
        Not Returns value.
    """
    shutil.rmtree(path, ignore_errors=ignore_errors)
