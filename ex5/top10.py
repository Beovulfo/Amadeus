#!/usr/bin/env python
import web
import json

urls = (
    '/(.*)', 'index'
)

class index:
    def GET(self,name):
        # How to obtain the name key and then print the value?
        pyDict  = {'one':1,'two':2}
        web.header('Content-Type','application/json')
        return json.dumps(pyDict)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
