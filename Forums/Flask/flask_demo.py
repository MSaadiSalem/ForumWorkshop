#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/index/")
def home():
    return "Hi there!!"


@app.route("/SayHello/<user_name>")
def SayHello(user_name):
    return "Hi {0}".format(user_name)


if __name__ == "__main__":
    app.run(debug=True)
