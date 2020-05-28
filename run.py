import os

import pytest

from common.filepath import REPORTDIR

if __name__ == '__main__':
    pytest.main(['-s', '-q', "--alluredir=allure_report"])

