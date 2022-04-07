from pathlib import Path
import os
import tweepy
from dotenv import load_dotenv
load_dotenv()


def main(output_path, usernames, max_results=5):
    consumer_key = os.environ["CONSUMER_KEY"]
    consumer_secret = os.environ["CONSUMER_SECRET"]
    access_token = os.environ["ACCESS_TOKEN"]
    access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]
    bearer_token = os.environ["BEARER_TOKEN"]

    client = tweepy.Client(
        bearer_token,
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )
    user_data = client.get_users(usernames=usernames)
    id = user_data.data[0]["id"]

    with open(output_path / f"{usernames}.txt", "w") as f:

        pagination_token=None
        for i in range(max_results // 100 + 1):
            tweets = client.get_users_tweets(
                id=id,
                max_results=100,
                pagination_token=pagination_token,
            )
            for tweet in tweets.data:
                text = tweet.text
                text = text.replace("\n", " ")
                f.write(text + "\n")
            pagination_token = tweets.meta["next_token"]


if __name__ == "__main__":
    txt_path = Path("data", "processed", "txt")
    txt_path.mkdir(parents=True, exist_ok=True)

    main(
        output_path=txt_path,
        usernames="pamyurin",
        max_results=5
    )