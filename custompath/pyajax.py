# -*- coding: utf-8 -*-

import json
import requests
import urllib
import urllib2
import cookielib

gcj = cookielib.CookieJar()
goper_cookie = urllib2.build_opener(urllib2.HTTPCookieProcessor(gcj))
urllib2.install_opener(goper_cookie)

def requestAjax(url, body):
    response_ = requests.post(url, data=body)
    return response_.text

def requestAjaxUrl(url, body, cookie=None, referer=None, **headers):
    # post_data_ = urllib.urlencode(body).encode()
    post_data_ = json.dumps(body)
    req_ = urllib2.Request(url, data=post_data_)
    req_.add_header("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8")
    req_.add_header("Accept", "application/json")
    req_.add_header("X-Requested-With", "XMLHttpRequest")
    req_.add_header("User-Agent",
                    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_1 like Mac OS X) "
                    "AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A403 Html5Plus/1.0")
    # req_.add_header("Connection", "keep-alive")
    if cookie:
        req_.add_header('Cookie', cookie)
    if referer:
        req_.add_header('Referer', referer)
    if headers:
        for k in headers.keys():
            req_.add_header(k, headers[k])
    response_ = urllib2.urlopen(req_)
    if response_:
        return response_.read()
    else:
        return None

if __name__ == "__main__":
    pass
