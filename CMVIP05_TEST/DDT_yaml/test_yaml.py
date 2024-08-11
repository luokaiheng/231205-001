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

dict001 = {
    "name": "罗凯恒",
    "job": "软件测试"
}


class Read_Yaml():
    '''
        指定文件夹中的数据文件，限定文件格式为txt、yaml
    '''
    # 类属性，相当于全局变量
    directory_path = './data'
    li01 = []

    def count_files_in_directory(self):
        file_count = 0
        for entry in os.scandir(Read_Yaml.directory_path):
            if entry.is_file():
                file_count += 1
        print('这个文件目录下，有' + str(file_count) + '个文件' + '\n')
        return file_count

    def list_files_in_directory(self):
        # 获取目录下的所有文件和子目录名
        filenames = os.listdir(Read_Yaml.directory_path)

        # 打印文件名
        for filename in filenames:
            Read_Yaml.li01.append(filename)

    def read_yaml(self):
        for name in Read_Yaml.li01:
            file_path = './data/' + name
            file = open(file_path, 'r', encoding='utf_8', )
            # 读取yaml中的内容，和之前学过的文件读取有所不同
            data = yaml.load(stream=file, Loader=yaml.FullLoader)
            print('\n' + name + '文件下存储的数据：')
            print(data)
        print('读取数据结束！')


class Write_Yaml():
    '''
        写入yaml文件
    '''

    def __init__(self, dict_):
        self.dict_ = dict_

    def write_yaml(self):
        # w 是覆盖， a 是追加，r 是读取
        with open('./data/data05.yaml', 'w', encoding='utf-8') as file:
            yaml.dump(self.dict_, file, allow_unicode=True)
        # 写入后读取写入的数据
        file = open('./data/data05.yaml', 'r', encoding='utf-8')
        data = yaml.load(stream=file, Loader=yaml.FullLoader)
        print('\n' + str(data))


if __name__ == '__main__':
    # 实例化一个对象，然后读取yaml文件数量、文件名和被解析后的文件内容
    myRead_Yaml = Read_Yaml()
    myRead_Yaml.count_files_in_directory()
    myRead_Yaml.list_files_in_directory()
    print('遍历后的目录文件：', end='')
    print(Read_Yaml.li01)
    myRead_Yaml.read_yaml()

    # 创建一个实例
    myclass = Write_Yaml(dict001)
    # 调用实例方法
    myclass.write_yaml()
