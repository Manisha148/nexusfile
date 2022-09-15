from flask import Flask, render_template
import os

app = Flask(__name__)

# app.config["Debug"] = True

@app.route('/')
def mydef():
    return render_template("index.html")
  
PORT = int(os.environ.get("PORT", 8000))
if _name_ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=PORT)
