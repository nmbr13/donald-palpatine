from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

import Trump_Tweets as tt

quote = tt.trump_tweets()

@app.route("/")
def hello():
    return render_template(
        'index.html',quote=quote)

if __name__ == "__main__":
    app.run()
