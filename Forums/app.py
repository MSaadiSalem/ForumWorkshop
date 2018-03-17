#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from flask import Flask, render_template

import dummy_data

app = Flask(__name__)


@app.route("/")
@app.route("/index/")
def home():
    return render_template("index.html", posts=dummy_data.post_store.get_all())


if __name__ == "__main__":
    app.run(debug=True)
