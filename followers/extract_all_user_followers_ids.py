import datetime
import os
from typing import List, TextIO

import tweepy
from tweepy import TweepError

from api import get_twitter_api as api

PATH_TO_APP_DATA = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'app_data')


def extract_all_user_followers_ids(screen_name: str) -> str:
    """
    Get all of an account's followers' user IDs and write them to a JSON file with today's date.
    :param screen_name: The screen name of the account to query. If left blank, will use the API user's screen name.
    :return: The file path where the queried data was written.
    """
    _api = api.get_twitter_api(os.path.join(PATH_TO_APP_DATA, 'twitter_api_keys.json'))
    if screen_name == '' or not screen_name:
        screen_name = api.get_current_user_json_field('screen_name')
    _output_file_name = f'user_followers_ids {screen_name.lower()} {datetime.date.today()}.txt'
    _output_file_path = os.path.join(PATH_TO_APP_DATA, _output_file_name)
    _followers_count: int = 0
    try:
        _output_file: TextIO
        with open(_output_file_path, 'w') as _output_file:
            for page in tweepy.Cursor(_api.followers_ids, screen_name=screen_name).pages():
                for item in page:
                    _output_file.write(f'{item}\n')
        return _output_file_path
    except TweepError as err:
        print(f'Could not query screen name: {screen_name}\nError(s) found:')
        print(err)
        raise err


if __name__ == '__main__':
    print('Enter user screen name you wish to extract followers\' IDs, then press Enter.')
    print('Do not include @ symbol before screen name.')
    print('Leave blank to use your own screen name.')
    _screen_name: str = input('Screen name: ')
    # Just in case they don't read instructions ;-)
    _screen_name = _screen_name.replace('@', '')

    _api = api.get_twitter_api(os.path.join(PATH_TO_APP_DATA, 'twitter_api_keys.json'))
    if _screen_name == '' or not _screen_name:
        _screen_name = _api.me()._json['screen_name']
    _target_user = _api.get_user(screen_name=_screen_name)
    _target_followers_count: int = _target_user._json['followers_count']
    print(f'{datetime.datetime.now()} Target user\'s followers count: {_target_followers_count}')
    print(f'{datetime.datetime.now()} Guesstimated query time: {_target_followers_count / 5000} seconds')
    print(f'{datetime.datetime.now()} Make sure your computer doesn\'t go to sleep mode or shut down during this time.')

    output_file_path: str = extract_all_user_followers_ids(_screen_name)
    print(f'{datetime.datetime.now()} Results saved to file: {output_file_path}')
    followers_count: int = 0
    with open(output_file_path, 'r') as file:
        for line in file.read().splitlines():
            followers_count += 1
    print(f'{datetime.datetime.now()} Follower IDs saved: {followers_count}')
