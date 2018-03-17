#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from flask import Flask, render_template

import models
import stores

app = Flask(__name__)

post_store = stores.PostStore()
post_store.add(models.Post("Life", "Life is alawys great", 1))
post_store.add(models.Post("Sunshine", "Sunshine is amazing", 2))
post_store.add(models.Post("Engineering", "I love engineering", 3))
post_store.add(models.Post("Astronomy", "Space is awesome", 5))
post_store.add(models.Post("ComputerSci", "Our passion", 20))
post_store.add(models.Post("Medicine", "Medicine is great", 15))


@app.route("/")
@app.route("/index/")
def home():
    return render_template("index.html", posts=post_store.get_all())


if __name__ == "__main__":
    app.run(debug=True)
