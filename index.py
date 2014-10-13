import web
from web.contrib.template import render_jinja
import json

import ip_find

urls = ("/ip", "IPFind",
        "/api/ip/(.*)", "IPFindAPI")

app = web.application(urls, globals())
render = render_jinja("templates", encoding='utf-8')
ipInfo = ip_find.IPInfo("data/qqwry.dat")

def find_loc_by_ip(ip):
    try:
        i = ipInfo
        (c, a) = i.getIPAddr(ip);
        c = unicode(c, 'utf-8')
        a = unicode(a, 'utf-8')
    except:
        raise
    return (c, a)

class IPFind:
    def GET(self):
        return render.ip()

class IPFindAPI:
    def GET(self, ip):
        try:
            c, a = find_loc_by_ip(ip)
        except:
            return web.InternalError()
        json_s = {"ip": ip,
                "loc": c,
                "belong": a}
        return json.dumps(json_s)

if __name__ == "__main__":
    app.run()
