#!/usr/bin/env python3
# encoding: utf-8
'''
@author: Loeb{luokaiheng}
@file: test_yaml.py
@time: 2024/6/8  15:59
@software: PyCharm
@desc:读取yaml文件的内容，open读取任何文件都可以，但是yaml格式，在open之后还需要额外的操作
'''
import yaml

import os


def count_files_in_directory(directory_path):
    file_count = 0
    for entry in os.scandir(directory_path):
        if entry.is_file():
            file_count += 1
    return file_count


# 示例用法
directory_path = './data'
file_count = count_files_in_directory(directory_path)


# print(f"The directory '{directory_path}' contains {file_count} files.")
# print(file_count)

li01 = []
def list_files_in_directory(directory):
    # 获取目录下的所有文件和子目录名
    filenames = os.listdir(directory)

    # 打印文件名
    for filename in filenames:
        li01.append(filename)
        # print(filename)


# 指定要列出文件的目录
# list_files_in_directory(directory_path)


def read_yaml():
    for name in li01:
        file_path = './data/' + name
        file = open(file_path, 'r', encoding='utf_8', )
        # 读取yaml中的内容，和之前学过的文件读取有所不同
        data = yaml.load(stream=file, Loader=yaml.FullLoader)
        print(data)


if __name__ == '__main__':
    read_yaml()
