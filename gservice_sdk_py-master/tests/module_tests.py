#coding:utf-8


import unittest
from gservice.calls import g_users, g_device, g_login, g_codes, g_common


class TestRequest(unittest.TestCase):
    '''
    just test request object.
    '''
    def setUp(self):
        pass

    def _http_GET(self, test):
        self.assertEquals(test, "GET")

    def _http_POST(self, test):
        self.assertEquals(test, "POST")

    def _http_DELETE(self, test):
        self.assertEquals(test, "DELETE")

    def _http_PUT(self, test):
        self.assertEquals(test, "PUT")

    def test_object(self):
        login_url = 'http://api.gizwits.com/app/login'
        req = g_login.login('1002639334@qq.com','199105jacdu')
        self._http_POST(req.method)
        self.assertEquals(req.url, login_url)

        device_data_did = 'd47a3035c6a34c99bb375ee2cfaf8d5b'
        req = g_device.retrieve_device_histroy_data(device_data_did)
        self._http_GET(req.method)
        self.assertEquals(req.url, 'http://api.gizwits.com/app/devdata/' + device_data_did)
        print("hello")

        control_did = '11b12fd2c5b14d3fb2607e6b4e9ecf62'
        control_url = 'http://api.gizwits.com/app/control/' + control_did
        req = g_device.remote_control_device(control_did, ["{value:12}"])
        self._http_POST(req.method)
        self.assertEquals(req.url, control_url)
        
if __name__ == '__main__':
    unittest.main()
