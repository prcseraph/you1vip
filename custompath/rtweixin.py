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
    _wechat = WechatBasic(token=_fktoken)

    def _sanhuiQiandao(self, content=None):
        result_qd_ = "failed"
        if content:
            if shconfig.gUsersDict.has_key(content):
                njsanhui.appEntry(content)
                result_qd_ = shconfig.gUsersDict[content]["my_name"]
        return result_qd_

    def post(self, *args, **kwargs):
        print "post: ", args, kwargs
        print "params: ", self.request.arguments
        xml_content_ = self.request.body
        print "xml: ", xml_content_
        self._wechat.parse_data(xml_content_)
        wechat_message_ = self._wechat.get_message()
        message_content_ = "undefined."
        response_ = "undefined."
        if "text" == wechat_message_.type:
            message_content_ = wechat_message_.content
            if shconfig.gUsersDict.has_key(message_content_):
                njsanhui.appEntry(message_content_)
                response_ = shconfig.gUsersDict[message_content_]["my_name"]
        response_ = "Rx:%s, Tx:%s" % (message_content_, response_)
        self.write(self._wechat.response_text(response_))

    def get(self, *args, **kwargs):
        print "get:", args, kwargs
        print "params: ", self.request.arguments
        echo_str_ = self.get_argument("echostr", "")
        if echo_str_:
            self.write(echo_str_)
