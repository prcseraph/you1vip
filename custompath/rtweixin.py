# -*- coding: utf-8 -*-
import tornado.web
import njsanhui
import shconfig
from wechat_sdk import WechatBasic

class RtWeiXin(tornado.web.RequestHandler):
    # _success_h5 = "<body style='background-color:#93FF93'>Y</body>"
    # _failed_h5 = "<body style='background-color:#BEBEBE'>N</body>"
    _fktoken = "you1vip"
    _fksignature = "z69h8Q04AWZDi1mtQtPC1SjwCa6NK0OfIiq1LNBABlf"
    _fkapp_id = "wx453ca7ac04b693b5"

    def __init__(self):
        super(tornado.web.RequestHandler, self).__init__()
        self._wechat = WechatBasic(token=self._fktoken)

    def _sanhuiQiandao(self, content=None):
        result_qd_ = "failed"
        if content:
            if shconfig.gUsersDict.has_key(content):
                njsanhui.appEntry(content)
                result_qd_ = shconfig.gUsersDict[content]["my_name"]
        return result_qd_

    def post(self, *args, **kwargs):
        print "post", args, kwargs
        print self.request.arguments
        xml_content_ = self.request.body
        self._wechat.parse_data(xml_content_)
        wechat_message_ = self._wechat.get_message()
        response_ = "undefined."
        if "text" == wechat_message_.type:
            message_content_ = wechat_message_.content
            response_ = message_content_
        self.write(self._wechat.response_text(response_))

    def get(self, *args, **kwargs):
        print "get", args, kwargs
        print self.request.arguments
        echo_str_ = self.get_argument("echostr", "")
        if echo_str_:
            self.write(echo_str_)
