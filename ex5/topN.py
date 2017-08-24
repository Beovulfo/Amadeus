#!/usr/bin/env python
import web
import numpy as np
import json
import pandas as pd

urls = (
    '/(.*)', 'index'
)

class index:
    def GET(self,name):
	if not name:
		name = '10'
        fnew = 'topN.h5';#File to read
        df = pd.read_hdf(fnew,mode='r')
        N = np.int(name)#Convert to integer
	df = df.head(N)
	mydict = df.to_dict()
        web.header('Content-Type','application/json')
        return json.dumps(mydict)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
