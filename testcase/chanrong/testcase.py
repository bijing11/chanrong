import unittest,ddt,requests


@ddt.ddt
class Testcase(unittest.TestCase):
    @ddt.data(*"testdata里面的方法名")
    @ddt.unpack
    def testcase(self, url, method, headers, body, expected, message):
        response = requests.request(method, url, headers = headers, data = body)
        actual = "实际响应结果"
        expected = expected
        self.assertEqual(actual, expected, message)