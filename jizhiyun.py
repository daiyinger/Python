import http.client    #�޸����õ�ģ��
import urllib

params = urllib.parse.urlencode({"email":"1002639334@qq.com","password":"199105jacdu"})  
headers = {"X-Gizwits-Application-Id": "{x6XqefTKTU2nPayScLXEfn}","Content-Type": "application/json","Accept": "text/html","Connection": "close"}  

reqconn=http.client.HTTPConnection("api.gizwits.com:80")  #�޸Ķ�Ӧ�ķ���
reqconn.request("POST", "/app/login", params, headers)
res=reqconn.getresponse()
print (res.status,  res.reason)
print (res.msg)
print (res.read().decode())

