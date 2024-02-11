from flask import Flask,render_template
from threading import Thread

app = Flask(___name___)

@app.route('/')
def index():
  return "alive"

def run ():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
  t = thread(target=gun)
  t.start()
