#coding:utf-8

import hashlib
import web

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            print("[debug] get.data:",data)
            if len(data) == 0:
                return "hello,this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            #公众号设置    
            token = "mytoken"

            data_list = [token,timestamp,nonce]
            data_list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update,data_list)
            hashcode = sha1.hexdigest()
            print("[debug] handle/GET hashcode,signature:",hashcode,signature)
            if hashcode == signature:
                return echostr
            else:
                return ""

        except Exception as Argument:
            return Argument        