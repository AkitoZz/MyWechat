# -*- coding: utf-8 -*-

import hashlib
import web
import reply
import receive

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
            list(map(sha1.update,list(map(lambda x : x.encode("utf-8"),data_list))))
            hashcode = sha1.hexdigest()
            print("[debug] handle/GET hashcode,signature:",hashcode,signature)
            if hashcode == signature:
                return echostr
            else:
                return ""

        except Exception as Argument:
            return Argument        

    def POST(self):
        try:
            webData = web.data()
            print("[debug] post data",webData)

            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg,receive.Msg) and recMsg.MsgType == 'text':
                #需要check
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = "test"
                replyMsg = reply.TextMsg(toUser,fromUser,content)
                return replyMsg.send()
            else:
                print("暂不处理")
                return "success"
        except Exception as Argument:
            return Argument       
