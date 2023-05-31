from threading import Thread
from flask import Flask, render_template

app = Flask("")


@app.route("/")
def index():
    return render_template("index.html")


def run():
    app.run(host="0.0.0.0", port=5000)


def start():
    t = Thread(target=run)
    t.start()


start()

def keep_alive():
    start()

   #Credit to Larss_J#8982
