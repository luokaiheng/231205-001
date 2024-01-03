'''
    读取yaml文件的内容：open读取任何文件都可以，但是yaml格式，在open之后还需要额外的操作
'''

# 获取文件
import yaml

file = open('./data/data_login.yaml', 'r', encoding='utf-8')
# 读取yaml中的内容
data = yaml.load(stream=file, Loader=yaml.FullLoader)
for i in data:
    print(i)

# 写入yaml
# 定义写入的内容
# dic = {
#     'name': '虚竹'
# }
# dic1 = {
#     'age': '14'
# }
# # 写入操作:为了避免中文编码被解析成其他内容，需要添加一个参数，在文件中追加内容，则读写模式参数为a
# with open('./data/data4.yaml', 'a', encoding='utf-8') as file:
#     yaml.dump(dic, file, allow_unicode=True)
#
# # 读取写入后的yaml文件内容
# file = open('./data/data4.yaml', 'r', encoding='utf-8')
# # 读取yaml中的内容
# data = yaml.load(stream=file, Loader=yaml.FullLoader)
# print(data)
