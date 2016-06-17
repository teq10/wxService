# -*- coding: utf-8 -*-

from base import *
import requests
import json

class WxOauthHandler(BaseHandler):

    """
    微信授权类

    """

    def get_authorize(self):
        """
        微信授权
        :return:
        """
        redirect_uri = "http://wx.teq6.com/oauth?m=callback"
        self.api_authorize = Const.WXAPI_AUTHORIZE.format(APPID=Const.WXAPP,
                                                          REDIRECT_URI=redirect_uri,
                                                          SCOPE="snsapi_userinfo",
                                                          STATE=0)

        self.redirect(self.api_authorize)


    def _get_access_token(self, code=""):
        """
        获取微信授权的access_token
        :param code: code
        :return:
        """
        token = {}
        if code:
            token = json.loads(requests.get(Const.WXAPI_WXUSER_ACCESS_TOKEN.format(APPID=Const.WXAPP, SECRET=Const.WXAPP_SECRET, CODE=code)).content)
        else:
            print "code is None"
        return token

    def _get_userinfo(self, access_token="", openid=""):
        """
        获取微信用户信息

        :param access_token: 处理token
        :param openid: 微信用户的openid
        :return:
        """
        wxuser = json.loads(requests.get(Const.WXAPI_USERINFO.format(ACCESS_TOKEN=access_token, OPENID=openid)).content)
        return wxuser


    def get_callback(self):
        """
        微信授权回调地址

        :return:
        """
        code = self.get_argument("code")
        if not code:
            self.render("error.html", message="get code failed!")
            return

        token = self._get_access_token(code)
        print token

        if not token:
            self.render("error.html", message="get access_token failed!")
            return

        wxuser = self._get_userinfo(token.get("access_token"), token.get("openid"))
        print wxuser

        if not wxuser:
            self.render("error.html", message="get wxuser failed!")
            return

        self.write(str(wxuser))




