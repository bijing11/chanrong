import unittest
from BeautifulReport import BeautifulReport


r = unittest.defaultTestLoader.discover("./testcase/chanrong", pattern='test*.py')
runner = BeautifulReport(r)
runner.report(description="描述",filename="./report/chanrong/文件名")