import time
import requests
import json


class PlusPushHandler:
    def __init__(self, token):
        self.token = token

    def ppmsgsend(self, msg, mode="QR", QRID=0):
        headers = {"Content-Type": "application/json"}  # 定义数据类型
        if mode == "QR":
            data = {
                "token": self.token,
                "title": "学习强国",
                "template": "markdown",
                "content": "#### 学习强国登录学习\n > ![](" + msg + ")\n > ###### 二维码生成时间" +
                time.strftime(
                    "%Y-%m-%d %H:%M:%S", time.localtime()) + "\n > ###### 二维码ID:" + str(QRID)
            }
        elif mode == "link":
            data = {
                "token": self.token,
                "title": "学习强国登录",
                "template": "markdown",
                "content": "因PlusPush无法直接在本消息中打开学习强国App。\n请点击右下角按钮复制Web地址到浏览器中打开（注意去掉地址前的两个斜杠），然后点击以下链接打开学习强国：\n [点击此处打开强国App进行登录](%s)" % msg
            }
        else:
            data = {
                "token": self.token,
                "title": "学习强国",
                "template": "markdown",
                "content": msg
            }
        try:
            res = requests.post(
                "http://www.pushplus.plus/send", data=json.dumps(data), headers=headers)
            print("已通过PlusPush发送成功")
        except Exception as e:
            print("发送失败. 错误信息: " + str(e))
