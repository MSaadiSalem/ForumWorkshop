#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from flask import render_template

from forums import app, db_con


@app.route("/")
@app.route("/index/")
def home():
    return render_template("index.html",
                           posts=db_con.post_store.get_all(),
                           members=db_con.member_store)
