import func.common
from func.common import *
from func.urls import *

xue_cfg = load_config(True)


def get_userInfo(cookies):
    jar = RequestsCookieJar()
    for cookie in cookies:
        jar.set(cookie['name'], cookie['value'])
    custom_headers = {'Cache-Control': 'no-cache', 'User-Agent': func.common.user_agent}
    userInfo_json = requests.get(user_Info_url, cookies=jar, headers=custom_headers).content.decode("utf8")
    userInfo_uid = json.loads(userInfo_json)["data"]["uid"]
    userInfo_nick = json.loads(userInfo_json)["data"]["nick"]
    # 记录登录信息到本地
    status = get_user_status()
    status["userID_mapping"][userInfo_uid] = userInfo_nick
    save_user_status(status)
    return userInfo_uid, userInfo_nick


def list_user():
    status = get_user_status()
    userlist = status['userID_mapping']
    last_userID = int(status['last_userID'])
    user_count = len(userlist)
    force_muser = 0
    # 检查是否配置有多用户模式
    # 防批量挂机隐藏配置
    try:
        if int(xue_cfg["base"]["multiuser"]) == 1:
            force_muser = 1
    except:
        pass

    if last_userID == 0:
        return 0

    if(user_count > 1 or force_muser == 1):
        print(f"\033[33m检测到有{user_count}个用户记录\033[0m")
        check_select = select_user(force_muser)
        if last_userID != check_select and check_select != 404:
            return 1
        elif check_select == 404:
            return 2
    else:
        return 0


def check_user_cookie(userID=None):
    if userID is None:
        userID = get_last_userID()
    else:
        userID = userID
    if userID == 0:
        print(color.red("[*] 没有找到登录信息"))
        print("=" * 60)
        return []
    userID = get_last_userID()
    userName = get_userName(userID)
    print_list = [color.yellow(str(userID)), color.yellow(userName)]
    print(
        "=" * 60, "\n当前用户ID:{0[0]}，当前用户名称:{0[1]}".format(print_list), end=" ")
    # 检查Cookie是否生效
    cookies = get_user_cookie(userID)
    if len(cookies) == 0:
        print(color.red("[*]Cookie信息失效，需登录"))
        return []
    delta_seconds = get_cookie_expire_second(cookies)
    if delta_seconds <= 0:
        print(color.red("[*]Cookie信息失效，需登录"))
        return []
    else:
        delta_hours = round(delta_seconds / 3600)
        print(color.green("[*]Cookie信息生效中，大约剩余%d小时" % delta_hours))
        return cookies


def get_last_userID():
    status = get_user_status()
    # 默认获取上次登录ID
    userID = status['last_userID']
    return userID


def get_userName(userID):
    status = get_user_status()
    # userID = int(userID)strip()
    userlist = status['userID_mapping']
    userName = userlist[str(userID)]
    return userName


def update_last_user(userID):
    status = get_user_status()
    # 此处双引号为int，单引号为str
    status["last_userID"] = userID
    save_user_status(status)


def get_user_status():
    user_patch = get_appsyspatch() + "/User/user_status.json"
    if(not os.path.exists(user_patch)):
        template_status = '''{\n    "#-说明1":"此文件是保存用户数据及登陆状态的配置文件",''' +\
            '''\n    "#-说明2":"程序会自动读写该文件。",''' +\
            '''\n    "#-说明3":"如不熟悉，请勿自行修改内容。错误修改可能导致程序崩溃",''' +\
            '''\n    "last_userID":0,\n "userID_mapping":{\n }\n}'''
        template_status = json.loads(template_status)
        save_user_status(template_status)
        status = get_user_status()
    else:
        status = get_json_data(user_patch)
    return status


def save_user_status(status):
    save_json_data(get_appsyspatch()+"/User/user_status.json", status)


def select_user(multiuser=0):
    status = get_user_status()
    last_userID = int(status['last_userID'])
    return last_userID
    # userlist = status['userID_mapping']
    # user_count = len(userlist)
    # userIDs = []
    # if(user_count > 1 or multiuser == 1):
    #     print("=" * 60)
    #     print("请选择要进行操作的用户（默认选择上次登录用户）: ")
    #     no = 1
    #     for i in userlist:
    #         print("-" * 30)
    #         print("序号【" + str(no) + "】\033[33m" + str(i) + "〖" + userlist[i] + "〗\033[0m")
    #         userIDs.append(i)
    #         no += 1
    #     print("-" * 30)
    #     user_choose = input("请选择用户序号: ")
    #     #隐藏多号模式
    #     if user_choose == "more":
    #         print("\033[31mDEBUG: 进入创建新用户模式\033[0m")
    #         return 404
    #     elif user_choose.isdigit() == False:
    #         print("自动选择上次登录用户")
    #         print("=" * 60)
    #         return last_userID
    #     elif(int(user_choose) <= 0 or int(user_choose) > user_count):
    #         print("输入的范围不对，自动选择上次登录用户")
    #         print("=" * 60)
    #         return last_userID
    #     else:
    #         userID = userIDs[int(user_choose) - 1]
    #         update_last_user(userID)
    #         print("已选择用户: \033[33m" + str(userID) + "〖" + userlist[str(userID)] + "〗\033[0m")
    #         return userID


def save_user_cookies(cookies, userID):
    if xue_cfg["base"]["SetUser"] == "1":
        cookies_json_obj = get_json_data(
            get_appsyspatch()+"/User/cookies.json")
        cookies_bytes = pickle.dumps(cookies)
        cookies_b64 = base64.b64encode(cookies_bytes)
        cookies_json_obj[str(userID)] = str(cookies_b64, encoding='utf-8')
        save_json_data(get_appsyspatch() +
                       "/User/cookies.json", cookies_json_obj)


def get_user_cookie(userID):
    userID = str(userID)
    cookies_json_obj = get_json_data(get_appsyspatch()+"/User/cookies.json")
    for i in cookies_json_obj:
        if(i == userID):
            cookies_b64 = cookies_json_obj[i]
            cookies_bytes = base64.b64decode(cookies_b64)
            cookie_list = pickle.loads(cookies_bytes)
            return cookie_list
    return []


def get_cookie_expire_second(cookie):
    for d in cookie:
        if 'name' in d and 'value' in d and 'expiry' in d and d['name'] == 'token':
            expiry_date = int(d['expiry'])
            return expiry_date - (int)(time.time())
    return 0
