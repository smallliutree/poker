# -*- coding: utf-8 -*-
# @Time : 2022/8/11 19:05
# @Author : minghe_liu
# @File : server
from sanic import Sanic
from sanic.response import text

SERVER_PORT = 12345
PROCESS_CNT = 4
DEBUG = True

app = Sanic('first_view_of_poker')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=SERVER_PORT, workers=PROCESS_CNT, debug=DEBUG)
