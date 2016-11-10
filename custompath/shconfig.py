# -*- coding: utf-8 -*-

gVersion = "2.0.1"
# gHostUrl = "http://1565ek6742.iok.la:8088/njsanhui/AttachFiles/employeePhoto/"
# gServerUrl = "http://1565ek6742.iok.la:8088/njsanhui/"
# gServerUrlSSL = "http://1565ek6742.iok.la:8088/njsanhui/"
# gAttachUrl = "http://1565ek6742.iok.la:8088/njsanhui/"
gHostUrl = ' http://pic.haopan.net/employeePhoto/'
gServerUrl = 'http://cloud.haopan.net/cloud/'
gServerUrlSSL = 'http://cloud.haopan.net/cloud/'
gAttachUrl = 'http://cloud.haopan.net/cloud/'

gUsersDict = {
    "13952010386": {
        "rx_time": None,
        "my_name": "lq",
        "device_os": "IOS",
        "md5_pwd": "7ef5a27a887292981e8b7806405e5c9f",
        "mobile_id": "c5581de51e5956c5c3f30a6f7d38efe3",
        "device_id": "32014066-AD8E-4518-B83F-87A9E690AEE2",
        "qiandao": 0,
        "response": {}
    },
    "13813948023": {
        "rx_time": None,
        "my_name": "jy",
        "device_os": "IOS",
        "md5_pwd": "6cd1b4683f9ea3ad7c3e3a370494d3b3",
        "mobile_id": "6e110225688f68ee4708566ed971a27d",
        "device_id": "78265209-05AA-443F-A20B-502C902E63FF",
        "qiandao": 0,
        "response": {}
    },
    "13912996234": {
        "rx_time": None,
        "my_name": "wzq",
        "device_os": "IOS",
        "md5_pwd": "d8e6d32cdd8ee6af55e432dea3bcc161",
        "mobile_id": "80cc4428e019be8d45bab8e19bc5811f",
        "device_id": "9177AEDE-D67C-49E0-94BB-DE21B9AF90C7",
        "qiandao": 0,
        "response": {}
    },
    "13951801524": {
        "rx_time": None,
        "my_name": "llx",
        "device_os": "IOS",
        "md5_pwd": "e19a4ed4a9a0ff620f4eaff6d384f6c1",
        "mobile_id": "c5581de51e5956c5c3f30a6f7d38efe3",
        "device_id": "32014066-AD8E-4518-B83F-87A9E690AEE2",
        "qiandao": 0,
        "response": {}
    }
}

def getInterfaceUrlSSL(usr, interface_name, method_name, token="null"):
    url_ = gServerUrlSSL + interface_name + '?method=' + method_name + '&token=' + token \
           + '&deviceid=' + gUsersDict[usr]["device_id"]
    return url_
