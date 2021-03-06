# -*- coding: utf-8 -*-
import tornado.web
import time
import datetime
import requests

from wechat_sdk import WechatBasic
# import njsanhui
import shconfig

class RtWeiXin(tornado.web.RequestHandler):
    # _success_h5 = "<body style='background-color:#93FF93'>Y</body>"
    # _failed_h5 = "<body style='background-color:#BEBEBE'>N</body>"
    _fktoken = "you1vip"
    _fksignature = "z69h8Q04AWZDi1mtQtPC1SjwCa6NK0OfIiq1LNBABlf"
    _fkapp_id = "wx453ca7ac04b693b5"
    _wechat = WechatBasic(token=_fktoken)
    _sanhui_qiandao_url = "http://180.96.28.83:83/shqd?vip="

    def _sanhuiQiandao(self, content=None):
        if content:
            # if shconfig.gUsersDict.has_key(content):
            #     njsanhui.appEntry(content)
            requests.post(self._sanhui_qiandao_url + content)

    def post(self, *args, **kwargs):
        print "post: ", args, kwargs
        print "params: ", self.request.arguments
        xml_content_ = self.request.body
        print "xml: ", xml_content_
        self._wechat.parse_data(xml_content_)
        wechat_message_ = self._wechat.get_message()
        message_content_ = "undefined."
        response_ = "undefined."
        current_time_ = datetime.datetime.now()
        qd_tag_ = False
        if "text" == wechat_message_.type:
            message_content_ = wechat_message_.content
            if shconfig.gUsersDict.has_key(message_content_):
                cache_time_ = shconfig.gUsersDict[message_content_]["rx_time"]
                if not cache_time_:
                    qd_tag_ = True
                else:
                    diff_time_ = abs(current_time_ - cache_time_)
                    if diff_time_.seconds > 5 * 60: qd_tag_ = True
                response_ = shconfig.gUsersDict[message_content_]["my_usr"]
        response_ = "Rx:%s, Tx:%s" % (message_content_, response_)
        self.write(self._wechat.response_text(response_))
        if qd_tag_:
            shconfig.gUsersDict[message_content_]["rx_time"] = current_time_
            self._sanhuiQiandao(message_content_)

    def get(self, *args, **kwargs):
        print "get:", args, kwargs
        print "params: ", self.request.arguments
        echo_str_ = self.get_argument("echostr", "")
        if echo_str_:
            self.write(echo_str_)

if __name__ == "__main__":
    requests.post("http://192.168.0.99:83/shqd?vip=12345678907")
