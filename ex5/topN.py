#!/usr/bin/env python
import web
import json
import pandas as pd

urls = (
    '/(.*)', 'index'
)

class index:
    def GET(self,name):
        fnew = 'topN.h5';#File to read
        df = pd.read_hdf(fnew,mode='r')
        output = df.head(name)
        web.header('Content-Type','application/json')
        return json.dumps(output)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
