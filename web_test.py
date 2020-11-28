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
    sabi = random.choice([f"{keyword}! {keyword}! ({sub_word}~~!)({sub_word}~~!)",
                          f"絶対{keyword}なのさ！！{sub_word}が{sub_word2}でも~!"])

    chord = {1: "C", 2: "C#", 3: "D", 4: "D#", 5: "E", 6: "F", 7: "F#", 8: "G", 9: "G#", 10: "A", 11: "A#", 12: "B"}

    fake_list = [A_mero_list[1], A_mero_list[2], A_mero_list[3], sabi, sabi, A_mero_list[4], A_mero_list[5],
                 A_mero_list[6], sabi, sabi, A_mero_list[2], A_mero_list[3], sabi, sabi, sabi]

    return render_template('index.html', fake_list=fake_list, keyword=keyword)

def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
