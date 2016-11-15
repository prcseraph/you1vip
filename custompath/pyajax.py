# -*- coding: utf-8 -*-

import json
import requests
# import urllib
import urllib2
import re

# import cookielib
# gcj = cookielib.CookieJar()
# goper_cookie = urllib2.build_opener(urllib2.HTTPCookieProcessor(gcj))
# urllib2.install_opener(goper_cookie)

global g_cookies
g_cookies = {}

def requestAjax(url, body):
    global g_cookies
    response_ = requests.post(url, data=body, cookies=g_cookies)
    return response_.text

def requestAjaxUrl(url, body, cookie=None, referer=None, **headers):
    global g_cookies
    post_data_ = json.dumps(body)
    req_ = urllib2.Request(url, data=post_data_)
    req_.add_header("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8")
    # req_.add_header("Connection", "keep-alive")
    req_.add_header("Accept", "application/json")
    req_.add_header("User-Agent",
                    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_1_1 like Mac OS X) "
                    "AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 Html5Plus/1.0")
    # req_.add_header("Accept-Encoding", "gzip, deflate")
    req_.add_header("X-Requested-With", "XMLHttpRequest")
    if cookie:
        req_.add_header('Cookie', cookie)
    elif g_cookies:
        req_.add_header("Cookie", g_cookies)
    if referer:
        req_.add_header('Referer', referer)
    if headers:
        for k in headers.keys():
            req_.add_header(k, headers[k])
    req_.get_method = lambda: "POST"
    response_ = urllib2.urlopen(req_)
    if response_:
        g_cookies = parseSetCookies(response_.headers["set-cookie"])
        return response_.read()
    else:
        return None

def parseSetCookies(set_cookies):
    regex_ = re.compile("(HP\d{4}Frame)")
    result_cookies_ = {}
    for line_ in set_cookies.split(';'):
        print line_
        try:
            name_, value_ = line_.strip().split('=', 1)
            find_key_ = regex_.findall(name_)
            if find_key_:
                result_cookies_[find_key_[0]] = value_
            else:
                result_cookies_[name_] = value_
        except:
            pass
    return result_cookies_

if __name__ == "__main__":
    pass
