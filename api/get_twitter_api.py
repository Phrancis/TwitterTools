import json
import os
from typing import Dict, TextIO
from tweepy import API
from tweepy import OAuthHandler

PATH_TO_APP_DATA = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'app_data')


def get_twitter_api(file_path: str = os.path.join(PATH_TO_APP_DATA, 'twitter_api_keys.json')) -> API:
    """
    Authenticates Twitter API using stored values, and returns an API instance.
    :param file_path: The path to app_data/twitter_api_keys.json
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


def get_current_user_json_field(field_name: str) -> object:
    """
    Queries the current API user's JSON data (protected member, sorry no public access method provided by tweepy) to find the value of a field.
    Return type varies depending on which field is queried, most often will be str or int.
    API reference: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object.html
    :param field_name: Name of the JSON field
    :return: Value of the JSON field
    """
    _api = get_twitter_api(os.path.join(PATH_TO_APP_DATA, 'twitter_api_keys.json'))
    return _api.me()._json[field_name]


if __name__ == '__main__':
    api: API = get_twitter_api(os.path.join('app_data', 'twitter_api_keys.json'))
    # Query the API for self data to make sure it's working
    print(f'Current API user: {get_current_user_json_field("_screen_name")}')
