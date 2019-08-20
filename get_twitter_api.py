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
        _keys: Dict = dict()
        with open(file_path, 'r') as _file:
            _keys = json.load(_file)
    except FileNotFoundError as _err:
        print(f'File not found: {file_path}\nRun "init_twitter_api.py" first, or verify the file path.')
        raise _err

    # Make sure keys are not empty
    if not bool(_keys):
        raise ValueError(f'No data found in {file_path}\nRun "init_twitter_api.py" first, or verify the file path.')

    _auth: OAuthHandler = OAuthHandler(_keys['api_key'], _keys['api_secret'])
    _auth.set_access_token(_keys['access_token'], _keys['access_secret'])
    return API(
        _auth,
        wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True,
        compression=True)


if __name__ == '__main__':
    api: API = get_twitter_api()
    # Query the API for self data to make sure it's working
    print(f'Current API user: {api.me()._json["screen_name"]}')
