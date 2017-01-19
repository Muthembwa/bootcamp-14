import httplib

x = httplib.HTTPConnection("www.python.org")

x.request("GET", "/index.html")

r1 = x.getresponse()

print r1.status, r1.reason

data1 = r1.read()

x.request("GET", "/parrot.spam")

r2 = x.getresponse()

print r2.status, r2.reason

data2 = r2.read()

x.close()
