#coding:utf-8

import web
from handle import Handle

urls = (
    "/wechat", "Handle",
)

if __name__ == "__main__":
    app = web.application(urls,globals())        
    app.run()