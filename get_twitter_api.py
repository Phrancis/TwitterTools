import json
from typing import Dict
from tweepy import API
from tweepy import OAuthHandler


def get_twitter_api(file_path: str = 'app_data/twitter_api_keys.json') -> API:
    """
    Authenticates Twitter API using stored values, and returns an API instance ready for use.
    :return: A Twitter API instance from tweepy.
    """
    try:
        with open(file_path, 'r') as f:
            keys: Dict = json.load(f)
    except FileNotFoundError as err:
        print('File not found. Run "init_twitter_api.py" first.')
        raise err

    auth: OAuthHandler = OAuthHandler(keys['api_key'], keys['api_secret'])
    auth.set_access_token(keys['access_token'], keys['access_secret'])
    return API(
        auth,
        wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True,
        compression=True)


if __name__ == '__main__':
    print(get_twitter_api())
