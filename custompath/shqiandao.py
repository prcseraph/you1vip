# -*- coding: utf-8 -*-

import tornado.web
import njsanhui

class RtShQiandao(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        tag_ = int(self.get_argument("qd_tag", '0'))
        # print self.request.arguments, tag_
        if 1 == tag_:
            njsanhui.appEntry("13813948023", "88888")
            self.write("qd success!")
        else:
            self.write("qd failed!")

    def get(self, *args, **kwargs):
        self.render("shqiandao.html")
