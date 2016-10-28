#!/usr/bin/env python
#
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import os.path
import tornado.auth
import tornado.escape
import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line

from custompath.rtweixin import RtWeiXin

define("port", default=80, help="run on the given port", type=int)

class TMainHandle(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        print "post", args, kwargs
        print self.request.arguments

    def get(self, *args, **kwargs):
        print "get", args, kwargs
        print self.request.arguments

def main():
    parse_command_line()
    app = tornado.web.Application(
        [
            (r"/", TMainHandle),
            (r"/wx", RtWeiXin),
        ],
        cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        login_url="/",
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        xsrf_cookies=True,
    )
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
