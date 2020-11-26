from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World"


@app.route("/ad_search")
def ad_search():
    zipcode = request.args.get("zipcode")
    return f"{zipcode}だよ"


@app.route("/shout/<string:name>")
def shout(name: str):
    return f"{name}だよ"


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
