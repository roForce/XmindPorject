# -*- coding: utf-8 -*-            
# @Author : Code_nickusual
# @Time : 2023/10/25 21:37
import xmindparser

class dataOp:
    #初始化数据操作，需要保存读取的xmind文件
    def __init__(self):
        self.data = self.getXmind()
    def getXmind(self):
        # xmindparser配置
        xmindparser.config = {
            'showTopicId': True,  # 是否展示主题ID
            'hideEmptyValue': True  # 是否隐藏空值
        }
        filePath = './data/国产化.xmind'
        # 解析成dict数据类型
        #content = xmindparser.xmind_to_dict(filePath)
        # 解析成json数据类型
        content = xmindparser.xmind_to_json(filePath)
        print(content)

if __name__ == "__main__":
    data = dataOp()



