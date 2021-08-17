from flask import Flask


app = Flask(__name__)


@app.route('/')
def main():
    """Show homepage or signup page depending on global user variable"""

    return('hello')