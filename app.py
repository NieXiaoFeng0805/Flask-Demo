# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : app.py
# Time       ：2024/9/23 15:42
# Author     ：author name
# version    ：python 3.7
# Description：
"""
from flask import Flask, render_template

app = Flask(__name__)  # 使用Flask类创建一个App对象，__name__表示当前app.py这个模块
app.config['SECRET_KEY'] = '1245272985@qq.com'


# 创建路由和视图函数进行映射
@app.route("/")
def root():
    """ 主页 :return: Index.html """
    return render_template('Index.html')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5000')
