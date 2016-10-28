# -*- coding: utf-8 -*-

gHostUrl = "http://1565ek6742.iok.la:8088/njsanhui/AttachFiles/employeePhoto/"
gServerUrl = "http://1565ek6742.iok.la:8088/njsanhui/"
gServerUrlSSL = "http://1565ek6742.iok.la:8088/njsanhui/"
gAttachUrl = "http://1565ek6742.iok.la:8088/njsanhui/"
gVersion = "1.9.4"
# "LoginName": "13813948023",
# "MobileID": "6e110225688f68ee4708566ed971a27d",
# "OS": "IOS",
# "MD5_Password": "6cd1b4683f9ea3ad7c3e3a370494d3b3",
# "DeviceID": "78265209-05AA-443F-A20B-502C902E63FF"
# method=get_token&token=null&deviceid=78265209-05AA-443F-A20B-502C902E63FF
gUsersDict = {
    "13813948023": {
        "my_name": "jy",
        "device_os": "IOS",
        "device_id": "78265209-05AA-443F-A20B-502C902E63FF",
        "mobile_id": "6e110225688f68ee4708566ed971a27d",
        "qiandao": 0,
        "response": {}
    },
    "13912996234": {
        "my_name": "wzq",
        "device_os": "IOS",
        "device_id": "32014066-AD8E-4518-B83F-87A9E690AEE2",
        "mobile_id": "c5581de51e5956c5c3f30a6f7d38efe3",
        "qiandao": 0,
        "response": {}
    },
    "13951801524": {
        "my_name": "llx",
        "device_os": "IOS",
        "device_id": "32014066-AD8E-4518-B83F-87A9E690AEE2",
        "mobile_id": "c5581de51e5956c5c3f30a6f7d38efe3",
        "qiandao": 0,
        "response": {}
    }
}

def getInterfaceUrlSSL(usr, interface_name, method_name, token="null"):
    url_ = gServerUrlSSL + interface_name + '?method=' + method_name + '&token=' + token \
           + '&deviceid=' + gUsersDict[usr]["device_id"]
    return url_
