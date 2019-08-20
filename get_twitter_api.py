import json
from typing import Dict, TextIO
from tweepy import API
from tweepy import OAuthHandler


def get_twitter_api(file_path: str = 'app_data/twitter_api_keys.json') -> API:
    """
    Authenticates Twitter API using stored values, and returns an API instance.
    :return: A Twitter API instance from tweepy.
    """
    try:
        _file: TextIO
        with open(file_path, 'r') as _file:
            keys: Dict = json.load(_file)
    except FileNotFoundError as _err:
        print(f'File not found: {file_path}')
        print('Run "init_twitter_api.py" first, or verify the file path.')
        raise _err

    auth: OAuthHandler = OAuthHandler(keys['api_key'], keys['api_secret'])
    auth.set_access_token(keys['access_token'], keys['access_secret'])
    return API(
        auth,
        wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True,
        compression=True)


if __name__ == '__main__':
    print(get_twitter_api())
