import random

from faker import Faker
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def top_page():
    return render_template("top_page.html")


@app.route("/song_writing", methods=["GET"])
def songs():
    fake = Faker("ja_JP")  # 歌詞作成
    A_ly = []
    for i in range(50):
        full = fake.text().split("。")
        if 18 <= len(full[0]) <= 23:
            A_ly.append(full[0])

    keyword = request.args.get("keyword", "")
    sub_word = fake.word()
    sub_word2 = fake.word()
    sabi = random.choice([f"{keyword}! {keyword}! ({sub_word}～～!)({sub_word}～～!)",
                          f"絶対{keyword}なのさ！！{sub_word}が{sub_word2}でも～!",
                          f"{keyword}!!!その{sub_word}に{sub_word2}して～",
                          f"{keyword}が{sub_word}だから～！（{sub_word2}も{sub_word}なのさ～！）"])  # サビパターン（追加予定）

    # コード進行作成
    chord = {1: "C", 2: "C#", 3: "D", 4: "D#", 5: "E", 6: "F", 7: "F#", 8: "G", 9: "G#", 10: "A", 11: "A#", 12: "B",
             13: "C", 14: "C#", 15: "D", 16: "D#", 17: "E", 18: "F", 19: "F#", 20: "G", 21: "G#", 22: "A", 23: "A#",
             24: "B"}
    key = random.choice([1, 3, 5, 6, 8, 10, 12])  # トニックに#がつくのは避けてみた。こっちが見やすいかな？
    sinkou = [f"{chord[key + 5]}_______{chord[key + 7]}_______{chord[key]}_______{chord[key]}_______",
              f"{chord[key]}_______{chord[key + 7]}_______{chord[key]}_______{chord[key + 7]}___{chord[key]}___",
              f"{chord[key + 5]}_______{chord[key + 5]}m7_____{chord[key]}_______{chord[key]}_______",
              f"{chord[key + 5]}M7_____{chord[key + 4]}7______{chord[key + 9]}m7_____{chord[key]}M7_____",
              f"{chord[key + 9]}m7_____{chord[key + 4]}m7_____{chord[key + 5]}___{chord[key + 7]}___{chord[key]}_______",
              f"{chord[key + 5]}_______{chord[key + 7]}_______{chord[key + 4]}m______{chord[key + 9]}m______",
              f"{chord[key + 5]}_______{chord[key]}_______{chord[key + 7]}_______{chord[key + 9]}m7_____",
              f"{chord[key + 9]}m______{chord[key + 5]}_______{chord[key + 7]}_______{chord[key]}_______",
              f"{chord[key]}_______{chord[key + 7]}_______{chord[key + 9]}m______{chord[key + 5]}_______",
              f"{chord[key]}_______{chord[key + 9]}m7_____{chord[key + 2]}m7_____{chord[key + 7]}7______",
              f"{chord[key + 9]}m______{chord[key + 5]}_______{chord[key + 7]}_______{chord[key]}_______",
              f"{chord[key + 4]}m______{chord[key + 5]}_______{chord[key + 7]}_______{chord[key + 9]}m______"]
    s_a = random.choice(sinkou)
    s_b = random.choice(sinkou)
    s_c = random.choice(sinkou)

    # 曲構成作成
    songs_list = [(s_a, A_ly[1], s_a, A_ly[2], "|", s_b, sabi, s_b, sabi, "｜", s_a, A_ly[3], s_a, A_ly[4]
                   , "｜", s_b, sabi, s_b, sabi, "｜", s_a, A_ly[1], s_a, A_ly[2], "｜", s_b, sabi, s_b, sabi),

                  (s_a, A_ly[1], s_a, A_ly[2], "|", s_b, sabi, s_a, A_ly[3], "|", s_a, A_ly[4], s_a, A_ly[5], "|", s_b,
                   sabi, s_a, A_ly[6],
                   "|", s_a, A_ly[1], s_c, A_ly[7], "|", s_b, sabi, s_b, sabi)]

    songs = random.choice(songs_list)

    writer_j = fake.name()
    lyric = fake.name()
    fake_e = Faker("en_US")
    writer_e = fake_e.name()
    writer = random.choice([writer_j, writer_e])
    return render_template('index.html', songs=songs, keyword=keyword, writer=writer, lyric=lyric)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
