#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from flask import Flask, render_template

import dummy_data
import stores

app = Flask(__name__)

member_store = stores.MemberStore()
post_store = stores.PostStore()
dummy_data.seed_stores(member_store, post_store)


@app.route("/")
@app.route("/index/")
def home():
    return render_template("index.html", posts=post_store.get_all(), members=member_store)


if __name__ == "__main__":
    app.run(debug=True)
