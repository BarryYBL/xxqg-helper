import os
import sys
import random
import time
import json
import base64
import pickle
import requests
import re
from requests.cookies import RequestsCookieJar
from configparser import ConfigParser
from func import color
from func.dingding import DingDingHandler
from func.pluspush import PlusPushHandler
import platform

user_agent = ""

def get_appsyspatch():
    application_path = './'
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.split(os.path.abspath(sys.argv[0]))[0]
    return application_path


def load_config(nologo=False):
    if nologo == False:
        print("=" * 60 + "\n" + load_logo())
    else:
        pass
    xue_cfg = ConfigParser()
    sys_patch = get_appsyspatch()
    if (not os.path.exists(sys_patch + "/Config")):
        os.mkdir(sys_patch + "/Config")
    if (not os.path.exists(sys_patch + "/User")):
        os.mkdir(sys_patch + "/User")
    if (not os.path.exists(sys_patch + "/Config/Config.cfg")):
        print("=" * 60)
        print("@启动失败，缺少配置文件: Config/Config.cfg")
        os._exit(0)
    else:
        xue_cfg.read(sys_patch + "/Config/Config.cfg", encoding='utf-8')
        # 读取环境变量
        if os.environ.get("ModeType") is not None:
            xue_cfg.set("base", "ModeType", os.environ.get("ModeType"))
        if os.environ.get("maxtrylogin") is not None:
            xue_cfg.set("base", "maxtrylogin", os.environ.get("maxtrylogin"))
        if os.environ.get("tryloginsleep") is not None:
            xue_cfg.set("base", "tryloginsleep",
                        os.environ.get("tryloginsleep"))
        if os.environ.get("SetUser") is not None:
            xue_cfg.set("base", "SetUser", os.environ.get("SetUser"))
        if os.environ.get("AutoQuit") is not None:
            xue_cfg.set("base", "AutoQuit", os.environ.get("AutoQuit"))
        if not xue_cfg.has_option("base", "AutoQuit"):
            xue_cfg.set("base", "AutoQuit", "0")
        if os.environ.get("PushMode") is not None:
            xue_cfg.set("push", "PushMode", os.environ.get("PushMode"))
        if os.environ.get("DDtoken") is not None:
            xue_cfg.set("push", "DDtoken", os.environ.get("DDtoken"))
        if os.environ.get("DDsecret") is not None:
            xue_cfg.set("push", "DDsecret", os.environ.get("DDsecret"))
        if os.environ.get("PPtoken") is not None:
            xue_cfg.set("push", "PPtoken", os.environ.get("PPtoken"))
    return xue_cfg


def save_json_data(filename, filedata):
    with open(filename, 'w', encoding='utf-8') as j:
        json.dump(filedata, j, indent=4, ensure_ascii=False)


def get_json_data(filename):
    template_json_str = '''{}'''
    if (os.path.exists(filename) and os.path.getsize(filename) != 0):
        with open(filename, 'r', encoding='utf-8') as j:
            try:
                json_data = json.load(j)
            except Exception as e:
                print(filename, "解析错误：", str(e))
                print("请检查", filename, "信息")
                exit()
    else:
        json_data = json.loads(template_json_str)
    return json_data


def check_delay(mintime=2, maxtime=5):
    delay_time = random.randint(mintime, maxtime)
    print('等待 ', delay_time, ' 秒')
    time.sleep(delay_time)


def log_data(datapatch, logdata):
    datapatch = get_appsyspatch() + datapatch
    with open(datapatch, "a", encoding='utf-8') as f:
        for i in logdata:
            f.write(str(i) + "\n")


def get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def sendMessage(msg):
    xue_cfg = load_config(True)
    if xue_cfg["push"]["PushMode"] == "2":
        token = xue_cfg["push"]["DDtoken"]
        secret = xue_cfg["push"]["DDsecret"]
        if token is not None and secret is not None:
            ddhandler = DingDingHandler(token, secret)
            ddhandler.ddmsgsend(msg, "msg")
        else:
            print("钉钉token未设置，取消发送消息")
    elif xue_cfg["push"]["PushMode"] == "3":
        token = xue_cfg["push"]["PPtoken"]
        if token is not None:
            ddhandler = PlusPushHandler(token)
            ddhandler.ppmsgsend(msg, "msg")
        else:
            print("PlusPush token未设置，取消发送消息")


def load_logo():
    xue_logo = ("     ____  ___             ________    ________ " + "\n" +
                r"     \   \/  /__ __   ____ \_____  \  /  _____/ " + "\n" +
                r"      \     /|  |  \_/ __ \ /  / \  \/   \  ___ " + "\n" +
                r"      /     \|  |  /\  ___//   \_/   \    \_\  \ " + "\n" +
                r"     /___/\  \____/  \___  >_____\ \_/\______  /" + "\n" +
                r"           \_/           \/       \__>       \/ ")
    #xue_logo = color.cyan(xue_logo)
    return xue_logo
