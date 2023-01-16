from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# @app.route('/static/<path:path>')
# def send_js(path):
#     return send_from_directory('static', path)

if __name__ == "__main__":
    app.run(debug=True) #Run in a test environment
    #app.run()