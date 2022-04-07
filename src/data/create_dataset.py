from pathlib import Path
import re
from sklearn.model_selection import train_test_split


def main():
    raw_path = Path("data", "raw", "tweets")

    processed_path = Path("data", "processed", "tweets")
    processed_path.mkdir(parents=True, exist_ok=True)

    for file_name in ["kawattidesuyo.txt", "pamyurin.txt", "rikichannel1203.txt"]:
        with open(raw_path / file_name, "r") as f:
            texts = f.readlines()  # list of string

        texts = preprocess_texts(texts)
        train_texts, test_texts = train_test_split(texts, test_size=0.25)

        with open(processed_path / f"train_{file_name}", "w") as f:
            f.writelines(train_texts)
        with open(processed_path / f"test_{file_name}", "w") as f:
            f.writelines(test_texts)


def preprocess_texts(texts):
    # RT削除
    texts = [s for s in texts if s.startswith('RT @') == False]
    # 長州力スタッフからのお知らせ削除
    texts = [s for s in texts if s.startswith('【スタッフ') == False]

    for i in range(len(texts)):
        # URLを削除
        texts[i] = re.sub("https?://[\w!\?/\+\-_~=;\.,\*&@#\$%\(\)'\[\]]+", "", texts[i])
        # @ツイートの宛先を削除
        texts[i] = re.sub("@[\\w]{1,15}", "", texts[i])

    return texts


if __name__ == "__main__":
    main()
