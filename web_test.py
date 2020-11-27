from faker import Faker
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World"


@app.route("/song_writing")
def ad_search():
    keyword = request.args.get("keyword")
    return f"{keyword}だよ"


@app.route("/test")
def shout():
    fake = Faker("ja_JP")
    fake_list = []
    for i in range(3):
        full = fake.text().split("。")
        fake_list.append(full[0])

    return render_template('index.html', fake_list=fake_list)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
