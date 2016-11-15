# -*- coding: utf-8 -*-

import hashlib
import json

import shconfig
import pyajax

def getMd5Password(usr, pwd):
    source_ = usr + "|" + pwd
    md5_ = hashlib.md5()
    md5_.update(source_)
    return md5_.hexdigest()

def getValidCookie(cookie):
    list_ = []
    cookie_list_ = cookie.split(";")
    for key_value_ in cookie_list_:
        if key_value_.find("SessionId") != -1:
            list_.append(key_value_)
    return ";".join(list_)

def logInSanhui(sh_usr, sh_pwd):
    # http://1565ek6742.iok.la:8088/njsanhui/XD.Login/token.ashx?method=get_token&token=null
    # &deviceid=32014066-AD8E-4518-B83F-87A9E690AEE2
    #
    # {"LoginName": "13813948023", "MobileID": "c5581de51e5956c5c3f30a6f7d38efe3", "OS": "IOS",
    #  "MD5_Password": "6cd1b4683f9ea3ad7c3e3a370494d3b3", "DeviceID": "32014066-AD8E-4518-B83F-87A9E690AEE2"}
    #
    # {"LoginName": "13813948023", "MobileID": "c5581de51e5956c5c3f30a6f7d38efe3", "OS": "IOS",
    #  "MD5_Password": "6cd1b4683f9ea3ad7c3e3a370494d3b3", "DeviceID": "32014066-AD8E-4518-B83F-87A9E690AEE2"}
    #
    if sh_pwd:
        md5_password_ = getMd5Password(sh_usr, sh_pwd)
    else:
        md5_password_ = shconfig.gUsersDict[sh_usr]["md5_pwd"]
    url_ = shconfig.getInterfaceUrlSSL(sh_usr, "XD.Login/token.ashx", "get_token")
    params_ = {
        # "method": "get_token",
        # "token": "null",
        "LoginName": sh_usr,
        "MobileID": shconfig.gUsersDict[sh_usr]["mobile_id"],
        "OS": shconfig.gUsersDict[sh_usr]["device_os"],
        "MD5_Password": md5_password_,
        "DeviceID": shconfig.gUsersDict[sh_usr]["device_id"],
    }
    # return pyajax.requestAjax(url_, params_)
    return pyajax.requestAjaxUrl(url_, params_)

def updateApplication(usr):
    url_ = shconfig.gServerUrl + "AppService/App_Data.ashx"
    params_ = {
        "method": "updateApp",
        "token": shconfig.gUsersDict[usr]["response"]["token"],
        "device_id": shconfig.gUsersDict[usr]["device_id"],
        "currentVersion": shconfig.gVersion
    }
    return pyajax.requestAjax(url_, params_)
    # return pyajax.requestAjaxUrl(url_, params_)

def getMyInfo(usr):
    url_ = shconfig.gServerUrl + "AppService/App_Data.ashx"
    params_ = {
        "method": "getMyInfo",
        "token": shconfig.gUsersDict[usr]["response"]["token"],
        "device_id": shconfig.gUsersDict[usr]["device_id"],
    }
    return pyajax.requestAjax(url_, params_)
    # return pyajax.requestAjaxUrl(url_, params_)

def queryQianDao(usr):
    if not shconfig.gUsersDict[usr]["response"]:
        return None
    url_ = shconfig.gServerUrl + "HR/Attendance/Attendance_Data.ashx"
    params_ = {
        "method": 'SignTime',
        # "method": 'SignInfo',
        "token": shconfig.gUsersDict[usr]["response"]["token"],
        "device_id": shconfig.gUsersDict[usr]["device_id"]
    }
    return pyajax.requestAjax(url_, params_)
    # return pyajax.requestAjaxUrl(url_, params_)

def postQianDao(usr):
    sign_type_ = 2
    if shconfig.gUsersDict[usr]["qiandao"] == 0:
        sign_type_ = 1
    url_ = shconfig.gServerUrl + "HR/Attendance/Attendance_Data.ashx"
    params_ = {
        "method": 'Sign',
        "token": shconfig.gUsersDict[usr]["response"]["token"],
        "device_id": shconfig.gUsersDict[usr]["device_id"],
        "SignType": sign_type_,
        # "Address": u"南京艺术学院-专家楼",
        # "X": "118.758136","Y": "32.068306"
        "Address": u"南京市鼓楼区古林公园",
        "x": 118.760549, "Y": 32.072486
    }
    return pyajax.requestAjax(url_, params_)
    # return pyajax.requestAjaxUrl(url_, params_)

def appEntry(sh_usr, sh_pwd=None):
    response_ = logInSanhui(sh_usr, sh_pwd)
    if not response_:
        return False
    response_json_ = json.loads(response_)
    shconfig.gUsersDict[sh_usr]["response"] = response_json_
    #
    # print updateApplication(sh_usr)
    # response_ = getMyInfo(sh_usr)
    # if not response_:
    #     return False
    # print response_
    #
    response_ = queryQianDao(sh_usr)
    if not response_:
        return False
    response_json_ = json.loads(response_)
    shconfig.gUsersDict[sh_usr]["qiandao"] = int(response_json_["message"])
    #
    response_ = postQianDao(sh_usr)
    print response_
    if response_:
        return True
    else:
        return False

if __name__ == "__main__":
    for usr_ in shconfig.gUsersDict:
        md5_pwd_ = getMd5Password(usr_, shconfig.gUsersDict[usr_]["my_pwd"])
        print usr_, md5_pwd_
        # appEntry("13813948023")
