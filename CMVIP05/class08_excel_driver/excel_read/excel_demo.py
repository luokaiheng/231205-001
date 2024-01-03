import openpyxl

from class07_web_Keys.web_keys.keys import Keys


# 获取单元格的参数信息，进行重新编码，匹配传递。
def demo(value):
    data = {}
    str_temp = value.split(';')
    # 单元格内容变成字典格式就达到目的：key和value
    for temp in str_temp:
        temp = temp.split('=', 1)
        # 在data字典中增加一组键值对。k-v
        # data.update({temp[0]: temp[1]})
        data[temp[0]] = temp[1]
    return data


# //xpath[contains(asdsad,"asd")]


excel = openpyxl.load_workbook('../data/11.xlsx')
sheet = excel['Sheet1']
for values in sheet.values:
    # 如果第一个单元格是int类型，则表示进入了测试用例的正文
    if type(values[0]) is int:
        data = demo(values[2])
        print(data)
        # 实例化关键字驱动
        if values[1] == 'open_browser':
            keys = Keys(**data)
            # Keys(txt='Chrome')
        else:
            getattr(keys, values[1])(**data)
