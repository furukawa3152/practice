import random

from faker import Faker
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World"


@app.route("/song_writing")
def songs():
    fake = Faker("ja_JP")
    A_mero_list = []
    for i in range(50):
        full = fake.text().split("。")
        if 18 <= len(full[0]) <= 23:
            A_mero_list.append(full[0])
    keyword = request.args.get("keyword")
    sub_word = fake.word()
    sub_word2 = fake.word()
    sabi = random.choice([f"{keyword}! {keyword}! ({sub_word}~~!)",
                          f"{keyword}なのさ{sub_word},{sub_word2}でも"])
    fake_list = [A_mero_list[1], A_mero_list[2], A_mero_list[3], sabi, sabi]

    return render_template('index.html', fake_list=fake_list)

def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
