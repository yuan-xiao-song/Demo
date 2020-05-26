import os

import pytest

from common.filepath import REPORTDIR

if __name__ == '__main__':
    allure_report_path = REPORTDIR + '/allure_report'
    html_report_path = REPORTDIR + '/html'
    pytest.main(['-s', '-q', "--alluredir={}".format(allure_report_path)])
    os.system('allure generate {} -o {} --clean'.format(allure_report_path, html_report_path))
