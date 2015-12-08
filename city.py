# Create by CodeMeow

# -*- coding:utf-8 -*- 

import urllib2
import sys, os, json
reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == '__main__':
    import pdb
    pdb.set_trace()
    f = open('city.json', 'r')
    o = json.loads(f.read())
    x = []
    for (k, v) in o.items():
        n = {}
        n["provinceName"] = k
        l = []
        for kk in v.keys():
            l.append(kk)
        n["city"] = l
        x.append(n)
    str = json.dumps(x, indent=4).decode('unicode_escape')
    print str
    f2 = open('city2.json', 'w')
    f2.write(str)