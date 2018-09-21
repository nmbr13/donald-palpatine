from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

@app.route("/<string:name>/")
def hello(name):
    return render_template(
        'index.html',name=name)

if __name__ == "__main__":
    app.run()
