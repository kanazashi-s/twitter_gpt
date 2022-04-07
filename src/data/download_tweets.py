from pathlib import Path
import data


def main(max_results=5):
    txt_path = Path("data", "raw", "tweets")
    txt_path.mkdir(parents=True, exist_ok=True)

    data.get_tweets.main(
        output_path=txt_path,
        usernames="pamyurin",
        max_results=max_results
    )

    data.get_tweets.main(
        output_path=txt_path,
        usernames="rikichannel1203",
        max_results=max_results
    )

    data.get_tweets.main(
        output_path=txt_path,
        usernames="kawattidesuyo",
        max_results=max_results
    )


if __name__ == "__main__":
    main(max_results=5)
